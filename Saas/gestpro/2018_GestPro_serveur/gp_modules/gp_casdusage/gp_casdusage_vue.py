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
    def __init__(self,parent,largeur=1200,hauteur=1000):
                
        self.root=tix.Tk()
        self.root.title(os.path.basename(sys.argv[0]))
        self.root.attributes("-fullscreen", False)
        self.root.protocol("WM_DELETE_WINDOW", self.fermerfenetre)
        self.root.config(bg="#E4E9F3")
        self.parent=parent
        self.modele=None
        self.defaultcolor =self.root["bg"];
        self.largeurDefault=self.largeur=largeur
        self.hauteurDefault=self.hauteur=hauteur
        self.largeurEcran=self.root.winfo_screenwidth()
        self.hauteurEcran=self.root.winfo_screenmmheight()
        self.cadreExiste=False

        self.usager= ["Lorem", "", "", "Ipsum Lorem"]
        self.casdusage= ["Lorem", "Ipsum", "Lorem Ipsum", "Ipsum Lorem"]
        self.machine= ["", "Ipsum", "Lorem Ipsum", ""]

        self.images={}
        self.cadreactif=None
        self.fullscreen=True
        self.creercadres()
        self.changecadre(self.cadreUsage)
        
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
        self.creercadreUsage()
        
    def creercadreUsage(self):
        if(self.cadreExiste):
            self.cadreUsage.destroy()
        self.root.overrideredirect(True)

        #Cas d'usage
        self.cadreUsage=Frame(self.root,bg="#E4E9F3",height=int((self.root.winfo_screenheight()/6)*5),width=int((self.root.winfo_screenwidth()/6)*5))
        self.cadreUsage.grid(row=0,column=0,)
        
        self.labelCas=Label(self.cadreUsage, text="Cas d'usage", bg="#E4E9F3", font= "arial, 24")
        self.labelCas.grid(row=0,column=0,pady=(20,10),columnspan=2)

        
        self.listeCas = Listbox(self.cadreUsage, width=50,height=int((self.hauteur/130)*5))
        self.listeCas.grid(row=1,column=0,padx=20,columnspan=2)
        self.listeCas.bind('<<ListboxSelect>>', self.afficherScenarii)
        self.boutonAjouterCas = Button(self.cadreUsage,text="Ajouter",bg="white",command=self.ajouterCas,relief=FLAT,width=10)
        self.boutonAjouterCas.grid(row=2,column=0,pady=(10,0),padx=(75,0))
        
        # --------Bouton POur JF
        self.boutonSupprimerCas = Button(self.cadreUsage,text="Supprimer",bg="white",command=self.ajouterCas,relief=FLAT,width=10)
        self.boutonSupprimerCas.grid(row=2,column=1,pady=(10,0),padx=(0,75))
        
        #Scenarii
        self.cadreScenarii=Frame(self.root,bg="#E4E9F3",height=int((self.root.winfo_screenheight()/6)*5),width=int((self.root.winfo_screenwidth()/6)*5))
        self.cadreScenarii.grid(row=0,column=2)
        
        self.titreScenarii= Label(self.cadreScenarii , text="Scenarii d'Utilisation",font="-size 24",bg="#E4E9F3")
        self.titreScenarii.grid(row=0,column=1,columnspan=2,pady=(20,10))
        
        self.labelUsager = Label(self.cadreScenarii , text="Usager",font="-size 20",bg="#E4E9F3")
        self.labelUsager.grid(row=1,column=1)

        self.labelMachine = Label(self.cadreScenarii , text="Machine",font="-size 20",bg="#E4E9F3")  
        self.labelMachine.grid(row=1,column=2)      
        
        self.listeScenariiUsager = Listbox(self.cadreScenarii, width=int(self.largeur/20),height=int((self.hauteur/150)*5))
        self.listeScenariiUsager.grid(row=2,column=1)
        
        self.listeScenariiMachine = Listbox(self.cadreScenarii, width=int(self.largeur/20),height=int((self.hauteur/150)*5))
        self.listeScenariiMachine.grid(row=2,column=2)
                
        self.boutonAjouterScenarii = Button(self.cadreScenarii,text="Ajouter",bg="white",command=self.ajouterScenarii,relief=FLAT,width=10)
        self.boutonAjouterScenarii.grid(row=3,column=1,columnspan=2, padx=(0,100))
        #-----------BOUTON POUR JF!
        self.boutonSupprimerScenarii = Button(self.cadreScenarii,text="Supprimer",bg="white",command=self.ajouterScenarii,relief=FLAT,width=10)
        self.boutonSupprimerScenarii.grid(row=3,column=1,columnspan=2, padx=(100,0))
        
        self.parent.modele.selectCas()
        self.casdusage = self.parent.modele.Cas
        for item in self.casdusage:
            self.listeCas.insert(END, item)
            
        self.listeCas.select_set(0)

        
        self.root.geometry('%dx%d+%d+%d' % (self.largeurDefault, self.hauteurDefault, (self.largeurEcran/2)-(self.largeurDefault/2),(self.hauteurEcran/2)))

        self.cadreExiste=True
        
    def afficherScenarii(self, evt):
        self.parent.modele.selectScenarii(self.listeCas.get(ACTIVE))
        print(self.listeCas.get(ACTIVE))
        self.usager = self.parent.modele.casUsagers
        self.machine = self.parent.modele.casMachines
        self.listeScenariiUsager.delete(0, 'end')
        for item in self.usager:
            self.listeScenariiUsager.insert(END, item)
            
        self.listeScenariiMachine.delete(0, 'end')    
        for item in self.machine:
            self.listeScenariiMachine.insert(END, item)
    def ajouterCas(self):
        self.fenetreCreationCas = Toplevel(self.root, bg="#234078"  )
        self.fenetreCreationCas.wm_title("Creer un Cas d'utilisation")
        
        largeurEcran = self.root.winfo_screenwidth()
        hauteurEcran = self.root.winfo_screenheight()
        x = (largeurEcran/2)-(220/2)
        y = (hauteurEcran/2)-(220/2)
        self.fenetreCreationCas.geometry("+%d+%d" % (x, y))
        
        self.texteCreationCas = Label(self.fenetreCreationCas, text="Nouveau cas :", bg="#234078",fg="white")
        self.texteCreationCas.grid(row=1,column=1, padx=50, pady=(30,10))
        
        self.entreeCreationCas = Entry(self.fenetreCreationCas)
        self.entreeCreationCas.grid(row=2,column=1, padx=50, pady=(0,10))
        
        self.boutonCreationCas = Button(self.fenetreCreationCas, text="Creer Cas", command=self.creerCas, relief=FLAT, bg="white")
        self.boutonCreationCas.grid(row=3,column=1, padx=50, pady=(0,30))
        

    def ajouterScenarii(self):
        self.fenetreCreationScenarii = Toplevel(self.root, bg="#234078"  )
        self.fenetreCreationScenarii.wm_title("Creer un Scenarii")
        
        largeurEcran = self.root.winfo_screenwidth()
        hauteurEcran = self.root.winfo_screenheight()
        x = (largeurEcran/2)-(500/2)
        y = (hauteurEcran/2)-(220/2)
        self.fenetreCreationScenarii.geometry("+%d+%d" % (x, y))
        
        self.texteCreationUtilisateur = Label(self.fenetreCreationScenarii, text="Utilisateur :", bg="#234078",fg="white")
        self.texteCreationUtilisateur.grid(row=1,column=1, padx=50, pady=(30,10))
        
        self.entreeCreationUtilisateur = Entry(self.fenetreCreationScenarii)
        self.entreeCreationUtilisateur.grid(row=2,column=1, padx=50, pady=(0,10))
        
        self.texteCreationMachine = Label(self.fenetreCreationScenarii, text="Machine :", bg="#234078",fg="white")
        self.texteCreationMachine.grid(row=1,column=2, padx=50, pady=(30,10))
        
        self.entreeCreationMachine = Entry(self.fenetreCreationScenarii)
        self.entreeCreationMachine.grid(row=2,column=2, padx=50, pady=(0,10))
        
        self.boutonCreationScenarii = Button(self.fenetreCreationScenarii, text="Creer ligne de Scenarii",command=self.creerScenarii, relief=FLAT, bg="white")
        self.boutonCreationScenarii.grid(row=3,column=1, padx=50, pady=(0,30),columnspan=2)
    def creerCas(self):
        self.parent.modele.insertCas(self.listeCas.size(),self.entreeCreationCas.get())
        self.casdusage.append(self.entreeCreationCas.get())
        self.listeCas.insert(END, self.entreeCreationCas.get())
        self.fenetreCreationCas.destroy()
    def creerScenarii(self):
        self.parent.modele.insertScenarii(self.listeCas.get(ACTIVE),self.entreeCreationUtilisateur.get(),self.entreeCreationUtilisateur.get())
        self.usager.append(self.entreeCreationUtilisateur.get())
        self.machine.append(self.entreeCreationMachine.get())
        self.fenetreCreationScenarii.destroy()

    def fermerfenetre(self):
        print("ON FERME la fenetre")
        self.root.destroy()
    