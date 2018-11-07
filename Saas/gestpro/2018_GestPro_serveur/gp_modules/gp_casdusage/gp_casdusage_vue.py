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
    def __init__(self,parent,largeur=1200,hauteur=1000):
                
        self.root=tix.Tk()
        self.root.title(os.path.basename(sys.argv[0]))
        self.root.attributes("-fullscreen", False)
        self.root.protocol("WM_DELETE_WINDOW", self.fermerfenetre)
        self.parent=parent
        self.modele=None
        self.defaultcolor =self.root["bg"];
        self.largeurDefault=self.largeur=largeur
        self.hauteurDefault=self.hauteur=hauteur
        self.largeurEcran=self.root.winfo_screenwidth()
        self.hauteurEcran=self.root.winfo_screenmmheight()
        self.cadreExiste=False

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
        self.cadreUsage=Frame(self.root,bg=self.defaultcolor,height=int((self.root.winfo_screenheight()/6)*5),width=int((self.root.winfo_screenwidth()/6)*5))
        
        self.titreCas = Text(self.cadreUsage,height=1,width=15,font="-size 24",bg=self.defaultcolor)
        self.titreCas.insert(END, "Cas d'usage")
        self.titreCas.config(state=DISABLED)
        self.titreCas.grid(row=0,column=1,padx=20)
        
        self.listeCas = Listbox(self.cadreUsage, width=int(self.largeur/20),height=int((self.hauteur/130)*5))
        self.listeCas.grid(row=1,column=1,pady=20,padx=20)
        
        self.boutonAjouterCas = Button(self.cadreUsage,text="Ajouter un Cas",bg="lightblue",command=self.ajouterCas)
        self.boutonAjouterCas.grid(row=2,column=1,pady=20,padx=20)
        
        #Scenarii
        self.cadreScenarii=Frame(self.cadreUsage,bg=self.defaultcolor,height=int((self.root.winfo_screenheight()/6)*5),width=int((self.root.winfo_screenwidth()/6)*5))
        
        self.titreScenarii = Text(self.cadreScenarii,height=1,width=15,font="-size 24",bg=self.defaultcolor)
        self.titreScenarii.insert(END, "Scenarii d'Utilisation")
        self.titreScenarii.config(state=DISABLED)
        self.titreScenarii.grid(row=0,column=1,padx=20,pady=20,columnspan=2)
        
        self.titreScenariiUsager = Text(self.cadreScenarii,height=1,width=15,font="-size 24",bg=self.defaultcolor)
        self.titreScenariiUsager.insert(END, "Usager")
        self.titreScenariiUsager.config(state=DISABLED)
        self.titreScenariiUsager.grid(row=1,column=1,padx=20,pady=20)
        
        self.titreScenariiMachine = Text(self.cadreScenarii,height=1,width=15,font="-size 24",bg=self.defaultcolor)
        self.titreScenariiMachine.insert(END, "Machine")
        self.titreScenariiMachine.config(state=DISABLED)
        self.titreScenariiMachine.grid(row=1,column=2,padx=20,pady=20)
        
        self.listeScenariiUsager = Listbox(self.cadreScenarii, width=int(self.largeur/20),height=int((self.hauteur/150)*5))
        self.listeScenariiUsager.grid(row=2,column=1,pady=20,padx=20)
        
        self.listeScenariiMachine = Listbox(self.cadreScenarii, width=int(self.largeur/20),height=int((self.hauteur/150)*5))
        self.listeScenariiMachine.grid(row=2,column=2,pady=20,padx=20)
        
        self.cadreScenarii.grid(row=1,column=2)
        
        self.boutonAjouterScenarii = Button(self.cadreScenarii,text="Ajouter un Scenarii",bg="lightblue",command=self.ajouterScenarii)
        self.boutonAjouterScenarii.grid(row=3,column=1,columnspan=2,pady=20,padx=20)
        
        casdusage= ["Lorem", "Ipsum", "Lorem Ipsum", "Ipsum Lorem"]
        for item in casdusage:
            self.listeCas.insert(END, item)
            
        machine= ["Lorem", "Ipsum", "Lorem Ipsum", "Ipsum Lorem"]
        for item in machine:
            self.listeScenariiMachine.insert(END, item)
        usager= ["Lorem", "Ipsum", "Lorem Ipsum", "Ipsum Lorem"]
        for item in usager:
            self.titreScenariiUsager.insert(END, item)
        
        self.root.geometry('%dx%d+%d+%d' % (self.largeurDefault, self.hauteurDefault, (self.largeurEcran/2)-(self.largeurDefault/2),(self.hauteurEcran/2)))

        self.cadreExiste=True
    def ajouterCas(self):
        pass
    def ajouterScenarii(self):
        pass
    def fermerfenetre(self):
        print("ON FERME la fenetre")
        self.root.destroy()
    