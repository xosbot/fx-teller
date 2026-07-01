#!/usr/bin/env python3
"""Convert STRATEGIC_BLUEPRINT.md to a professional PDF using DejaVu Unicode fonts."""

import re
from fpdf import FPDF


FONT_DIR = "/usr/share/fonts/truetype/dejavu"


class StrategicBlueprint(FPDF):
    def __init__(self):
        super().__init__()
        self.set_auto_page_break(auto=True, margin=20)
        self.set_margins(20, 20, 20)
        self.add_font("DejaVu", "", f"{FONT_DIR}/DejaVuSans.ttf")
        self.add_font("DejaVu", "B", f"{FONT_DIR}/DejaVuSans-Bold.ttf")
        self.add_font("DejaVu", "I", f"{FONT_DIR}/DejaVuSans.ttf")

    def header(self):
        if self.page > 1:
            self.set_font("DejaVu", "I", 7)
            self.set_text_color(120, 120, 120)
            self.cell(95, 5, "FX Teller  |  Strategic Blueprint  |  Version 1.0", align="L")
            self.cell(0, 5, f"Page {self.page}", align="R")
            self.ln(8)
            self.set_draw_color(200, 200, 200)
            self.set_line_width(0.2)
            self.line(20, self.get_y(), self.w - 20, self.get_y())
            self.ln(5)
            self.set_text_color(0, 0, 0)

    def footer(self):
        self.set_y(-15)
        self.set_font("DejaVu", "I", 6)
        self.set_text_color(150, 150, 150)
        self.cell(0, 10, "CONFIDENTIAL  |  For Founder, Executive, and Investor Distribution", align="C")

    def cover_page(self):
        self.add_page()
        self.ln(80)
        self.set_font("DejaVu", "B", 14)
        self.set_text_color(40, 40, 40)
        self.cell(0, 15, "FX TELLER", align="C", new_x="LMARGIN", new_y="NEXT")
        self.set_font("DejaVu", "I", 9)
        self.set_text_color(100, 100, 100)
        self.cell(0, 8, "---", align="C", new_x="LMARGIN", new_y="NEXT")
        self.ln(30)
        self.set_font("DejaVu", "B", 32)
        self.set_text_color(20, 20, 20)
        self.cell(0, 18, "Strategic Blueprint", align="C", new_x="LMARGIN", new_y="NEXT")
        self.ln(5)
        self.set_font("DejaVu", "I", 14)
        self.set_text_color(80, 80, 80)
        self.cell(0, 12, "Founder Edition", align="C", new_x="LMARGIN", new_y="NEXT")
        self.ln(50)
        self.set_font("DejaVu", "", 11)
        self.set_text_color(60, 60, 60)
        self.cell(0, 8, "Version 1.0", align="C", new_x="LMARGIN", new_y="NEXT")
        self.cell(0, 8, "July 2026", align="C", new_x="LMARGIN", new_y="NEXT")
        self.ln(20)
        self.cell(0, 8, "Prepared by the Executive Strategy Office", align="C", new_x="LMARGIN", new_y="NEXT")

    def section_divider(self, part_label, part_title):
        self.add_page()
        self.ln(60)
        self.set_font("DejaVu", "B", 10)
        self.set_text_color(140, 100, 60)
        self.cell(0, 8, part_label.upper(), align="C", new_x="LMARGIN", new_y="NEXT")
        self.ln(5)
        self.set_font("DejaVu", "B", 28)
        self.set_text_color(20, 20, 20)
        self.cell(0, 15, part_title, align="C", new_x="LMARGIN", new_y="NEXT")
        self.ln(15)
        self.set_draw_color(180, 180, 180)
        self.set_line_width(0.3)
        self.line(60, self.get_y(), self.w - 60, self.get_y())
        self.ln(10)

    def h1(self, text):
        if self.get_y() > 200:
            self.add_page()
        self.set_font("DejaVu", "B", 16)
        self.set_text_color(20, 20, 20)
        self.ln(8)
        self.cell(0, 12, text, new_x="LMARGIN", new_y="NEXT")
        self.ln(4)
        self.set_draw_color(140, 100, 60)
        self.set_line_width(0.6)
        self.line(20, self.get_y(), 80, self.get_y())
        self.ln(6)

    def h2(self, text):
        self.set_font("DejaVu", "B", 12)
        self.set_text_color(30, 30, 30)
        self.ln(3)
        self.cell(0, 8, text, new_x="LMARGIN", new_y="NEXT")
        self.ln(2)

    def h3(self, text):
        self.set_font("DejaVu", "B", 10)
        self.set_text_color(60, 60, 60)
        self.ln(2)
        self.cell(0, 7, text, new_x="LMARGIN", new_y="NEXT")
        self.ln(2)

    def body(self, text, indent=False):
        self.set_font("DejaVu", "", 9)
        self.set_text_color(30, 30, 30)
        x = self.l_margin + (5 if indent else 0)
        self.set_x(x)
        self.multi_cell(self.w - self.l_margin - self.r_margin - (5 if indent else 0), 4.5, text)
        self.ln(2)

    def bullet(self, text, indent=0):
        self.set_font("DejaVu", "", 9)
        self.set_text_color(30, 30, 30)
        x = self.l_margin + (indent * 4)
        self.set_x(x)
        self.cell(4, 4.5, "-", new_x="END")
        self.multi_cell(0, 4.5, " " + text)
        self.ln(1)

    def bold_line(self, text):
        self.set_font("DejaVu", "B", 9)
        self.set_text_color(20, 20, 20)
        self.multi_cell(0, 4.5, text)
        self.ln(1)

    def table(self, headers, rows):
        self.ln(1)
        h = 5
        col_count = len(headers)
        col_w = (self.w - self.l_margin - self.r_margin) / col_count
        self.set_font("DejaVu", "B", 7)
        self.set_fill_color(40, 40, 40)
        self.set_text_color(255, 255, 255)
        for i, hdr in enumerate(headers):
            x = self.l_margin + i * col_w
            self.set_xy(x, self.get_y())
            self.cell(col_w, h, " " + hdr, border=1, fill=True)
        self.ln()
        self.set_font("DejaVu", "", 7)
        self.set_text_color(30, 30, 30)
        for row in rows:
            y_before = self.get_y()
            max_lines = 1
            for i, cell in enumerate(row):
                lines = cell.count("\n") + 1
                max_lines = max(max_lines, lines)
            row_h = max_lines * 4 + 2
            if self.get_y() + row_h > self.h - 20:
                self.add_page()
            y_start = self.get_y()
            for i, cell in enumerate(row):
                x = self.l_margin + i * col_w
                self.set_xy(x, y_start)
                self.multi_cell(col_w, 4, " " + str(cell), border=1, max_line_height=4)
            self.set_y(max(self.get_y(), y_start + row_h))
        self.ln(2)

    def hr(self):
        self.ln(2)
        self.set_draw_color(200, 200, 200)
        self.set_line_width(0.2)
        self.line(self.l_margin, self.get_y(), self.w - self.l_margin, self.get_y())
        self.ln(2)


def clean_text(text):
    """Replace Unicode characters that might cause issues."""
    replacements = {
        "\u2014": "--",   # em-dash
        "\u2013": "-",    # en-dash
        "\u2018": "'",    # left single quote
        "\u2019": "'",    # right single quote
        "\u201c": '"',    # left double quote
        "\u201d": '"',    # right double quote
        "\u2026": "...",  # ellipsis
        "\u2022": "-",    # bullet
        "\u2192": "->",   # arrow
        "\u2190": "<-",   # left arrow
        "\u00a0": " ",    # non-breaking space
        "\u202f": " ",    # narrow non-breaking space
        "\u00b7": "*",    # middle dot
        "\u00d7": "x",    # multiplication sign
        "\u2713": "v",    # check mark
    }
    for old, new in replacements.items():
        text = text.replace(old, new)
    # Remove carriage returns
    text = text.replace("\r\n", "\n").replace("\r", "\n")
    return text


def render_markdown_to_pdf(md_path, pdf_path):
    with open(md_path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    pdf = StrategicBlueprint()
    pdf.cover_page()

    # Track if we're inside a table
    i = 0
    while i < len(lines):
        line = lines[i].rstrip()

        # Skip separator lines that aren't tables
        if re.match(r"^[\s\|]*[-]+\s*[-| ]*\s*[-]+\s*$", line) and "|" not in line:
            i += 1
            continue

        # Horizontal rule (but not a separator in a table context)
        if re.match(r"^---+$", line.strip()) and "|" not in line:
            pdf.hr()
            i += 1
            continue

        # Headings
        h1_match = re.match(r"^# (.+)", line)
        h2_match = re.match(r"^## (.+)", line)
        h3_match = re.match(r"^### (.+)", line)

        if h1_match:
            text = h1_match.group(1)
            part_match = re.match(r"Part (\w+): (.+)", text)
            if part_match:
                pdf.section_divider(part_match.group(1), part_match.group(2))
            else:
                pdf.h1(text)
            i += 1
            continue

        if h2_match:
            pdf.h2(h2_match.group(1))
            i += 1
            continue

        if h3_match:
            pdf.h3(h3_match.group(1))
            i += 1
            continue

        # Empty lines
        if not line.strip():
            i += 1
            continue

        # Tables
        if line.startswith("|") and len(line) > 2:
            table_lines = []
            while i < len(lines) and lines[i].startswith("|"):
                table_lines.append(lines[i].rstrip())
                i += 1
            # Parse table
            clean = [l for l in table_lines if "|" in l and l.strip() and not re.match(r"^[\s|:]+$", l)]
            if len(clean) >= 3:
                headers = [c.strip() for c in clean[0].strip("|").split("|")]
                rows = []
                for tl in clean[2:]:
                    cells = [c.strip() for c in tl.strip("|").split("|")]
                    rows.append(cells)
                if rows:
                    pdf.table(headers, rows)
            continue

        # Bold line
        if line.startswith("**") and line.endswith("**"):
            pdf.bold_line(clean_text(line[2:-2]))
            i += 1
            continue

        # Bullet points
        stripped = line.lstrip()
        indent = (len(line) - len(stripped)) // 2
        if stripped.startswith("- ") or stripped.startswith("* "):
            text = clean_text(stripped[2:])
            pdf.bullet(text, indent)
            i += 1
            continue

        # Numbered list
        if re.match(r"^\s*\d+[.)]\s", line):
            text = clean_text(re.sub(r"^\s*\d+[.)]\s+", "", line))
            pdf.bullet(text, indent)
            i += 1
            continue

        # Regular paragraph
        text = clean_text(line)
        # Remove inline bold markers
        text = re.sub(r"\*\*([^*]+)\*\*", r"\1", text)
        text = re.sub(r"\*([^*]+)\*", r"\1", text)
        # Remove inline links
        text = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", text)
        if text.strip():
            pdf.body(text)
        i += 1

    pdf.output(pdf_path)
    print(f"PDF generated: {pdf_path} ({pdf.pages_count} pages)")


if __name__ == "__main__":
    render_markdown_to_pdf(
        "/mnt/d/FX Teller/STRATEGIC_BLUEPRINT.md",
        "/mnt/d/FX Teller/STRATEGIC_BLUEPRINT.pdf",
    )
