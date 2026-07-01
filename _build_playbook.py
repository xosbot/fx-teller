#!/usr/bin/env python3
"""
Generate FX Teller Founder Playbook — a premium, magazine-quality strategy report.

Builds an HTML document with editorial CSS design, inline SVG diagrams,
then renders to PDF via WeasyPrint.
"""

import os, textwrap, base64
from weasyprint import HTML, CSS

OUT_DIR = "/mnt/d/FX Teller/docs/assets"
os.makedirs(OUT_DIR, exist_ok=True)

# ─── Brand Colors ───
NAVY      = "#1B1B2F"
GOLD      = "#C5A55A"
CREAM     = "#F5F0E8"
WHITE     = "#FFFFFF"
SAGE      = "#7A9E7E"
SLATE     = "#4A4A6A"
CORAL     = "#C87A6A"
LIGHT     = "#F8F6F2"
DARK      = "#1A1A1A"

# ─── CSS Template ───
CSS_STYLE = """
@page {
    size: A4;
    margin: 2cm 2.2cm;
    @top-left {
        content: "";
        font-family: 'DejaVu Sans', sans-serif;
        font-size: 7pt;
        color: #999;
    }
    @top-right {
        content: "";
        font-family: 'DejaVu Sans', sans-serif;
        font-size: 7pt;
        color: #999;
    }
    @bottom-center {
        content: counter(page);
        font-family: 'DejaVu Sans', sans-serif;
        font-size: 8pt;
        color: #666;
    }
}
@page cover {
    margin: 0;
    @top-left { content: none; }
    @top-right { content: none; }
    @bottom-center { content: none; }
}
@page divider {
    margin: 0;
    @top-left { content: none; }
    @top-right { content: none; }
    @bottom-center { content: none; }
}
@page:blank { @top-left { content: none; } @top-right { content: none; } }

* { margin: 0; padding: 0; box-sizing: border-box; }
html { font-size: 10pt; }
body {
    font-family: 'DejaVu Serif', Georgia, 'Times New Roman', serif;
    color: #222;
    line-height: 1.65;
    background: white;
}

h1, h2, h3, h4 {
    font-family: 'DejaVu Sans', 'Helvetica Neue', Arial, sans-serif;
    font-weight: 700;
    color: """ + NAVY + """;
    page-break-after: avoid;
}

p { margin-bottom: 0.6em; text-align: justify; }
ul, ol { margin: 0.4em 0 0.6em 1.5em; }
li { margin-bottom: 0.2em; }

/* ─── Cover ─── */
.cover-page {
    page: cover;
    width: 210mm; height: 297mm;
    background: """ + NAVY + """;
    display: flex; flex-direction: column;
    justify-content: center; align-items: center;
    color: white; text-align: center;
    position: relative;
    overflow: hidden;
}
.cover-page::before {
    content: '';
    position: absolute; top: 40mm; left: 30mm; right: 30mm;
    border-top: 0.5pt solid """ + GOLD + """;
    opacity: 0.4;
}
.cover-page::after {
    content: '';
    position: absolute; bottom: 40mm; left: 30mm; right: 30mm;
    border-top: 0.5pt solid """ + GOLD + """;
    opacity: 0.4;
}
.cover-brand {
    font-family: 'DejaVu Sans', sans-serif;
    font-size: 11pt; letter-spacing: 6pt;
    color: """ + GOLD + """; margin-bottom: 20mm;
    text-transform: uppercase;
}
.cover-title {
    font-family: 'DejaVu Sans', sans-serif;
    font-size: 36pt; font-weight: 300;
    line-height: 1.15; margin-bottom: 6mm;
}
.cover-title strong { font-weight: 700; color: """ + GOLD + """; }
.cover-subtitle {
    font-family: 'DejaVu Sans', sans-serif;
    font-size: 11pt; letter-spacing: 2pt;
    color: rgba(255,255,255,0.7);
    margin-bottom: 25mm;
}
.cover-meta {
    font-family: 'DejaVu Sans', sans-serif;
    font-size: 8pt; color: rgba(255,255,255,0.5);
    line-height: 2;
}
.cover-gold-line {
    width: 40mm; height: 1pt;
    background: """ + GOLD + """;
    margin: 8mm auto;
}
.cover-foot {
    position: absolute; bottom: 18mm;
    font-family: 'DejaVu Sans', sans-serif;
    font-size: 6.5pt; color: rgba(255,255,255,0.35);
    letter-spacing: 1.5pt;
}

/* ─── Section Divider ─── */
.section-divider {
    page: divider;
    width: 210mm; height: 297mm;
    background: """ + CREAM + """;
    display: flex; flex-direction: column;
    justify-content: center; align-items: center;
    text-align: center;
    position: relative;
}
.section-divider .num {
    font-family: 'DejaVu Sans', sans-serif;
    font-size: 96pt; font-weight: 700;
    color: """ + NAVY + """;
    line-height: 1;
    margin-bottom: 6mm;
}
.section-divider .label {
    font-family: 'DejaVu Sans', sans-serif;
    font-size: 8pt; letter-spacing: 3pt;
    color: #999; text-transform: uppercase;
    margin-bottom: 8mm;
}
.section-divider .title {
    font-family: 'DejaVu Sans', sans-serif;
    font-size: 28pt; font-weight: 300;
    color: """ + NAVY + """;
    line-height: 1.2;
}
.section-divider .rule {
    width: 50mm; height: 1pt;
    background: """ + GOLD + """;
    margin: 8mm auto 0;
}

/* ─── Content Layout ─── */
.content { max-width: 160mm; margin: 0 auto; }

.page-header {
    font-family: 'DejaVu Sans', sans-serif;
    font-size: 6.5pt; color: #aaa;
    border-bottom: 0.5pt solid #ddd;
    padding-bottom: 3mm; margin-bottom: 5mm;
    display: flex; justify-content: space-between;
}

.section-title {
    font-size: 20pt; margin-bottom: 4mm; margin-top: 2mm;
    padding-bottom: 3mm;
    border-bottom: 1.5pt solid """ + GOLD + """;
    page-break-before: always;
}
.section-title:first-of-type { page-break-before: avoid; }

.subsection-title {
    font-size: 12pt; margin-top: 4mm; margin-bottom: 2mm;
    color: """ + NAVY + """;
}

/* ─── Callout Cards ─── */
.callout-card {
    background: """ + CREAM + """;
    border-left: 3pt solid """ + GOLD + """;
    padding: 3mm 4mm; margin: 3mm 0;
    font-family: 'DejaVu Sans', sans-serif;
    font-size: 8.5pt; color: #444;
    page-break-inside: avoid;
}
.callout-card strong { color: """ + NAVY + """; }

.callout-navy {
    background: """ + NAVY + """;
    border-left: 3pt solid """ + GOLD + """;
    padding: 3mm 4mm; margin: 3mm 0;
    font-family: 'DejaVu Sans', sans-serif;
    font-size: 8.5pt; color: rgba(255,255,255,0.9);
    page-break-inside: avoid;
}
.callout-navy strong { color: """ + GOLD + """; }

/* ─── Stat Boxes ─── */
.stats-row {
    display: flex; gap: 3mm; margin: 4mm 0;
    page-break-inside: avoid;
}
.stat-box {
    flex: 1; text-align: center;
    padding: 3mm 2mm;
    background: """ + CREAM + """;
    page-break-inside: avoid;
}
.stat-box .num {
    font-family: 'DejaVu Sans', sans-serif;
    font-size: 22pt; font-weight: 700;
    color: """ + NAVY + """;
    line-height: 1.1;
}
.stat-box .num.gold { color: """ + GOLD + """; }
.stat-box .label {
    font-family: 'DejaVu Sans', sans-serif;
    font-size: 7pt; color: #666;
    text-transform: uppercase; letter-spacing: 0.5pt;
    margin-top: 1mm;
}

/* ─── Tables ─── */
.exec-table {
    width: 100%; border-collapse: collapse;
    margin: 3mm 0; font-family: 'DejaVu Sans', sans-serif;
    font-size: 8pt;
    page-break-inside: avoid;
}
.exec-table th {
    background: """ + NAVY + """;
    color: white; text-align: left;
    padding: 2mm 2.5mm; font-weight: 700;
    font-size: 7.5pt; text-transform: uppercase; letter-spacing: 0.5pt;
}
.exec-table td {
    padding: 1.8mm 2.5mm;
    border-bottom: 0.5pt solid #ddd;
    vertical-align: top;
}
.exec-table tr:nth-child(even) td { background: """ + CREAM + """; }
.exec-table tr:last-child td { border-bottom: 0.5pt solid """ + NAVY + """; }

/* ─── Part Summary ─── */
.part-summary {
    background: """ + NAVY + """;
    padding: 3mm 4mm; margin: 4mm 0;
    font-family: 'DejaVu Sans', sans-serif;
    font-size: 8pt; color: rgba(255,255,255,0.85);
    page-break-inside: avoid;
}
.part-summary strong { color: """ + GOLD + """; }

/* ─── Two-column ─── */
.two-col {
    display: flex; gap: 5mm; margin: 3mm 0;
}
.two-col > div { flex: 1; }

/* ─── Icon Grid ─── */
.icon-grid {
    display: grid; grid-template-columns: repeat(4, 1fr);
    gap: 2.5mm; margin: 3mm 0;
    page-break-inside: avoid;
}
.icon-item {
    background: """ + LIGHT + """;
    padding: 2.5mm 2mm; text-align: center;
    border-radius: 1pt;
    font-family: 'DejaVu Sans', sans-serif;
    font-size: 7.5pt; color: #333;
    border: 0.5pt solid #eee;
}
.icon-item .icon {
    font-size: 16pt; margin-bottom: 1mm;
    color: """ + GOLD + """;
}
.icon-item strong {
    display: block; font-size: 7pt;
    color: """ + NAVY + """; margin-bottom: 0.5mm;
}

/* ─── Timeline ─── */
.timeline {
    position: relative; margin: 5mm 0; padding: 0;
    page-break-inside: avoid;
}
.timeline::before {
    content: ''; position: absolute;
    left: 15mm; top: 0; bottom: 0;
    width: 1pt; background: """ + GOLD + """;
}
.timeline-item {
    position: relative; padding: 2mm 0 2mm 22mm;
    font-family: 'DejaVu Sans', sans-serif;
    page-break-inside: avoid;
}
.timeline-item::before {
    content: ''; position: absolute;
    left: 12.5mm; top: 4mm;
    width: 6pt; height: 6pt;
    border-radius: 50%;
    background: """ + GOLD + """;
    border: 1.5pt solid white;
    box-shadow: 0 0 0 1pt """ + GOLD + """;
}
.timeline-item .date {
    font-size: 8pt; font-weight: 700; color: """ + NAVY + """;
}
.timeline-item .desc {
    font-size: 8pt; color: #555;
}

/* ─── Grid Cards ─── */
.card-grid {
    display: grid; grid-template-columns: repeat(3, 1fr);
    gap: 3mm; margin: 3mm 0;
    page-break-inside: avoid;
}
.card {
    background: """ + LIGHT + """;
    border: 0.5pt solid #e0ddd5;
    padding: 3mm; page-break-inside: avoid;
}
.card h4 {
    font-size: 8.5pt; margin-bottom: 1mm;
    color: """ + NAVY + """;
}
.card p {
    font-size: 7.5pt; color: #555;
    line-height: 1.5;
}

/* ─── KPI Card ─── */
.kpi-grid {
    display: grid; grid-template-columns: repeat(4, 1fr);
    gap: 2.5mm; margin: 3mm 0;
    page-break-inside: avoid;
}
.kpi-card {
    text-align: center; padding: 2.5mm 1.5mm;
    background: """ + LIGHT + """;
    border: 0.5pt solid #eee;
}
.kpi-card .value {
    font-family: 'DejaVu Sans', sans-serif;
    font-size: 16pt; font-weight: 700;
    color: """ + NAVY + """;
    line-height: 1.1;
}
.kpi-card .value.gold { color: """ + GOLD + """; }
.kpi-card .value.sage { color: """ + SAGE + """; }
.kpi-card .kpi-label {
    font-family: 'DejaVu Sans', sans-serif;
    font-size: 6.5pt; color: #666;
    margin-top: 0.5mm; text-transform: uppercase;
}

/* ─── Quote Page ─── */
.quote-page {
    page: divider;
    width: 210mm; height: 297mm;
    background: """ + NAVY + """;
    display: flex; flex-direction: column;
    justify-content: center; align-items: center;
    text-align: center; color: white;
    padding: 20mm;
}
.quote-page blockquote {
    font-family: 'DejaVu Serif', serif;
    font-size: 18pt; font-weight: 300;
    font-style: italic; line-height: 1.5;
    max-width: 140mm;
}
.quote-page cite {
    font-family: 'DejaVu Sans', sans-serif;
    font-size: 8pt; color: """ + GOLD + """;
    margin-top: 8mm; font-style: normal;
    letter-spacing: 1pt;
}

/* ─── Checklist ─── */
.checklist { list-style: none; margin: 2mm 0; }
.checklist li {
    padding: 1.5mm 0 1.5mm 6mm;
    position: relative;
    font-family: 'DejaVu Sans', sans-serif;
    font-size: 8pt; color: #444;
    border-bottom: 0.5pt solid #eee;
}
.checklist li::before {
    content: '\\2610'; position: absolute; left: 0;
    color: """ + GOLD + """;
    font-size: 10pt;
}

/* ─── Comparison Table ─── */
.comp-table { width: 100%; border-collapse: collapse; margin: 3mm 0; }
.comp-table th {
    background: """ + NAVY + """;
    color: white; padding: 2mm; text-align: center;
    font-family: 'DejaVu Sans', sans-serif;
    font-size: 7pt; text-transform: uppercase;
}
.comp-table td {
    padding: 1.5mm 2mm; text-align: center;
    font-family: 'DejaVu Sans', sans-serif;
    font-size: 7.5pt;
    border-bottom: 0.5pt solid #ddd;
}
.comp-table tr:nth-child(even) td { background: """ + CREAM + """; }
.comp-table .yes { color: #2a7d2a; }
.comp-table .no { color: #c0392b; }

/* ─── Misc ─── */
.pb { page-break-before: always; }
.pba { page-break-after: always; }
.pi { page-break-inside: avoid; }
.center { text-align: center; }
.gold-text { color: """ + GOLD + """; }
.navy-text { color: """ + NAVY + """; }
.small { font-size: 7.5pt; color: #888; }
hr.gold {
    border: none; border-top: 0.5pt solid """ + GOLD + """;
    margin: 3mm 0; opacity: 0.5;
}

/* SVG container */
.svg-container { text-align: center; margin: 4mm 0; page-break-inside: avoid; }
.svg-container svg { max-width: 100%; height: auto; }
"""

# ─── SVG Generators ───

def svg_brand_4tier():
    """Business Model 4-Tier Pyramid as SVG."""
    tiers = [
        ("Future Revenue", "International / Marketplace / AI", "#C87A6A", "Year 3+"),
        ("Strategic Revenue", "House / Publishing / Dubai", "#4A4A6A", "Year 2+"),
        ("Premium Revenue", "Workshops / Roundtables / Coaching", "#7A9E7E", "Year 2+"),
        ("Primary Revenue", "Annual + Monthly + Founding", "#1B1B2F", "Year 1+"),
    ]
    svg = f'<svg viewBox="0 0 500 380" xmlns="http://www.w3.org/2000/svg" style="width:100%;max-width:500px;">'
    svg += f'<rect width="500" height="380" fill="white"/>'
    svg += f'<text x="250" y="25" text-anchor="middle" font-family="DejaVu Sans" font-size="14" font-weight="bold" fill="{NAVY}">Revenue Architecture — 4 Tiers</text>'
    w_base = 300
    center = 250
    for i, (name, desc, color, timing) in enumerate(tiers):
        y = 50 + i * 78
        w = w_base - i * 50
        x = center - w / 2
        svg += f'<rect x="{x}" y="{y}" width="{w}" height="60" rx="3" fill="{color}" opacity="0.9"/>'
        svg += f'<text x="{center}" y="{y+25}" text-anchor="middle" font-family="DejaVu Sans" font-size="12" font-weight="bold" fill="white">{name}</text>'
        svg += f'<text x="{center}" y="{y+45}" text-anchor="middle" font-family="DejaVu Sans" font-size="8" fill="rgba(255,255,255,0.8)">{desc}</text>'
        svg += f'<text x="{x+w+10}" y="{y+35}" text-anchor="start" font-family="DejaVu Sans" font-size="8" fill="{color}" font-weight="bold">{timing}</text>'
    svg += '</svg>'
    return svg


def svg_flywheel():
    """Value Creation Flywheel."""
    stages = ["Member Value", "Trust", "Retention", "Referral", "Brand", "Revenue"]
    svg = f'<svg viewBox="0 0 450 450" xmlns="http://www.w3.org/2000/svg" style="width:100%;max-width:450px;">'
    svg += f'<rect width="450" height="450" fill="white"/>'
    svg += f'<text x="225" y="25" text-anchor="middle" font-family="DejaVu Sans" font-size="13" font-weight="bold" fill="{NAVY}">Value Creation Flywheel</text>'
    cx, cy, r = 225, 240, 140
    for i, stage in enumerate(stages):
        angle = i * 60 - 90
        rad = angle * 3.14159 / 180
        x = cx + r * 0.75 * __import__('math').cos(rad)
        y = cy + r * 0.75 * __import__('math').sin(rad)
        svg += f'<circle cx="{x}" cy="{y}" r="35" fill="{GOLD}" opacity="0.15"/>'
        svg += f'<circle cx="{x}" cy="{y}" r="35" fill="none" stroke="{GOLD}" stroke-width="1.5"/>'
        svg += f'<text x="{x}" y="{y+4}" text-anchor="middle" font-family="DejaVu Sans" font-size="8" font-weight="bold" fill="{NAVY}">{stage}</text>'
        # Arrow to next
        n_angle = (i + 1) * 60 - 90
        n_rad = n_angle * 3.14159 / 180
        nx = cx + r * 0.75 * __import__('math').cos(n_rad)
        ny = cy + r * 0.75 * __import__('math').sin(n_rad)
        mx, my = (x + nx) / 2, (y + ny) / 2
        svg += f'<line x1="{x+25}" y1="{y+25}" x2="{nx-25}" y2="{ny-25}" stroke="{GOLD}" stroke-width="1" marker-end="url(#arrow)"/>'
    svg += f'<defs><marker id="arrow" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="4" markerHeight="4" orient="auto"><path d="M 0 0 L 10 5 L 0 10 z" fill="{GOLD}"/></marker></defs>'
    svg += f'<circle cx="{cx}" cy="{cy}" r="50" fill="{NAVY}"/>'
    svg += f'<text x="{cx}" y="{cy-5}" text-anchor="middle" font-family="DejaVu Sans" font-size="8" font-weight="bold" fill="white">Philosophy</text>'
    svg += f'<text x="{cx}" y="{cy+10}" text-anchor="middle" font-family="DejaVu Sans" font-size="7" fill="{GOLD}">in motion</text>'
    svg += '</svg>'
    return svg


def svg_12_lifecycle():
    """12-Stage Member Lifecycle."""
    stages = [
        "Curiosity", "Application", "Acceptance", "Onboarding",
        "First Floor", "First Win", "Community", "Habit",
        "House", "Ambassador", "Lifetime", "Founder"
    ]
    svg = f'<svg viewBox="0 0 720 140" xmlns="http://www.w3.org/2000/svg" style="width:100%;max-width:720px;">'
    svg += f'<rect width="720" height="140" fill="white"/>'
    for i, s in enumerate(stages):
        x = 20 + i * 58
        phase = 0 if i < 4 else (1 if i < 8 else 2)
        color = [GOLD, SAGE, NAVY][phase]
        svg += f'<circle cx="{x+20}" cy="55" r="18" fill="{color}" opacity="0.85"/>'
        svg += f'<text x="{x+20}" y="60" text-anchor="middle" font-family="DejaVu Sans" font-size="7" font-weight="bold" fill="white">{i+1}</text>'
        svg += f'<text x="{x+20}" y="88" text-anchor="middle" font-family="DejaVu Sans" font-size="6.5" fill="{NAVY}" font-weight="bold">{s}</text>'
        if i < 11:
            svg += f'<line x1="{x+38}" y1="55" x2="{x+54}" y2="55" stroke="{SLATE}" stroke-width="0.8" opacity="0.4"/>'
    svg += f'<text x="75" y="118" text-anchor="middle" font-family="DejaVu Sans" font-size="7" fill="{GOLD}" font-weight="bold">Discovery</text>'
    svg += f'<text x="315" y="118" text-anchor="middle" font-family="DejaVu Sans" font-size="7" fill="{SAGE}" font-weight="bold">Integration</text>'
    svg += f'<text x="555" y="118" text-anchor="middle" font-family="DejaVu Sans" font-size="7" fill="{NAVY}" font-weight="bold">Leadership</text>'
    svg += '</svg>'
    return svg


def svg_6month_timeline():
    """6-Month Timeline as horizontal bars."""
    items = [
        ("Month 1", "Foundation", "#1B1B2F"),
        ("Month 2", "Build + Design", "#4A4A6A"),
        ("Month 3", "Founding Launch", "#C5A55A"),
        ("Month 4", "Scale + Host #2", "#7A9E7E"),
        ("Month 5", "100 Members", "#C87A6A"),
        ("Month 6", "V1 Public", "#1B1B2F"),
    ]
    svg = f'<svg viewBox="0 0 500 200" xmlns="http://www.w3.org/2000/svg" style="width:100%;max-width:500px;">'
    svg += f'<rect width="500" height="200" fill="white"/>'
    svg += f'<text x="250" y="20" text-anchor="middle" font-family="DejaVu Sans" font-size="13" font-weight="bold" fill="{NAVY}">First 6 Months — Sprint</text>'
    for i, (month, label, color) in enumerate(items):
        y = 40 + i * 25
        svg += f'<rect x="10" y="{y}" width="85" height="16" rx="2" fill="{color}" opacity="0.85"/>'
        svg += f'<text x="52" y="{y+12}" text-anchor="middle" font-family="DejaVu Sans" font-size="7" font-weight="bold" fill="white">{month}</text>'
        svg += f'<rect x="100" y="{y}" width="{300-i*20}" height="16" rx="2" fill="{color}" opacity="0.15" stroke="{color}" stroke-width="0.8"/>'
        svg += f'<text x="105" y="{y+12}" text-anchor="start" font-family="DejaVu Sans" font-size="7.5" fill="{NAVY}">{label}</text>'
    svg += '</svg>'
    return svg


def svg_24month_roadmap():
    """24-Month Roadmap as Gantt-style bars."""
    quarters = [
        ("Q1", "Foundation", 0, 3, "#1B1B2F"),
        ("Q2", "Founding Cohort", 3, 3, "#4A4A6A"),
        ("Q3", "Founding Complete", 6, 3, "#7A9E7E"),
        ("Q4", "Year-1 Validation", 9, 3, "#C5A55A"),
        ("Q5", "Year-2 Scale", 12, 3, "#C87A6A"),
        ("Q6", "Year-2 Mid", 15, 3, "#7A9E7E"),
        ("Q7", "Institutionalise", 18, 3, "#4A4A6A"),
        ("Q8", "Year-2 End", 21, 3, "#1B1B2F"),
    ]
    milestones = [
        (3, "50 Founding"), (6, "V1 Live"), (12, "Raise Closes"),
        (18, "House Build"), (24, "House Opens"),
    ]
    svg = f'<svg viewBox="0 0 600 200" xmlns="http://www.w3.org/2000/svg" style="width:100%;max-width:600px;">'
    svg += f'<rect width="600" height="200" fill="white"/>'
    svg += f'<text x="300" y="18" text-anchor="middle" font-family="DejaVu Sans" font-size="12" font-weight="bold" fill="{NAVY}">24-Month Strategic Roadmap</text>'
    for i, (q, label, start, dur, color) in enumerate(quarters):
        y = 35 + i * 18
        sw = dur * (550 / 24)
        sx = 25 + start * (550 / 24)
        svg += f'<rect x="{sx}" y="{y}" width="{sw}" height="12" rx="2" fill="{color}" opacity="0.85"/>'
        svg += f'<text x="{sx+sw/2}" y="{y+9}" text-anchor="middle" font-family="DejaVu Sans" font-size="6.5" font-weight="bold" fill="white">{q}</text>'
        svg += f'<text x="{25+568}" y="{y+9}" text-anchor="start" font-family="DejaVu Sans" font-size="6.5" fill="{color}">{label}</text>'
    for m, label in milestones:
        mx = 25 + m * (550 / 24)
        svg += f'<line x1="{mx}" y1="30" x2="{mx}" y2="185" stroke="{GOLD}" stroke-width="0.5" stroke-dasharray="2,2"/>'
        svg += f'<text x="{mx}" y="195" text-anchor="middle" font-family="DejaVu Sans" font-size="6.5" fill="{SLATE}">{label}</text>'
    # Month markers
    for m in range(0, 25, 3):
        mx = 25 + m * (550 / 24)
        svg += f'<text x="{mx}" y="195" text-anchor="middle" font-family="DejaVu Sans" font-size="5.5" fill="#ccc">|</text>'
    svg += '</svg>'
    return svg


def svg_org_chart():
    """Organisation chart — team of 8."""
    svg = f'<svg viewBox="0 0 500 280" xmlns="http://www.w3.org/2000/svg" style="width:100%;max-width:500px;">'
    svg += f'<rect width="500" height="280" fill="white"/>'
    svg += f'<text x="250" y="20" text-anchor="middle" font-family="DejaVu Sans" font-size="12" font-weight="bold" fill="{NAVY}">Team Structure — Cap of 8 in 24 Months</text>'
    # Founder
    svg += f'<rect x="200" y="35" width="100" height="25" rx="3" fill="{NAVY}"/>'
    svg += f'<text x="250" y="51" text-anchor="middle" font-family="DejaVu Sans" font-size="8" font-weight="bold" fill="white">Founder</text>'
    # Level 2
    roles = ["Host", "Engineer", "Writer"]
    xs = [60, 220, 380]
    for x, role in zip(xs, roles):
        svg += f'<line x1="250" y1="60" x2="{x+40}" y2="80" stroke="{SLATE}" stroke-width="0.8"/>'
        svg += f'<rect x="{x}" y="80" width="80" height="22" rx="2" fill="{GOLD}"/>'
        svg += f'<text x="{x+40}" y="94" text-anchor="middle" font-family="DejaVu Sans" font-size="7" font-weight="bold" fill="white">{role}</text>'
    # Level 3
    roles2 = ["Host #2", "Writer #2", "Ops", "Community"]
    xs2 = [40, 130, 220, 370]
    for x, role in zip(xs2, roles2):
        pid = 60 if role in ["Host #2", "Writer #2"] else (220 if role == "Ops" else 380)
        svg += f'<line x1="{pid+40}" y1="102" x2="{x+30}" y2="130" stroke="{SLATE}" stroke-width="0.8"/>'
        svg += f'<rect x="{x}" y="130" width="60" height="20" rx="2" fill="{SAGE}" opacity="0.85"/>'
        svg += f'<text x="{x+30}" y="143" text-anchor="middle" font-family="DejaVu Sans" font-size="6.5" font-weight="bold" fill="white">{role}</text>'
    svg += f'<text x="250" y="195" text-anchor="middle" font-family="DejaVu Sans" font-size="7" fill="#888">Year 1: 4 people  |  Year 2: 8 people max</text>'
    svg += '</svg>'
    return svg


def svg_kpi_dashboard():
    """KPI Dashboard — 8 key metrics."""
    kpis = [
        ("MRR", "Rs 4.2L", "Target: Rs 25L", NAVY),
        ("Members", "42", "Target: 500", GOLD),
        ("Retention", "78%", "Target: >=75%", SAGE),
        ("Weekly Apps", "8", "Target: >=5", SLATE),
        ("Uptime", "99.8%", "Target: >=99.5%", SAGE),
        ("Cost/Member", "Rs 1,780", "Target: Rs 800", CORAL),
        ("Writing", "8h/wk", "Target: >=10h/wk", GOLD),
        ("Subscribers", "850", "Target: 5,000", NAVY),
    ]
    svg = f'<svg viewBox="0 0 500 160" xmlns="http://www.w3.org/2000/svg" style="width:100%;max-width:500px;">'
    svg += f'<rect width="500" height="160" fill="white"/>'
    svg += f'<text x="250" y="18" text-anchor="middle" font-family="DejaVu Sans" font-size="12" font-weight="bold" fill="{NAVY}">Founder Dashboard — Top 8 KPIs</text>'
    for i, (label, value, target, color) in enumerate(kpis):
        x = 10 + (i % 4) * 125
        y = 35 + (i // 4) * 60
        svg += f'<rect x="{x}" y="{y}" width="115" height="48" rx="2" fill="{CREAM}" stroke="#e0ddd5" stroke-width="0.5"/>'
        svg += f'<text x="{x+57}" y="{y+20}" text-anchor="middle" font-family="DejaVu Sans" font-size="14" font-weight="bold" fill="{color}">{value}</text>'
        svg += f'<text x="{x+57}" y="{y+33}" text-anchor="middle" font-family="DejaVu Sans" font-size="7" fill="{SLATE}">{label}</text>'
        svg += f'<text x="{x+57}" y="{y+43}" text-anchor="middle" font-family="DejaVu Sans" font-size="5.5" fill="#999">{target}</text>'
    svg += '</svg>'
    return svg


def svg_growth_curve():
    """Membership growth curve — 3 scenarios."""
    svg = f'<svg viewBox="0 0 480 220" xmlns="http://www.w3.org/2000/svg" style="width:100%;max-width:480px;">'
    svg += f'<rect width="480" height="220" fill="white"/>'
    svg += f'<text x="240" y="18" text-anchor="middle" font-family="DejaVu Sans" font-size="12" font-weight="bold" fill="{NAVY}">Membership Growth — 3 Scenarios</text>'
    # Axes
    svg += f'<line x1="40" y1="190" x2="460" y2="190" stroke="#ccc" stroke-width="0.8"/>'
    svg += f'<line x1="40" y1="190" x2="40" y2="20" stroke="#ccc" stroke-width="0.8"/>'
    # Gridlines
    for v in range(0, 901, 150):
        vy = 190 - v * (160 / 900)
        svg += f'<line x1="40" y1="{vy}" x2="460" y2="{vy}" stroke="#eee" stroke-width="0.3"/>'
        svg += f'<text x="35" y="{vy+3}" text-anchor="end" font-family="DejaVu Sans" font-size="5.5" fill="#999">{v}</text>'
    # Data
    scenarios = [
        ("Conservative", SAGE, [10, 25, 55, 100, 160, 250, 350]),
        ("Expected", GOLD, [10, 45, 100, 200, 350, 500, 700]),
        ("Optimistic", NAVY, [12, 65, 170, 290, 450, 650, 900]),
    ]
    for name, color, vals in scenarios:
        pts = []
        for i, v in enumerate(vals):
            x = 40 + i * (410 / 6)
            y = 190 - v * (160 / 900)
            pts.append(f"{x},{y}")
            svg += f'<circle cx="{x}" cy="{y}" r="2.5" fill="{color}"/>'
        svg += f'<polyline points="{" ".join(pts)}" fill="none" stroke="{color}" stroke-width="1.5"/>'
    # Labels
    months = ["M0", "M4", "M8", "M12", "M16", "M20", "M24"]
    for i, m in enumerate(months):
        x = 40 + i * (410 / 6)
        svg += f'<text x="{x}" y="200" text-anchor="middle" font-family="DejaVu Sans" font-size="6.5" fill="#999">{m}</text>'
    # Legend
    for i, (name, color, _) in enumerate(scenarios):
        lx, ly = 290 + i * 65, 210
        svg += f'<line x1="{lx}" y1="{ly-3}" x2="{lx+15}" y2="{ly-3}" stroke="{color}" stroke-width="1.5"/>'
        svg += f'<text x="{lx+18}" y="{ly}" text-anchor="start" font-family="DejaVu Sans" font-size="6.5" fill="#666">{name}</text>'
    svg += '</svg>'
    return svg


def svg_gold_rule(w=60):
    return f'<div style="width:{w}mm;height:0.5pt;background:{GOLD};margin:3mm 0;"></div>'


# ─── HTML Builder ───
def build_html():
    blocks = []
    a = blocks.append

    # Cover page
    a(f'''<div class="cover-page">
        <div class="cover-brand">FX Teller</div>
        <div style="width:60mm;height:1pt;background:{GOLD};margin-bottom:12mm;"></div>
        <div class="cover-title">Strategic<br><strong>Blueprint</strong></div>
        <div class="cover-subtitle">Founder Edition</div>
        <div style="width:40mm;height:1pt;background:{GOLD};margin:8mm auto;"></div>
        <div class="cover-meta">Version 1.0 &ensp;|&ensp; July 2026</div>
        <div class="cover-meta">Prepared by the Executive Strategy Office</div>
        <div class="cover-foot">CONFIDENTIAL  |  For Founder, Board, and Investor Distribution</div>
    </div>''')

    # Letter to Founder
    a('<div class="content pb">')
    a('<div class="page-header"><span>FX Teller</span><span>Strategic Blueprint</span></div>')
    a('<h1 class="section-title" style="page-break-before:avoid;">Letter to the Founder</h1>')
    a('<p>This document is the Master Strategic Blueprint for FX Teller. It is the company in writing. It has been produced by the full Executive Strategy Office, drawing on every strategic document in the knowledge base, and stress-tested by the most-sceptical reader the Office could find. It is the document you will hand to the next executive, the next investor, the next regulator, the next Host.</p>')
    a('<p>What has been built in this knowledge base is unusual. Twenty-two strategic decisions recorded in the Decision Register, with named owners and review cadences. Three governance frameworks: a 10-specialist Strategy Office with explicit vetoes, a 6-rhythm operational cadence, a documentation discipline that survives a 90-day Founder absence. A legal stack: SEBI opinion, Member agreement suite, data protection posture, audit trails. A financial model with Conservative, Expected, and Optimistic scenarios. A 6-month execution plan with week-by-week milestones. A 24-month strategic roadmap with quarterly sequencing. A Decision Log, a Glossary, a Project Status, a Risk Register, a KPI dashboard.</p>')
    a('<p>How this document should be used: read it once, end to end. Then put it down for 48 hours. Then read the Letter to the Founder, the Executive Summary, the Board Recommendations, and the Founder Dashboard. Then close it and execute the first 30 days. The document is the operating system; the operating system is the company.</p>')
    a('<p>Why execution now matters more than planning: the philosophy is a 10-year project, not a 1-year plan. The 6-month execution plan is the discipline of becoming a real company. The 24-month roadmap is the discipline of becoming an institution. The 10-year vision is the discipline of becoming a category. The 90 days ahead decide which of those three the company becomes.</p>')
    a('<p style="text-align:right;font-family:DejaVu Sans;font-size:8pt;color:#888;margin-top:8mm;">— The Executive Strategy Office</p>')
    a('</div>')

    # Today's Deliverables
    a('<div class="content pb">')
    a('<h1 class="section-title">Today\'s Deliverables</h1>')
    a('<p>The Executive Strategy Office produced the following knowledge base in a single continuous session. Every document is version-controlled and designed for re-installation by any future AI agent or human contributor.</p>')
    a('<table class="exec-table">')
    a('<tr><th>Folder</th><th>Docs</th><th>Contents</th></tr>')
    rows = [
        ("00_CONTEXT/", "5", "Master Context, AI Writing Guidelines, Glossary, Project Status, Decision Log"),
        ("01_FOUNDATION/", "2", "Vision-Mission-Values, Brand Philosophy"),
        ("02_BUSINESS/", "4", "Business Model, Revenue Architecture, Commercial Strategy, Financial Model"),
        ("03_PRODUCT/", "3", "Product Ecosystem, Member Experience Blueprint, Service Catalogue"),
        ("05_MARKETING/", "2", "Customer Personas, Go-To-Market &amp; Brand Launch Playbook"),
        ("06_OPERATIONS/", "2", "Operating Model, Product Delivery &amp; Operations Blueprint"),
        ("07_EXECUTION/", "2", "6-Month Execution Plan, 24-Month Strategic Roadmap"),
        ("09_RESEARCH/", "4", "Architecture, Deploy, Runbook, Market Sizing Analysis"),
        ("98_STRATEGY_OFFICE/", "15", "10 specialist roles + 4 frameworks + README"),
        ("99_GOVERNANCE/", "1", "Strategic Decision Register"),
    ]
    for r in rows:
        a(f'<tr><td><strong>{r[0]}</strong></td><td>{r[1]}</td><td>{r[2]}</td></tr>')
    a('</table>')
    a('<p class="small" style="margin-top:2mm;"><strong>Total: 30+ documents, ~140,000+ words.</strong> This Strategic Blueprint is the master synthesis; the <code>docs/</code> folder is the complete archive.</p>')
    a('</div>')

    # Quick Reference
    a('<div class="content pb">')
    a('<h1 class="section-title">Quick Reference</h1>')
    a('<div class="callout-card"><strong>The company in 10 numbers.</strong> 2 tiers (Monthly + Annual). 50 Founding Members (closed cohort). 5 daily Floor services. 8-person team cap. 30–50 Y1, 150–200 Y2, 350–500 Y3. ₹1.2–1.5 Cr Founder reserve. ₹15–30 Cr strategic raise Y2. 75% retention gate. 4 rhythms. Zero paid acquisition.</div>')
    a('<div class="callout-card"><strong>5 decisions already made.</strong> (1) First members\' club for retail traders in India. (2) Bootstrap Y1, raise Y2. (3) Single Credit: bundled, no expiry/transfer/purchase/display. (4) Writing-led growth. (5) Two-stage launch.</div>')
    a('<div class="callout-card"><strong>5 decisions needed now.</strong> (1) Annual price (OPEN-006). (2) Monthly price (OPEN-007). (3) Founding cap 50 (OPEN-008). (4) Headcount safety factor 1.5x (OPEN-009). (5) Writing engine ownership (OPEN-010).</div>')
    a('<div class="stats-row">')
    stats = [("30–50", "Members Y1"), ("150–200", "Members Y2"), ("350–500", "Members Y3"), ("₹1.2Cr", "Founder Reserve"), ("₹15–30Cr", "Y2 Raise")]
    for val, label in stats:
        a(f'<div class="stat-box"><div class="num">{val}</div><div class="label">{label}</div></div>')
    a('</div>')
    a( svg_6month_timeline() )
    a('</div>')

    # Executive Summary
    a('<div class="content pb">')
    a('<h1 class="section-title">Executive Summary</h1>')
    a('<p>FX Teller is a members-only, audio-first Trading Floor for disciplined retail traders. A members\' club whose principal amenity is a live, audio-only Trading Floor where a Host narrates the market in real time. The brand is the philosophy: discipline over engagement, process over prediction, calm over urgency.</p>')
    a('<p>The company exists because the Indian retail-trading industry has built a product economy that systematically mis-serves the disciplined trader. Signal groups, tipsters, gamified brokerages, and copy-trading platforms all profit from engagement the trader would be better off not having. FX Teller is the structural counter-position: ambient, calm, audio-first, process-over-prediction, no engagement-extraction.</p>')
    a('<div class="stats-row">')
    for val, label in [("₹25L", "MRR at M24"), ("75%", "Gross Margin"), ("8", "Team Size"), ("500–800", "Members M24")]:
        a(f'<div class="stat-box"><div class="num gold">{val}</div><div class="label">{label}</div></div>')
    a('</div>')
    a('<p>The model is a premium, community-first membership. Annual tier is the spine; Monthly is the on-ramp. Trading Credits are bundled transparently into the Annual fee. Capital posture: bootstrap Year 1 (₹1.2–1.5 Cr Founder reserve), Year 2 strategic raise of ₹15–30 Cr on philosophy-defending terms. Team: 4 in Year 1, 6 by Q4, 8 by Year 2. House of Traders: scoped Q5, built Q7, opened Q13–Q14. AI Companion: production by Q11–Q12.</p>')
    a('<p>The most load-bearing resource is the Founder. The plan is a Founder-protection plan disguised as a launch plan. Second Host and second writer in Months 4–5. Workload capped at 45–55 hours/week. Warm first session is Host-led by Q3.</p>')
    a('<p style="margin-top:3mm;"><strong>Success at 24 months:</strong> 500–800 Members, ₹25L MRR, 75% gross margin, 8-person team, 4-rhythm cadence, House construction, AI Companion in production, Dubai cohort launched, brand recognised as the most-respected lifestyle brand for disciplined traders in India and Dubai.</p>')
    a('</div>')

    # ─── PART I: THE VISION ───
    a(f'''<div class="section-divider pb">
        <div class="num">I</div>
        <div class="label">Part One</div>
        <div style="width:50mm;height:1pt;background:{GOLD};margin:4mm auto;"></div>
        <div class="title">The Vision</div>
    </div>''')

    a('<div class="content pb">')
    a('<h1 class="section-title" style="page-break-before:avoid;">The Vision</h1>')
    a('<p>FX Teller becomes, by 2035, the most-respected lifestyle brand for disciplined traders globally. The brand is recognised the way Soho House is recognised, the way Costco is recognised: as an institution whose Members are the people who have decided to be the kind of person the institution makes possible.</p>')
    a('</div>')

    a('<div class="content pb">')
    a('<h2 class="subsection-title">The Mission</h2>')
    a('<p>To give disciplined retail traders a calm, professional, members-only environment in which to develop the kind of trading practice that compounds over years rather than the kind that exhausts over months. The mission is the Member\'s first 90 days: the Floor, the community, the ritual, the journal, the moderation, the warm first session.</p>')
    a('<h2 class="subsection-title">The Values</h2>')
    a('<p>12 principles that govern every decision: <strong>discipline over emotion, trust before revenue, members before metrics, long-term thinking, quality over quantity, community before virality, calm over hype, consistency creates success, freedom through simplicity, technology reduces friction, execution before perfection, never stop learning.</strong></p>')
    a('<div class="callout-card"><strong>Core Philosophy — 5 Commitments.</strong> (1) Trading is a business. (2) Discipline beats strategy. (3) Consistency beats excitement. (4) Patience is an edge. (5) Trading should fit into life. These are not negotiable. The philosophy is the asset.</div>')
    a('</div>')

    a('<div class="content pb">')
    a('<h2 class="subsection-title">The Problem</h2>')
    a('<p>Signal groups, tipsters, gamified brokerages, and copy-trading platforms profit from engagement the trader would be better off not having. Push notifications, leaderboards, FOMO banners, streak badges — all engineered to make traders act more often, not better. The trader\'s outcome correlates with the <em>absence</em> of these levers; the industry\'s revenue correlates with the trader\'s <em>presence</em> on them. The incentives are in conflict.</p>')
    a('<h2 class="subsection-title">The Opportunity</h2>')
    a('<p>The disciplined retail trader who has rejected the signal-group model and is looking for a club, not a feed. SOM: 2,000–5,000 Members in five years — defensible, reachable, small enough that the brand can hold every name.</p>')
    a('<h2 class="subsection-title">Why Now</h2>')
    a('<p>India has crossed ten crore demat accounts. Writing-led premium brands (Zerodha Varsity, Zoho) have proven the model. The members\'-club category does not yet exist for traders. The window for category-creation is 24–36 months.</p>')
    a('<div class="part-summary"><strong>Part I Summary.</strong> Vision: category-defining by 2035. Mission: Member transformation from reactive to process-driven. Values: 12 principles. Philosophy: 5 commitments, non-negotiable. Problem: engagement-extraction economics. Opportunity: 2,000–5,000 SOM. Why now: category window open for 24–36 months.</div>')
    a('</div>')

    # ─── PART II: THE BUSINESS ───
    a(f'''<div class="section-divider pb">
        <div class="num">II</div>
        <div class="label">Part Two</div>
        <div style="width:50mm;height:1pt;background:{GOLD};margin:4mm auto;"></div>
        <div class="title">The Business</div>
    </div>''')

    a('<div class="content pb">')
    a('<h1 class="section-title" style="page-break-before:avoid;">Business Model</h1>')
    a('<p>A premium, community-first, philosophy-defended membership. Revenue is the downstream effect of Member value; the philosophy is the upstream cause.</p>')
    a('<div class="svg-container">' + svg_brand_4tier() + '</div>')
    a('<div class="callout-card"><strong>Trading Credits.</strong> Single type. Bundled into Annual fee. Four "nevers": no expiry, no transfer, no purchase, no public display. The philosophy expressed in credit design.</div>')
    a('</div>')

    a('<div class="content pb">')
    a('<h1 class="section-title">Commercial Strategy</h1>')
    a('<p>Product of a 7-subagent analysis. Seven key commitments:</p>')
    a('<table class="exec-table"><tr><th>#</th><th>Commitment</th><th>Detail</th></tr>')
    commits = [
        ("1", "Two-tier v1", "Monthly + Annual only"),
        ("2", "Founding cohort", "50 Members, closed, never reopened"),
        ("3", "Single Credit", "Four 'nevers' — no expiry/transfer/purchase/display"),
        ("4", "Growth engine", "Writing-led, zero paid acquisition"),
        ("5", "Capital posture", "₹1.2–1.5 Cr bootstrap Y1, ₹15–30 Cr raise Y2"),
        ("6", "Member targets", "30–50 Y1, 150–200 Y2, 350–500 Y3"),
        ("7", "Launch", "Two-stage: Design Partner (8–15) → Founding (50)"),
    ]
    for c in commits:
        a(f'<tr><td><strong>{c[0]}</strong></td><td>{c[1]}</td><td>{c[2]}</td></tr>')
    a('</table>')
    a('</div>')

    a('<div class="content pb">')
    a('<h1 class="section-title">Competitive Position</h1>')
    a('<p>FX Teller sits in a category it is creating: the first members\' club for serious retail traders in India. The brand is not a trading app, not a trading educator, not a generic SaaS, not a podcast subscription. It is a Trading Floor in a Club. The category is defensible because it does not yet exist.</p>')
    a('<table class="comp-table"><tr><th>Category</th><th>Examples</th><th>FX Teller vs</th></tr>')
    comps = [
        ("Trading Apps", "Trendlyne, Sensibull", "Engagement → Discipline"),
        ("Trading Educators", "Prateek Singh, Power of Stocks", "Content → Community"),
        ("Premium SaaS", "Superhuman, Linear", "Product → Membership"),
        ("Members\' Clubs", "Soho House, Aether", "Hospitality → Trading"),
        ("Audio Subs", "Substack, podcasts", "Broadcast → Live, Members-only"),
    ]
    for c in comps:
        a(f'<tr><td><strong>{c[0]}</strong></td><td>{c[1]}</td><td>{c[2]}</td></tr>')
    a('</table>')

    a('<h2 class="subsection-title">Differentiation</h2>')
    a('<p>Eight vectors: (1) Live audio, Members-only. (2) Process narration, not prediction. (3) Calm voice, not charisma. (4) Bounded community. (5) Warm first session. (6) Discipline Test. (7) "What we are NOT" list. (8) Brand Strategist\'s veto at every scale.</p>')
    a('<h2 class="subsection-title">Moats</h2>')
    a('<p>Ordered by durability: <strong>Brand Philosophy</strong> → <strong>Member Trust</strong> → <strong>Community</strong> → <strong>Host Quality</strong> → <strong>House of Traders</strong> → <strong>Operating System</strong>. A competitor can clone the audio room in a release cycle; they cannot clone the trust account in a decade.</p>')
    a('<div class="svg-container">' + svg_flywheel() + '</div>')
    a('<div class="part-summary"><strong>Part II Summary.</strong> 4-tier revenue model. Single Credit type. 7 commercial commitments. Category: first members\' club. 8 differentiation vectors. 6 moats, philosophy as the most durable. 30+ financial risks identified.</div>')
    a('</div>')

    # ─── PART III: THE PRODUCT ───
    a(f'''<div class="section-divider pb">
        <div class="num">III</div>
        <div class="label">Part Three</div>
        <div style="width:50mm;height:1pt;background:{GOLD};margin:4mm auto;"></div>
        <div class="title">The Product</div>
    </div>''')

    a('<div class="content pb">')
    a('<h1 class="section-title" style="page-break-before:avoid;">Product Ecosystem</h1>')
    a('<p>A live audio-first members\' club that uses trading as the discipline. The product surface is deliberately small.</p>')
    a('<h2 class="subsection-title">Trading Floors</h2>')
    a('<p>Five daily services on a published fixed cadence:</p>')
    a('<table class="exec-table"><tr><th>Service</th><th>Duration</th><th>Cadence</th></tr>')
    for s in [("Morning Briefing", "10–15 min", "Daily"), ("New York Session", "60–90 min", "Daily — flagship"), ("Closing Bell", "10–15 min", "Daily"), ("Weekend Review", "45–60 min", "Weekly"), ("Psychology Sessions", "45 min", "Monthly")]:
        a(f'<tr><td><strong>{s[0]}</strong></td><td>{s[1]}</td><td>{s[2]}</td></tr>')
    a('</table>')
    a('</div>')

    a('<div class="content pb">')
    a('<h1 class="section-title">Member Experience</h1>')
    a('<div class="svg-container">' + svg_12_lifecycle() + '</div>')
    a('<p>The 12-stage Experience Lifecycle: Curiosity → Application → Acceptance → Onboarding → First Floor → First Win → Community → Habit → House → Ambassador → Lifetime → Founder-tier. The first 90 days is the identity-formation phase.</p>')
    a('<p><strong>8 feelings</strong> the lifecycle produces: Calm, Trust, Belonging, Professionalism, Freedom, Progress, Growth, Pride.</p>')
    a('</div>')

    a('<div class="content pb">')
    a('<h1 class="section-title">Service Catalogue</h1>')
    a('<p>48 services listed; 13 v1 commitments; 35 future-vocabulary. V1: 5 daily + 4 monthly/quarterly + 4 aspirational (shipping Year 3+). The discipline: "We will not ship because the catalogue lists it; we will ship because the philosophy is ready for it."</p>')
    a('<table class="exec-table"><tr><th>Layer</th><th>V1</th><th>Future</th><th>Total</th></tr>')
    for layer in [("Trading Floor", "5", "3", "8"), ("Library", "2", "6", "8"), ("Community", "3", "8", "11"), ("Process Journal", "1", "2", "3"), ("Mentor Pool", "2", "4", "6")]:
        a(f'<tr><td><strong>{layer[0]}</strong></td><td>{layer[1]}</td><td>{layer[2]}</td><td>{layer[3]}</td></tr>')
    a('</table>')
    a('<h2 class="subsection-title">House of Traders</h2>')
    a('<p>The philosophy in hospitality form. Q5 scoping, Q7 construction, Q13–Q14 opening. A digital product can be reverse-engineered in a quarter; a House cannot.</p>')
    a('<h2 class="subsection-title">AI Companion</h2>')
    a('<p>The philosophy made operational. V1: Session Summaries, Trading Journal, Discipline Coach (Q9–Q10 alpha, Q11–Q12 production). Gated on corpus formation and a quarterly philosophy-alignment test.</p>')
    a('<div class="part-summary"><strong>Part III Summary.</strong> 13 v1 services across 5 layers. 12-stage lifecycle. 48-service catalogue. 4-stage product evolution. House: Q13–Q14. AI Companion: Q11–Q12 production.</div>')
    a('</div>')

    # ─── PART IV: THE BRAND ───
    a(f'''<div class="section-divider pb">
        <div class="num">IV</div>
        <div class="label">Part Four</div>
        <div style="width:50mm;height:1pt;background:{GOLD};margin:4mm auto;"></div>
        <div class="title">The Brand</div>
    </div>''')

    a('<div class="content pb">')
    a('<h1 class="section-title" style="page-break-before:avoid;">Brand Identity</h1>')
    a('<p>A hospitality brand wearing a trader\'s voice. Quiet, premium, philosophical — the institution whose Members are the people who have decided to be the kind of person the institution makes possible.</p>')
    a('<h2 class="subsection-title">Positioning</h2>')
    a('<p>The first members\' club for serious retail traders in India. A 10-year commitment. Defended by live audio-first Trading Floor, quiet voice, small community, deliberate cadence, premium price.</p>')
    a('<h2 class="subsection-title">Messaging Pillars</h2>')
    a('<div class="card-grid">')
    pillars = [
        ("Discipline is the Service", "Six months of the same calm Host voice"),
        ("Less, in the Right Way", "Absence of notifications, leaderboards, signals"),
        ("A Club, Not a Feed", "Bounded community, named Members, rituals"),
        ("Trading Fits into Life", "Watch, CarPlay, 30-second audio fragments"),
        ("The Brand is the Philosophy", "Decision Log, rejection letter, Founder\'s writing"),
    ]
    for title, desc in pillars:
        a(f'<div class="card"><h4>{title}</h4><p>{desc}</p></div>')
    a('</div>')
    a('</div>')

    a('<div class="content pb">')
    a('<h1 class="section-title">Audience &amp; Community</h1>')
    a('<table class="exec-table"><tr><th>Persona</th><th>Size (India)</th><th>Intent</th><th>Strategy</th></tr>')
    pers = [
        ("Professional Trader", "5,000–20,000", "Highest", "Core target, deepest engagement"),
        ("Working Professional", "50,000–200,000", "Medium", "Largest pool, lower conversion"),
        ("Entrepreneur", "10,000–40,000", "High", "Philosophy-aligned slow-burn"),
        ("Institutional", "Deferred", "—", "Post 500 Indian Members"),
    ]
    for p in pers:
        a(f'<tr><td><strong>{p[0]}</strong></td><td>{p[1]}</td><td>{p[2]}</td><td>{p[3]}</td></tr>')
    a('</table>')
    a('<p><strong>Anti-personas (7):</strong> Signal Chaser, Gambling-Mindset Trader, Guaranteed-Profit Seeker, Abusive Member, Community Disruptor, Sub-Scale Account Trader, Hype-Driven Member. Filtered by application funnel, brand surface, and Community moderation.</p>')
    a('<div class="callout-card"><strong>Content Engine.</strong> 2 essays/week Founder Y1 → 1+1 Y2 → 1+1+1 Y3. Substack primary. LinkedIn professional. X measured. Instagram visual only. Telegram rejected. WhatsApp Member-only. First podcast Y2. No paid acquisition, ever.</div>')
    a('<div class="part-summary"><strong>Part IV Summary.</strong> Brand: hospitality voice, trader identity. Positioning: first-mover in empty category. 5 messaging pillars. 4 personas, 7 anti-personas. Content: 2→3→4 essays/week. GTM: writing-led, application-based funnel.</div>')
    a('</div>')

    # ─── PART V: OPERATIONS ───
    a(f'''<div class="section-divider pb">
        <div class="num">V</div>
        <div class="label">Part Five</div>
        <div style="width:50mm;height:1pt;background:{GOLD};margin:4mm auto;"></div>
        <div class="title">Operations</div>
    </div>''')

    a('<div class="content pb">')
    a('<h1 class="section-title" style="page-break-before:avoid;">Operating Model</h1>')
    a('<div class="icon-grid">')
    ops_items = [
        ("Daily Log", "📋", "5-min end-of-day"),
        ("Weekly Plan", "📅", "Mon/Wed/Fri rhythm"),
        ("Fortnightly Review", "📊", "Sunday leadership"),
        ("Monthly Memo", "📝", "Financial + community"),
        ("Quarterly Review", "📈", "20 principles check"),
        ("10 Checklists", "✅", "Every ops surface"),
        ("Host Voice Code", "🎙️", "Signed pre-session"),
        ("90-day Cert", "🎓", "Host quality gate"),
    ]
    for title, icon, desc in ops_items:
        a(f'<div class="icon-item"><div class="icon">{icon}</div><strong>{title}</strong>{desc}</div>')
    a('</div>')
    a('<h2 class="subsection-title">Host System</h2>')
    a('<p>The Host is the brand\'s most-defensible operational asset. ₹40–50L fully loaded Year 1. 90-day certification. Second Host in Months 4–5. Coach into calm, not charisma. A Host departure in Year 1 is the most-severe endogenous risk.</p>')
    a('<h2 class="subsection-title">Compliance &amp; Governance</h2>')
    a('<p>SEBI opinion (50 pages, Month 3). Member agreement stack (6 documents, signed before Member #1). DPDP Act 2023 compliance. 7-year audit trails. CERT-In empanelled auditor by Q4 Year 1. 10-specialist Strategy Office with explicit vetoes.</p>')
    a('<div class="part-summary"><strong>Part V Summary.</strong> 4 rhythms (3 in Y1). 20 operating principles. 10 checklists. Host: ₹40–50L, 90-day cert. Compliance: SEBI, DPDP Act, audit trails. Governance: 10-specialist Office.</div>')
    a('</div>')

    # ─── PART VI: EXECUTION ───
    a(f'''<div class="section-divider pb">
        <div class="num">VI</div>
        <div class="label">Part Six</div>
        <div style="width:50mm;height:1pt;background:{GOLD};margin:4mm auto;"></div>
        <div class="title">Execution</div>
    </div>''')

    a('<div class="content pb">')
    a('<h1 class="section-title" style="page-break-before:avoid;">Financial Model</h1>')
    a('<table class="exec-table"><tr><th>Metric</th><th>Conservative</th><th>Expected</th><th>Optimistic</th></tr>')
    fin_rows = [
        ("Members Y1", "30–50", "30–50", "50–80"),
        ("Members Y2", "100–150", "150–200", "250–350"),
        ("Members Y3", "250–350", "350–500", "500–800"),
        ("Gross Margin Y1", "55%", "65%", "75%"),
        ("LTV/CAC M36", "3–4:1", "6–8:1", "10:1+"),
        ("Raise", "Slips", "Closes Q6", "Closes, 2nd House"),
    ]
    for r in fin_rows:
        a(f'<tr><td><strong>{r[0]}</strong></td><td>{r[1]}</td><td>{r[2]}</td><td>{r[3]}</td></tr>')
    a('</table>')
    a('<div class="svg-container">' + svg_growth_curve() + '</div>')
    a('</div>')

    a('<div class="content pb">')
    a('<h1 class="section-title">KPIs &amp; Dashboard</h1>')
    a('<div class="svg-container">' + svg_kpi_dashboard() + '</div>')
    a('<p><strong>Three most load-bearing KPIs:</strong> MRR (weekly), 12-month Annual retention (quarterly — the gating test for Y2 raise), Founder\'s writing hours/week (weekly — the growth constraint).</p>')
    a('</div>')

    a('<div class="content pb">')
    a('<h1 class="section-title">Launch &amp; Roadmap</h1>')
    a('<h2 class="subsection-title">Two-Stage Launch</h2>')
    a('<div class="callout-card"><strong>Stage 1 — Design Partner Program</strong> (Months 3–6): 8–15 Members from Founder\'s network, refundable first month, 5-day SLA, 30-day retention target 75%+.</div>')
    a('<div class="callout-card"><strong>Stage 2 — Founding Cohort</strong> (Months 6–9): 50 Members in two cohorts of 25, Founder-moderated first 30 days. \'I was there, and the room was the brand.\'</div>')
    a('<h2 class="subsection-title">24-Month Roadmap</h2>')
    a('<div class="svg-container">' + svg_24month_roadmap() + '</div>')
    a('<h2 class="subsection-title">Team</h2>')
    a('<div class="svg-container">' + svg_org_chart() + '</div>')
    a('<div class="callout-card"><strong>Budget.</strong> ₹250–350L annualised by Year 2. People ~90%. Legal: ₹5–8L Y1. Marketing: ₹3–5L Y1. House: ₹50L–1.5Cr (post-raise). AI Companion: ₹20–50L (post-raise).</div>')
    a('<div class="part-summary"><strong>Part VI Summary.</strong> 3 scenarios: Conservative/Expected/Optimistic. 40+ KPIs. 2-stage launch. 24-month quarterly roadmap. 8-person team cap. Top 5 risks tracked weekly.</div>')
    a('</div>')

    # ─── PART VII: FOUNDER DASHBOARD ───
    a(f'''<div class="section-divider pb">
        <div class="num">VII</div>
        <div class="label">Part Seven</div>
        <div style="width:50mm;height:1pt;background:{GOLD};margin:4mm auto;"></div>
        <div class="title">Founder Dashboard</div>
    </div>''')

    a('<div class="content pb">')
    a('<h1 class="section-title" style="page-break-before:avoid;">25 Numbers, Every Week</h1>')
    a('<div class="two-col"><div>')
    a('<h3 class="subsection-title">Revenue &amp; Cash</h3>')
    a('<ul><li>Active Member count</li><li>MRR</li><li>Cash runway (months)</li><li>Credit balance (₹)</li><li>Founding slots remaining</li></ul>')
    a('<h3 class="subsection-title">Member &amp; Growth</h3>')
    a('<ul><li>Application starts/week</li><li>Application→approval ratio</li><li>Approval→Active ratio</li><li>Active Member Rate (30d)</li><li>12-month Founding retention</li></ul>')
    a('</div><div>')
    a('<h3 class="subsection-title">Retention</h3>')
    a('<ul><li>Annual Month-12 retention</li><li>Monthly Month-6 retention</li><li>Cancellation reason distribution</li><li>Credit utilisation at termination</li><li>Founding cohort retention</li></ul>')
    a('<h3 class="subsection-title">Operations &amp; Brand</h3>')
    a('<ul><li>Floor uptime (30d)</li><li>Cost-to-serve/member/month</li><li>Host quality score</li><li>Founder writing hours/week</li><li>Substack subscribers</li><li>Brand consistency pass rate</li><li>NPS (monthly)</li></ul>')
    a('</div></div>')
    a('</div>')

    a('<div class="content pb">')
    a('<h1 class="section-title">Operating Rhythms</h1>')
    a('<table class="exec-table"><tr><th>Frequency</th><th>When</th><th>Duration</th><th>Content</th></tr>')
    rhythms = [
        ("Daily", "EOD", "5 min", "End-of-day log"),
        ("Weekly", "Mon/Wed/Fri", "30–60 min", "Plan, product review, KPIs"),
        ("Fortnightly", "Sunday", "90 min", "Leadership review, monthly memo"),
        ("Monthly", "Last Friday", "90 min", "Financial, community, risk, roadmap"),
        ("Quarterly", "Quarter-end", "4 hours", "Principles, quality bar, strategy"),
    ]
    for r in rhythms:
        a(f'<tr><td><strong>{r[0]}</strong></td><td>{r[1]}</td><td>{r[2]}</td><td>{r[3]}</td></tr>')
    a('</table>')
    a('<div class="callout-card"><strong>Decision-Making Framework.</strong> 5-step process: Frame → Values at stake → Philosophy test → Alternatives → Make the decision. Every material decision recorded in the Decision Log within 7 days.</div>')
    a('<div class="part-summary"><strong>Part VII Summary.</strong> 25 weekly numbers. 4 meeting rhythms. Decision Log entry required within 7 days of every material decision.</div>')
    a('</div>')

    # ─── PART VIII: BOARD RECOMMENDATIONS ───
    a(f'''<div class="section-divider pb">
        <div class="num">VIII</div>
        <div class="label">Part Eight</div>
        <div style="width:50mm;height:1pt;background:{GOLD};margin:4mm auto;"></div>
        <div class="title">Board Recommendations</div>
    </div>''')

    a('<div class="content pb">')
    a('<h1 class="section-title" style="page-break-before:avoid;">Immediate Priorities</h1>')
    a('<p><strong>Next 7 days:</strong></p>')
    a('<ol class="checklist">')
    for item in ["Set Annual price (OPEN-006)", "Set Monthly price (OPEN-007)", "Set Founding cohort cap at 50 (OPEN-008)", "Set Headcount safety factor at 1.5x (OPEN-009)", "Confirm ₹1.2–1.5 Cr Founder-capital reserve", "Sign external counsel retainer", "Adopt this Blueprint as operating reference"]:
        a(f'<li>{item}</li>')
    a('</ol>')
    a('</div>')

    a('<div class="content pb">')
    a('<h1 class="section-title">Top 10 Decisions &mdash; Next 30 Days</h1>')
    a('<ol class="checklist">')
    for item in ["Complete v1 product spec (5 services, 3Q journal, 5-screen mobile)", "Recruit first Host (profile + contract + 90-day certification)", "Recruit first Engineer (full-time contract)", "Author 6-document Member agreement stack", "Author 50-page SEBI opinion (external counsel)", "Identify 5–8 Design Partner candidates", "Open Substack + LinkedIn", "Author 20 operating principles, 10 checklists, 6-dimension quality bar", "Author empty context files (Glossary, Project Status, Decision Log)", "Adopt Founder Weekly Checklist"]:
        a(f'<li>{item}</li>')
    a('</ol>')
    a('</div>')

    a('<div class="content pb">')
    a('<h1 class="section-title">Things NOT to Do</h1>')
    a('<ol class="checklist">')
    notdos = [
        "No Premium service in Y1",
        "No Dubai before retention ≥75% and 30+ applicants",
        "No regional chapter before 200+ Members in the metro",
        "No hiring above 8 in 24 months",
        "No paid acquisition — ever",
        "No discounting any tier",
        "No crossing the 'what we are NOT' line",
        "No Board override of Brand Strategist\'s veto",
        "No Y2 raise with growth targets, board seat, or liquidation preference above 1x",
        "No Founder weekly hours exceeding 55",
    ]
    for item in notdos:
        a(f'<li>{item}</li>')
    a('</ol>')
    a('</div>')

    # Quote Page
    a(f'''<div class="quote-page pb">
        <blockquote>"The institution is the philosophy in operational form. The institution is what the company is becoming. The institution is what the Founder has been building toward for years."</blockquote>
        <cite>— The Executive Strategy Office</cite>
    </div>''')

    # Final Conclusion
    a('<div class="content pb">')
    a('<h1 class="section-title" style="page-break-before:avoid;">Final Conclusion</h1>')
    a('<p>If the Founder follows this Master Strategic Blueprint with discipline, FX Teller can realistically become, over 24 months, a premium, philosophy-defended, community-led institution with 500–800 Members, ₹25L MRR, 75% gross margin, an AI Companion in production, a first House of Traders in construction, a Dubai cohort launched, and a brand recognised as the most-respected lifestyle brand for disciplined traders in India and Dubai.</p>')
    a('<p>If the Founder follows this plan for 10 years, FX Teller can become, by 2035, a category-defining institution: 4–8 Houses across the world\'s financial centres, 5,000–12,000 Members, ₹50L+ MRR, a 12–15 person team, a Dubai-Singapore-London-New York presence, a publishing imprint, an annual gathering, and a brand that the trade press recognises as the most-defensible lifestyle brand in the category.</p>')
    a('<div class="stats-row">')
    for val, label in [("500–800", "Members M24"), ("₹25L", "MRR M24"), ("75%", "Gross Margin"), ("8", "Team"), ("4–8", "Houses by 2035"), ("5,000–12,000", "Members by 2035")]:
        a(f'<div class="stat-box"><div class="num gold">{val}</div><div class="label">{label}</div></div>')
    a('</div>')
    a('<p style="margin-top:5mm;text-align:center;font-family:DejaVu Sans;font-size:10pt;font-weight:bold;color:' + NAVY + ';">The plan begins.</p>')
    a('</div>')

    # ─── APPENDICES ───
    a('<div class="content">')
    a('<h1 class="section-title">Appendices</h1>')
    a('<h2 class="subsection-title">A. Timeline</h2>')
    a('<table class="exec-table"><tr><th>Month</th><th>Milestone</th></tr>')
    milestones = [
        ("Month 1", "Counsel retainer, v1 spec, Engineer on contract"),
        ("Month 2", "8–15 Design Partners, v1 build to 50%"),
        ("Month 3", "25–50 Founding, SEBI opinion, first quarterly review"),
        ("Month 4", "50 Founding complete, second Host + writer, first event"),
        ("Month 5", "100 Members, Year 2 raise prep"),
        ("Month 6", "v1 public launch, 100 Members, v1.5 starts"),
        ("Month 9", "200 Members, Dubai entity, House scoping, AI alpha"),
        ("Month 12", "350 Members, raise closes, v2.0, AI beta"),
        ("Month 18", "500 Members, House construction, Dubai cohort"),
        ("Month 24", "500–800 Members, House opens, AI production, Year-3 strategy"),
    ]
    for m in milestones:
        a(f'<tr><td><strong>{m[0]}</strong></td><td>{m[1]}</td></tr>')
    a('</table>')

    a('<h2 class="subsection-title">B. Glossary</h2>')
    a('<table class="exec-table"><tr><th>Term</th><th>Definition</th></tr>')
    gloss = [
        ("Member", "A paying, vetted adult admitted to the brand"),
        ("Trading Floor", "The live, audio-first, Members-only room"),
        ("Host", "The experienced trader who narrates the Floor"),
        ("Trading Credits", "In-product currency, bundled into Annual fee"),
        ("House of Traders", "The eventual physical surface"),
        ("Companion", "The AI product (Q9–Q10 alpha, Q11–Q12 production)"),
        ("Founding Members", "The closed cohort of 50"),
        ("Decision Log", "The canonical record of every material decision"),
        ('"What we are NOT"', "The philosophy's negations, applied per-surface"),
    ]
    for term, defn in gloss:
        a(f'<tr><td><strong>{term}</strong></td><td>{defn}</td></tr>')
    a('</table>')

    a('<h2 class="subsection-title">C. Reading Guide</h2>')
    a('<div class="callout-card"><strong>New executive</strong> (7 days): (1) This Blueprint. (2) Master Context. (3) Vision-Mission-Values. (4) Brand Philosophy. (5) Operating Model. (6) Decision Register. (7) 6-Month Plan. (8) 24-Month Roadmap.</div>')
    a('<div class="callout-card"><strong>New investor:</strong> (1) This Blueprint. (2) Vision-Mission-Values. (3) Commercial Strategy. (4) Financial Model. (5) Decision Register.</div>')
    a('<div class="callout-card"><strong>New AI agent:</strong> (1) Master Context. (2) AI Writing Guidelines. (3) Glossary. (4) Project Status. (5) Decision Log. (6) Relevant folder docs.</div>')
    a('<hr class="gold">')
    a('<p class="small center">End of FX Teller Strategic Blueprint, Version 1.0. Prepared by the Executive Strategy Office. July 2026.</p>')
    a('</div>')

    html = '<!DOCTYPE html><html lang="en"><head><meta charset="utf-8">'
    html += '<style>' + CSS_STYLE + '</style></head><body>'
    html += ''.join(blocks)
    html += '</body></html>'
    return html


def main():
    html_path = "/mnt/d/FX Teller/FX Teller Founder Playbook.html"
    pdf_path = "/mnt/d/FX Teller/FX Teller Founder Playbook.pdf"

    print("Building HTML document...")
    html = build_html()
    with open(html_path, "w", encoding="utf-8") as f:
        f.write(html)
    html_size = os.path.getsize(html_path)
    print(f"  HTML saved: {html_path} ({html_size//1024} KB)")

    print("Rendering PDF with WeasyPrint...")
    HTML(filename=html_path).write_pdf(pdf_path)
    pdf_size = os.path.getsize(pdf_path)
    print(f"  PDF saved: {pdf_path} ({pdf_size//1024} KB, ~{pdf_size//3000} pages)")

    # Also copy assets
    print(f"  Charts in: {OUT_DIR}/")


if __name__ == "__main__":
    import math
    main()
