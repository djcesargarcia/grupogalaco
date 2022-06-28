from fpdf import FPDF
from routes.models import Routes
# creating a pdf variable to save the PDF() class

pdf = FPDF()
pdf.add_page()

#set font style and size for pdf
pdf.set_font('Arial', size=16)

#creating call
pdf.cell(200, 10, txt = 'Hello World', ln=2, align='C')
pdf.write(Routes.id)

#save file with extension
pdf.output('Attempt.pdf')