"""
FX Teller Publication Website Generator
Builds a static executive-quality documentation website.

Outputs: publication/build/website/
"""
import os
import re
import json
import shutil
import html
from pathlib import Path

REPO_ROOT = Path("/mnt/d/FX Teller")
PUB_ROOT = REPO_ROOT / "publication"
OUT_ROOT = PUB_ROOT / "build" / "website"
SITE_DIR = PUB_ROOT / "site"  # source templates
ASSETS_DIR = PUB_ROOT / "diagrams"

# Re-use the content loader
import sys
sys.path.insert(0, str(PUB_ROOT / "generators"))
from content_loader import build_index, FOLDER_MAP, slugify, title_from_filename


# Page-specific diagram assignments
PAGE_DIAGRAMS = {
    "home": ["revenue-pyramid", "flywheel", "lifecycle", "kpi-dashboard"],
    "business": ["revenue-pyramid", "growth-curve", "flywheel"],
    "product": ["lifecycle"],
    "marketing": [],
    "operations": ["org-chart"],
    "execution": ["roadmap", "org-chart", "kpi-dashboard", "growth-curve", "risk-heatmap"],
    "governance": ["risk-heatmap"],
    "roadmap": ["roadmap", "growth-curve"],
    "financial": ["growth-curve", "kpi-dashboard"],
}


def read_template(name):
    return (SITE_DIR / name).read_text(encoding="utf-8")


def md_to_html(content: str) -> str:
    """Convert markdown to HTML (limited, for content display)."""
    # Strip frontmatter
    if content.startswith("---"):
        end = content.find("---", 3)
        if end > 0:
            content = content[end+3:].lstrip()
    out = []
    in_code = False
    in_list = False
    in_table = False
    for line in content.split("\n"):
        if line.startswith("```"):
            if in_code:
                out.append("</code></pre>")
                in_code = False
            else:
                out.append("<pre><code>")
                in_code = True
            continue
        if in_code:
            out.append(html.escape(line))
            continue
        if line.startswith("# "):
            out.append(f'<h1 class="h1">{line[2:].strip()}</h1>')
        elif line.startswith("## "):
            out.append(f'<h2 class="h2">{line[3:].strip()}</h2>')
        elif line.startswith("### "):
            out.append(f'<h3 class="h3">{line[4:].strip()}</h3>')
        elif line.startswith("#### "):
            out.append(f'<h4 class="h4">{line[5:].strip()}</h4>')
        elif line.startswith("> "):
            out.append(f'<blockquote class="callout"><p>{line[2:].strip()}</p></blockquote>')
        elif line.startswith("- ") or line.startswith("* "):
            if not in_list:
                out.append("<ul class='md-list'>")
                in_list = True
            text = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", line[2:].strip())
            text = re.sub(r"\*(.+?)\*", r"<em>\1</em>", text)
            out.append(f"<li>{text}</li>")
        elif line.startswith("|") and "|" in line[1:]:
            # Table
            cells = [c.strip() for c in line.strip("|").split("|")]
            if all(re.match(r"^[\s:\-]+$", c) for c in cells):
                continue  # separator
            if not in_table:
                out.append('<table class="md-table"><tbody>')
                in_table = True
            row = "".join(f'<td>{c}</td>' for c in cells)
            out.append(f"<tr>{row}</tr>")
        elif re.match(r"^\d+\.\s", line):
            if not in_list:
                out.append("<ol class='md-list'>")
                in_list = True
            text = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", line[3:].strip())
            out.append(f"<li>{text}</li>")
        elif line.strip() == "---":
            if in_list:
                out.append("</ul>")
                in_list = False
            if in_table:
                out.append("</tbody></table>")
                in_table = False
            out.append('<hr class="gold-rule"/>')
        elif line.strip() == "":
            if in_list:
                out.append("</ul>")
                in_list = False
            if in_table:
                out.append("</tbody></table>")
                in_table = False
        else:
            if in_list:
                out.append("</ul>")
                in_list = False
            if in_table:
                out.append("</tbody></table>")
                in_table = False
            text = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", line)
            text = re.sub(r"\*(.+?)\*", r"<em>\1</em>", text)
            text = re.sub(r"`(.+?)`", r"<code>\1</code>", text)
            out.append(f"<p>{text}</p>")
    if in_list: out.append("</ul>")
    if in_table: out.append("</tbody></table>")
    return "\n".join(out)


def nav_html(active_slug=None):
    """Render the navigation sidebar."""
    items = []
    sections = [
        ("home", "Home", "🏠"),
        ("context", "Context", "📋"),
        ("foundation", "Foundation", "🏛️"),
        ("business", "Business", "💼"),
        ("product", "Product", "📦"),
        ("marketing", "Marketing", "📣"),
        ("operations", "Operations", "⚙️"),
        ("execution", "Execution", "🎯"),
        ("governance", "Governance", "⚖️"),
        ("roadmap", "Roadmap", "🗺️"),
        ("research", "Research", "🔬"),
        ("strategy-office", "Strategy Office", "👥"),
        ("archive", "Archive", "📦"),
    ]
    for slug, label, icon in sections:
        cls = "nav-item active" if active_slug == slug else "nav-item"
        items.append(f'<a href="/page/{slug}" class="{cls}"><span class="nav-icon">{icon}</span> {label}</a>')
    return "\n".join(items)


def diagram_html(name):
    """Embed a diagram from the SVG library."""
    from pathlib import Path
    import sys
    sys.path.insert(0, str(PUB_ROOT))
    from diagrams.library import render_diagram
    return f'<div class="diagram">{render_diagram(name)}</div>'


def stats_row(items):
    """Render a row of stat boxes."""
    out = ['<div class="stats-row">']
    for val, label in items:
        out.append(f'<div class="stat-box"><div class="stat-num">{val}</div><div class="stat-label">{label}</div></div>')
    out.append('</div>')
    return "\n".join(out)


def main():
    print("Loading content...")
    index = build_index()
    print(f"  {index['total_docs']} docs · {index['total_words']:,} words · {len(index['sections'])} sections")

    # Load templates
    base_template = read_template("base.html")
    page_template = None  # not used; all page content is inlined

    OUT_ROOT.mkdir(parents=True, exist_ok=True)

    # Copy assets
    assets_dst = OUT_ROOT / "assets"
    assets_dst.mkdir(exist_ok=True)
    for f in ASSETS_DIR.glob("*.svg"):
        shutil.copy2(f, assets_dst / f.name)
    # Copy theme.css and search.js
    shutil.copy2(SITE_DIR / "theme.css", OUT_ROOT / "theme.css")
    shutil.copy2(SITE_DIR / "search.js", OUT_ROOT / "search.js")
    print(f"  Copied {len(list(assets_dst.glob('*.svg')))} SVG assets + theme + search")

    # Generate index.json for search
    search_index = {
        "docs": [
            {
                "title": d["title"],
                "url": d["url"],
                "summary": d["summary"],
                "folder": d["folder_slug"],
            }
            for d in index["all_docs"]
        ]
    }
    (OUT_ROOT / "search-index.json").write_text(json.dumps(search_index, indent=2))

    # Generate pages
    pages = []

    # Home page
    pages.append(("home", generate_home(index, base_template)))

    # Section pages
    section_pages = {
        "context": ("Context", "Master context, writing guidelines, glossary, project status, decision log"),
        "foundation": ("Foundation", "Vision, mission, values, brand philosophy"),
        "business": ("Business", "Business model, revenue, pricing, unit economics"),
        "product": ("Product", "Product ecosystem, member experience, service catalogue"),
        "marketing": ("Marketing", "Customer personas, go-to-market, brand launch"),
        "operations": ("Operations", "Operating model, delivery, community, compliance"),
        "execution": ("Execution", "6-month plan, 24-month roadmap, KPIs"),
        "financial": ("Financial", "Financial model, projections, unit economics"),
        "governance": ("Governance", "Strategic Decision Register, governance"),
        "roadmap": ("Roadmap", "6-month plan, 24-month strategic roadmap"),
        "research": ("Research", "Market sizing, technical architecture, runbooks"),
        "strategy-office": ("Strategy Office", "10 specialist roles + 4 frameworks"),
        "archive": ("Archive", "Historical documents"),
    }

    for slug, (title, desc) in section_pages.items():
        if slug == "financial":
            # Financial is a special view — show financial-relevant docs
            relevant = []
            for s_slug, section in index["sections"].items():
                if s_slug in ("business", "execution"):
                    relevant.extend(section["docs"])
            docs = relevant
            page_title = "Financial"
        elif slug == "roadmap":
            relevant = []
            for s_slug, section in index["sections"].items():
                if s_slug == "execution":
                    relevant.extend(section["docs"])
            docs = relevant
            page_title = "Roadmap"
        elif slug == "governance":
            section = index["sections"].get("governance")
            docs = section["docs"] if section else []
            page_title = "Governance"
        else:
            section = index["sections"].get(slug)
            if not section:
                continue
            docs = section["docs"]
            page_title = section["title"]
        pages.append((slug, generate_section_page(slug, page_title, desc, docs, index, base_template)))

    # Individual doc pages
    doc_count = 0
    for doc in index["all_docs"]:
        content = generate_doc_page(doc, index, base_template)
        doc_dir = OUT_ROOT / "doc" / doc["folder_slug"] / doc["slug"]
        doc_dir.mkdir(parents=True, exist_ok=True)
        (doc_dir / "index.html").write_text(content)
        doc_count += 1
    print(f"  Generated {doc_count} document pages")

    # Search page
    (OUT_ROOT / "search" / "index.html").parent.mkdir(parents=True, exist_ok=True)
    (OUT_ROOT / "search" / "index.html").write_text(generate_search_page(index, base_template))
    (OUT_ROOT / "downloads" / "index.html").parent.mkdir(parents=True, exist_ok=True)
    (OUT_ROOT / "downloads" / "index.html").write_text(generate_downloads_page(base_template))

    # Index page (redirect to home)
    (OUT_ROOT / "index.html").write_text(pages[0][1])

    # Section pages
    for slug, html_content in pages:
        (OUT_ROOT / "page" / slug).mkdir(parents=True, exist_ok=True)
        (OUT_ROOT / "page" / slug / "index.html").write_text(html_content)

    print(f"  Generated {len(pages)} section pages")
    print(f"  Output: {OUT_ROOT}")


def page_html(slug, title, content_html, base_template, description=""):
    """Combine base + page template."""
    return (
        base_template
        .replace("{{title}}", title)
        .replace("{{description}}", description)
        .replace("{{content}}", content_html)
        .replace("{{slug}}", slug)
    )


def generate_home(index, base_template):
    total = index["total_docs"]
    words = index["total_words"]
    sections = index["sections"]

    content = f"""
    <div class="hero">
        <div class="hero-brand">FX Teller</div>
        <div class="hero-rule"></div>
        <h1 class="hero-title">Strategic<br><strong>Blueprint</strong></h1>
        <div class="hero-subtitle">Founder Edition · Knowledge Base</div>
        <div class="hero-stats">
            <div class="stat-box"><div class="stat-num">{total}</div><div class="stat-label">Documents</div></div>
            <div class="stat-box"><div class="stat-num">{words//1000}k</div><div class="stat-label">Words</div></div>
            <div class="stat-box"><div class="stat-num">{len(sections)}</div><div class="stat-label">Sections</div></div>
            <div class="stat-box"><div class="stat-num">30+</div><div class="stat-label">Decisions Logged</div></div>
        </div>
    </div>

    <div class="content-section">
        <h2 class="h2">The company, in one sentence</h2>
        <p class="lead">FX Teller is a members-only, audio-first Trading Floor for disciplined retail traders — a members' club whose principal amenity is a live, audio-only Trading Floor where a Host narrates the market in real time. The brand is the philosophy: discipline over engagement, process over prediction, calm over urgency.</p>
    </div>

    <div class="content-section">
        <h2 class="h2">Today's Deliverables</h2>
        <p>The Executive Strategy Office produced the complete knowledge base in a single continuous session. Every document is version-controlled and designed for re-installation by any future AI agent or human contributor.</p>
        <table class="exec-table">
            <thead><tr><th>Section</th><th>Description</th><th>Docs</th></tr></thead>
            <tbody>
    """

    for slug, section in sections.items():
        desc = section.get('description', '')
        ndocs = len(section['docs'])
        content += f'<tr><td><a href="/page/{slug}"><strong>{section["title"]}</strong></a></td><td>{desc}</td><td>{ndocs}</td></tr>\n'

    content += """
            </tbody>
        </table>
    </div>

    <div class="content-section">
        <h2 class="h2">Visual System</h2>
        <p>Key diagrams from the publication:</p>
        <div class="diagram-grid">
            {flywheel}
            {revenue}
        </div>
        <div class="diagram-grid">
            {lifecycle}
            {kpi}
        </div>
    </div>

    <div class="content-section">
        <h2 class="h2">Quick Reference</h2>
        <div class="callout">
            <strong>The company in 10 numbers.</strong> 2 tiers (Monthly + Annual). 50 Founding Members (closed cohort). 5 daily Floor services. 8-person team cap. 30–50 Y1, 150–200 Y2, 350–500 Y3. ₹1.2–1.5 Cr Founder reserve. ₹15–30 Cr strategic raise Y2. 75% retention gate. 4 rhythms. Zero paid acquisition.
        </div>
        <div class="callout">
            <strong>5 decisions already made.</strong> (1) First members' club for retail traders in India. (2) Bootstrap Y1, raise Y2. (3) Single Credit: bundled, no expiry/transfer/purchase/display. (4) Writing-led growth. (5) Two-stage launch.
        </div>
        <div class="callout">
            <strong>5 decisions needed now.</strong> (1) Annual price (OPEN-006). (2) Monthly price (OPEN-007). (3) Founding cap 50 (OPEN-008). (4) Headcount safety factor 1.5x (OPEN-009). (5) Writing engine ownership (OPEN-010).
        </div>
    </div>
    """.format(
        flywheel=diagram_html("flywheel"),
        revenue=diagram_html("revenue-pyramid"),
        lifecycle=diagram_html("lifecycle"),
        kpi=diagram_html("kpi-dashboard"),
    )

    return page_html("home", "FX Teller — Strategic Blueprint", content, base_template,
                     description="The complete FX Teller strategy knowledge base")


def generate_section_page(slug, title, description, docs, index, base_template):
    content = f"""
    <header class="page-header">
        <div class="page-breadcrumb"><a href="/">Home</a> · <span>{title}</span></div>
        <div class="page-meta">{len(docs)} documents</div>
    </header>
    <h1 class="h1">{title}</h1>
    <p class="lead">{description}</p>
    """

    # Add section-specific diagrams
    for diagram_name in PAGE_DIAGRAMS.get(slug, []):
        content += diagram_html(diagram_name)

    content += '<h2 class="h2">Documents</h2>'
    content += '<div class="doc-grid">'
    for doc in docs:
        content += f"""
        <a href="/doc/{doc['folder_slug']}/{doc['slug']}/" class="doc-card">
            <h3 class="doc-card-title">{doc['title']}</h3>
            <p class="doc-card-summary">{doc['summary'][:200]}{'…' if len(doc['summary']) > 200 else ''}</p>
            <div class="doc-card-meta">{doc['word_count']} words · {doc['section_count']} sections</div>
        </a>
        """
    content += '</div>'

    return page_html(slug, f"{title} — FX Teller", content, base_template, description=description)


def generate_doc_page(doc, index, base_template):
    content_html = md_to_html(doc["content"])

    related_html = ""
    if doc.get("related"):
        related_html = '<h2 class="h2">Related Documents</h2><div class="doc-grid">'
        for r in doc["related"]:
            related_html += f"""
            <a href="{r['url']}/" class="doc-card">
                <h3 class="doc-card-title">{r['title']}</h3>
                <p class="doc-card-summary">{r.get('summary', '')[:200]}</p>
            </a>
            """
        related_html += '</div>'

    # Build frontmatter / metadata box
    meta_html = f"""
    <div class="doc-meta-card">
        <div class="doc-meta-row">
            <div class="doc-meta-label">Section</div>
            <div class="doc-meta-value">{doc['folder_slug'].title()}</div>
        </div>
        <div class="doc-meta-row">
            <div class="doc-meta-label">Length</div>
            <div class="doc-meta-value">{doc['word_count']:,} words · {doc['section_count']} sections</div>
        </div>
        <div class="doc-meta-row">
            <div class="doc-meta-label">Source</div>
            <div class="doc-meta-value">docs/{doc['folder']}/{doc['filename']}</div>
        </div>
    </div>
    """

    insights_html = ""
    if doc.get("key_insights"):
        insights_html = '<div class="callout"><strong>Key Insights.</strong><ul class="insight-list">'
        for insight in doc["key_insights"][:5]:
            insights_html += f'<li>{insight}</li>'
        insights_html += '</ul></div>'

    content = f"""
    <header class="page-header">
        <div class="page-breadcrumb">
            <a href="/">Home</a> · <a href="/page/{doc['folder_slug']}">{doc['folder_slug'].title()}</a> · <span>{doc['title']}</span>
        </div>
    </header>
    {meta_html}
    <h1 class="h1">{doc['title']}</h1>
    {insights_html}
    {content_html}
    {related_html}
    """

    return page_html(doc['slug'], f"{doc['title']} — FX Teller", content, base_template, description=doc['summary'])


def generate_search_page(index, base_template):
    content = """
    <header class="page-header">
        <div class="page-breadcrumb"><a href="/">Home</a> · <span>Search</span></div>
    </header>
    <h1 class="h1">Search the Knowledge Base</h1>
    <p class="lead">Search across all 40+ documents in the FX Teller strategy repository.</p>
    <div class="search-container">
        <input type="text" id="search-input" placeholder="Search documents…" autocomplete="off">
        <div id="search-results" class="search-results"></div>
    </div>
    <script src="/search.js"></script>
    """
    return page_html("search", "Search — FX Teller", content, base_template)


def generate_downloads_page(base_template):
    content = """
    <header class="page-header">
        <div class="page-breadcrumb"><a href="/">Home</a> · <span>Downloads</span></div>
    </header>
    <h1 class="h1">Downloads</h1>
    <p class="lead">Download the complete publication in the format you need.</p>

    <div class="download-grid">
        <a href="/Founder_Playbook.pdf" class="download-card" download>
            <div class="download-icon">📄</div>
            <h3>Founder Playbook PDF</h3>
            <p>Premium 40-page printable A4 PDF with cover, dividers, headers, footers, vector diagrams, executive tables.</p>
            <div class="download-meta">PDF · 40 pages · 200KB</div>
        </a>

        <a href="/Founder_Playbook.html" class="download-card" download>
            <div class="download-icon">🌐</div>
            <h3>Founder Playbook HTML</h3>
            <p>Self-contained HTML with full print-optimized CSS. Open in any browser and print to PDF if needed.</p>
            <div class="download-meta">HTML · ~80KB</div>
        </a>

        <a href="/Deck.pptx" class="download-card" download>
            <div class="download-icon">📊</div>
            <h3>Strategy Deck (PowerPoint)</h3>
            <p>Executive presentation deck for board meetings, investor pitches, and strategic partnerships.</p>
            <div class="download-meta">PPTX · ~20 slides</div>
        </a>

        <a href="/downloads/assets.zip" class="download-card" download>
            <div class="download-icon">🎨</div>
            <h3>Asset Bundle</h3>
            <p>All SVG diagrams, theme tokens, and design system assets for reuse in your own documents.</p>
            <div class="download-meta">ZIP · SVG + JSON</div>
        </a>
    </div>
    """
    return page_html("downloads", "Downloads — FX Teller", content, base_template)


if __name__ == "__main__":
    main()
