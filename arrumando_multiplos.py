from fpdf import FPDF

TABLE_DATA = (
    ("First name", "Last name", "Age", "City"),
    ("Jules", "Smith", "34", "San Juan"),
    ("Mary", "Ramos", "45", "Orlando"),
    ("Carlson", "Banks", "19", "Los Angeles"),
    ("Lucas", "Cimon", "31", "Saint-Mathurin-sur-Loire"),
)

pdf = FPDF()
pdf.add_page()
pdf.set_font("Times", size=16)

# Define a custom function to draw cells with specified borders
def draw_cell(x, y, w, h, txt, border):
    pdf.rect(x, y, w, h)
    pdf.set_xy(x, y)
    pdf.multi_cell(w, h / 2, txt, border=0, align="C")

with pdf.table() as table:
    for i, data_row in enumerate(TABLE_DATA):
        row = table.row()
        for j, datum in enumerate(data_row):
            if j < 2:  # Only for the first name and last name cells
                draw_cell(row.x, row.y, row.width / 2, row.height, datum, 'LTRB' if j == 0 else 'LRTB')
                row.x += row.width / 2
            else:
                draw_cell(row.x, row.y, row.width, row.height, datum, 'LTRB')
        row.x = table.x
        row.y += row.height

pdf.output('table.pdf')
