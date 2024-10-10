import PyPDF2

original_pdf = "file_naem.pdf"
watermark_pdf = "watermark.pdf"
output_pdf = "watermarked_output.pdf"

with open(original_pdf, "rb") as file, open(watermark_pdf, "rb") as watermark_file:
    reader = PyPDF2.PdfReader(file)
    watermark = PyPDF2.PdfReader(watermark_file)
    writer = PyPDF2.PdfWriter()

    watermark_page = watermark.pages[0]

    for i in range(len(reader.pages)):
        page = reader.pages[i]
        page.merge_page(watermark_page)
        writer.add_page(page)

    with open(output_pdf, "wb") as output_file:
        writer.write(output_file)

print(f"Watermark added to all pages. Output saved as {output_pdf}")
