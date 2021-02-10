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
            self.num = 0
            self.prv = []
            self.sub = []
            self.w = Spinbox(fine)
            self.EB = Button(fine, text ="Elimina")
            self.SB = Button(fine)
            self.SeparaBoto()
            self.EnB = Button(fine)
            self.text_area = scrolledtext.ScrolledText(fine,
                            width = 30,
                            height = 8,
                            font = ("Comic Sans",
                                    8))

        def SeparaPdf(self):
            name = filedialog.askopenfilename(title = "Escull el fitxer que conté la informació", filetypes = (("PDF files","*.pdf"),))
            cachos = name.split("/")
            if(name != ''):
                self.sub.append(name)
                self.prv.append(cachos[len(cachos)-1])
                self.num+=1
                self.funcioScrollbar()
                self.SB.config(text = "Afegeix PDF")
                self.EliminaBoto()
                if(self.num > 1):
                    self.EliminaSpin()
                self.EndavantBoto()

        def EliminaSpin(self):
            self.w.config(from_=1, to=self.num)
            self.w.place(relx = 0.65, rely = 0.65)

        def EliminaPdf(self):
            if(self.w.get() != ''):
                prv = []
                sub = []
                i = 0
                while(i < self.num):
                    if(i != int(self.w.get())-1):
                        prv.append(self.prv[i])
                        sub.append(self.sub[i])
                    i+=1
                self.prv = prv
                self.sub = sub
                self.num-=1
                self.w.delete(0,"end")
                self.EliminaSpin()
                if(len(self.prv) == 1):
                    self.w.delete(0,"end")
                    self.w.place_forget()
                self.funcioScrollbar()
            else:
                if(len(self.prv) == 1):
                    self.w.delete(0,"end")
                    self.w.place_forget()
                prv = []
                sub = []
                self.prv = prv
                self.sub = sub
                self.num-=1
                self.funcioScrollbar()
                if(len(self.prv) == 0):
                    self.text_area.place_forget()
                    self.EB.place_forget()
                    self.SB.config(text = "Separa PDF")
                    self.EnB.place_forget()

        def crearLabels(self):
            i = 0
            string = ""
            while(i < self.num):
                string = string + str(i+1) + ". " + self.prv[i]+'\n'
                i+=1
            return string

        def funcioScrollbar(self):
            self.text_area.config(state = 'normal')
            self.text_area.delete("1.0", END)
            self.text_area.insert(INSERT, self.crearLabels())
            self.text_area.config(state ='disabled')
            self.text_area.place(relx = 0.45, rely = 0.4, relheight = 0.2, relwidth = 0.5)

        def SeparaBoto(self):
            if(self.num == 0):
                self.SB.config(text = "Separa PDF")
                self.SB.place(relx = 0.25, rely = 0.25)
            self.SB.config(command = lambda: self.SeparaPdf())

        def EliminaBoto(self):
            self.EB.config(command = lambda: self.EliminaPdf())
            self.EB.place(relx = 0.45, rely = 0.65)

        def EndavantClick(self,vector1,vector2):
            self.EnB.config(state = DISABLED)
            Finestra2(vector1,vector2)

        def EndavantBoto(self):
            self.EnB.config(text = "Endavant!", command = lambda: self.EndavantClick(self.prv,self.sub))
            self.EnB.place(relx = 0.65, rely = 0.85)

    aplicacio(fine)
    fine.mainloop()


def Finestra2(vct1,vct2):
    fine = Tk()
    fine.title("Separar PDF")
    #el path es vct2 i el nom vct1
    fine.minsize(550,385)
    fine.maxsize(550,385)
    class SepPDF:
        def __init__(self,fine,vct1,vct2):
            self.num = 0
            self.et = vct1
            self.pa = vct2
            self.top = Spinbox(fine)
            self.bot = Spinbox(fine)
            self.FA = Frame(fine,bg = "white")
            self.etiquetaArxiu()
            self.lbl = Label(self.FA, bg = "white", text = self.et[self.num])
            self.TextEtiqueta()
            if(len(vct1)>1):
                self.BD = Button(fine)
                self.BotoDret()
                self.BE = Button(fine)

        def ClickBotoDret(self):
            self.num+=1
            self.BotoEsquerre()
            self.TextEtiqueta()
            if(self.num < len(self.et)-1):
                self.BotoDret()
            if(self.num == len(self.et)-1):
                self.BD.place_forget()

        def ClickBotoEsquerre(self):
            self.num-=1
            self.BotoDret()
            self.TextEtiqueta()
            if(self.num > 1):
                self.BotoEsquerre()
            if(self.num == 0):
                self.BE.place_forget()

        def TextEtiqueta(self):
            self.lbl.config(text = self.et[self.num])
            self.lbl.pack()

        def etiquetaArxiu(self):
            self.FA.place(rely = 0.1,relx = 0.5,relwidth = 0.35, relheight = 0.05)

        def BotoDret(self):
            self.BD.config(text = ">>", command = lambda: self.ClickBotoDret())
            self.BD.place(relx = 0.9, rely = 0.1)

        def BotoEsquerre(self):
            self.BE.config(text = "<<", command = lambda: self.ClickBotoEsquerre())
            self.BE.place(relx = 0.4, rely = 0.1)


    SepPDF(fine,vct1,vct2)
    fine.mainloop()

    #pdf = PdfFileReader(name, "rb")

    pdf_writer = PdfFileWriter()

    #for page in range(2, 4):
        #pdf_writer.addPage(pdf.getPage(page))

    #output_fname = "Output.pdf"

    #with open(output_fname, 'wb') as out:
        #pdf_writer.write(out)

    #print ("PDF file has been split")

Finestra1()
