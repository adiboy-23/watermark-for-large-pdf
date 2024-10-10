from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4

watermark_file = "watermark.pdf"
c = canvas.Canvas(watermark_file, pagesize=A4)

c.setFont("Helvetica", 180)
c.setFillGray(0.5, 0.5)

c.translate(350, 450)
c.rotate(45)

c.drawCentredString(0, 0, "WATERMARK_NAME")

c.save()
