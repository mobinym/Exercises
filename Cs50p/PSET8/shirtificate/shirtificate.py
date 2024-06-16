from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'CS50 Shirtificate', 0, 1, 'C')

def create_shirtificate(name):
    pdf = PDF()
    pdf.add_page()

    # Add shirt image
    pdf.image('shirtificate.png', x = 65, y = 80, w = 80)

    # Add name
    pdf.set_xy(105, 130)
    pdf.set_text_color(255, 255, 255) # Set text color to white
    pdf.set_font('Arial', '', 12)
    pdf.cell(0, 10, name, 0, 1, 'C')

    pdf.output('shirtificate.pdf', 'F')

def main():
    name = input("Enter your name: ")
    create_shirtificate(name)

if __name__ == "__main__":
    main()
