import fitz

pdffile = "Output.pdf"
doc = fitz.open(pdffile)
i = 0
while(i < 50):
    if(i == 2 or i == 4):
        page = doc.loadPage(i)  # number of page
        pix = page.getPixmap()
        output = "./imag/outfile" +str(i+1)+".png"
        pix.writePNG(output)
    i+=1
