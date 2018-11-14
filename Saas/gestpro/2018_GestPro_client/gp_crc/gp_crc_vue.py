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
        self.largeurDefault=largeur/7
        self.hauteurDefault=hauteur/4.5
        self.largeur=self.root.winfo_screenwidth()/7
        self.hauteur=self.root.winfo_screenmmheight()/4.5
        self.cadrebaseExiste=False

        self.images={}
        self.cadreactif=None
        self.fullscreen=True
        self.creercadres()
        self.changecadre(self.cadrebase)
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
        self.creercadrebase()
        #self.cadrejeu=Frame(self.root,bg="blue")
        #self.modecourant=None
        
    def requetemodule(self,mod):
        rep=self.serveur.requetemodule(mod)
        if rep:
            print(rep[0])
            cwd=os.getcwd()
            lieuApp="/gp_"+rep[0]
            lieu=cwd+lieuApp
            print(lieu)
            if not os.path.exists(lieu):
                os.mkdir(lieu) #plante s'il exist deja
            reso=rep[1]
            print(rep[1])
            for i in rep[2]:
                if i[0]=="fichier":
                    nom=reso+i[1]
                    rep=self.serveur.requetefichier(nom)
                    fiche=open(lieu+"/"+i[1],"wb")
                    fiche.write(rep.data)
                    fiche.close()
            chaineappli="."+lieuApp+lieuApp+".py"

            self.pid = Popen([sys.executable, chaineappli,self.monnom,self.monip,self.nodeport],shell=0) 
        else:
            print("RIEN") 
            
    def creermenu(self):
        self.menubar = Menu(self.root)

        self.filemenu = Menu(self.menubar, tearoff=0)
        
        self.filemenu = Menu(self.menubar, tearoff=0)
        self.filemenu.add_command(label="Nouveau Projet", command=self.salutations)
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
    def fullScreenMode(self): 
        if(self.fullscreen):
            self.fullscreen=False
            self.largeur=self.largeurDefault
            self.hauteur=self.hauteurDefault
            self.root.attributes("-fullscreen", False)
            self.creercadres()
            self.changecadre(self.cadrebase)
        else:
             self.fullscreen=True
             self.largeur=self.root.winfo_screenwidth()/7
             self.hauteur=self.root.winfo_screenmmheight()/4.5
             self.root.attributes("-fullscreen", True)
             self.creercadres()
             self.changecadre(self.cadrebase)
    def destroyCadreBase(self):
        self.cadrebase.destroy()
        self.boutonAnalyse.destroy()
        self.affichagemenu.destroy()
        self.boutonBudget.destroy()
        self.boutonCasUsage.destroy()
        self.boutonCrc.destroy()
        self.boutonDonnee.destroy()
        self.boutonMandat.destroy()
        self.boutonMaquette.destroy()
        self.boutonProjet1.destroy()
        self.boutonProjet2.destroy()                        
        self.boutonProjet3.destroy()
        self.boutonScrum.destroy()
        self.boutonTchat.destroy()
        self.boutonTerlow.destroy()                      
              
    def creercadrebase(self):
        self.cadrebase=Frame(self.root)

        self.lTitreCRC= Label(self.cadrebase, text= "CRC",font= "arial, 20")
        self.lTitreCRC.grid(padx=100 ,row=0, column=0,  columnspan=2)
        self.AjouterCRC = Button(self.cadrebase ,text= "+", font= "arial, 20",command=self.ajoutCRC, height=1)
        self.AjouterCRC.grid(row=1, column=2)
        self.ListeCRC= Listbox(self.cadrebase,selectmode=SINGLE)
        self.ListeCRC.insert(0, "Modele")
        self.ListeCRC.insert(1, "Vue")
        self.ListeCRC.insert(2, "Controleur")
        self.ListeCRC.grid(row=1, column=1)
        self.ListeCRC.bind("<ButtonRelease-1>",self.modifierCRC)
        self.ListeCRC.select_set(0)
        self.SupprimerCRC = Button(self.cadrebase ,text= "-", font= "arial, 20",command=self.delCRC, height=1, width=2)
        self.SupprimerCRC.grid(row=1, column=3, padx=(10,0))

        self.cadrebaseExiste=True

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
        
        self.ListeCRC.insert(self.compteurBouton, texteboutton)
        
        self.carteCRC.destroy()
        
        self.compteurBouton=self.compteurBouton+1
        
    def modifierCRC(self,evt):
        a=()
        a=self.ListeCRC.curselection()
        b=self.ListeCRC.get(a)
        
        
        
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
        self.boutonModifier= Button(self.frameCarteCRC, text="Modifier", command=self.ModfiCRC)
        self.boutonModifier.grid()
        

    def delCRC(self):
        a=()
        a=self.ListeCRC.curselection()
        #b=self.ListeCRC.get(a)
        self.ListeCRC.delete(a)
    