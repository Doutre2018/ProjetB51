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
        image= Image.open("./terlow.png")
        image= image.resize((self.largeur, self.hauteur), Image.ANTIALIAS)

        self.img=ImageTk.PhotoImage(image)
        self.cadreterlow.create_image(0,0,image=self.img,anchor=NW)
    def creermenu(self):
        self.menubar = Menu(self.root)

        self.filemenu = Menu(self.menubar, tearoff=0)
        
        self.filemenu = Menu(self.menubar, tearoff=0)
        self.filemenu.add_command(label="Nouvelle colonne", command=self.salutations)
        self.filemenu.add_command(label="Ouvrir", command=self.salutations)
        self.filemenu.add_command(label="Enregistrer", command=self.salutations)
        self.filemenu.add_command(label="Enregistrer sous ...", command=self.salutations)
        self.filemenu.add_separator()
        self.filemenu.add_command(label="Fermer", command=self.root.quit)
        self.menubar.add_cascade(label="Fichier", menu=self.filemenu)
        
        self.editmenu = Menu(self.menubar, tearoff=0)
        self.editmenu.add_command(label="Undo", command=self.salutations)
        self.editmenu.add_command(label="Redo", command=self.salutations)
        self.editmenu.add_separator()
        self.editmenu.add_command(label="Copier", command=self.salutations)
        self.editmenu.add_command(label="Couper", command=self.salutations)
        self.editmenu.add_command(label="Coller", command=self.salutations)
        self.menubar.add_cascade(label="Edition", menu=self.editmenu)
        
        self.aidemenu = Menu(self.menubar, tearoff=0)
        self.aidemenu.add_command(label="Read-Me 1", command=self.salutations)
        self.aidemenu.add_command(label="Read-Me 2", command=self.salutations)
        self.aidemenu.add_command(label="Read-Me 3", command=self.salutations)
        self.aidemenu.add_command(label="Read-Me 4", command=self.salutations)
        self.aidemenu.add_command(label="Read-Me 5", command=self.salutations)
        self.menubar.add_cascade(label="Aide", menu=self.aidemenu)
        
        self.affichagemenu = Menu(self.menubar, tearoff=0)
        self.affichagemenu.add_command(label="FullScreen", command=self.fullScreenMode)
        self.menubar.add_cascade(label="Affichage", menu=self.affichagemenu)
        
        self.menubar.add_command(label="Fermer", command=self.root.quit)
        self.menu = Menu(self.root, tearoff=0)
        self.menu.add_command(label="Nom", command=self.salutations)
        self.menu.add_command(label="Verbe", command=self.salutations)
        
        #self.frame = Frame(self.root, width=512, height=512)
        #self.frame.pack()
        #self.frame.bind("<Button-3>", self.popup)
        self.root.config(menu=self.menubar) 

               
              
    def creercadreterlow(self):
        #permet d'intégrer l'application dans l'application de base
        self.root.overrideredirect(True) #Enleve la bordure
        self.root.geometry('%dx%d+%d+%d' % (self.largeurDefault, self.hauteurDefault, (self.largeurEcran/2)-(self.largeurDefault/2),(self.hauteurEcran/2)))

        self.cadreterlow=Frame(self.root,width=self.largeur,height=self.hauteur)
        self.cadreterlow.grid()
        #self.afficherImage()
        
        self.boutonAjoutListe = Button(self.cadreterlow, text="Ajouter Colonne",command=self.ajouterListe)
        self.boutonAjoutListe.grid()
        self.cadreterlowExiste=True
    def ajouterListe(self):
        self.tableauDeColonne.append(Frame(self.cadreterlow,width=100,height=600,bg="white",bd=4,highlightcolor="red",highlightthickness=1))
        liste = self.tableauDeColonne[self.nbListe]
        
        titre = Entry(liste, width=32)
        titre.insert(END, "Titre")
        noListe=self.nbListe
        boutonAjoutCarte = Button(liste, text="Ajouter Carte",command= lambda: self.ajouterCarte(noListe))
        
        liste.grid(column=self.nbListe,row=1,padx=10)
        titre.grid(row=0)
        boutonAjoutCarte.grid(row=1)
        self.nbListe+=1

        
        
    def ajouterCarte(self, noListe):
        noCarte=0
        colonne = self.tableauDeColonne[noListe]
        contenu = Entry(colonne,width=32)
        contenu.bind("<Button-1>", self.modifierCarte(noCarte,colonne))
        contenu.grid()
        noCarte+=1

        
    def changerCarte(self,noCarte):
        listeInfoCarte = [self.entreeModificationCarte.get()]

        self.tableauDeCarte[noCarte]=listeInfoCarte;
        self.fenetreModificationCarte.destroy()


    def modifierCarte(self,noCarte,colonne):
        self.tableauDeCarte.append([])

        self.fenetreModificationCarte = Toplevel(self.root )
        self.fenetreModificationCarte.wm_title("Modification de Carte")
            
        self.texteModificationCarte = Label(self.fenetreModificationCarte, text="Nom de la carte :",)
        self.texteModificationCarte.grid(row=1,column=1, padx=50, pady=(30,10))
              
        self.entreeModificationCarte = Entry(self.fenetreModificationCarte)
        self.entreeModificationCarte.grid(row=2,column=1, padx=50, pady=(0,10))
                
        self.boutonModificationCarte = Button(self.fenetreModificationCarte, text="Modifier Carte",command= lambda:self.changerCarte(noCarte))
        self.boutonModificationCarte.grid(row=3,column=1, padx=50, pady=(0,30))

        
        
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
    