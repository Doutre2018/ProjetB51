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
        
        self.cadreterlowExiste=False
        self.tableauDeColonne=[]
        self.tableauDeCarte=[]
        self.nbListe=0
        self.images={}
        self.cadreactif=None
        self.fullscreen=True
        self.creercadres()
        self.changecadre(self.cadreterlow)
        
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
        self.creercadreterlow()
        #self.cadrejeu=Frame(self.root,bg="blue")
        #self.modecourant=None
    def afficherImage(self):
        canvasImage = Canvas(self.root,width=self.largeur,height=self.hauteur)
        image= Image.open("./terlow.png")
        image= image.resize((self.largeur, self.hauteur), Image.ANTIALIAS)

        self.img=ImageTk.PhotoImage(image)
        canvasImage.create_image(0,0,image=self.img,anchor=NW)
        canvasImage.grid()
    def creercadreterlow(self):
        #permet d'intégrer l'application dans l'application de base
        self.root.overrideredirect(True) #Enleve la bordure
        self.root.geometry('%dx%d+%d+%d' % (self.largeurDefault, self.hauteurDefault, (self.largeurEcran/2)-(self.largeurDefault/2),(self.hauteurEcran/2)))
        
        #Enlever pour voir vrai logiciel
        #self.afficherImage()
        
        self.cadreterlow=Frame(self.root,width=self.largeur,height=self.hauteur, bg="#E4E9F3")
        self.cadreterlow.grid()
        
        
        self.boutonAjoutListe = Button(self.cadreterlow, bg="white", fg ="#234078", text="Ajouter Colonne",command=self.ajouterListe)
        self.boutonAjoutListe.grid()
        self.cadreterlowExiste=True
        

    def ajouterListe(self):
        self.tableauDeColonne.append(Frame(self.cadreterlow,width=100,height=600,bg="#d5e0e3",bd=4,highlightcolor="#234078",highlightthickness=1))
        liste = self.tableauDeColonne[self.nbListe]

        liste.bind('<Button-3>', lambda evt: self.deplacerColonneRight(evt, liste,self.nbListe))
        liste.bind('<Button-2>', lambda evt: self.deplacerColonneLeft(evt, liste,self.nbListe))

        titre = Entry(liste, width=32)
        titre.insert(END, "Titre")
        noListe=self.nbListe
        boutonAjoutCarte = Button(liste, text="Ajouter Carte", bg="white", fg ="#234078",command= lambda: self.ajouterCarte(noListe))
        
        liste.grid(column=self.nbListe,row=1,padx=10)
        titre.grid(row=0)

        boutonAjoutCarte.grid(row=1)
        self.nbListe+=1

        
        
    def ajouterCarte(self, noListe):
        noCarte=0
        colonne = self.tableauDeColonne[noListe]
        contenuText =StringVar()
        contenu = Entry(colonne,width=32,text=contenuText)
        self.tableauDeCarte.append([])
        contenu.bind("<Double-Button-1>", lambda evt: self.modifierCarte(evt,noCarte,colonne,contenuText))
        contenu.grid()
        noCarte+=1

    def deplacerColonneRight(self,evt,colonne,noliste):
        g = colonne.grid_info()
        
        if(g['column'] < self.nbListe):
            colonne.grid(column=g['column']+1,row=g['row'])
            colonne.bind('<Button-3>', lambda evts: self.deplacerColonneRight(evts, colonne,g['column']+1))
    
            if 'self.tableauDeColonne[self.nbListe+1]' in globals():
                colonne2=self.tableauDeColonne[g['column']+1]
                colonne2.grid(column=g['column'],row=g['row'])
                colonne2.bind('<Button-3>', lambda evts: self.deplacerColonneRight(evts, colonne,g['column']))

                temp = self.tableauDeColonne[self.nbListe]
                self.tableauDeColonne[self.nbListe] = self.tableauDeColonne[self.nbListe+1]
                self.tableauDeColonne[self.nbListe+1]=temp
    def deplacerColonneLeft(self,evt,colonne,noliste):
        g = colonne.grid_info()
        
        if(g['column'] < self.nbListe):
            colonne.grid(column=g['column']+1,row=g['row'])
            colonne.bind('<Button-2>', lambda evts: self.deplacerColonneLeft(evts, colonne,g['column']-1))
    
            if 'self.tableauDeColonne[self.nbListe+1]' in globals():
                colonne2=self.tableauDeColonne[g['column']-1]
                colonne2.grid(column=g['column'],row=g['row'])
                colonne2.bind('<Button-2>', lambda evts: self.deplacerColonneLeft(evts, colonne,g['column']))

                temp = self.tableauDeColonne[self.nbListe]
                self.tableauDeColonne[self.nbListe] = self.tableauDeColonne[self.nbListe-1]
                self.tableauDeColonne[self.nbListe-1]=temp
            
    def changerCarte(self,noCarte,contenuText):
        listeInfoCarte = []
        listeInfoCarte.append(self.entreeNomCarte.get())
        listeInfoCarte.append(self.entreeDescriptionCarte.get("1.0",END))
        listeInfoCarte.append(self.entreeeProprietaireCarte.get())
        self.tableauDeCarte[noCarte]=listeInfoCarte;
        contenuText.set(listeInfoCarte[0])
        self.fenetreModificationCarte.destroy()


    def modifierCarte(self,evt,noCarte,colonne,contenuText):
        self.tableauDeCarte.append([])

        self.fenetreModificationCarte = Toplevel(self.root, bg ="#234078")
        self.fenetreModificationCarte.wm_title("Modification de Carte")
            
        self.texteNomCarte = Label(self.fenetreModificationCarte, text="Nom de la carte :", bg ="#234078",fg="white")
        self.texteNomCarte.grid(row=1,column=1, padx=50, pady=(30,10))
              
        self.entreeNomCarte = Entry(self.fenetreModificationCarte)
        self.entreeNomCarte.grid(row=2,column=1, padx=50, pady=(0,10))
        
        self.texteDescriptionCarte = Label(self.fenetreModificationCarte, text="Description :", bg ="#234078",fg="white")
        self.texteDescriptionCarte.grid(row=3,column=1, padx=50, pady=(30,10))
              
        self.entreeDescriptionCarte = Text(self.fenetreModificationCarte)
        self.entreeDescriptionCarte.grid(row=4,column=1, padx=50, pady=(0,10))
        
        self.texteProprietaireCarte = Label(self.fenetreModificationCarte, text="Proprietaire :", bg ="#234078",fg="white")
        self.texteProprietaireCarte.grid(row=5,column=1, padx=50, pady=(30,10))
              
        self.entreeeProprietaireCarte = Entry(self.fenetreModificationCarte)
        self.entreeeProprietaireCarte.grid(row=6,column=1, padx=50, pady=(0,10))
                
        self.boutonModificationCarte = Button(self.fenetreModificationCarte, text="Modifier Carte", bg="white", fg ="#234078",command= lambda:self.changerCarte(noCarte,contenuText))
        self.boutonModificationCarte.grid(row=7,column=1, padx=50, pady=(0,30))

        
    def salutations(self):
        pass
    def fermerfenetre(self):
        print("ON FERME la fenetre")
        self.root.destroy()
    