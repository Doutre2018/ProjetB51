# -*- coding: utf-8 -*-
from tkinter import *
from tkinter import tix
from tkinter import ttk
from PIL import Image,ImageDraw, ImageTk
import os,os.path
import math
from helper import Helper as hlp
from msilib.schema import Font

class Vue():
    def __init__(self,parent,largeur=800,hauteur=900):
        self.user = "Employe007"
        self.root=tix.Tk()
        self.root.title(os.path.basename(sys.argv[0]))
        self.root.protocol("WM_DELETE_WINDOW", self.fermerfenetre)
        self.parent=parent
        self.modele=None
        self.largeurDefault=largeur
        self.hauteurDefault=hauteur
        self.largeurEcran=self.root.winfo_screenwidth()
        self.hauteurEcran=self.root.winfo_screenmmheight()
        self.cadreTchatExiste=False

        self.images={}
        self.cadreactif=None
        self.creercadres()
        self.changecadre(self.cadreTchat)
        
    def changemode(self,cadre):
        if self.modecourant:
            self.modecourant.pack_forget()
        self.modecourant=cadre
        self.modecourant.pack(expand=1,fill=BOTH)            

    def changecadre(self,cadre,etend=0):
        if self.cadreactif:
            pass#self.cadreactif.grid_forget()
        self.cadreactif=cadre
        if etend:
            self.cadreactif.grid(expand=1,fill=BOTH)
        else:
            self.cadreactif.grid()
    
        
    def creercadres(self):
        self.creercadreTchat()
        #self.cadrejeu=Frame(self.root,bg="blue")
        #self.modecourant=None
    def afficherImage(self):
        canvasImage = Canvas(self.cadreTchat,width=120,height=100)
        image= Image.open("./chat.jpg")
        image= image.resize((120, 100), Image.ANTIALIAS)

        self.img=ImageTk.PhotoImage(image)
        canvasImage.create_image(0,0,image=self.img,anchor=NW)
        canvasImage.grid(row=0,column=1)
            
        
              
    def creercadreTchat(self):
        self.cadreTchat=Frame(self.root)
        self.root.overrideredirect(True) #Enleve la bordure
        self.root.geometry('%dx%d+%d+%d' % (self.largeurDefault, self.hauteurDefault, (self.largeurEcran/2)-(self.largeurDefault/2),(self.hauteurEcran/2)))
        self.titre = Label(self.cadreTchat, text="LE TCHAT", font="Arial 32")
        self.titre.grid(row=0,column=2)
        self.afficherImage()
        
        self.titreMessages = Label(self.cadreTchat,width=80,text="Messages :")
        self.titreMessages.grid(columnspan=4,column=0,row=3,pady=(10,0))
        self.listeMessage = Listbox(self.cadreTchat,width=80,height=40)
        self.listeMessage.grid(columnspan=4,column=0,row=4,padx=70,pady=(0,20))
        self.message = Text(self.cadreTchat, width=80,height=3)
        self.message.grid(columnspan=4,column=0,row=5,padx=70,pady=10)
        self.boutonMessage = Button(self.cadreTchat, text="Envoyer", width = 15,command=self.ajouterMessage)
        self.boutonMessage.grid(columnspan=4,column=0,row=6,padx=70)
    def ajouterMessage(self):
        self.listeMessage.insert(END, self.user + " : \n" + '\t' + self.message.get("1.0", END))
        self.message.delete("1.0", END)
    def fermerfenetre(self):
        print("ON FERME la fenetre")
        self.root.destroy()
    