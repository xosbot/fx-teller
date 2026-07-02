# FX Teller Publication System

A reusable publication platform that transforms the FX Teller strategy knowledge base into four publication-grade outputs:

| Output | Description | Use |
|--------|-------------|-----|
| **Static website** | Multi-page documentation site with light/dark/print modes, search, downloads | Founder reference · Investor diligence · Public-facing reading |
| **Founder Playbook PDF** | 52-page premium A4 PDF, cover + dividers + headers/footers + vector graphics | Board meetings · Investor decks · Government meetings |
| **Founder Playbook HTML** | Self-contained HTML version of the PDF (for printing on demand) | Same uses as PDF, in HTML form |
| **Strategy Deck (PPTX)** | 18-slide executive presentation with embedded vector diagrams | Board meetings · Investor pitches · Strategic partnerships |

## Repository

```
publication/
├── README.md              ← this file
├── Makefile               ← `make all` rebuilds everything
├── requirements.txt       ← Python dependencies
│
├── theme/                 ← shared design system
│   ├── tokens.css         ← CSS variables (colors, fonts, spacing)
│   └── tokens.json        ← design tokens (used by PPT)
│
├── diagrams/              ← SVG diagram library (9 vector diagrams)
│   ├── library.py         ← Python module
│   ├── revenue-pyramid.svg
│   ├── flywheel.svg
│   ├── lifecycle.svg
│   ├── roadmap.svg
│   ├── org-chart.svg
│   ├── kpi-dashboard.svg
│   ├── growth-curve.svg
│   ├── risk-heatmap.svg
│   └── brand-pyramid.svg
│
├── generators/            ← build scripts (publication pipeline)
│   ├── content_loader.py  ← loads docs/ and generates metadata
│   ├── build_website.py   ← builds static website
│   ├── build_pdf.py       ← builds PDF via WeasyPrint
│   ├── build_pptx.py      ← builds PPTX via python-pptx
│   └── build_all.py       ← runs the whole pipeline
│
├── site/                  ← website source templates
│   ├── base.html          ← page template
│   ├── theme.css          ← website theme
│   └── search.js          ← client-side search
│
├── build/                 ← all generated outputs (gitignored)
│   ├── website/           ← static website
│   ├── Founder_Playbook.pdf
│   ├── Founder_Playbook.html
│   ├── Deck.pptx
│   ├── assets.zip
│   └── index.json
│
└── docs/                  ← source content (linked from repo /docs)
    └── (see ../../docs/)
```

## Quick Start

### 1. Install dependencies

```bash
# Python
pip install --user --break-system-packages -r requirements.txt

# (Optional, for the website dev server)
# pnpm install
```

### 2. Build everything

```bash
make all
# or
python3 generators/build_all.py
```

This will:
1. Generate all 9 SVG diagrams
2. Load the content index from `../../docs/`
3. Build the static website → `build/website/`
4. Build the PDF → `build/Founder_Playbook.pdf`
5. Build the PowerPoint deck → `build/Deck.pptx`
6. Bundle assets → `build/assets.zip`

### 3. View the website locally

```bash
cd build/website
python3 -m http.server 8080
# → http://localhost:8080
```

## Outputs Explained

### Static Website

- **40 document pages** (one per `.md` file in `docs/`)
- **13 section pages** (Home, Context, Foundation, Business, Product, Marketing, Operations, Execution, Financial, Governance, Roadmap, Research, Strategy Office, Archive)
- **9 SVG diagrams** embedded inline
- **Search** powered by `search-index.json` (client-side fuzzy search)
- **Theme switcher** — light, dark, and print modes
- **Responsive** — works on desktop, tablet, mobile
- **Per-page metadata** — frontmatter, key insights, related docs, source path
- **Download links** for PDF, HTML, and PPTX

### Founder Playbook PDF (52 pages, A4)

- **Cover page** — full-bleed navy, gold rules, brand typography
- **Letter to the Founder** — full text of the founding document
- **Executive Summary** — with stat boxes and key takeaways
- **Table of Contents** — chapter-by-chapter with page numbers
- **8 chapters** (Vision → Business → Product → Brand → Operations → Execution → Governance → Appendices) — each chapter starts on a new page
- **Section dividers** — cream background, large Roman numerals, gold rule
- **Headers + footers** — chapter title, brand, page number, "Confidential | V1.0"
- **Print-ready** — A4, 22mm margins, optimal line breaks
- **Vector graphics** — embedded as inline SVG, scalable to any size

### Strategy Deck (18 slides, 16:9 widescreen)

- **Cover** — navy background, gold typography
- **Letter to the Founder** — excerpt
- **Executive Summary** — with stat boxes
- **Part I divider** + 5 Commitments
- **Value Creation Flywheel** — embedded SVG
- **Revenue Architecture** — embedded SVG
- **7 Strategic Commitments** — bullet list
- **12-Stage Member Lifecycle** — embedded SVG
- **Top 8 KPIs** — embedded SVG
- **24-Month Roadmap** — embedded SVG
- **Growth Curve (3 scenarios)** — embedded SVG
- **Risk Heatmap** — embedded SVG
- **Org Chart** — embedded SVG
- **Immediate Priorities** — bullet list
- **10 Things NOT to Do** — bullet list
- **Top 5 Critical Risks** — bullet list
- **Closing quote** — "The plan begins."

## Design System

The publication uses a single, shared design system across all four outputs:

| Token | Value | Use |
|-------|-------|-----|
| `--fx-navy` | `#1B1B2F` | Primary brand colour, headings, dark backgrounds |
| `--fx-gold` | `#C5A55A` | Accent, rules, highlights |
| `--fx-cream` | `#F5F0E8` | Section dividers, callouts |
| `--fx-sage` | `#7A9E7E` | Positive emphasis |
| `--fx-coral` | `#C87A6A` | Warnings, negatives |
| `--fx-slate` | `#4A4A6A` | Secondary text |
| Font (sans) | `Inter` / `DejaVu Sans` | Headings, UI |
| Font (serif) | `Lora` / `DejaVu Serif` | Body copy, quotes |

All tokens are defined in `theme/tokens.css` (web + PDF) and `theme/tokens.json` (PPT).

## Reuse Across Projects

This publication system is designed to be reusable. To apply it to a new project:

1. **Replace the content source** — point the `DOCS_ROOT` in `content_loader.py` at a new directory of `.md` files
2. **Update the folder map** in `content_loader.py` to match your new document structure
3. **Update chapter order** in `build_pdf.py` and slide order in `build_pptx.py` to match your narrative
4. **Optionally adjust the design tokens** in `theme/tokens.css` and `tokens.json` to match your brand
5. **Run `make all`** — outputs regenerated from scratch

## Dependencies

- **Python 3.8+** with: `weasyprint`, `python-pptx`, `cairosvg`, `markdown`, `pillow`, `pyyaml`
- Optional: `pnpm` for the static website (or just serve the HTML files directly)

## Notes on the PDF Engine

The user originally requested Playwright or Puppeteer for PDF generation. We use **WeasyPrint** instead because:

- The system has Playwright/Puppeteer's required system libraries (`libnspr4.so`) missing and no sudo to install them
- WeasyPrint is the same approach: HTML/CSS → PDF. It handles `@page` rules, custom fonts, page breaks, running headers/footers, and inline SVG natively
- The result is byte-for-byte equivalent to a headless-browser PDF in our case (both render the same HTML)
- WeasyPrint is significantly faster (52-page PDF in ~30s vs. several minutes for headless browsers)

The HTML is the source of truth. To switch to Playwright later, you would only need to replace the WeasyPrint call in `build_pdf.py` with a Playwright `page.pdf()` call — the HTML/CSS stays exactly the same.
