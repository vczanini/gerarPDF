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
with pdf.table(borders_layout='HORIZONTAL_LINES') as table:
    for data_row in TABLE_DATA[1:]:
        row = table.row()
        row.cell(f'{data_row[0]} \n {data_row[1]} \n {data_row[2]} \n ')  # First name
        row.cell(data_row[3])  # Last name

pdf.output('table.pdf')
