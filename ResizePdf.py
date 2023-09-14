import PyPDF2
from reportlab.lib.pagesizes import letter, landscape
from reportlab.pdfgen import canvas

# Create a new PDF with a custom size (45mm x 45mm)
output_pdf = "output.pdf"
c = canvas.Canvas(output_pdf, pagesize=(45, 45))

# Create a PDF reader object for the original A4 PDF
original_pdf = PyPDF2.PdfReader(open("/Users/07607.ben.yang/Downloads/XYPolicycopy.pdf", "rb"))
#original_pdf = PyPDF2.PdfReader(open("/Users/07607.ben.yang/Downloads/mvfl.pdf", "rb"))
length = original_pdf.pages[0].mediabox.width()
print(f"length is: {length}")
# Calculate the scaling factor to fit the A4 content into the 45mm x 45mm page
"""
scaling_factor = min(45 / float(original_pdf.pages[0].mediabox.width()),
                      45 / float(original_pdf.pages[0].mediabox.height()))

# Apply the scaling factor and add the A4 content to the new PDF
c.scale(scaling_factor, scaling_factor)
c.showPage()
c.save()

# Merge the resized content with the original A4 PDF
output_pdf_file = PyPDF2.PdfFileReader(open(output_pdf, "rb"))
original_pdf_file = PyPDF2.PdfFileReader(open("original.pdf", "rb"))
output = PyPDF2.PdfFileWriter()

for i in range(original_pdf_file.getNumPages()):
    page = original_pdf_file.getPage(i)
    page.mergeTranslatedPage(output_pdf_file.getPage(0), 0, 0)
    output.addPage(page)

# Save the final resized PDF
with open("resized.pdf", "wb") as output_file:
    output.write(output_file)
    """