from pathlib import Path
import re
from xml.sax.saxutils import escape

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import mm
from reportlab.platypus import (
    BaseDocTemplate, Frame, PageTemplate, Paragraph, Spacer, Table,
    TableStyle, PageBreak, KeepTogether
)


ROOT = Path(r"S:\Charlotte")
SOURCE = ROOT / "Udyaan - G9 Banana Packaging Development Project.md"
OUTPUT_DIR = ROOT / "output" / "pdf"
OUTPUT = OUTPUT_DIR / "Udyaan - G9 Banana Packaging Development Project.pdf"


def inline_markup(text):
    text = escape(text)
    text = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", text)
    text = re.sub(r"`(.+?)`", r"<font name='Courier'>\1</font>", text)
    return text


def parse_table(lines, styles, available_width):
    rows = []
    for line in lines:
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if all(re.fullmatch(r":?-{3,}:?", c) for c in cells):
            continue
        cell_style = styles["TableHeader"] if not rows else styles["TableCell"]
        rows.append([Paragraph(inline_markup(c), cell_style) for c in cells])
    if not rows:
        return Spacer(1, 1)
    ncols = max(len(row) for row in rows)
    for row in rows:
        while len(row) < ncols:
            row.append(Paragraph("", styles["TableCell"]))
    col_widths = [available_width / ncols] * ncols
    table = Table(rows, colWidths=col_widths, repeatRows=1, hAlign="LEFT")
    table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#17324D")),
        ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
        ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
        ("GRID", (0, 0), (-1, -1), 0.35, colors.HexColor("#B8C5D1")),
        ("BACKGROUND", (0, 1), (-1, -1), colors.HexColor("#F6F8FA")),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, colors.HexColor("#F6F8FA")]),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 5),
        ("RIGHTPADDING", (0, 0), (-1, -1), 5),
        ("TOPPADDING", (0, 0), (-1, -1), 5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
    ]))
    return table


def build_story(styles, width):
    lines = SOURCE.read_text(encoding="utf-8").splitlines()
    story = []
    i = 0
    paragraph_lines = []
    list_items = []
    ordered_items = []

    def flush_paragraph():
        nonlocal paragraph_lines
        if paragraph_lines:
            text = " ".join(x.strip() for x in paragraph_lines)
            story.append(Paragraph(inline_markup(text), styles["BodyTextCustom"]))
            story.append(Spacer(1, 3 * mm))
            paragraph_lines = []

    def flush_list():
        nonlocal list_items
        for item in list_items:
            story.append(Paragraph("- " + inline_markup(item), styles["BulletCustom"]))
        if list_items:
            story.append(Spacer(1, 2 * mm))
        list_items = []

    def flush_ordered():
        nonlocal ordered_items
        if ordered_items:
            cells = [Paragraph(f"{num}. {inline_markup(item)}", styles["NumberedCell"])
                     for num, item in ordered_items]
            while len(cells) % 2:
                cells.append(Paragraph("", styles["NumberedCell"]))
            rows = [cells[j:j + 2] for j in range(0, len(cells), 2)]
            table = Table(rows, colWidths=[width / 2 - 4 * mm, width / 2 - 4 * mm], hAlign="LEFT")
            table.setStyle(TableStyle([
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("LEFTPADDING", (0, 0), (-1, -1), 0),
                ("RIGHTPADDING", (0, 0), (-1, -1), 8),
                ("TOPPADDING", (0, 0), (-1, -1), 2),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 3),
            ]))
            story.append(table)
            story.append(Spacer(1, 2 * mm))
        ordered_items = []

    while i < len(lines):
        line = lines[i]
        if not line.strip():
            flush_paragraph()
            flush_list()
            flush_ordered()
            i += 1
            continue
        if line.strip() == "---":
            flush_paragraph(); flush_list()
            flush_ordered()
            story.append(Spacer(1, 2 * mm))
            i += 1
            continue
        if line.startswith("|"):
            flush_paragraph(); flush_list()
            flush_ordered()
            table_lines = []
            while i < len(lines) and lines[i].strip().startswith("|"):
                table_lines.append(lines[i])
                i += 1
            story.append(parse_table(table_lines, styles, width))
            story.append(Spacer(1, 5 * mm))
            continue
        heading = re.match(r"^(#{1,4})\s+(.*)$", line)
        if heading:
            flush_paragraph(); flush_list()
            level = len(heading.group(1))
            text = heading.group(2).strip()
            if level == 1:
                story.append(Paragraph(inline_markup(text), styles["TitleCustom"]))
                story.append(Spacer(1, 2 * mm))
            elif level == 2:
                if re.match(r"^\d+\.\s", text):
                    story.append(PageBreak())
                story.append(Paragraph(inline_markup(text), styles["Heading2Custom"]))
                story.append(Spacer(1, 2 * mm))
            elif level == 3:
                if text.startswith("Milestone 8:"):
                    story.append(PageBreak())
                story.append(Paragraph(inline_markup(text), styles["Heading3Custom"]))
                story.append(Spacer(1, 1 * mm))
            else:
                story.append(Paragraph(inline_markup(text), styles["Heading4Custom"]))
            i += 1
            continue
        bullet = re.match(r"^\s*[-*]\s+(.*)$", line)
        if bullet:
            flush_paragraph()
            list_items.append(bullet.group(1).strip())
            i += 1
            continue
        numbered = re.match(r"^\s*(\d+)\.\s+(.*)$", line)
        if numbered:
            flush_paragraph()
            flush_list()
            while i < len(lines):
                match = re.match(r"^\s*(\d+)\.\s+(.*)$", lines[i])
                if not match:
                    break
                ordered_items.append((match.group(1), match.group(2).strip()))
                i += 1
            flush_ordered()
            continue
        paragraph_lines.append(line)
        i += 1
    flush_paragraph(); flush_list(); flush_ordered()
    return story


def footer(canvas, doc):
    canvas.saveState()
    canvas.setStrokeColor(colors.HexColor("#D8E0E7"))
    canvas.line(18 * mm, 14 * mm, A4[0] - 18 * mm, 14 * mm)
    canvas.setFont("Helvetica", 8)
    canvas.setFillColor(colors.HexColor("#64748B"))
    canvas.drawString(18 * mm, 9 * mm, "Udyaan | G9 Banana Packaging Development Project")
    canvas.drawRightString(A4[0] - 18 * mm, 9 * mm, f"Page {doc.page}")
    canvas.restoreState()


def main():
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    styles = getSampleStyleSheet()
    styles.add(ParagraphStyle(
        name="TitleCustom", parent=styles["Title"], fontName="Helvetica-Bold",
        fontSize=24, leading=29, textColor=colors.HexColor("#17324D"),
        alignment=TA_CENTER, spaceAfter=3 * mm
    ))
    styles.add(ParagraphStyle(
        name="Heading2Custom", parent=styles["Heading2"], fontName="Helvetica-Bold",
        fontSize=15, leading=19, textColor=colors.HexColor("#17324D"),
        spaceBefore=2 * mm, spaceAfter=3 * mm, keepWithNext=True
    ))
    styles.add(ParagraphStyle(
        name="Heading3Custom", parent=styles["Heading3"], fontName="Helvetica-Bold",
        fontSize=11.5, leading=15, textColor=colors.HexColor("#2C5B7C"),
        spaceBefore=2 * mm, spaceAfter=2 * mm, keepWithNext=True
    ))
    styles.add(ParagraphStyle(
        name="Heading4Custom", parent=styles["Heading4"], fontName="Helvetica-Bold",
        fontSize=10, leading=13, textColor=colors.HexColor("#334155"), keepWithNext=True
    ))
    styles.add(ParagraphStyle(
        name="BodyTextCustom", parent=styles["BodyText"], fontName="Helvetica",
        fontSize=9.3, leading=13.2, textColor=colors.HexColor("#1F2937"), alignment=TA_LEFT
    ))
    styles.add(ParagraphStyle(
        name="BulletCustom", parent=styles["BodyText"], fontName="Helvetica",
        fontSize=9.2, leading=12.5, leftIndent=10, firstLineIndent=-7,
        textColor=colors.HexColor("#1F2937")
    ))
    styles.add(ParagraphStyle(
        name="NumberedCell", parent=styles["BodyText"], fontName="Helvetica",
        fontSize=9.2, leading=12.5, textColor=colors.HexColor("#1F2937")
    ))
    styles.add(ParagraphStyle(
        name="TableCell", parent=styles["BodyText"], fontName="Helvetica",
        fontSize=7.2, leading=9.2, textColor=colors.HexColor("#1F2937")
    ))
    styles.add(ParagraphStyle(
        name="TableHeader", parent=styles["BodyText"], fontName="Helvetica-Bold",
        fontSize=7.2, leading=9.2, textColor=colors.white
    ))
    frame = Frame(18 * mm, 19 * mm, A4[0] - 36 * mm, A4[1] - 37 * mm,
                  leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0)
    doc = BaseDocTemplate(str(OUTPUT), pagesize=A4, leftMargin=18 * mm,
                          rightMargin=18 * mm, topMargin=18 * mm, bottomMargin=19 * mm,
                          title="Udyaan - G9 Banana Packaging Development Project",
                          author="Udyaan Project Team")
    doc.addPageTemplates([PageTemplate(id="main", frames=[frame], onPage=footer)])
    story = build_story(styles, A4[0] - 36 * mm)
    doc.build(story)
    print(OUTPUT)


if __name__ == "__main__":
    main()
