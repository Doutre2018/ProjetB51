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
    def __init__(self,parent,largeur=800,hauteur=600):
        #Variable de BD
        self.projetName="Projet de Gestion de Projet"
        self.utilisateursEtRole ={"Joé":"Donnée",
                                  "Claudia":"Maquette",
                                  "Ludovic":"Maquette",
                                  "JF":"Rien",
                                  "Simon":"Rien",
                                  "Danick":"Maquette",
                                  "Marylene":"Rien",}
        self.dicodesprint={1:"29 oct. 2018",
                           2:"29 oct. 2018",
                           3:"29 oct. 2018"}
        
        
        self.root=tix.Tk()
        self.root.title(os.path.basename(sys.argv[0]))
        self.root.attributes("-fullscreen", False)
        self.root.protocol("WM_DELETE_WINDOW", self.fermerfenetre)
        self.parent=parent
        self.modele=None
        self.largeur=largeur
        self.hauteur=hauteur
        self.cadremandatExiste=False

        self.images={}
        self.cadreactif=None
        self.fullscreen=True
        self.creercadres()
        self.changecadre(self.cadremandat)
        
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
        self.creercadremandat()
        #self.cadrejeu=Frame(self.root,bg="blue")
        #self.modecourant=None
         
            
    

    def destroycadremandat(self):
        self.cadremandat.destroy()                   
              
    def creercadremandat(self):
        self.root.overrideredirect(True)
        
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        x = (screen_width/2) - (self.largeur/2)
        y = (screen_height/3) - (self.hauteur/3)
        self.root.geometry('%dx%d+%d+%d' % (self.largeur, self.hauteur, x, y))
    
        self.cadremandat=Frame(self.root)
        
        self.root.grid(800,600,100,100)
        self.scroll = Scrollbar(self.cadremandat)
        self.mandatTexte = Text(self.cadremandat,bg="#09436B",height=int(self.hauteur/(4*10)),foreground="white")
        self.scroll.grid(row=1,column=3,rowspan=4)
        self.mandatTexte.grid(row=1,column=3,columnspan=6)
        self.scroll.config(command=self.mandatTexte.yview)
        self.mandatTexte.config(yscrollcommand=self.scroll.set)
        self.mandatTexte.insert(INSERT, "MANDAT :")
        self.mandatTexte.config(state=DISABLED)

        #self.fontTitle = tkFont.Font(family="Helvetica",size=36,weight="bold")
        self.projetTexte = Entry(self.cadremandat,foreground="black",font="-size 34", width=32,background="#526EFF",justify='center')
        self.projetTexte.grid(row=5,column=2,columnspan=8)
        self.projetTexte.insert(INSERT, self.projetName)
        self.projetTexte.config(state=DISABLED)
        
        self.listeSprint = Listbox(self.cadremandat,width=30, font="-size 16",height=int(self.hauteur/(6*7)))
        self.listeSprint.grid(row=6,column=4,rowspan=4,columnspan=4)
        for sprint in self.dicodesprint.keys():
                 self.listeSprint.insert(END,"Sprint " + str(sprint) + "................."+self.dicodesprint[sprint])
        
        
        self.listeTexte = Entry(self.cadremandat,foreground="black", font="-size 16",width=80,background="#526EFF",justify='center')
        self.listeTexte.grid(row=10,column=2,columnspan=8)
        self.listeTexte.insert(INSERT, "Membre \t\t\t\t Travail sur")
        self.listeTexte.config(state=DISABLED)
        
        self.listeMembre = Listbox(self.cadremandat,width=30, font="-size 16",height=int(self.hauteur/(5*10)))
        self.listeMembre.grid(row=11,column=3,rowspan=5,columnspan=4)
        for membre in self.utilisateursEtRole.keys():
                 self.listeMembre.insert(END,membre )
        self.listeOccupation = Listbox(self.cadremandat,width=30, font="-size 16",height=int(self.hauteur/(5*10)))
        self.listeOccupation.grid(row=11,column=6,rowspan=5,columnspan=4)
        for membre in self.utilisateursEtRole.keys():
                 self.listeOccupation.insert(END,self.utilisateursEtRole[membre])
        self.cadremandatExiste=True
    def accesScrum(self):
        ad="http://"+ipserveur+":"+self.nodeport
        self.serveur=ServerProxy(ad)
        mod = self.serveur.requetemodule()
        self.requetemodule(mod)    
    def salutations(self):
        pass
    def fermerfenetre(self):
        print("ON FERME la fenetre")
        self.root.destroy()
    