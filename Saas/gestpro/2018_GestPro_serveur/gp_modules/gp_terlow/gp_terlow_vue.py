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
from tkinter.ttk import Combobox

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
        
        self.cadreterlowExiste=False
        self.tableauDeColonne=[]
        self.listeColonnes = self.parent.modele.listeColonnes
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
        
        self.cadreterlow=Frame(self.root,width=self.largeur,height=self.hauteur)
        self.cadreterlow.grid()
        
        self.boutonAjoutListe = Button(self.cadreterlow, text="Ajouter Colonne",command=self.ajouterListe)
        self.boutonAjoutListe.grid()
        self.cadreterlowExiste=True
        
        commande = "SELECT * FROM Colonnes_Terlow"
        sql = self.parent.serveur.requeteSelection(commande)
        
        for n in sql:
            self.nbListe += 1
        
        if self.parent.modele.listeColonnes:
            self.fetchTerlow()
        

    def ajouterListe(self):
        self.tableauDeColonne.append(Frame(self.cadreterlow,width=100,height=600,bg="white",bd=4,highlightcolor="red",highlightthickness=1))
        liste = self.tableauDeColonne[self.nbListe]

        liste.bind('<Button-3>', lambda evt: self.deplacerColonneRight(evt, liste,self.nbListe))
        liste.bind('<Button-2>', lambda evt: self.deplacerColonneLeft(evt, liste,self.nbListe))

        entreeTitre = Entry(liste, width=32)
        entreeTitre.insert(END, "Titre")
        noListe=self.nbListe
        boutonAjoutCarte = Button(liste, text="Ajouter Carte",command= lambda ordre = noListe: self.ajouterCarte(ordre))
        
        liste.grid(column=self.nbListe,row=1,padx=10)
        entreeTitre.grid(row=0)

        boutonAjoutCarte.grid(row=1)
        
        ordre = str(noListe)
        titre = entreeTitre.get()
        param = (ordre, titre,)
        self.parent.serveur.requeteInsertionPerso("INSERT INTO Colonnes_Terlow (ordre, titre) VALUES (?, ?)", param )
        self.nbListe+=1

    def ajouterCarte(self, noListe):
        noCarte=0
        noColonne = 0
        index = 0
        colonne = self.tableauDeColonne[noListe]
        
        for n in self.tableauDeColonne:
            if colonne == n:
                noColonne = index
                
            index += 1
        
        contenuText =StringVar()
        contenu = Entry(colonne,width=32,text=contenuText)
        self.tableauDeCarte.append([])
        contenu.bind("<Button-1>", lambda evt: self.modifierCarte(evt,noCarte,noColonne,contenuText))
        contenu.grid()
        noCarte+=1
        
    # ------------------ DM ------------------
    def fetchTerlow(self):
        noListe = 0
        
        for n, colonne in enumerate(self.parent.modele.listeColonnes):
            self.tableauDeColonne.append(Frame(self.cadreterlow,width=100,height=600,bg="white",bd=4,highlightcolor="red",highlightthickness=1))
            liste = self.tableauDeColonne[noListe]
            
            titre = Entry(liste, width=32)
            titre.insert(END, colonne.titre)
            boutonAjoutCarte = Button(liste, text="Ajouter Carte",command= lambda ordre = noListe: self.ajouterCarte(ordre))
        
            liste.grid(column=noListe,row=1,padx=10)
            titre.grid(row=0)

            boutonAjoutCarte.grid(row=1)
            
            
            if colonne.listeCartes:
                for n in colonne.listeCartes:
                    noCarte=0
                    col = self.tableauDeColonne[noListe]
                    contenuText = StringVar()
                    contenu = Entry(col,width=32,text=contenuText)
                    contenu.insert(0, n.titre)
                    self.tableauDeCarte.append([])
                    contenu.bind("<Button-1>", lambda evt, noColonne = noListe: self.modifierCarte(evt,noCarte,noColonne,contenuText))
                    contenu.grid()
                    noCarte+=1
        
            noListe += 1

        self.nbListe = noListe
    # ----------------------------------------

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
    
     
    def changerCarte(self, noColonne, noCarte, contenuText):
        nom = self.entreeNomCarte.get()
        description = self.entreeDescriptionCarte.get("1.0",END)
        #heureEst = (int(self.entreeHeuresEstimees.get()) * 60) + int(self.entreeMinutesEstimees)
        
        #insère les infos entrées par l'user dans la listeInfoCarte
        listeInfoCarte = []
        listeInfoCarte.append(nom)
        listeInfoCarte.append(description)
        #listeInfoCarte.append(self.entreeAnneeFin.get())
        #listeInfoCarte.append(self.entreeMoisFin.get())
        #listeInfoCarte.append(self.entreeJoursFin.get())
        #listeInfoCarte.append(self.entreeHeureFin.get())
        #listeInfoCarte.append(self.entreeMinuteFin.get())
        #listeInfoCarte.append(heureEst)
        #listeInfoCarte.append(self.entreeeProprietaireCarte.get())
        
        commande = "UPDATE Cartes_Terlow" 
        commande += " SET titre = '" + str(nom) + "', description = '" + str(description) + "'"
        commande += " WHERE id_colonne = " + str(noColonne + 1) + " AND ordre = " + str(noCarte)
        self.parent.serveur.requeteMiseAJour(commande)

        #prend les infos et les insère dans le tableau de cartes
        self.tableauDeCarte[noCarte]=listeInfoCarte;
        contenuText.set(listeInfoCarte[0])
        self.fenetreModificationCarte.destroy()
        
        print("Fonctionalité encore en développement")
        #self.cadreterlow.destroy()
        #self.tableauDeCarte = []
        #self.tableauDeColonne = []
        #self.creercadreterlow()

    def modifierCarte(self,evt,noCarte,noColonne,contenuText):
        commande = "SELECT * FROM Cartes_Terlow WHERE id_colonne = " + str(noColonne + 1)
        carte = self.parent.serveur.requeteSelection(commande)
        for n in carte:
            carte = n
        print(carte)
        
        self.tableauDeCarte.append([])

        self.fenetreModificationCarte = Toplevel(self.root )
        self.fenetreModificationCarte.wm_title("Modification de Carte")
            
        self.texteNomCarte = Label(self.fenetreModificationCarte, text="Nom de la carte :",)
        self.texteNomCarte.grid(row=1,column=1, padx=50, pady=(30,10))
              
        self.entreeNomCarte = Entry(self.fenetreModificationCarte)
        
        self.texteDescriptionCarte = Label(self.fenetreModificationCarte, text="Description :",)
        self.texteDescriptionCarte.grid(row=3,column=1, padx=50, pady=(30,10))
              
        self.entreeDescriptionCarte = Text(self.fenetreModificationCarte)
        # ------------------ DM ------------------
        self.frameFinEstimation = Frame(self.fenetreModificationCarte, width = self.fenetreModificationCarte.winfo_width(), height = 10, relief = FLAT)
        self.frameFinEstimation.grid(row = 5, column = 1, padx = 50, pady = (0, 10))
        
        self.frameDateFin = Frame(self.frameFinEstimation, width = self.frameFinEstimation.winfo_width() / 2, height = 10, relief = FLAT)
        self.frameDateFin.grid(row = 1, column = 1, padx = 50, pady = (0, 10))
        
        self.frameTempsEstime = Frame(self.frameFinEstimation, width = self.frameFinEstimation.winfo_width() / 2, height = 10, relief = FLAT)
        self.frameTempsEstime.grid(row = 1, column = 2, padx = 50, pady = (0, 10))
        
        # Section pour entrer la date de fin
        self.texteDateFin = Label(self.frameDateFin, text="Date de fin :",)
        self.texteDateFin.grid(row = 1, column = 1, padx = 5, pady = (0, 10))
        
        annees = []
        for i in range(2018, 2025):
            annees.append(i)
            
        self.entreeAnneeFin = ttk.Combobox(self.frameDateFin, width = 6, justify = CENTER, values = annees)
        
        mois = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
        self.entreeMoisFin = ttk.Combobox(self.frameDateFin, width = 4, justify = CENTER, values = mois)
        
        jours = []
        for i in range(1, 32):
            jours.append(i)
            
        self.entreeJoursFin = ttk.Combobox(self.frameDateFin, width = 4, justify = CENTER, values = jours)
        
        self.entreeHeureFin = Entry(self.frameDateFin, width = 6, justify = CENTER)
        
        self.entreeMinuteFin = Entry(self.frameDateFin, width = 6, justify = CENTER)
        
        # Section pour entrer le temps de travail estimé
        self.texteTempsEstime = Label(self.frameTempsEstime, text = "Temps estimé :")
        self.texteTempsEstime.grid(row = 1, column = 1, padx = 5, pady = (0, 10))
        
        self.entreeHeuresEstimees = Entry(self.frameTempsEstime, width = 4, justify = CENTER)
        
        self.entreeMinutesEstimees = Entry(self.frameTempsEstime, width = 4, justify = CENTER)
        # ----------------------------------------
        
        self.texteProprietaireCarte = Label(self.fenetreModificationCarte, text="Proprietaire :",)
        self.texteProprietaireCarte.grid(row=6,column=1, padx=50, pady=(30,10))
              
        self.entreeeProprietaireCarte = Entry(self.fenetreModificationCarte)
        self.entreeeProprietaireCarte.grid(row=7,column=1, padx=50, pady=(0,10))
        
        if carte:
            self.entreeNomCarte.insert(0, carte[3])
            self.entreeDescriptionCarte.insert(INSERT, carte[4])
            self.entreeAnneeFin.insert(0, 2018)
            self.entreeMoisFin.insert(0, 12)
            self.entreeJoursFin.insert(0, 21)
            self.entreeHeureFin.insert(0, 23)
            self.entreeMinuteFin.insert(0, 59)
            self.entreeHeuresEstimees.insert(0, 48)
            self.entreeMinutesEstimees.insert(0, 1)
        
        else:                
            self.entreeAnneeFin.insert(0, "AAAA")
            self.entreeMoisFin.insert(0, "MM")
            self.entreeJoursFin.insert(0, "JJ")
            self.entreeHeureFin.insert(0, "HH")
            self.entreeMinuteFin.insert(0, "Min")
            self.entreeHeuresEstimees.insert(0, "HH")
            self.entreeMinutesEstimees.insert(0, "Min")
            
        # Grids
        self.entreeNomCarte.grid(row=2,column=1, padx=50, pady=(0,10))
        self.entreeDescriptionCarte.grid(row=4,column=1, padx=50, pady=(0,10))        
        self.entreeAnneeFin.grid(row = 1, column = 2, padx = 5, pady = (0, 10))
        self.entreeMoisFin.grid(row = 1, column = 3, padx = 5, pady = (0, 10))
        self.entreeJoursFin.grid(row = 1, column = 4, padx = 5, pady = (0, 10))
        self.entreeHeureFin.grid(row = 1, column = 5, padx = 7, pady = (0, 10))
        self.entreeMinuteFin.grid(row = 1, column = 6, padx = 5, pady = (0, 10))
        self.entreeHeuresEstimees.grid(row = 1, column = 2, padx = 5, pady = (0, 10))
        self.entreeMinutesEstimees.grid(row = 1, column = 3, padx = 5, pady = (0, 10))
        
        self.boutonModificationCarte = Button(self.fenetreModificationCarte, text="Modifier Carte", command= lambda:self.changerCarte(noColonne, noCarte,contenuText))
        self.boutonModificationCarte.grid(row=8,column=1, padx=50, pady=(0,30))
        
    def fermerfenetre(self):
        self.root.destroy()
    