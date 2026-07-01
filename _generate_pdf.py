#!/usr/bin/env python3
"""Generate a professional, visually rich PDF of the FX Teller Strategic Blueprint."""

import re, os
from fpdf import FPDF

FONT = "/usr/share/fonts/truetype/dejavu"
ASSETS = "/mnt/d/FX Teller/docs/assets"
CHARTS = {
    "timeline": f"{ASSETS}/chart_01_timeline.png",
    "growth": f"{ASSETS}/chart_02_growth.png",
    "pyramid": f"{ASSETS}/chart_03_revenue_pyramid.png",
    "moats": f"{ASSETS}/chart_04_moats.png",
    "lifecycle": f"{ASSETS}/chart_05_lifecycle.png",
    "risk": f"{ASSETS}/chart_06_risk_heatmap.png",
    "kpi": f"{ASSETS}/chart_07_kpi_dashboard.png",
    "services": f"{ASSETS}/chart_08_service_catalogue.png",
}

NAVY = "#1B1B2F"
GOLD = "#C5A55A"
CREAM = "#F5F0E8"
WHITE = "#FFFFFF"
SAGE = "#7A9E7E"
SLATE = "#4A4A6A"

PAGE_W = 210
PAGE_H = 297
MARGIN = 20
BODY_W = PAGE_W - 2 * MARGIN


class BlueprintPDF(FPDF):
    def __init__(self):
        super().__init__()
        self.set_auto_page_break(auto=True, margin=22)
        self.set_margins(MARGIN, MARGIN, MARGIN)
        self.add_font("Serif", "", f"{FONT}/DejaVuSerif.ttf")
        self.add_font("Serif", "B", f"{FONT}/DejaVuSerif-Bold.ttf")
        self.add_font("Sans", "", f"{FONT}/DejaVuSans.ttf")
        self.add_font("Sans", "B", f"{FONT}/DejaVuSans-Bold.ttf")
        self.add_font("Sans", "I", f"{FONT}/DejaVuSans.ttf")
        self.charts_embedded = False

    def header(self):
        if self.page > 1:
            self.set_font("Sans", "I", 6.5)
            self.set_text_color(160, 160, 160)
            part = getattr(self, "current_part", "Strategic Blueprint")
            self.cell(90, 4, f"FX Teller  |  {part}", align="L")
            self.cell(0, 4, f"Confidential  |  Page {self.page}", align="R")
            self.ln(6)
            self.set_draw_color(200, 200, 200)
            self.set_line_width(0.2)
            self.line(MARGIN, self.get_y(), PAGE_W - MARGIN, self.get_y())
            self.ln(4)

    def footer(self):
        pass

    # ---- Layout helpers ----
    def cover_page(self):
        self.add_page()
        self.ln(70)
        # Gold rule
        self.set_draw_color(197, 165, 90)
        self.set_line_width(1)
        self.line(50, self.get_y(), PAGE_W - 50, self.get_y())
        self.ln(15)
        # Brand name
        self.set_font("Sans", "B", 16)
        self.set_text_color(40, 40, 40)
        self.cell(0, 10, "FX TELLER", align="C", new_x="LMARGIN", new_y="NEXT")
        self.ln(3)
        self.set_font("Sans", "I", 9)
        self.set_text_color(120, 120, 120)
        self.cell(0, 7, "---", align="C", new_x="LMARGIN", new_y="NEXT")
        self.ln(20)
        # Title
        self.set_font("Sans", "B", 30)
        self.set_text_color(27, 27, 47)
        self.cell(0, 16, "Strategic Blueprint", align="C", new_x="LMARGIN", new_y="NEXT")
        self.ln(4)
        self.set_font("Sans", "I", 13)
        self.set_text_color(80, 80, 80)
        self.cell(0, 10, "Founder Edition", align="C", new_x="LMARGIN", new_y="NEXT")
        self.ln(40)
        # Gold rule
        self.set_draw_color(197, 165, 90)
        self.set_line_width(0.3)
        self.line(70, self.get_y(), PAGE_W - 70, self.get_y())
        self.ln(10)
        self.set_font("Sans", "", 10)
        self.set_text_color(80, 80, 80)
        self.cell(0, 7, "Version 1.0  |  July 2026", align="C", new_x="LMARGIN", new_y="NEXT")
        self.cell(0, 7, "Prepared by the Executive Strategy Office", align="C", new_x="LMARGIN", new_y="NEXT")
        self.ln(40)
        self.set_font("Sans", "I", 7)
        self.set_text_color(160, 160, 160)
        self.cell(0, 5, "CONFIDENTIAL  |  For Founder, Executive, and Investor Distribution", align="C",
                  new_x="LMARGIN", new_y="NEXT")

    def section_divider(self, part_num, part_title):
        self.add_page()
        self.set_fill_color(245, 240, 232)
        self.rect(0, 0, PAGE_W, PAGE_H, "F")
        self.set_draw_color(197, 165, 90)
        self.set_line_width(2)
        self.line(60, 90, PAGE_W - 60, 90)
        self.ln(40)
        self.set_font("Sans", "B", 72)
        self.set_text_color(27, 27, 47)
        self.cell(0, 25, part_num, align="C", new_x="LMARGIN", new_y="NEXT")
        self.ln(5)
        self.set_font("Sans", "", 9)
        self.set_text_color(160, 160, 160)
        self.cell(0, 8, "PART", align="C", new_x="LMARGIN", new_y="NEXT")
        self.ln(15)
        self.set_font("Sans", "B", 24)
        self.set_text_color(27, 27, 47)
        self.cell(0, 14, part_title, align="C", new_x="LMARGIN", new_y="NEXT")
        self.ln(10)
        self.set_draw_color(197, 165, 90)
        self.set_line_width(1)
        self.line(80, self.get_y(), PAGE_W - 80, self.get_y())
        self.current_part = f"Part {part_num}"

    def h1(self, text):
        if self.get_y() > 230:
            self.add_page()
        self.set_font("Serif", "B", 16)
        self.set_text_color(27, 27, 47)
        self.ln(6)
        self.cell(0, 10, text, new_x="LMARGIN", new_y="NEXT")
        self.ln(3)
        self.set_draw_color(197, 165, 90)
        self.set_line_width(0.6)
        self.line(MARGIN, self.get_y(), MARGIN + 60, self.get_y())
        self.ln(5)

    def h2(self, text):
        self.set_font("Sans", "B", 11)
        self.set_text_color(27, 27, 47)
        self.ln(3)
        self.cell(0, 7, text, new_x="LMARGIN", new_y="NEXT")
        self.ln(2)

    def h3(self, text):
        self.set_font("Sans", "B", 9.5)
        self.set_text_color(60, 60, 60)
        self.ln(2)
        self.cell(0, 6, text, new_x="LMARGIN", new_y="NEXT")
        self.ln(1.5)

    def body(self, text):
        self.set_font("Serif", "", 9)
        self.set_text_color(40, 40, 40)
        self.multi_cell(0, 4.8, text, align="L")
        self.ln(2)

    def bullet(self, text, indent=0):
        self.set_font("Serif", "", 9)
        self.set_text_color(40, 40, 40)
        x = MARGIN + indent * 4
        self.set_x(x)
        self.cell(4, 4.8, "-", new_x="END")
        self.multi_cell(0, 4.8, " " + text)
        self.ln(1)

    def callout(self, text):
        self.ln(2)
        self.set_fill_color(245, 240, 232)
        y = self.get_y()
        self.set_draw_color(197, 165, 90)
        self.set_line_width(0.8)
        self.rect(MARGIN, y, BODY_W, 12, style="DF")
        self.set_xy(MARGIN + 4, y + 1)
        self.set_font("Sans", "I", 8)
        self.set_text_color(80, 70, 40)
        self.multi_cell(BODY_W - 8, 4.5, text)
        self.set_y(max(self.get_y(), y + 14))
        self.ln(2)

    def callout_block(self, lines):
        self.ln(2)
        line_h = 4.5
        total_h = len(lines) * line_h + 6
        y = self.get_y()
        if y + total_h > PAGE_H - 22:
            self.add_page()
            y = self.get_y()
        self.set_fill_color(245, 240, 232)
        self.set_draw_color(197, 165, 90)
        self.set_line_width(0.8)
        self.rect(MARGIN, y, BODY_W, total_h, style="DF")
        self.set_xy(MARGIN + 5, y + 3)
        self.set_font("Sans", "", 8)
        self.set_text_color(60, 50, 30)
        for line in lines:
            self.set_x(MARGIN + 5)
            self.cell(0, line_h, line, new_x="LMARGIN", new_y="NEXT")
        self.set_y(y + total_h + 3)

    def img_center(self, path, w=150):
        if not os.path.exists(path):
            return
        if self.get_y() > PAGE_H - 50:
            self.add_page()
        y_before = self.get_y()
        try:
            self.image(path, x=(PAGE_W - w) / 2, w=w)
        except Exception:
            pass
        self.ln(2)

    def table(self, headers, rows):
        self.ln(1)
        col_w = BODY_W / len(headers)
        self.set_font("Sans", "B", 7)
        self.set_fill_color(27, 27, 47)
        self.set_text_color(255, 255, 255)
        for i, hdr in enumerate(headers):
            x = MARGIN + i * col_w
            self.set_xy(x, self.get_y())
            self.cell(col_w, 6, " " + hdr, border=1, fill=True)
        self.ln()
        self.set_text_color(40, 40, 40)
        for row_idx, row in enumerate(rows):
            if row_idx % 2 == 0:
                self.set_fill_color(245, 240, 232)
            else:
                self.set_fill_color(255, 255, 255)
            self.set_font("Sans", "", 7)
            max_lines = max((str(c).count("\n") + 1 for c in row), default=1)
            row_h = max_lines * 4 + 2
            if self.get_y() + row_h > PAGE_H - 22:
                self.add_page()
            y_start = self.get_y()
            for i, cell in enumerate(row):
                x = MARGIN + i * col_w
                self.set_xy(x, y_start)
                self.multi_cell(col_w, 4, " " + str(cell), border=1,
                                fill=True, max_line_height=4)
            self.set_y(max(self.get_y(), y_start + row_h))
        self.ln(2)

    def numbered_list(self, items):
        for i, item in enumerate(items, 1):
            self.bullet(f"{i}. {item}")

    def hr(self):
        self.ln(2)
        self.set_draw_color(200, 200, 200)
        self.set_line_width(0.2)
        self.line(MARGIN, self.get_y(), PAGE_W - MARGIN, self.get_y())
        self.ln(3)

    def part_summary(self, text):
        self.ln(2)
        self.set_fill_color(27, 27, 47)
        y = self.get_y()
        if y + 14 > PAGE_H - 22:
            self.add_page()
            y = self.get_y()
        self.rect(MARGIN, y, BODY_W, 14, style="F")
        self.set_xy(MARGIN + 3, y + 1)
        self.set_font("Sans", "I", 8)
        self.set_text_color(197, 165, 90)
        self.multi_cell(BODY_W - 6, 4.5, text)
        self.set_y(max(self.get_y(), y + 15))
        self.ln(1)


def render_pdf(md_path, pdf_path):
    with open(md_path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    pdf = BlueprintPDF()

    # Track state
    in_todays_deliverables = False
    in_blockquote = False
    blockquote_lines = []
    current_part_num = ""
    current_part_title = ""
    num_bullet_mode = False
    num_bullet_items = []
    in_table = False
    table_headers = []
    table_rows = []

    def flush_blockquote():
        nonlocal blockquote_lines, in_blockquote
        if blockquote_lines:
            pdf.callout_block(blockquote_lines)
            blockquote_lines = []
            in_blockquote = False

    def flush_table():
        nonlocal in_table, table_headers, table_rows
        if in_table and table_headers and table_rows:
            pdf.table(table_headers, table_rows)
        in_table = False
        table_headers = []
        table_rows = []

    pdf.cover_page()

    # Page 2: Today's Deliverables (built directly)
    pdf.add_page()
    pdf.h1("Today's Deliverables")
    pdf.body("The Executive Strategy Office produced the following knowledge base in a single continuous session. Every document is saved in docs/, version-controlled, and designed for re-installation by any future AI agent or human contributor.")
    pdf.table(
        ["Folder", "Docs", "What It Covers"],
        [
            ["00_CONTEXT/", "5", "Master Context, AI Writing Guidelines, Glossary, Project Status, Decision Log"],
            ["01_FOUNDATION/", "2", "Vision-Mission-Values, Brand Philosophy"],
            ["02_BUSINESS/", "4", "Business Model, Revenue Architecture, Commercial Strategy, Financial Model"],
            ["03_PRODUCT/", "3", "Product Ecosystem, Member Experience Blueprint, Service Catalogue (48 services)"],
            ["05_MARKETING/", "2", "Customer Personas, Go-To-Market & Brand Launch Playbook"],
            ["06_OPERATIONS/", "2", "Operating Model, Product Delivery & Operations Blueprint"],
            ["07_EXECUTION/", "2", "6-Month Execution Plan, 24-Month Strategic Roadmap"],
            ["09_RESEARCH/", "4", "Architecture, Deploy, Runbook, Market Sizing Analysis"],
            ["10_ARCHIVE/", "2", "Phase 1 proposal (historical)"],
            ["98_STRATEGY_OFFICE/", "15", "10 specialist roles + 4 frameworks + README"],
            ["99_GOVERNANCE/", "1", "Strategic Decision Register"],
        ]
    )
    pdf.body("Total: 30+ documents, ~140,000+ words across the knowledge base. The STRATEGIC_BLUEPRINT.md at project root is the master synthesis; the docs/ folder is the complete archive.")

    # Page 3: Quick Reference
    pdf.add_page()
    pdf.h1("Quick Reference")
    pdf.callout_block([
        "THE COMPANY IN 10 NUMBERS: 2 tiers (Monthly + Annual). 50 Founding Members (closed). 5 daily Floor services. 8-person team cap. 30-50 Y1, 150-200 Y2, 350-500 Y3.",
        "Rs 1.2-1.5 Cr Founder reserve Y1. Rs 15-30 Cr strategic raise Y2. 75% 12-month retention gate. 4 rhythms. Zero paid acquisition."
    ])
    pdf.callout_block([
        "5 DECISIONS ALREADY MADE: (1) First members' club for Indian retail traders. (2) Bootstrap Y1, raise Y2. (3) Single Credit: bundled, no expiry/transfer/purchase/display. (4) Writing-led growth. (5) Two-stage launch."
    ])
    pdf.callout_block([
        "5 DECISIONS NEEDED NOW: (1) Annual price (OPEN-006). (2) Monthly price (OPEN-007). (3) Founding cap at 50 (OPEN-008). (4) Headcount safety factor 1.5x (OPEN-009). (5) Writing engine ownership (OPEN-010)."
    ])
    pdf.callout_block([
        "THE ARC IN ONE LINE: M3: 25-50 Founding. M6: v1 live. M12: raise closes. M18: House construction. M24: House open, AI production, Dubai cohort live."
    ])
    pdf.img_center(CHARTS["timeline"], w=160)

    i = 0
    while i < len(lines):
        line = lines[i].rstrip()

        # Skip empty lines after the Today's Deliverables section
        if "Today's Deliverables" in line or "Quick Reference" in line:
            i += 1
            continue

        # Horizontal rule
        if re.match(r"^---+$", line.strip()) and "|" not in line:
            flush_blockquote()
            flush_table()
            pdf.hr()
            i += 1
            continue

        # Headings
        h1_m = re.match(r"^# (.+)", line)
        h2_m = re.match(r"^## (.+)", line)
        h3_m = re.match(r"^### (.+)", line)

        if h1_m:
            flush_blockquote()
            flush_table()
            text = h1_m.group(1)
            part_m = re.match(r"Part (\w+): (.+)", text)
            if part_m:
                current_part_num = part_m.group(1)
                current_part_title = part_m.group(2)
                pdf.section_divider(current_part_num, current_part_title)
                # Embed chart after appropriate part dividers
                part_map = {
                    "I": None,
                    "II": "moats",
                    "III": "lifecycle",
                    "IV": None,
                    "V": None,
                    "VI": "growth",
                    "VII": "kpi",
                    "VIII": "risk",
                }
                chart_key = part_map.get(current_part_num)
                if chart_key and chart_key in CHARTS:
                    pdf.ln(20)
                    pdf.img_center(CHARTS[chart_key], w=150)
            else:
                pdf.h1(text)
            i += 1
            continue

        if h2_m:
            flush_blockquote()
            flush_table()
            text = h2_m.group(1)
            if text == "Today's Deliverables" or text == "Quick Reference":
                i += 1
                continue
            # Skip appendices on extra pages
            if text.startswith("Appendix"):
                pdf.h2(text)
            else:
                pdf.h2(text)
            i += 1
            continue

        if h3_m:
            flush_blockquote()
            flush_table()
            pdf.h3(h3_m.group(1))
            i += 1
            continue

        # Blockquote
        if line.startswith(">"):
            in_blockquote = True
            bt = re.sub(r"^\>\s*", "", line)
            blockquote_lines.append(bt)
            i += 1
            continue

        flush_blockquote()

        # Empty line
        if not line.strip():
            i += 1
            continue

        # Table
        if line.startswith("|") and len(line) > 2:
            if not in_table:
                in_table = True
                table_lines = [line]
                i += 1
                while i < len(lines) and lines[i].startswith("|"):
                    table_lines.append(lines[i].rstrip())
                    i += 1
                clean = [l for l in table_lines if l.strip() and not re.match(r"^[\s|:\-]+$", l)]
                if len(clean) >= 3:
                    table_headers = [c.strip() for c in clean[0].strip("|").split("|")]
                    table_rows = []
                    for tl in clean[2:]:
                        cells = [c.strip() for c in tl.strip("|").split("|")]
                        table_rows.append(cells)
            else:
                i += 1
            continue
        else:
            flush_table()

        # Bold line
        if line.startswith("**") and line.endswith("**"):
            pdf.set_font("Sans", "B", 9)
            pdf.set_text_color(27, 27, 47)
            pdf.multi_cell(0, 4.8, line[2:-2])
            pdf.ln(1)
            i += 1
            continue

        # Bullet
        stripped = line.lstrip()
        indent = (len(line) - len(stripped)) // 2
        if stripped.startswith("- ") or stripped.startswith("* "):
            text = re.sub(r"\*\*([^*]+)\*\*", r"\1", stripped[2:])
            text = re.sub(r"\*([^*]+)\*", r"\1", text)
            text = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", text)
            pdf.bullet(text, indent)
            i += 1
            continue

        # Numbered in markdown
        if re.match(r"^\s*\d+[.)]\s", line):
            text = re.sub(r"^\s*\d+[.)]\s+", "", line)
            text = re.sub(r"\*\*([^*]+)\*\*", r"\1", text)
            text = re.sub(r"\*([^*]+)\*", r"\1", text)
            pdf.bullet(text, indent)
            i += 1
            continue

        # Regular paragraph
        text = re.sub(r"\*\*([^*]+)\*\*", r"\1", line)
        text = re.sub(r"\*([^*]+)\*", r"\1", text)
        text = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", text)
        if text.strip():
            pdf.body(text)
        i += 1

    flush_table()
    flush_blockquote()

    # Add service catalogue chart after appendices
    pdf.ln(5)
    pdf.img_center(CHARTS["services"], w=150)
    # Add pyramid chart
    pdf.img_center(CHARTS["pyramid"], w=120)

    pdf.output(pdf_path)
    print(f"PDF generated: {pdf_path} ({pdf.pages_count} pages)")


if __name__ == "__main__":
    render_pdf(
        "/mnt/d/FX Teller/STRATEGIC_BLUEPRINT.md",
        "/mnt/d/FX Teller/STRATEGIC_BLUEPRINT.pdf",
    )
