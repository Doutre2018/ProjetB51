# -*- coding: utf-8 -*-
from tkinter import *
from tkinter import tix
from tkinter import ttk
#from PIL import Image,ImageDraw, ImageTk
import os,os.path
import math
from helper import Helper as hlp
from msilib.schema import Font

class Vue():
    def __init__(self,parent,largeur=800,hauteur=600):

        self.root=tix.Tk()
        self.root.title(os.path.basename(sys.argv[0]))
        self.root.attributes("-fullscreen", False)
        self.root.protocol("WM_DELETE_WINDOW", self.fermerfenetre)
        self.parent=parent
        self.modele=parent.modele
        
        self.largeurDefault=largeur
        self.hauteurDefault=hauteur
        self.largeurEcran=self.root.winfo_screenwidth()
        self.hauteurEcran=self.root.winfo_screenmmheight()
        
        self.cadrecrcExiste=False

        self.images={}
        self.cadreactif=None
        self.creercadres()
        self.changecadre(self.cadrecrc)
        self.compteurBouton=3;
        self.dicBouton={}
        
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
        self.creercadrecrc()
        #self.cadrejeu=Frame(self.root,bg="blue")
        #self.modecourant=None

            
                         
              
    def creercadrecrc(self):
        #permet d'intégrer l'application dans l'application de base
        self.root.overrideredirect(True) #Enleve la bordure
        self.root.geometry('%dx%d+%d+%d' % (self.largeurDefault, self.hauteurDefault, (self.largeurEcran/2)-(self.largeurDefault/2),(self.hauteurEcran/2)))

        self.cadrecrc=Frame(self.root)

        self.lTitreCRC= Label(self.cadrecrc, text= "CRC",font= "arial, 20")
        self.lTitreCRC.grid(padx=100 ,row=0, column=0,  columnspan=2)
        self.AjouterCRC = Button(self.cadrecrc ,text= "+", font= "arial, 20",command=self.ajoutCRC, height=1)
        self.AjouterCRC.grid(row=1, column=2)
        self.ListeCRC= Listbox(self.cadrecrc,selectmode=SINGLE)
        
        #valeur=0
        #for i in self.modele.listeCartes:
           # self.listeCRC.insert(valeur+1,i)
        
        
        #self.ListeCRC.insert(0, "Modele")
        for nom in self.modele.listeCartes:
            for i in nom:
                self.ListeCRC.insert(0,i)

        self.ListeCRC.grid(row=1, column=1)
        self.ListeCRC.bind("<ButtonRelease-1>",self.modifierCRC)
        self.ListeCRC.select_set(0)
        self.SupprimerCRC = Button(self.cadrecrc ,text= "-", font= "arial, 20",command=self.delCRC, height=1, width=2)
        self.SupprimerCRC.grid(row=1, column=3, padx=(10,0))

        self.cadrecrcExiste=True

    def fermerfenetre(self):
        print("ON FERME la fenetre")
        self.root.destroy()
        
    def ajoutCRC(self):
        self.carteCRC =Toplevel(self.root)
        self.frameCarteCRC = Frame(self.carteCRC)
        self.frameCarteCRC.grid()
        
        self.labelNomClasse= Label(self.frameCarteCRC, text="Classe: ")
        self.labelNomClasse.grid()
        self.entryNomClasse= Entry(self.frameCarteCRC)
        self.entryNomClasse.grid()
        
        self.frameInterieur= Frame(self.frameCarteCRC,)
        self.frameInterieur.grid()
        
        #Partie du frame pour heritage et responsable
        self.frameHeriatageResponsable= Frame(self.frameInterieur)
        self.frameHeriatageResponsable.grid(row=0,column=1)
        self.labelHeritage= Label(self.frameHeriatageResponsable, text="Héritage: ")
        self.labelHeritage.grid(row=0,column=1,pady=(10,0))
        self.entryHeritage=Entry(self.frameHeriatageResponsable)
        self.entryHeritage.grid(row=0, column=2,pady=(10,0))
        self.labelResponsable= Label(self.frameHeriatageResponsable, text="Responsable: ")
        self.labelResponsable.grid(row=1, column=1)
        self.entryResponsable= Entry(self.frameHeriatageResponsable)
        self.entryResponsable.grid(row=1, column=2)
        
        #Partie du frame pour les fonction, Attribut , objet
        self.frameFonction= Frame(self.frameInterieur)
        self.frameFonction.grid(row=1,column=1)
        self.labelFonction= Label(self.frameFonction, text="Fonction")
        self.labelFonction.grid(row=0, column=1)
        self.labelAttribut= Label(self.frameFonction, text="Attribut")
        self.labelAttribut.grid(row=0, column=2)
        self.labelObjet= Label(self.frameFonction, text="Objet")
        self.labelObjet.grid(row=0, column=3)
        self.textFonction = Text(self.frameFonction, height = 10, width=15)
        self.textFonction.grid(row=1, column=1)
        self.textAttribut = Text(self.frameFonction, height = 10, width=15)
        self.textAttribut.grid(row=1, column=2)
        self.textObjet = Text(self.frameFonction, height = 10, width=15)
        self.textObjet.grid(row=1, column=3)
        
        #partie du frame pour Collaboration
        self.frameCollaboration= Frame(self.frameInterieur)
        self.frameCollaboration.grid(row=0 , column= 2, rowspan=2)
        self.labelCollaboration= Label(self.frameCollaboration, text="Collaboration")
        self.labelCollaboration.grid()
        self.textCollaboration=Text(self.frameCollaboration,height = 15, width=15)
        self.textCollaboration.grid()
        
        
        #Bouton Ajouter
        self.boutonAjouter= Button(self.frameCarteCRC, text="Ajouter", command=self.nouveauCRC)
        self.boutonAjouter.grid()

    def nouveauCRC(self):
        texteboutton=self.entryNomClasse.get()
        texteResponsable=self.entryResponsable.get()
        texteHeritage=self.entryHeritage.get()
        #AJOUT DE LA CARTE À LA BD
        #id du projet
        listeValeurCarte=[None]*5
        listeValeurCarte[0]=0
        
        #nom de la classe
        listeValeurCarte[1]=texteboutton
        #responsable
        listeValeurCarte[2]=texteHeritage
        #ordre
        listeValeurCarte[3]=0
        
        listeValeurCarte[4]=texteResponsable
        #insertion des infos de base de la carte dans la BD
        self.modele.insertCarte(listeValeurCarte)
        #id de la carte qui vient d'être ajoutée
        temp = self.modele.selectIdCarte(texteboutton)
        for n in temp:
            for i in n:
                idCarteAjoutee=str(i)
        
        texteAtt = self.textAttribut.get(1.0, "end-1c")
        self.modele.insertAttributsDeCarte(texteAtt, idCarteAjoutee)
        
        #FONCTIONS
        texteFonction = self.textFonction.get(1.0, "end-1c")
        listeValeurFonct=[None]*2
        listeValeurFonct[0]="'"+idCarteAjoutee+"'"
        listeValeurFonct[1]="'"+texteFonction+"'"
        self.modele.insertFonctionDeCarte(listeValeurFonct)
        
        #COLLABO
        texteCollabo = self.textCollaboration.get(1.0, "end-1c")
        self.modele.insertCollaboDeCarte(idCarteAjoutee,texteCollabo)
        
        self.ListeCRC.insert(self.compteurBouton, texteboutton)
        
        self.carteCRC.destroy()
        
        self.compteurBouton=self.compteurBouton+1
        
    def modifierCRC(self,evt):
        a=()
        a=self.ListeCRC.curselection()
        b=self.ListeCRC.get(a)
        
        # ------------- DM -------------
        id = self.modele.selectIdCarte(b)
        attribut = self.modele.selectAttributDeCarte(id)
        # ------------------------------
        
        self.carteCRC =Toplevel(self.root)
        self.frameCarteCRC = Frame(self.carteCRC)
        self.frameCarteCRC.grid()
        
        self.labelNomClasse= Label(self.frameCarteCRC, text="Classe: ")
        self.labelNomClasse.grid()
        self.entryNomClasse= Entry(self.frameCarteCRC)
        self.entryNomClasse.grid()
        
        self.frameInterieur= Frame(self.frameCarteCRC,)
        self.frameInterieur.grid()
        
        #Partie du frame pour heritage et responsable
        self.frameHeriatageResponsable= Frame(self.frameInterieur)
        self.frameHeriatageResponsable.grid(row=0,column=1)
        self.labelHeritage= Label(self.frameHeriatageResponsable, text="Héritage: ")
        self.labelHeritage.grid(row=0,column=1,pady=(10,0))
        self.entryHeritage=Entry(self.frameHeriatageResponsable)
        self.entryHeritage.grid(row=0, column=2,pady=(10,0))
        self.labelResponsable= Label(self.frameHeriatageResponsable, text="Responsable: ")
        self.labelResponsable.grid(row=1, column=1)
        self.entryResponsable= Entry(self.frameHeriatageResponsable)
        self.entryResponsable.grid(row=1, column=2)
        
        # ------------- DM -------------
        self.entryNomClasse.insert(0, b)
        # ------------------------------
        
        #Partie du frame pour les fonction, Attribut , objet
        self.frameFonction= Frame(self.frameInterieur)
        self.frameFonction.grid(row=1,column=1)
        self.labelFonction= Label(self.frameFonction, text="Fonction")
        self.labelFonction.grid(row=0, column=1)
        self.labelAttribut= Label(self.frameFonction, text="Attribut")
        self.labelAttribut.grid(row=0, column=2)
        self.labelObjet= Label(self.frameFonction, text="Objet")
        self.labelObjet.grid(row=0, column=3)
        self.textFonction = Text(self.frameFonction, height = 10, width=15)
        self.textFonction.grid(row=1, column=1)
        self.textAttribut = Text(self.frameFonction, height = 10, width=15)
        self.textAttribut.grid(row=1, column=2)
        self.textObjet = Text(self.frameFonction, height = 10, width=15)
        self.textObjet.grid(row=1, column=3)
        
        # ------------- DM -------------
        self.textAttribut.insert(0, attribut)
        # ------------------------------
        
        #partie du frame pour Collaboration
        self.frameCollaboration= Frame(self.frameInterieur)
        self.frameCollaboration.grid(row=0 , column= 2, rowspan=2)
        self.labelCollaboration= Label(self.frameCollaboration, text="Collaboration")
        self.labelCollaboration.grid()
        self.textCollaboration=Text(self.frameCollaboration,height = 15, width=15)
        self.textCollaboration.grid()
        
        
        #Bouton Ajouter
        self.boutonModifier= Button(self.frameCarteCRC, text="Modifier", command=self.modifierCarteCRC)
        self.boutonModifier.grid()
        
    # ---------------- DM ----------------
    def modifierCarteCRC(self):
        pass
    # ------------------------------------
        

    def delCRC(self):
        a=()
        a=self.ListeCRC.curselection()
        nomClasse = str(self.ListeCRC.get(a))
        for i in self.modele.selectIdCarte(nomClasse):
            for n in i:
                idCarteCourante=str(n)
        #Supprime la rangée de la BD pour toutess les composantes
        self.modele.supprimerAttributsDeCarte(idCarteCourante)
        self.modele.supprimerCollaboDeCarte(idCarteCourante)
        self.modele.supprimerFonctionDeCarte(idCarteCourante)
        self.modele.supprimerCarte(nomClasse)
        
        self.ListeCRC.delete(a)
    