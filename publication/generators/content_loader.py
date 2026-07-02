"""
FX Teller Content Loader
Loads documents from docs/, generates automatic frontmatter,
produces structured content for the website, PDF, and PPT.
"""
import os
import re
import yaml
import json
from pathlib import Path
from datetime import datetime

REPO_ROOT = Path("/mnt/d/FX Teller")
DOCS_ROOT = REPO_ROOT / "docs"
PUB_ROOT = REPO_ROOT / "publication"
CONTENT_OUT = PUB_ROOT / "content"

# Map of source folder → (output section slug, display title, description)
FOLDER_MAP = {
    "00_CONTEXT": {
        "slug": "context",
        "title": "Context",
        "description": "Master context, writing guidelines, glossary, project status, decision log",
        "audience": ["Founders", "AI agents", "Strategy Office"],
    },
    "01_FOUNDATION": {
        "slug": "foundation",
        "title": "Foundation",
        "description": "Vision, mission, values, and brand philosophy",
        "audience": ["Founders", "Executives", "Strategy Office"],
    },
    "02_BUSINESS": {
        "slug": "business",
        "title": "Business",
        "description": "Business model, revenue architecture, pricing, and unit economics",
        "audience": ["Founders", "Investors", "Strategy Office"],
    },
    "03_PRODUCT": {
        "slug": "product",
        "title": "Product",
        "description": "Product ecosystem, member experience, and service catalogue",
        "audience": ["Founders", "Product", "Engineering", "Strategy Office"],
    },
    "04_BRAND": {
        "slug": "brand",
        "title": "Brand",
        "description": "Brand identity, voice, and visual system",
        "audience": ["Founders", "Marketing", "Strategy Office"],
    },
    "05_MARKETING": {
        "slug": "marketing",
        "title": "Marketing",
        "description": "Customer personas, go-to-market, and brand launch playbook",
        "audience": ["Founders", "Marketing", "Strategy Office"],
    },
    "06_OPERATIONS": {
        "slug": "operations",
        "title": "Operations",
        "description": "Operating model, product delivery, community, and compliance",
        "audience": ["Founders", "Operations", "Strategy Office"],
    },
    "07_EXECUTION": {
        "slug": "execution",
        "title": "Execution",
        "description": "6-month plan, 24-month roadmap, hiring, and budget",
        "audience": ["Founders", "Executives", "Strategy Office"],
    },
    "08_INVESTOR": {
        "slug": "investor",
        "title": "Investor",
        "description": "Pitch deck, financial model, cap table, and investor updates",
        "audience": ["Investors", "Founders", "Boards"],
    },
    "09_RESEARCH": {
        "slug": "research",
        "title": "Research",
        "description": "Active research, market studies, technical architecture",
        "audience": ["Strategy Office", "Engineering"],
    },
    "10_ARCHIVE": {
        "slug": "archive",
        "title": "Archive",
        "description": "Historical documents (read-only)",
        "audience": ["Founders", "Strategy Office"],
    },
    "98_STRATEGY_OFFICE": {
        "slug": "strategy-office",
        "title": "Strategy Office",
        "description": "Specialist roles and collaboration frameworks",
        "audience": ["Strategy Office", "Founders"],
    },
    "99_GOVERNANCE": {
        "slug": "governance",
        "title": "Governance",
        "description": "Strategic Decision Register — every material decision recorded",
        "audience": ["Founders", "Boards", "Investors", "Strategy Office"],
    },
}


def title_from_filename(name: str) -> str:
    """Convert 'Master_Context.md' to 'Master Context'."""
    return re.sub(r"[_\-]+", " ", Path(name).stem).strip()


def slugify(text: str) -> str:
    s = re.sub(r"[^\w\s-]", "", text.lower())
    s = re.sub(r"[_\s-]+", "-", s).strip("-")
    return s or "untitled"


def extract_first_paragraph(content: str) -> str:
    """Get the first non-heading paragraph from a markdown doc."""
    lines = content.split("\n")
    para_lines = []
    in_para = False
    for line in lines:
        if line.startswith("#") or line.startswith("---") or line.startswith(">"):
            if in_para:
                break
            continue
        if line.strip() == "":
            if in_para:
                break
            continue
        in_para = True
        para_lines.append(line.strip())
    text = " ".join(para_lines)
    text = re.sub(r"\*\*(.+?)\*\*", r"\1", text)
    text = re.sub(r"\*(.+?)\*", r"\1", text)
    text = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", text)
    return text[:500] + ("…" if len(text) > 500 else "")


def extract_key_insights(content: str, max_insights: int = 5) -> list:
    """Extract bullet points as key insights."""
    insights = []
    for line in content.split("\n"):
        stripped = line.strip()
        if stripped.startswith("- ") or stripped.startswith("* "):
            text = stripped[2:].strip()
            text = re.sub(r"\*\*(.+?)\*\*", r"\1", text)
            text = re.sub(r"\*(.+?)\*", r"\1", text)
            if 20 < len(text) < 300 and not text.startswith("**"):
                insights.append(text)
                if len(insights) >= max_insights:
                    break
    return insights


def extract_h1(content: str) -> str:
    """Get the first H1 from content."""
    for line in content.split("\n"):
        if line.startswith("# "):
            return line[2:].strip()
    return ""


def count_words(content: str) -> int:
    """Count words in markdown content."""
    text = re.sub(r"[#*_`>|]", " ", content)
    text = re.sub(r"\s+", " ", text)
    return len(text.split())


def count_sections(content: str) -> int:
    """Count H2 sections."""
    return sum(1 for line in content.split("\n") if line.startswith("## "))


def load_doc(folder: str, filename: str) -> dict:
    """Load a single document and generate its frontmatter."""
    path = DOCS_ROOT / folder / filename
    if not path.exists():
        return None
    content = path.read_text(encoding="utf-8")
    title = extract_h1(content) or title_from_filename(filename)
    return {
        "title": title,
        "filename": filename,
        "slug": slugify(filename),
        "folder": folder,
        "folder_slug": FOLDER_MAP[folder]["slug"],
        "content": content,
        "summary": extract_first_paragraph(content),
        "key_insights": extract_key_insights(content),
        "word_count": count_words(content),
        "section_count": count_sections(content),
        "url": f"/{FOLDER_MAP[folder]['slug']}/{slugify(filename)}",
    }


def load_all_docs() -> dict:
    """Walk docs/ and return all documents organized by section."""
    sections = {}
    for folder in sorted(os.listdir(DOCS_ROOT)):
        if not (DOCS_ROOT / folder).is_dir():
            continue
        if folder not in FOLDER_MAP:
            continue
        meta = FOLDER_MAP[folder]
        docs = []
        for filename in sorted(os.listdir(DOCS_ROOT / folder)):
            if filename.endswith(".md"):
                doc = load_doc(folder, filename)
                if doc:
                    docs.append(doc)
        if docs:
            sections[meta["slug"]] = {
                "title": meta["title"],
                "description": meta["description"],
                "audience": list(meta["audience"]),
                "docs": docs,
            }
    return sections


def related_docs(current: dict, all_docs: list, max_related: int = 3) -> list:
    """Find related docs by shared keywords."""
    text = (current["title"] + " " + current["summary"]).lower()
    keywords = set(re.findall(r"\b[a-z]{4,}\b", text))
    scored = []
    for other in all_docs:
        if other["url"] == current["url"]:
            continue
        other_text = (other["title"] + " " + other["summary"]).lower()
        other_kw = set(re.findall(r"\b[a-z]{4,}\b", other_text))
        overlap = len(keywords & other_kw)
        if overlap > 0:
            scored.append((overlap, other))
    scored.sort(key=lambda x: -x[0])
    # Return minimal info to avoid circular references
    return [
        {"title": d["title"], "url": d["url"], "summary": d["summary"][:200]}
        for _, d in scored[:max_related]
    ]


def build_index() -> dict:
    """Build the full publication index."""
    sections = load_all_docs()
    all_docs = []
    for slug, section in sections.items():
        for doc in section["docs"]:
            all_docs.append(doc)
    for section in sections.values():
        for doc in section["docs"]:
            doc["related"] = related_docs(doc, all_docs)
    return {
        "generated_at": datetime.now().isoformat(),
        "total_docs": len(all_docs),
        "total_words": sum(d["word_count"] for d in all_docs),
        "sections": sections,
        "all_docs": all_docs,
    }


def main():
    print("Loading FX Teller knowledge base...")
    index = build_index()
    print(f"  Total docs: {index['total_docs']}")
    print(f"  Total words: {index['total_words']:,}")
    print(f"  Sections: {len(index['sections'])}")

    # Save index
    out_index = PUB_ROOT / "build" / "index.json"
    out_index.parent.mkdir(parents=True, exist_ok=True)
    # Make a deep copy to avoid circular references
    import copy
    serializable = copy.deepcopy(index)
    for doc in serializable["all_docs"]:
        doc.pop("content", None)
    for section in serializable["sections"].values():
        for doc in section["docs"]:
            doc.pop("content", None)
    with open(out_index, "w") as f:
        json.dump(serializable, f, indent=2)
    print(f"  Saved: {out_index}")

    # Print sections
    for slug, section in index["sections"].items():
        print(f"  {section['title']} ({slug}): {len(section['docs'])} docs")
        for doc in section["docs"]:
            print(f"    - {doc['title']} ({doc['word_count']} words)")


if __name__ == "__main__":
    main()
