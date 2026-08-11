"""Build PDF from G9 Post-Harvest Functional Brief markdown."""

from pathlib import Path
import re
from xml.sax.saxutils import escape

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import mm
from reportlab.platypus import (
    BaseDocTemplate,
    Frame,
    Image,
    PageBreak,
    PageTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
)


ROOT = Path(r"S:\Charlotte")
SOURCE = ROOT / "G9 Post-Harvest Functional Brief.md"
OUTPUT_DIR = ROOT / "output" / "pdf"
OUTPUT = OUTPUT_DIR / "G9 Post-Harvest Functional Brief.pdf"


def inline_markup(text):
    text = escape(text)
    text = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", text)
    text = re.sub(r"\*(.+?)\*", r"<i>\1</i>", text)
    text = re.sub(r"`(.+?)`", r"<font name='Courier'>\1</font>", text)
    return text


def skip_frontmatter(lines):
    if lines and lines[0].strip() == "---":
        for i in range(1, len(lines)):
            if lines[i].strip() == "---":
                return lines[i + 1 :]
    return lines


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
    table.setStyle(
        TableStyle(
            [
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
            ]
        )
    )
    return table


def image_flowable(path, width, max_height=95 * mm):
    img_path = ROOT / path
    if not img_path.exists():
        return Paragraph(f"<i>[Image not found: {escape(path)}]</i>", styles_placeholder["Caption"])
    img = Image(str(img_path))
    scale = min(width / img.drawWidth, max_height / img.drawHeight, 1.0)
    img.drawWidth *= scale
    img.drawHeight *= scale
    img.hAlign = "CENTER"
    return img


styles_placeholder = {}


def build_story(styles, width):
    raw = SOURCE.read_text(encoding="utf-8").splitlines()
    lines = skip_frontmatter(raw)
    story = []
    i = 0
    paragraph_lines = []
    list_items = []

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
            story.append(Paragraph("&#8226; " + inline_markup(item), styles["BulletCustom"]))
        if list_items:
            story.append(Spacer(1, 2 * mm))
        list_items = []

    while i < len(lines):
        line = lines[i]

        if not line.strip():
            flush_paragraph()
            flush_list()
            i += 1
            continue

        if line.strip() == "---":
            flush_paragraph()
            flush_list()
            story.append(Spacer(1, 2 * mm))
            i += 1
            continue

        img_match = re.match(r"^!\[(.*?)\]\((.*?)\)\s*$", line.strip())
        if img_match:
            flush_paragraph()
            flush_list()
            alt, path = img_match.group(1), img_match.group(2)
            story.append(image_flowable(path, width))
            story.append(Spacer(1, 2 * mm))
            i += 1
            if i < len(lines) and lines[i].strip().startswith("*Figure"):
                story.append(Paragraph(inline_markup(lines[i].strip().strip("*")), styles["Caption"]))
                story.append(Spacer(1, 4 * mm))
                i += 1
            continue

        if line.startswith("```"):
            flush_paragraph()
            flush_list()
            code_lines = []
            i += 1
            while i < len(lines) and not lines[i].startswith("```"):
                code_lines.append(escape(lines[i]))
                i += 1
            if i < len(lines):
                i += 1
            code_text = "<br/>".join(code_lines)
            story.append(Paragraph(f"<font name='Courier' size='8'>{code_text}</font>", styles["CodeBlock"]))
            story.append(Spacer(1, 4 * mm))
            continue

        if line.startswith("|"):
            flush_paragraph()
            flush_list()
            table_lines = []
            while i < len(lines) and lines[i].strip().startswith("|"):
                table_lines.append(lines[i])
                i += 1
            story.append(parse_table(table_lines, styles, width))
            story.append(Spacer(1, 5 * mm))
            continue

        heading = re.match(r"^(#{1,4})\s+(.*)$", line)
        if heading:
            flush_paragraph()
            flush_list()
            level = len(heading.group(1))
            text = heading.group(2).strip()
            if level == 1:
                story.append(Paragraph(inline_markup(text), styles["TitleCustom"]))
                story.append(Spacer(1, 4 * mm))
            elif level == 2:
                if story and not isinstance(story[-1], PageBreak):
                    story.append(PageBreak())
                story.append(Paragraph(inline_markup(text), styles["Heading2Custom"]))
                story.append(Spacer(1, 2 * mm))
            elif level == 3:
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

        if line.strip().startswith("*Figure") or line.strip().startswith("*Note:"):
            flush_paragraph()
            flush_list()
            story.append(Paragraph(inline_markup(line.strip().strip("*")), styles["Caption"]))
            story.append(Spacer(1, 3 * mm))
            i += 1
            continue

        paragraph_lines.append(line)
        i += 1

    flush_paragraph()
    flush_list()
    return story


def footer(canvas, doc):
    canvas.saveState()
    canvas.setStrokeColor(colors.HexColor("#D8E0E7"))
    canvas.line(18 * mm, 14 * mm, A4[0] - 18 * mm, 14 * mm)
    canvas.setFont("Helvetica", 8)
    canvas.setFillColor(colors.HexColor("#64748B"))
    canvas.drawString(18 * mm, 9 * mm, "G9 Post-Harvest Functional Brief")
    canvas.drawRightString(A4[0] - 18 * mm, 9 * mm, f"Page {doc.page}")
    canvas.restoreState()


def main():
    global styles_placeholder
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    styles = getSampleStyleSheet()
    styles.add(
        ParagraphStyle(
            name="TitleCustom",
            parent=styles["Title"],
            fontName="Helvetica-Bold",
            fontSize=22,
            leading=27,
            textColor=colors.HexColor("#17324D"),
            alignment=TA_CENTER,
            spaceAfter=3 * mm,
        )
    )
    styles.add(
        ParagraphStyle(
            name="Heading2Custom",
            parent=styles["Heading2"],
            fontName="Helvetica-Bold",
            fontSize=14,
            leading=18,
            textColor=colors.HexColor("#17324D"),
            spaceBefore=2 * mm,
            spaceAfter=3 * mm,
            keepWithNext=True,
        )
    )
    styles.add(
        ParagraphStyle(
            name="Heading3Custom",
            parent=styles["Heading3"],
            fontName="Helvetica-Bold",
            fontSize=11,
            leading=14,
            textColor=colors.HexColor("#2C5B7C"),
            spaceBefore=2 * mm,
            spaceAfter=2 * mm,
            keepWithNext=True,
        )
    )
    styles.add(
        ParagraphStyle(
            name="Heading4Custom",
            parent=styles["Heading4"],
            fontName="Helvetica-Bold",
            fontSize=10,
            leading=13,
            textColor=colors.HexColor("#334155"),
            keepWithNext=True,
        )
    )
    styles.add(
        ParagraphStyle(
            name="BodyTextCustom",
            parent=styles["BodyText"],
            fontName="Helvetica",
            fontSize=9.3,
            leading=13.2,
            textColor=colors.HexColor("#1F2937"),
            alignment=TA_LEFT,
        )
    )
    styles.add(
        ParagraphStyle(
            name="BulletCustom",
            parent=styles["BodyText"],
            fontName="Helvetica",
            fontSize=9.2,
            leading=12.5,
            leftIndent=10,
            firstLineIndent=-7,
            textColor=colors.HexColor("#1F2937"),
        )
    )
    styles.add(
        ParagraphStyle(
            name="Caption",
            parent=styles["BodyText"],
            fontName="Helvetica-Oblique",
            fontSize=8.5,
            leading=11,
            textColor=colors.HexColor("#64748B"),
            alignment=TA_CENTER,
        )
    )
    styles.add(
        ParagraphStyle(
            name="CodeBlock",
            parent=styles["BodyText"],
            fontName="Courier",
            fontSize=8,
            leading=10,
            textColor=colors.HexColor("#1F2937"),
            leftIndent=6,
            backColor=colors.HexColor("#F1F5F9"),
        )
    )
    styles.add(
        ParagraphStyle(
            name="TableCell",
            parent=styles["BodyText"],
            fontName="Helvetica",
            fontSize=7,
            leading=9,
            textColor=colors.HexColor("#1F2937"),
        )
    )
    styles.add(
        ParagraphStyle(
            name="TableHeader",
            parent=styles["BodyText"],
            fontName="Helvetica-Bold",
            fontSize=7,
            leading=9,
            textColor=colors.white,
        )
    )
    styles_placeholder = styles

    frame = Frame(
        18 * mm,
        19 * mm,
        A4[0] - 36 * mm,
        A4[1] - 37 * mm,
        leftPadding=0,
        rightPadding=0,
        topPadding=0,
        bottomPadding=0,
    )
    doc = BaseDocTemplate(
        str(OUTPUT),
        pagesize=A4,
        leftMargin=18 * mm,
        rightMargin=18 * mm,
        topMargin=18 * mm,
        bottomMargin=19 * mm,
        title="G9 Post-Harvest Functional Brief",
        author="G9 Banana Packaging Project",
    )
    doc.addPageTemplates([PageTemplate(id="main", frames=[frame], onPage=footer)])
    story = build_story(styles, A4[0] - 36 * mm)
    doc.build(story)
    print(OUTPUT)


if __name__ == "__main__":
    main()
