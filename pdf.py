from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
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
            #self.trossos = plenarTrossos(subgrups,assignatures)
            self.prv = []
            self.sub = []
            self.TractaBoto(fine)

        def TractarPdf(self):
            name = filedialog.askopenfilename(title = "Escull el fitxer que conté la informació", filetypes = (("PDF files","*.pdf"),))
            cachos = name.split("/")
            self.num+=1
            self.sub.append(name)
            self.prv.append(cachos[len(cachos)-1])
            print("vector sub: " + ''.join(self.sub))
            print("vector prv: " + ''.join(self.prv))
            self.funcioScrollbar(fine)

            #Finestra2(name)

        def crearLabels(self,frame):
            t = 0
            while(t < self.num):
                Label(frame,
                      text = self.prv[t], anchor = W, bg = "white", fg = "black", font =("Arial",8), justify = LEFT).grid(row = t,sticky = W+E+N+S)
                t +=1

        def funcioScrollbar(self,fine):
            wrapper1 = LabelFrame(fine,bg = "white")

            myCanvas = Canvas(wrapper1,bg = "white", confine = "false")
            myCanvas.place(anchor = "nw")

            yscrollbar = Scrollbar(wrapper1, orient = 'vertical', command = myCanvas.yview)

            yscrollbar.place(relx=1, rely=0, relheight=1, anchor='ne')

            myCanvas.configure(yscrollcommand = yscrollbar.set)

            myCanvas.bind('<Configure>', lambda e:myCanvas.configure(scrollregion = myCanvas.bbox('all')))

            myFrame = Frame(myCanvas)
            myCanvas.create_window((0,0),window = myFrame,anchor='nw')

            wrapper1.place(relx = 0.45, rely = 0.4, relheight = 0.5, relwidth = 0.5)
            self.crearLabels(myFrame)


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
    fine.minsize(1250,685)
    fine.maxsize(1250,685)
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
