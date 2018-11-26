# -*- coding: utf-8 -*-
from tkinter import *
from tkinter import tix
from tkinter import ttk
from PIL import Image,ImageDraw, ImageTk
import os,os.path
import math
from helper import Helper as hlp
from msilib.schema import Font
from IdMaker import Id
from tkinter.tix import COLUMN

class Vue():
    def __init__(self,parent,largeur=1200,hauteur=800):

        self.root=tix.Tk()
        self.root.title(os.path.basename(sys.argv[0]))
        self.root.protocol("WM_DELETE_WINDOW", self.fermerfenetre)
        self.parent=parent
        self.modele=None
        
        self.largeur=self.largeurDefault=largeur
        self.hauteur=self.hauteurDefault=hauteur
        self.largeurEcran=self.root.winfo_screenwidth()
        self.hauteurEcran=self.root.winfo_screenmmheight()
        
        self.cadrescrumExiste=False
        self.tableauDeColonne=[]
        self.tableauDeCarte=[]
        self.nbListe=0
        self.images={}
        self.cadreactif=None
        self.fullscreen=True
        self.creercadres()
        self.changecadre(self.cadrescrum)
        
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
        self.creercadrescrum()
        #self.cadrejeu=Frame(self.root,bg="blue")
        #self.modecourant=None
              
    def creercadrescrum(self):
        #permet d'intégrer l'application dans l'application de base
        self.root.overrideredirect(True) #Enleve la bordure
        self.root.geometry('%dx%d+%d+%d' % (self.largeurDefault, self.hauteurDefault, (self.largeurEcran/2)-(self.largeurDefault/2),(self.hauteurEcran/2)))

        self.cadrescrum=Frame(self.root,width=self.largeur,height=self.hauteur)
        self.cadrescrum.grid()
        
        self.titreColonneDate = Label(self.cadrescrum,width=20,text="Date du Scrum", font= "Arial 18")
        self.titreColonneDate.grid(column = 1, row=0,pady=(20,0))
        self.listeDate = Listbox(self.cadrescrum,width=30, height = 30)
        self.listeDate.grid(column = 1, row=1, padx=40,pady=0)
        self.boutonAjoutDate = Button(self.cadrescrum, width = 10, command=self.creationDate,text="Ajout")
        self.boutonAjoutDate.grid(column=1,row=2)
        
        self.titreColonneEmploye = Label(self.cadrescrum,width=20,text="Employés", font= "Arial 18")
        self.titreColonneEmploye.grid(column = 2, row=0,pady=(20,0))
        self.listeEmploye = Listbox(self.cadrescrum,width=30, height = 30)
        self.listeEmploye.grid(column = 2, row=1, padx=40,pady=0)
        self.boutonAjoutEmployer = Button(self.cadrescrum, width = 10, command=self.creationEmploye,text="Ajout")
        self.boutonAjoutEmployer.grid(column=2,row=2)
        
        self.titreSectionInfo = Label(self.cadrescrum,width=20,text="Information", font= "Arial 18")
        self.titreSectionInfo.grid(column = 3, row=0,pady=(20,0))
        self.infoEmploye = Frame(self.cadrescrum,width = self.largeur/2, height =(self.hauteur/3)*2, bg = "lightgray")
        self.infoEmploye.grid(column = 3, row = 1,padx=40,pady=0)

        #ce qui a été fait
        self.titreFait= Label(self.infoEmploye,width=20,text="Ce qui a été fait : ", font= "Arial 14", bg = "lightgray")
        self.titreFait.grid(column = 0, row=1,pady=(10,0))
        self.infoFait = Text(self.infoEmploye,width = 70, height=10)
        self.infoFait.grid(column = 0, row = 2,padx=10,pady=(0,10))
        #ce qui va être fait
        self.titreAFaire= Label(self.infoEmploye,width=20,text="A faire aujourd'hui :", font= "Arial 14", bg = "lightgray")
        self.titreAFaire.grid(column = 0, row=3,pady=(10,0))
        self.infoAFaire = Text(self.infoEmploye,width = 70, height=10)
        self.infoAFaire.grid(column = 0, row = 4,padx=10,pady=(0,10))
        #probleme
        self.titreProbleme= Label(self.infoEmploye,width=20,text="Problème :", font= "Arial 14", bg = "lightgray")
        self.titreProbleme.grid(column = 0, row=5,pady=(10,0))
        self.infoProbleme = Text(self.infoEmploye,width = 70, height=10)
        self.infoProbleme.grid(column = 0, row = 6,padx=10,pady=(0,10))
    
    def creationEmploye(self):
        self.fenetreCreationEmploye = Toplevel(self.cadrescrum, bg="#F8C471"  )
        self.fenetreCreationEmploye.wm_title("Creer un nouvel Employe")
        
        self.titreEmploye= Label(self.fenetreCreationEmploye,width=20,text="Nom de l'Employe : ", font= "Arial 14", bg = "#F8C471")
        self.titreEmploye.grid(column = 0, row=1,padx=20,pady=(20,5))
        self.nomEmploye = Entry(self.fenetreCreationEmploye,width = 20)
        self.nomEmploye.grid(column = 0, row = 2,padx=20,pady=(5,5))
    
        self.boutonCreerEmploye = Button(self.fenetreCreationEmploye, width = 10, command=self.ajouterEmploye,text="Ajout")
        self.boutonCreerEmploye.grid(column=0,row=3,padx=20,pady=20)
    def ajouterEmploye(self):
        self.listeEmploye.insert(END,self.nomEmploye.get())
        self.fenetreCreationEmploye.destroy()
    def creationDate(self):
        self.fenetreCreationDate = Toplevel(self.cadrescrum, bg="#F8C471"  )
        self.fenetreCreationDate.wm_title("Ajouter une nouvelle Date")
        
        self.titreDate= Label(self.fenetreCreationDate,width=20,text="Date : ", font= "Arial 14", bg = "#F8C471")
        self.titreDate.grid(column = 0, row=1,padx=20,pady=(20,5))
        self.nomDate = Entry(self.fenetreCreationDate,width = 20)
        self.nomDate.grid(column = 0, row = 2,padx=20,pady=(5,5))
        
        self.boutonCreerDate = Button(self.fenetreCreationDate, width = 10, command=self.ajouterDate,text="Ajout")
        self.boutonCreerDate.grid(column=0,row=3,pady=20)
    def ajouterDate(self):
        self.listeDate.insert(END,self.nomDate.get())
        self.fenetreCreationDate.destroy()
    def salutations(self):
        pass
    def fermerfenetre(self):
        print("ON FERME la fenetre")
        self.root.destroy()
    