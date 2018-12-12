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
        self.root.config(bg="#E4E9F3")
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

        self.cadrescrum=Frame(self.root,width=self.largeur,height=self.hauteur,bg="#E4E9F3")
        self.cadrescrum.grid(column = 0, row = 0,)
        
        self.lTitre= Label()
        
        self.cadrescrumInfo = Frame(self.cadrescrum,bg="#E4E9F3")
        self.cadrescrumInfo.grid()
        self.titreColonneDate = Label(self.cadrescrumInfo,width=20,text="Date du Scrum", font= "Arial 14",bg="#E4E9F3")
        self.titreColonneDate.grid(column = 1, row=0,pady=(20,0))
        self.listeDate = Listbox(self.cadrescrumInfo,width=30, height = 30)
        self.listeDate.grid(column = 1, row=1, padx=40,pady=0)
        self.listeDate.bind("<ButtonRelease-1>",self.UpdateChampTexte)
        
        self.boutonAjoutDate = Button(self.cadrescrumInfo, width = 10, command=self.creationDate,text="Ajout",bg="white",relief=FLAT)
        self.boutonAjoutDate.grid(column=1,row=2,pady=(10,0))
        
        self.titreColonneEmploye = Label(self.cadrescrumInfo,width=20,text="Employés", font= "Arial 14",bg="#E4E9F3")
        self.titreColonneEmploye.grid(column = 2, row=0,pady=(20,5))
        self.listeEmploye = Listbox(self.cadrescrumInfo,width=30, height = 30)
        self.listeEmploye.grid(column = 2, row=1, padx=40,pady=0)
        self.listeEmploye.bind("<ButtonRelease-1>",self.AjoutNomDansText)
        self.boutonAjoutEmployer = Button(self.cadrescrumInfo, width = 10, command=self.creationEmploye,text="Ajout",bg="white",relief=FLAT)
        self.boutonAjoutEmployer.grid(column=2,row=2,pady=(10,0))
        

        self.infoEmploye = Frame(self.cadrescrum,width = self.largeur/2, height =(self.hauteur/3)*2,bg="#E4E9F3")
        self.infoEmploye.grid(column = 1, row = 0,padx=40,pady=0)
        self.titreSectionInfo = Label(self.infoEmploye,width=20,text="Information", font= "Arial 20",bg="#E4E9F3")
        self.titreSectionInfo.grid(column = 0, row=0,pady=(20,5))
        #ce qui a été fait
        self.titreFait= Label(self.infoEmploye,width=20,text="Ce qui a été fait : ", font= "Arial 14",bg="#E4E9F3")
        self.titreFait.grid(column = 0, row=1,pady=(10,0))
        self.infoFait = Text(self.infoEmploye,width = 70, height=10)
        self.infoFait.grid(column = 0, row = 2,padx=10,pady=(0,10))
        #ce qui va être fait
        self.titreAFaire= Label(self.infoEmploye,width=20,text="A faire aujourd'hui :", font= "Arial 14",bg="#E4E9F3")
        self.titreAFaire.grid(column = 0, row=3,pady=(10,0))
        self.infoAFaire = Text(self.infoEmploye,width = 70, height=10)
        self.infoAFaire.grid(column = 0, row = 4,padx=10,pady=(0,10))
        #probleme
        self.titreProbleme= Label(self.infoEmploye,width=20,text="Problème :", font= "Arial 14", bg="#E4E9F3")
        self.titreProbleme.grid(column = 0, row=5,pady=(10,0))
        self.infoProbleme = Text(self.infoEmploye,width = 70, height=10)
        self.infoProbleme.grid(column = 0, row = 6,padx=10,pady=(0,10))
    
    def creationEmploye(self):
        self.fenetreCreationEmploye = Toplevel(self.cadrescrum, bg="#234078"  )
        self.fenetreCreationEmploye.wm_title("Creer un nouvel Employe")
        
        largeurEcran = self.root.winfo_screenwidth()
        hauteurEcran = self.root.winfo_screenheight()
        x = (largeurEcran/2)-(500/2)
        y = (hauteurEcran/2)-(220/2)
        self.fenetreCreationEmploye.geometry("+%d+%d" % (x, y))
        
        self.titreEmploye= Label(self.fenetreCreationEmploye,width=20,text="Nom de l'Employe : ", font= "Arial 20", bg = "#234078",fg="white")
        self.titreEmploye.grid(column = 0, row=1,padx=20,pady=(20,5))
        self.nomEmploye = Entry(self.fenetreCreationEmploye,width = 20)
        self.nomEmploye.grid(column = 0, row = 2,padx=20,pady=(5,5))
    
        self.boutonCreerEmploye = Button(self.fenetreCreationEmploye, width = 10, command=self.ajouterEmploye,text="Ajout", bg="white", relief=FLAT)
        self.boutonCreerEmploye.grid(column=0,row=3,padx=20,pady=20)
    def ajouterEmploye(self):
        self.listeEmploye.insert(END,self.nomEmploye.get())
        self.fenetreCreationEmploye.destroy()
    def creationDate(self):
        self.fenetreCreationDate = Toplevel(self.cadrescrum, bg="#234078"  )
        self.fenetreCreationDate.wm_title("Ajouter une nouvelle Date")
        largeurEcran = self.root.winfo_screenwidth()
        hauteurEcran = self.root.winfo_screenheight()
        x = (largeurEcran/2)-(500/2)
        y = (hauteurEcran/2)-(220/2)
        self.fenetreCreationDate.geometry("+%d+%d" % (x, y))
        
        
        self.labelJour=Label(self.fenetreCreationDate, text="Ajouter une date",font= "arial, 18",bg="#234078", fg="white")
        self.labelJour.grid(row=0, column=0,columnspan=3, pady=(20,20));
        self.labeldate= Label(self.fenetreCreationDate, text="Date: ",font= "arial, 12",bg="#234078", fg="white")
        self.labeldate.grid(row=1, column=0,padx=(40,0));
        self.jour = Spinbox(self.fenetreCreationDate, width=2, relief=FLAT,from_=1, to=31,buttonuprelief=FLAT)
        self.jour.grid(row=1, column=1);
        self.comboMois= ttk.Combobox(self.fenetreCreationDate,justify=CENTER,values=[
                                    "Janvier", 
                                    "Février",
                                    "Mars",
                                    "Avril",
                                    "Mai",
                                    "Juin",
                                    "Juillet",
                                    "Aout",
                                    "Septembre",
                                    "Octobre",
                                    "Novembre",
                                    "Décembre"])
        self.comboMois.current(0)
        self.comboMois.grid(row=1, column=2, padx=(0,40))
        
        self.labelJour = Label(self.fenetreCreationDate, text="Jour",font= "arial, 10",bg="#234078", fg="white")
        self.labelJour.grid(row=2, column=1)
        self.labelJour = Label(self.fenetreCreationDate, text="Mois(Lettre)",font= "arial, 10",bg="#234078", fg="white")
        self.labelJour.grid(row=2, column=2,padx=(0,40))
        
        self.boutonCreerDate = Button(self.fenetreCreationDate, width = 10, command=self.ajouterDate,text="Ajout", bg="white", relief=FLAT)
        self.boutonCreerDate.grid(row=3,column=0,pady=20,columnspan=3)
    def ajouterDate(self):
        self.listeDate.insert(END,self.nomDate.get())
        self.fenetreCreationDate.destroy()
    def salutations(self):
        pass
    def fermerfenetre(self):
        print("ON FERME la fenetre")
        self.root.destroy()
        
    def UpdateChampTexte(self,evt):
        print("")
        #Coder ici je pense pour updater les champ de texte (Information) 
        #self.infoFait
        #self.infoAFaire
        #self.infoProbleme
        
    def AjoutNomDansText(self,evt):
        a=()
        a=self.listeEmploye.curselection()
        
        nomEmp=self.listeEmploye.get(a)
        self.infoFait.insert(END,"\n"+nomEmp+":")
        self.infoAFaire.insert(END,"\n"+nomEmp+":")
        self.infoProbleme.insert(END,"\n"+nomEmp+":")
        
        #Dans cette fonction on prend le nom cliquer dans la liste des employer et on rajoute un nom dans les champ de texte de information
    