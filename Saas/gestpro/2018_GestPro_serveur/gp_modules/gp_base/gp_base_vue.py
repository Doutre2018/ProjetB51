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
        self.root.attributes("-fullscreen", True)
        self.root.protocol("WM_DELETE_WINDOW", self.fermerfenetre)
        self.parent=parent
        self.modele=None
        self.largeur=self.root.winfo_screenwidth()/7
        self.hauteur=self.root.winfo_screenmmheight()/4.5
        self.images={}
        self.cadreactif=None
        self.creercadres()
        self.changecadre(self.cadrebase)
        
    def changemode(self,cadre):
        if self.modecourant:
            self.modecourant.pack_forget()
        self.modecourant=cadre
        self.modecourant.pack(expand=1,fill=BOTH)            

    def changecadre(self,cadre,etend=0):
        if self.cadreactif:
            self.cadreactif.grid_forget()
        self.cadreactif=cadre
        if etend:
            self.cadreactif.grid(expand=1,fill=BOTH)
        else:
            self.cadreactif.grid()
    
        
    def creercadres(self):
        self.creercadrebase()
        #self.cadrejeu=Frame(self.root,bg="blue")
        #self.modecourant=None
                
    def creercadrebase(self):
        
        self.cadrebase=Frame(self.root)
        self.boutonProjet1=Button(text="Projet 1",bg="#00BCD9",command=None,height=int(self.hauteur/3),width=int(self.largeur/11))
        self.boutonProjet2=Button(text="Projet 2",bg="#00BCD9",command=None,height=int(self.hauteur/3),width=int(self.largeur/11))
        self.boutonProjet3=Button(text="Projet 3",bg="#00BCD9",command=None,height=int(self.hauteur/3),width=int(self.largeur/11))

        self.boutonMandat=Button(text="Mandat",bg="#0B416C",command=None,height=4,width=int(self.largeur/11))
        self.boutonScrum=Button(text="Scrum",bg="#0072BB",command=None,height=4,width=int(self.largeur/11))
        self.boutonAnalyse=Button(text="Analyse \nTextuelle",bg="#2AABE2",command=None,height=4,width=int(self.largeur/11))
        self.boutonCasUsage=Button(text="Cas \nd'usage",bg="#01A89E",command=None,height=4,width=int(self.largeur/11))
        self.boutonMaquette=Button(text="Maquette",bg="#22B473",command=None,height=4,width=10)
        self.boutonCrc=Button(text="CRC",bg="#38B64A",command=None,height=4,width=int(self.largeur/11))
        self.boutonBudget=Button(text="Budget",bg="#8CC83E",command=None,height=4,width=int(self.largeur/11))
        self.boutonTchat=Button(text="Tchat",bg="#DAE121",command=None,height=4,width=int(self.largeur/11))
        self.boutonDonnee=Button(text="Modelisation \nde donnee",bg="#FAEF20",command=None,height=4,width=int(self.largeur/11))
        self.boutonTerlow=Button(text="Terlow",bg="#FFB242",command=None,height=4,width=int(self.largeur/11))
        
        self.boutonProjet1.grid(row=1,column=0,rowspan=5)
        self.boutonProjet2.grid(row=6,column=0,rowspan=5)
        self.boutonProjet3.grid(row=11,column=0,rowspan=5)

        self.boutonMandat.grid(row=0,column=1)
        self.boutonScrum.grid(row=0,column=2)
        self.boutonAnalyse.grid(row=0,column=3)
        self.boutonCasUsage.grid(row=0,column=4)
        self.boutonMaquette.grid(row=0,column=5)
        self.boutonCrc.grid(row=0,column=6)
        self.boutonBudget.grid(row=0,column=7)
        self.boutonTchat.grid(row=0,column=8)
        self.boutonDonnee.grid(row=0,column=9)
        self.boutonTerlow.grid(row=0,column=10)
        

        self.scroll = Scrollbar(self.root)
        self.mandatTexte = Text(self.root,bg="#09436B",height=int(self.hauteur/4),foreground="white")
        self.scroll.grid(row=1,column=3,rowspan=4)
        self.mandatTexte.grid(row=1,column=3,columnspan=6)
        self.scroll.config(command=self.mandatTexte.yview)
        self.mandatTexte.config(yscrollcommand=self.scroll.set)
        self.mandatTexte.insert(INSERT, "MANDAT :")
        self.mandatTexte.config(state=DISABLED)

        #self.fontTitle = tkFont.Font(family="Helvetica",size=36,weight="bold")
        self.projetTexte = Entry(self.root,foreground="black",font="-size 34", width=32,background="#526EFF",justify='center')
        self.projetTexte.grid(row=5,column=2,columnspan=8)
        self.projetTexte.insert(INSERT, self.projetName)
        self.projetTexte.config(state=DISABLED)
        
        self.listeSprint = Listbox(self.root,width=30, font="-size 16",height=int(self.hauteur/6))
        self.listeSprint.grid(row=6,column=4,rowspan=4,columnspan=4)
        for sprint in self.dicodesprint.keys():
                 self.listeSprint.insert(END,"Sprint " + str(sprint) + "................."+self.dicodesprint[sprint])
        
        
        self.listeTexte = Entry(self.root,foreground="black", font="-size 16",width=80,background="#526EFF",justify='center')
        self.listeTexte.grid(row=10,column=2,columnspan=8)
        self.listeTexte.insert(INSERT, "Membre \t\t\t\t Travail sur")
        self.listeTexte.config(state=DISABLED)
        
        self.listeMembre = Listbox(self.root,width=30, font="-size 16",height=int(self.hauteur/5))
        self.listeMembre.grid(row=11,column=3,rowspan=5,columnspan=4)
        for membre in self.utilisateursEtRole.keys():
                 self.listeMembre.insert(END,membre )
        self.listeOccupation = Listbox(self.root,width=30, font="-size 16",height=int(self.hauteur/5))
        self.listeOccupation.grid(row=11,column=6,rowspan=5,columnspan=4)
        for membre in self.utilisateursEtRole.keys():
                 self.listeOccupation.insert(END,self.utilisateursEtRole[membre])
             
    def salutations(self):
        pass
    def fermerfenetre(self):
        print("ON FERME la fenetre")
        self.root.destroy()
    