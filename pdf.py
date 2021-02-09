from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from tkinter import scrolledtext
import os
from PyPDF2 import PdfFileReader, PdfFileWriter

def Finestra1():
    fine = Tk()
    fine.title("Pagina principal")
    #fine.configure(bg = "#0077C8
    fine.minsize(550,385)
    fine.maxsize(550,385)
    class aplicacio:
        def __init__(self,fine):
            self.txt = 0
            self.num = 0
            self.prv = []
            self.sub = []
            self.TractaBoto(fine)

        def TractarPdf(self):
            name = filedialog.askopenfilename(title = "Escull el fitxer que conté la informació", filetypes = (("PDF files","*.pdf"),))
            cachos = name.split("/")
            self.sub.append(name)
            self.prv.append(cachos[len(cachos)-1])
            self.funcioScrollbar(fine)
            self.num+=1
            #Finestra2(name)

        def crearLabels(self):
            i = 0
            string = ""
            while(i <= self.num):
                string = string + self.prv[i]+'\n'
                i+=1
            return string


        def funcioScrollbar(self,fine):
            text_area = scrolledtext.ScrolledText(fine,
                            width = 30,
                            height = 8,
                            font = ("Comic Sans",
                                    8))
            text_area.place(relx = 0.45, rely = 0.4, relheight = 0.2, relwidth = 0.5)
            text_area.insert(INSERT, self.crearLabels())
            text_area.configure(state ='disabled')



        def TractaBoto(self,fine):
            B = Button(fine, text ="Tractar Pdf", command = lambda: self.TractarPdf())
            B.place(relx = 0.25, rely = 0.25)


    def Titol(fine):
        frameArxius = Frame(fine, bg = "white")
        frameArxius.place(relx = 0.65, rely = 0.25)
        funcioScrollbar(fine)
    aplicacio(fine)
    fine.mainloop()



def Finestra2(name):
    fine = Tk()
    fine.title("Tractar PDF")
    #fine.configure(bg = "#0077C8
    fine.minsize(550,385)
    fine.maxsize(550,385)
    fine.mainloop()

    pdf = PdfFileReader(name, "rb")

    pdf_writer = PdfFileWriter()

    for page in range(2, 4):
        pdf_writer.addPage(pdf.getPage(page))

    output_fname = "Output.pdf"

    with open(output_fname, 'wb') as out:
        pdf_writer.write(out)

    print ("PDF file has been split")

Finestra1()
