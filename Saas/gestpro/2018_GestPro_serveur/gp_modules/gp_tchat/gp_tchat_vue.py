# -*- coding: utf-8 -*-
from tkinter import *
from tkinter import tix
from tkinter import ttk
from PIL import Image,ImageDraw, ImageTk
import os,os.path
import math
from helper import Helper as hlp
from msilib.schema import Font
import random 

class Vue():
    def __init__(self,parent,largeur=800,hauteur=900):
        self.parent=parent
        self.modele=parent.modele
        self.messagesDeBD = []
        self.peuplerMessagesBD()
        self.root=tix.Tk()
        self.root.title(os.path.basename(sys.argv[0]))
        self.root.protocol("WM_DELETE_WINDOW", self.fermerfenetre)
        self.root.config(bg="#E4E9F3")
        self.user = self.modele.usager
        self.largeurDefault=largeur
        self.hauteurDefault=hauteur
        self.largeurEcran=self.root.winfo_screenwidth()
        self.hauteurEcran=self.root.winfo_screenmmheight()
        self.cadreTchatExiste=False
        self.color = {"user":"color"};
         #Tout ce qui a été écrit en BD
#         self.listeIdParticipant = self.modele.selectTousUtilisateursLigneChat()
#         if self.listeIdParticipant:
#             for i in self.listeIdParticipant:
#                 for n in i:
#                     self.listeIdParticipant = n
#         if self.listeIdParticipant:
#             for i in self.modele.triNomAvecIdUtilisateur(self.listeIdParticipant):
#                 for n in i:
#                     self.listeNomParticipant = n
        self.images={}
        self.cadreactif=None
        self.creercadres()
        
        self.changecadre(self.cadreTchat)
        
        
    def peuplerMessagesBD(self):
        for n in self.modele.selectIdLignesChat():
            for i in n:
                self.messagesDeBD.append([self.modele.selectNomUtilisateurDeLigneChat(i), self.modele.selectTexteLigneChat(i)])
            
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
        
        image= Image.open("./chat.jpg")
        image= image.resize((120, 100), Image.ANTIALIAS)
        self.img=ImageTk.PhotoImage(image)

        #image2= Image.open("./chat2.jpg")
        #image2= image2.resize((120, 100), Image.ANTIALIAS)
        #self.img2=ImageTk.PhotoImage(image2)
        
        canvasImage1 = Canvas(self.cadreTchat,width=120,height=100)
        canvasImage1.create_image(0,0,image=self.img,anchor=NW)
        canvasImage1.grid(row=0,column=0)
        canvasImage2 = Canvas(self.cadreTchat,width=120,height=100)
        canvasImage2.create_image(0,0,image=self.img,anchor=NW)
        canvasImage2.grid(row=0,column=4)
        #self.parent.reloadMessageBD();
    
        
              
    def creercadreTchat(self):
        self.cadreTchat=Frame(self.root, bg="#E4E9F3")
        self.root.overrideredirect(True) #Enleve la bordure
        self.root.geometry('%dx%d+%d+%d' % (self.largeurDefault, self.hauteurDefault, (self.largeurEcran/2)-(self.largeurDefault/2),(self.hauteurEcran/2)))
        self.titre = Label(self.cadreTchat, text="LE CHAT", font="Arial 32", bg="#E4E9F3")
        self.titre.grid(columnspan=5,row=0,column=0)
        self.afficherImage()
        
        self.titreMessages = Label(self.cadreTchat,width=80,text="Messages :", bg="#E4E9F3")
        self.titreMessages.grid(columnspan=5,column=0,row=3,pady=(10,0))
        self.listeMessage = Listbox(self.cadreTchat,width=80,height=40)
        self.listeMessage.grid(columnspan=5,column=0,row=4,padx=70,pady=(0,20))
        self.message = Text(self.cadreTchat, width=80,height=3)
        self.message.grid(columnspan=5,column=0,row=5,padx=70,pady=10)
        self.boutonMessage = Button(self.cadreTchat, text="Envoyer", width = 15,command=self.ajouterMessage,bg="white",fg="#234078")
        self.boutonMessage.grid(columnspan=5,column=0,row=6,padx=70)
        

                    
    def ajouterMessage(self):
        self.messagesDeBD.append([self.modele.usager, self.message.get("1.0", END)])
        self.modele.insertLigneChat(self.message.get("1.0", END))
        self.message.delete("1.0", END)
    def random_color(self):
        return random.randint(0,0x1000000)

    def ajoutMessageBD(self):
        self.listeMessage.delete(0, END)
        if self.messagesDeBD:
            for message in self.messagesDeBD:
                if message[0] not in self.color:
                    color = '{:06x}'.format(self.random_color())
                    while (color in self.color.values()):
                        color = '{:06x}'.format(self.random_color())
                    self.color[message[0]] = '#'+ color
                #print(self.color.get(message[0]))
                if self.messagesDeBD.index(message):
                    self.listeMessage.insert(END, message[0] + " : \n" + '\t' + message[1])
                    self.listeMessage.itemconfig(END, {'fg':self.color.get(message[0])})


    def fermerfenetre(self):
        #print("ON FERME la fenetre")
        self.root.destroy()
    