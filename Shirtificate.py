from fpdf import FPDF

def main():
    user = input("What is you Full Name? ").strip()
    pdf = FPDF(orientation="portrait",format="A4")
    pdf.add_page()
    pdf.set_font("helvetica",size=60)
    pdf.image("Task38_CS50_Shirtificate/shirtificate.png",x = 0, y = 70)
    pdf.cell(0, 75, txt="CS50 Shirtificate", align="C")
    pdf.set_font("helvetica",size=30)
    pdf.set_text_color(255,255,0)
    pdf.cell(-190,250, txt=f"{user} took CS50", align="C")
    pdf.output("Task38_CS50_Shirtificate/test.pdf")

if __name__ == "__main__":
    main()
