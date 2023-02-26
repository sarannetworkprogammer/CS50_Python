from fpdf import FPDF

pdf = FPDF()
pdf.add_page()
pdf.set_font('helvetica', size=12)
pdf.set_margin(0)

pdf.cell(200,10, txt="CS50 Shirtificate", align = 'C')

pdf.image("shirtificate.png", x = 0, y= 20)


name = input("name ")
pdf.set_font_size(30)
pdf.set_text_color(255, 255, 255)
pdf.text(x=70, y=100, txt=f"{name} took CS50")




pdf.output("shirtificate.pdf")

