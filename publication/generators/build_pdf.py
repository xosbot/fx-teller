"""
FX Teller PDF Playbook Generator
Generates a premium, magazine-quality A4 PDF from the knowledge base.

Uses WeasyPrint (HTML/CSS → PDF). This is the same HTML/CSS approach as a
headless browser (Playwright/Puppeteer) — but with native print CSS support.
"""
import os
import re
import html
import shutil
import sys
from pathlib import Path
from datetime import datetime

from weasyprint import HTML, CSS

REPO_ROOT = Path("/mnt/d/FX Teller")
PUB_ROOT = REPO_ROOT / "publication"
OUT_DIR = PUB_ROOT / "build"
PDF_PATH = OUT_DIR / "Founder_Playbook.pdf"
HTML_PATH = OUT_DIR / "Founder_Playbook.html"

sys.path.insert(0, str(PUB_ROOT / "generators"))
sys.path.insert(0, str(PUB_ROOT))
from content_loader import build_index, FOLDER_MAP
from diagrams.library import render_diagram


# Brand colors
NAVY = "#1B1B2F"
GOLD = "#C5A55A"
CREAM = "#F5F0E8"
WHITE = "#FFFFFF"
SAGE = "#7A9E7E"
SLATE = "#4A4A6A"
CORAL = "#C87A6A"


CSS_STYLE = """
@page {
    size: A4;
    margin: 22mm 22mm 22mm 22mm;
    @top-left {
        content: string(chapter);
        font-family: 'DejaVu Sans', sans-serif;
        font-size: 7pt;
        color: #999;
        margin-top: 6mm;
    }
    @top-right {
        content: "FX Teller  |  Strategic Blueprint";
        font-family: 'DejaVu Sans', sans-serif;
        font-size: 7pt;
        color: #999;
        margin-top: 6mm;
    }
    @bottom-center {
        content: counter(page) " / " counter(pages);
        font-family: 'DejaVu Sans', sans-serif;
        font-size: 8pt;
        color: #666;
    }
    @bottom-right {
        content: "Confidential  |  V1.0";
        font-family: 'DejaVu Sans', sans-serif;
        font-size: 7pt;
        color: #999;
    }
}
@page cover {
    margin: 0;
    @top-left { content: none; }
    @top-right { content: none; }
    @bottom-center { content: none; }
    @bottom-right { content: none; }
}
@page divider {
    margin: 0;
    @top-left { content: none; }
    @top-right { content: none; }
    @bottom-center { content: none; }
    @bottom-right { content: none; }
}
@page:blank {
    @top-left { content: none; }
    @top-right { content: none; }
    @bottom-center { content: none; }
    @bottom-right { content: none; }
}

* { margin: 0; padding: 0; box-sizing: border-box; }
body {
    font-family: 'DejaVu Serif', Georgia, 'Times New Roman', serif;
    color: #1A1A1A;
    line-height: 1.6;
    font-size: 9.5pt;
    background: white;
}
h1, h2, h3, h4 {
    font-family: 'DejaVu Sans', sans-serif;
    color: """ + NAVY + """;
    page-break-after: avoid;
}
p { margin-bottom: 0.5em; text-align: justify; }
strong { color: """ + NAVY + """; }

/* ─── Cover ─── */
.cover {
    page: cover;
    width: 100%; height: 100%;
    background: """ + NAVY + """;
    color: white;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    text-align: center;
    page-break-after: always;
    position: relative;
}
.cover::before, .cover::after {
    content: '';
    position: absolute;
    left: 25mm; right: 25mm;
    height: 0.5pt;
    background: """ + GOLD + """;
    opacity: 0.4;
}
.cover::before { top: 25mm; }
.cover::after  { bottom: 25mm; }
.cover-brand {
    font-family: 'DejaVu Sans', sans-serif;
    font-size: 9pt;
    letter-spacing: 5pt;
    color: """ + GOLD + """;
    text-transform: uppercase;
    margin-bottom: 18mm;
}
.cover-rule {
    width: 40mm; height: 0.5pt;
    background: """ + GOLD + """;
    margin: 0 auto 12mm;
}
.cover-title {
    font-family: 'DejaVu Sans', sans-serif;
    font-size: 36pt;
    font-weight: 300;
    line-height: 1.1;
    margin-bottom: 4mm;
}
.cover-title strong { font-weight: 700; color: """ + GOLD + """; }
.cover-subtitle {
    font-family: 'DejaVu Sans', sans-serif;
    font-size: 10pt;
    letter-spacing: 2pt;
    color: rgba(255,255,255,0.7);
    margin-bottom: 25mm;
}
.cover-meta {
    font-family: 'DejaVu Sans', sans-serif;
    font-size: 7.5pt;
    color: rgba(255,255,255,0.5);
    line-height: 2;
}
.cover-foot {
    position: absolute;
    bottom: 14mm;
    font-family: 'DejaVu Sans', sans-serif;
    font-size: 6pt;
    color: rgba(255,255,255,0.3);
    letter-spacing: 1.5pt;
}

/* ─── Section divider ─── */
.divider {
    page: divider;
    width: 100%; height: 100%;
    background: """ + CREAM + """;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    text-align: center;
    page-break-before: always;
    page-break-after: always;
}
.divider .num {
    font-family: 'DejaVu Sans', sans-serif;
    font-size: 96pt;
    font-weight: 700;
    color: """ + NAVY + """;
    line-height: 1;
    margin-bottom: 4mm;
}
.divider .label {
    font-family: 'DejaVu Sans', sans-serif;
    font-size: 7pt;
    letter-spacing: 3pt;
    color: #999;
    text-transform: uppercase;
    margin-bottom: 6mm;
}
.divider .rule {
    width: 35mm; height: 0.5pt;
    background: """ + GOLD + """;
    margin: 0 auto 4mm;
}
.divider .title {
    font-family: 'DejaVu Sans', sans-serif;
    font-size: 24pt;
    font-weight: 300;
    color: """ + NAVY + """;
    line-height: 1.2;
}

/* ─── Chapter header ─── */
.chapter {
    page-break-before: always;
    string-set: chapter content();
}
.chapter-title {
    font-family: 'DejaVu Sans', sans-serif;
    font-size: 18pt;
    font-weight: 700;
    color: """ + NAVY + """;
    margin-bottom: 4mm;
    padding-bottom: 2mm;
    border-bottom: 1.5pt solid """ + GOLD + """;
}
.chapter-num {
    font-family: 'DejaVu Sans', sans-serif;
    font-size: 8pt;
    letter-spacing: 2pt;
    color: """ + GOLD + """;
    text-transform: uppercase;
    margin-bottom: 2mm;
}

/* ─── Headings ─── */
h2 {
    font-size: 13pt;
    margin: 6mm 0 2mm;
    color: """ + NAVY + """;
    page-break-after: avoid;
}
h3 {
    font-size: 11pt;
    margin: 4mm 0 1mm;
    color: """ + NAVY + """;
    page-break-after: avoid;
}
h4 {
    font-size: 10pt;
    margin: 3mm 0 1mm;
    color: """ + NAVY + """;
    page-break-after: avoid;
}

/* ─── Callout ─── */
.callout {
    background: """ + CREAM + """;
    border-left: 2pt solid """ + GOLD + """;
    padding: 3mm 4mm;
    margin: 3mm 0;
    font-family: 'DejaVu Sans', sans-serif;
    font-size: 8.5pt;
    line-height: 1.55;
    page-break-inside: avoid;
}
.callout-navy {
    background: """ + NAVY + """;
    border-left: 2pt solid """ + GOLD + """;
    padding: 3mm 4mm;
    margin: 3mm 0;
    font-family: 'DejaVu Sans', sans-serif;
    font-size: 8.5pt;
    line-height: 1.55;
    color: rgba(255,255,255,0.9);
    page-break-inside: avoid;
}
.callout-navy strong { color: """ + GOLD + """; }

/* ─── Stat boxes ─── */
.stats-row {
    display: flex;
    gap: 2mm;
    margin: 3mm 0;
    page-break-inside: avoid;
}
.stat-box {
    flex: 1;
    text-align: center;
    padding: 2.5mm 1.5mm;
    background: """ + CREAM + """;
    page-break-inside: avoid;
}
.stat-num {
    font-family: 'DejaVu Sans', sans-serif;
    font-size: 18pt;
    font-weight: 700;
    color: """ + NAVY + """;
    line-height: 1.1;
}
.stat-num.gold { color: """ + GOLD + """; }
.stat-label {
    font-family: 'DejaVu Sans', sans-serif;
    font-size: 6.5pt;
    color: #666;
    text-transform: uppercase;
    margin-top: 1mm;
}

/* ─── Tables ─── */
table.exec-table {
    width: 100%;
    border-collapse: collapse;
    margin: 3mm 0;
    font-family: 'DejaVu Sans', sans-serif;
    font-size: 7.5pt;
    page-break-inside: avoid;
}
table.exec-table th {
    background: """ + NAVY + """;
    color: white;
    padding: 1.5mm 2.5mm;
    text-align: left;
    font-weight: 700;
    font-size: 6.5pt;
    text-transform: uppercase;
    letter-spacing: 0.3pt;
}
table.exec-table td {
    padding: 1.5mm 2.5mm;
    border-bottom: 0.3pt solid #ddd;
    vertical-align: top;
}
table.exec-table tr:nth-child(even) td {
    background: """ + CREAM + """;
}

/* ─── Diagrams ─── */
.diagram {
    text-align: center;
    margin: 4mm 0;
    page-break-inside: avoid;
}
.diagram svg { max-width: 100%; height: auto; }

/* ─── Lists ─── */
ul, ol { margin: 1mm 0 3mm 5mm; }
li { margin-bottom: 0.5mm; }

/* ─── Card grid (3-up) ─── */
.cards {
    display: flex;
    gap: 3mm;
    margin: 3mm 0;
    page-break-inside: avoid;
}
.card {
    flex: 1;
    padding: 3mm;
    background: #F8F6F2;
    border: 0.3pt solid #e0ddd5;
    page-break-inside: avoid;
}
.card h4 {
    font-size: 8.5pt;
    margin-bottom: 1mm;
}
.card p {
    font-size: 7.5pt;
    color: #555;
    line-height: 1.4;
}

/* ─── Quote ─── */
.quote {
    background: """ + NAVY + """;
    color: white;
    padding: 8mm;
    margin: 6mm 0;
    font-family: 'DejaVu Serif', serif;
    font-size: 11pt;
    font-style: italic;
    text-align: center;
    line-height: 1.5;
    page-break-inside: avoid;
}
.quote cite {
    display: block;
    font-family: 'DejaVu Sans', sans-serif;
    font-size: 7pt;
    font-style: normal;
    color: """ + GOLD + """;
    margin-top: 4mm;
    letter-spacing: 1pt;
}

/* ─── Icon grid (4-up) ─── */
.icons {
    display: flex;
    flex-wrap: wrap;
    gap: 2mm;
    margin: 3mm 0;
    page-break-inside: avoid;
}
.icon-item {
    flex: 1 1 22%;
    text-align: center;
    padding: 2mm;
    background: #F8F6F2;
    border: 0.3pt solid #e0ddd5;
}
.icon-item .ico {
    font-size: 14pt;
    color: """ + GOLD + """;
    margin-bottom: 0.5mm;
}
.icon-item strong {
    display: block;
    font-family: 'DejaVu Sans', sans-serif;
    font-size: 7pt;
    color: """ + NAVY + """;
    margin-bottom: 0.5mm;
}
.icon-item span {
    font-family: 'DejaVu Sans', sans-serif;
    font-size: 6.5pt;
    color: #666;
}

/* ─── Part summary ─── */
.part-summary {
    background: """ + NAVY + """;
    color: rgba(255,255,255,0.85);
    padding: 3mm 4mm;
    margin: 4mm 0;
    font-family: 'DejaVu Sans', sans-serif;
    font-size: 7.5pt;
    line-height: 1.55;
    page-break-inside: avoid;
}
.part-summary strong { color: """ + GOLD + """; }

/* ─── Checklist ─── */
.checklist { list-style: none; margin: 1mm 0 3mm 0; padding: 0; }
.checklist li {
    padding: 1.5mm 0 1.5mm 6mm;
    position: relative;
    font-family: 'DejaVu Sans', sans-serif;
    font-size: 8pt;
    border-bottom: 0.3pt solid #eee;
}
.checklist li::before {
    content: '\\2610';
    position: absolute; left: 0;
    color: """ + GOLD + """;
    font-size: 9pt;
}

/* ─── Misc ─── */
.pb { page-break-before: always; }
.pba { page-break-after: always; }
.center { text-align: center; }
hr.gold {
    border: none;
    border-top: 0.3pt solid """ + GOLD + """;
    margin: 3mm 0;
    opacity: 0.4;
}
.gold-text { color: """ + GOLD + """; }
.toc-entry {
    font-family: 'DejaVu Sans', sans-serif;
    font-size: 9pt;
    padding: 1.5mm 0;
    border-bottom: 0.3pt solid #eee;
    display: flex;
    justify-content: space-between;
}
.toc-entry .title { color: """ + NAVY + """; font-weight: 600; }
.toc-entry .pg { color: #999; }
"""


# ──────────────────────────────────────────────────────────────────────
# Content helpers
# ──────────────────────────────────────────────────────────────────────

def md_to_html(content: str, max_chars: int = 0) -> str:
    """Convert markdown to printable HTML. If max_chars > 0, truncate content."""
    if max_chars > 0 and len(content) > max_chars:
        # Find a good break point (end of a paragraph)
        truncated = content[:max_chars]
        last_para = truncated.rfind("\n\n")
        if last_para > max_chars * 0.7:
            content = truncated[:last_para] + "\n\n*[Excerpted — see full document in the web playbook.]*"
        else:
            content = truncated + "\n\n*[Excerpted — see full document in the web playbook.]*"

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
                out.append('<pre><code style="font-family:DejaVu Sans Mono,monospace;font-size:7.5pt;">')
                in_code = True
            continue
        if in_code:
            out.append(html.escape(line))
            continue
        if line.startswith("# "):
            out.append(f'<h1 style="font-size:18pt;margin:6mm 0 4mm;color:{NAVY};font-family:DejaVu Sans,sans-serif;">{line[2:].strip()}</h1>')
        elif line.startswith("## "):
            if in_list: out.append("</ul>"); in_list = False
            if in_table: out.append("</table>"); in_table = False
            out.append(f'<h2>{line[3:].strip()}</h2>')
        elif line.startswith("### "):
            if in_list: out.append("</ul>"); in_list = False
            if in_table: out.append("</table>"); in_table = False
            out.append(f'<h3>{line[4:].strip()}</h3>')
        elif line.startswith("#### "):
            if in_list: out.append("</ul>"); in_list = False
            out.append(f'<h4>{line[5:].strip()}</h4>')
        elif line.startswith("> "):
            text = line[2:].strip()
            text = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", text)
            out.append(f'<div class="callout">{text}</div>')
        elif line.startswith("- ") or line.startswith("* "):
            if in_table: out.append("</table>"); in_table = False
            if not in_list:
                out.append("<ul>")
                in_list = True
            text = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", line[2:].strip())
            out.append(f"<li>{text}</li>")
        elif line.startswith("|") and "|" in line[1:]:
            if in_list: out.append("</ul>"); in_list = False
            cells = [c.strip() for c in line.strip("|").split("|")]
            if all(re.match(r"^[\s:\-]+$", c) for c in cells):
                continue
            if not in_table:
                out.append('<table class="exec-table"><tbody>')
                in_table = True
            row = "".join(f'<td>{c}</td>' for c in cells)
            out.append(f"<tr>{row}</tr>")
        elif re.match(r"^\d+\.\s", line):
            if in_list: out.append("</ul>"); in_list = False
            if in_table: out.append("</table>"); in_table = False
            text = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", line[3:].strip())
            out.append(f'<div class="checklist"><li>{text}</li>')
        elif line.strip() == "---":
            if in_list: out.append("</ul>"); in_list = False
            if in_table: out.append("</table>"); in_table = False
            out.append('<hr class="gold"/>')
        elif line.strip() == "":
            if in_list: out.append("</ul>"); in_list = False
            if in_table: out.append("</table>"); in_table = False
        else:
            if in_list: out.append("</ul>"); in_list = False
            if in_table: out.append("</table>"); in_table = False
            text = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", line)
            text = re.sub(r"\*(.+?)\*", r"<em>\1</em>", text)
            text = re.sub(r"`(.+?)`", r"<code>\1</code>", text)
            out.append(f"<p>{text}</p>")

    if in_list: out.append("</ul>")
    if in_table: out.append("</table>")
    return "\n".join(out)


# ──────────────────────────────────────────────────────────────────────
# Build the document
# ──────────────────────────────────────────────────────────────────────

# Chapter ordering for the PDF (Founders-first narrative)
CHAPTER_ORDER = [
    ("I",    "The Vision",       ["fxteller-master-contextmd",
                                  "vision-mission-valuesmd",
                                  "brand-philosophymd"]),
    ("II",   "The Business",     ["business-modelmd",
                                  "revenue-architecturemd",
                                  "commercial-strategy-pricing-psychologymd",
                                  "financial-model-unit-economicsmd"]),
    ("III",  "The Product",      ["product-ecosystemmd",
                                  "member-experience-blueprintmd",
                                  "service-cataloguemd"]),
    ("IV",   "The Brand",        ["customer-personasmd",
                                  "go-to-market-brand-launch-playbookmd"]),
    ("V",    "Operations",       ["operating-modelmd",
                                  "product-delivery-operations-blueprintmd"]),
    ("VI",   "Execution",        ["6-month-execution-planmd",
                                  "24-month-strategic-roadmapmd"]),
    ("VII",  "Governance",       ["strategic-decision-registermd"]),
    ("VIII", "Appendices",       ["market-sizing-addressable-market-analysismd",
                                  "architecturemd",
                                  "deploymentmd",
                                  "runbookmd"]),
]


def lookup_doc(all_docs, slug):
    for d in all_docs:
        if d["slug"] == slug:
            return d
    return None


def build_toc():
    items = []
    items.append('<div class="toc-entry"><span class="title">Cover</span><span class="pg">1</span></div>')
    items.append('<div class="toc-entry"><span class="title">Letter to the Founder</span><span class="pg">2</span></div>')
    items.append('<div class="toc-entry"><span class="title">Executive Summary</span><span class="pg">3</span></div>')
    items.append('<div class="toc-entry"><span class="title">Table of Contents</span><span class="pg">4</span></div>')
    for num, title, doc_slugs in CHAPTER_ORDER:
        items.append(f'<div class="toc-entry"><span class="title">Part {num} — {title}</span><span class="pg"></span></div>')
    return "\n".join(items)


def build_html():
    print("Loading content...")
    index = build_index()
    all_docs = {d["slug"]: d for d in index["all_docs"]}
    # Re-load full content
    from content_loader import load_doc as raw_load_doc
    for d in index["all_docs"]:
        full = raw_load_doc(d["folder"], d["filename"])
        if full:
            d["content"] = full["content"]
    print(f"  {index['total_docs']} docs · {index['total_words']:,} words")

    parts = []
    a = parts.append

    # ─── Cover ───
    a(f'''<div class="cover">
        <div class="cover-brand">FX Teller</div>
        <div class="cover-rule"></div>
        <div class="cover-title">Strategic<br><strong>Blueprint</strong></div>
        <div class="cover-subtitle">Founder Edition</div>
        <div class="cover-rule"></div>
        <div class="cover-meta">Version 1.0 &ensp;|&ensp; July 2026</div>
        <div class="cover-meta">Prepared by the Executive Strategy Office</div>
        <div class="cover-foot">CONFIDENTIAL  |  For Founder, Board, and Investor Distribution</div>
    </div>''')

    # ─── Letter to the Founder ───
    a(f'''<div class="chapter" string-set="chapter content('Letter to the Founder')">
        <div class="chapter-num">PROLOGUE</div>
        <h1 class="chapter-title">Letter to the Founder</h1>
        <p>This document is the Master Strategic Blueprint for FX Teller. It is the company in writing. It has been produced by the full Executive Strategy Office, drawing on every strategic document in the knowledge base, and stress-tested by the most-sceptical reader the Office could find. It is the document you will hand to the next executive, the next investor, the next regulator, the next Host.</p>
        <p>What has been built in this knowledge base is unusual. Twenty-two strategic decisions recorded in the Decision Register, with named owners and review cadences. Three governance frameworks: a 10-specialist Strategy Office with explicit vetoes, a 6-rhythm operational cadence, a documentation discipline that survives a 90-day Founder absence. A legal stack: SEBI opinion, Member agreement suite, data protection posture, audit trails. A financial model with Conservative, Expected, and Optimistic scenarios. A 6-month execution plan with week-by-week milestones. A 24-month strategic roadmap with quarterly sequencing.</p>
        <p>How this document should be used: read it once, end to end. Then put it down for 48 hours. Then read the Letter to the Founder, the Executive Summary, the Board Recommendations, and the Founder Dashboard. Then close it and execute the first 30 days. The document is the operating system; the operating system is the company.</p>
        <p>Why execution now matters more than planning: the philosophy is a 10-year project, not a 1-year plan. The 6-month execution plan is the discipline of becoming a real company. The 24-month roadmap is the discipline of becoming an institution. The 10-year vision is the discipline of becoming a category. The 90 days ahead decide which of those three the company becomes.</p>
        <p style="text-align:right;font-family:DejaVu Sans,sans-serif;font-size:8pt;color:#888;margin-top:6mm;">— The Executive Strategy Office</p>
    </div>''')

    # ─── Executive Summary ───
    a(f'''<div class="chapter" string-set="chapter content('Executive Summary')">
        <div class="chapter-num">EXECUTIVE SUMMARY</div>
        <h1 class="chapter-title">Executive Summary</h1>
        <p>FX Teller is a members-only, audio-first Trading Floor for disciplined retail traders. A members' club whose principal amenity is a live, audio-only Trading Floor where a Host narrates the market in real time. The brand is the philosophy: discipline over engagement, process over prediction, calm over urgency.</p>
        <p>The company exists because the Indian retail-trading industry has built a product economy that systematically mis-serves the disciplined trader. Signal groups, tipsters, gamified brokerages, and copy-trading platforms all profit from engagement the trader would be better off not having. FX Teller is the structural counter-position: ambient, calm, audio-first, process-over-prediction, no engagement-extraction.</p>
        <div class="stats-row">
            <div class="stat-box"><div class="stat-num">30–50</div><div class="stat-label">Members Y1</div></div>
            <div class="stat-box"><div class="stat-num">150–200</div><div class="stat-label">Members Y2</div></div>
            <div class="stat-box"><div class="stat-num">350–500</div><div class="stat-label">Members Y3</div></div>
            <div class="stat-box"><div class="stat-num gold">₹25L</div><div class="stat-label">MRR at M24</div></div>
            <div class="stat-box"><div class="stat-num">75%</div><div class="stat-label">Gross Margin</div></div>
        </div>
        <p>The model is a premium, community-first membership. Annual tier is the spine; Monthly is the on-ramp. Trading Credits are bundled transparently into the Annual fee. Capital posture: bootstrap Year 1 (₹1.2–1.5 Cr Founder reserve), Year 2 strategic raise of ₹15–30 Cr on philosophy-defending terms. Team: 4 in Year 1, 6 by Q4, 8 by Year 2. House of Traders: scoped Q5, built Q7, opened Q13–Q14. AI Companion: production by Q11–Q12.</p>
        <p>The most load-bearing resource is the Founder. The plan is a Founder-protection plan disguised as a launch plan. Second Host and second writer in Months 4–5. Workload capped at 45–55 hours/week. Warm first session is Host-led by Q3.</p>
        <p><strong>Success at 24 months:</strong> 500–800 Members, ₹25L MRR, 75% gross margin, 8-person team, 4-rhythm cadence, House construction, AI Companion in production, Dubai cohort launched, brand recognised as the most-respected lifestyle brand for disciplined traders in India and Dubai.</p>
        <div class="part-summary"><strong>Today's Deliverables.</strong> 40 documents, ~176,000 words. 10 sections. 9 SVG diagrams. 30+ decisions logged. Brand Philosophy, 12 core values, 5 commitments, 4-tier revenue model, 6 moats, 12-stage lifecycle, 8-person team cap, 24-month roadmap. This is the operating system.</div>
    </div>''')

    # ─── Table of Contents ───
    a(f'''<div class="chapter" string-set="chapter content('Contents')">
        <div class="chapter-num">CONTENTS</div>
        <h1 class="chapter-title">Table of Contents</h1>
        {build_toc()}
    </div>''')

    # ─── Chapters ───
    for chapter_num, chapter_title, doc_slugs in CHAPTER_ORDER:
        a(f'''<div class="divider" string-set="chapter content('Part {chapter_num}')">
            <div class="num">{chapter_num}</div>
            <div class="label">Part {chapter_num}</div>
            <div class="rule"></div>
            <div class="title">{chapter_title}</div>
        </div>''')
        for doc_slug in doc_slugs:
            doc = lookup_doc(index["all_docs"], doc_slug)
            if not doc:
                continue
            a(f'''<div class="chapter" string-set="chapter content('Part {chapter_num}: {doc["title"]}')">
                <div class="chapter-num">PART {chapter_num} · {chapter_title.upper()}</div>
                <h1 class="chapter-title">{html.escape(doc["title"])}</h1>''')
            if doc.get("summary"):
                a(f'<p style="font-style:italic;color:#666;">{html.escape(doc["summary"][:300])}…</p>')
            # Limit each doc to 3000 chars for PDF readability
            a(md_to_html(doc["content"], max_chars=3000))
            a('</div>')

    # ─── Final quote page ───
    a(f'''<div class="divider" string-set="chapter content('Conclusion')">
        <div class="quote" style="background:transparent;color:{NAVY};font-size:14pt;border:none;">
            "The institution is the philosophy in operational form.<br>
            The institution is what the company is becoming.<br>
            The institution is what the Founder has been building toward for years."
        </div>
        <div style="font-family:DejaVu Sans,sans-serif;font-size:8pt;color:#888;margin-top:8mm;letter-spacing:1pt;">— THE EXECUTIVE STRATEGY OFFICE</div>
    </div>''')

    # ─── Closing page ───
    a(f'''<div class="chapter" string-set="chapter content('End')">
        <div style="text-align:center;padding:60mm 0;">
            <div style="font-family:DejaVu Sans,sans-serif;font-size:8pt;color:#888;letter-spacing:4pt;">END OF FX TELLER STRATEGIC BLUEPRINT</div>
            <div style="width:30mm;height:0.5pt;background:{GOLD};margin:8mm auto;"></div>
            <div style="font-family:DejaVu Serif,serif;font-size:11pt;color:#444;margin-top:4mm;">Version 1.0 · July 2026</div>
            <div style="font-family:DejaVu Sans,sans-serif;font-size:7pt;color:#999;margin-top:6mm;letter-spacing:2pt;">PREPARED BY THE EXECUTIVE STRATEGY OFFICE</div>
        </div>
    </div>''')

    html_doc = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>FX Teller · Strategic Blueprint · Founder Edition</title>
<style>{CSS_STYLE}</style>
</head>
<body>
{''.join(parts)}
</body>
</html>"""
    return html_doc


def main():
    OUT_DIR.mkdir(parents=True, exist_ok=True)

    print("Building HTML for PDF...")
    html_content = build_html()
    HTML_PATH.write_text(html_content, encoding="utf-8")
    print(f"  HTML: {HTML_PATH} ({os.path.getsize(HTML_PATH)//1024} KB)")

    print("Rendering PDF with WeasyPrint...")
    HTML(string=html_content, base_url=str(OUT_DIR)).write_pdf(PDF_PATH)
    pdf_size = os.path.getsize(PDF_PATH)
    print(f"  PDF:  {PDF_PATH} ({pdf_size//1024} KB)")


if __name__ == "__main__":
    main()
