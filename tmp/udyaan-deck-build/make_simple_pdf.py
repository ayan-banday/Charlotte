from pathlib import Path
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader

out = Path(r"S:\Charlotte\output\udyaan-playable-layer-simple")
pdf = canvas.Canvas(str(out / "Udyaan_Playable_Course_Layer_Simple_Proposal.pdf"), pagesize=(1280, 720))
for i in range(1, 15):
    pdf.drawImage(ImageReader(str(out / f"slide-{i:02d}.png")), 0, 0, 1280, 720)
    pdf.showPage()
pdf.save()
