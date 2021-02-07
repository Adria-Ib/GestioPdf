import os
from PyPDF2 import PdfFileReader, PdfFileWriter

pdf = PdfFileReader('Output.pdf', "rb")

i = 0
while(i < 2):
    pdf_writer = PdfFileWriter()
    pdf_writer.addPage(pdf.getPage(i+1))
    output_fname = "Out" + str(i+1) +".pdf"

    with open(output_fname, 'wb') as out:
        pdf_writer.write(out)
    i+=1

print ("PDF file has been split")
