import PyPDF2
import sys

# make all arguments given in *ledetekst*
inputs = sys.argv[1:]

# funcion for combining pdf
def pdf_combiner(pdf_list):
    merger =PyPDF2.PdfMerger()
    for pdf in pdf_list:
        print(pdf)
        merger.append(pdf)
    merger.write('super.pdf')
    merger.close()

pdf_combiner(inputs)
