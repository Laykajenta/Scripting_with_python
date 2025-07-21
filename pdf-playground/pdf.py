import PyPDF2

with open('dummy.pdf', 'rb') as file:
    reader = PyPDF2.PdfReader(file)
    side=reader.pages[0]
    side.rotate(90)
    writer = PyPDF2.PdfWriter()
    writer.add_page(side)
    with open('tilt.pdf', 'wb') as new_file:
        writer.write(new_file)
