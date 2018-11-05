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
    def __init__(self,parent,largeur=1000,hauteur=900):
                
        self.root=tix.Tk()
        self.root.title(os.path.basename(sys.argv[0]))
        self.root.attributes("-fullscreen", False)
        self.root.protocol("WM_DELETE_WINDOW", self.fermerfenetre)
        self.parent=parent
        self.modele=None
        self.largeurDefault=self.largeur=largeur
        self.hauteurDefault=self.hauteur=hauteur
        #self.largeur=self.root.winfo_screenwidth()/7
        #self.hauteur=self.root.winfo_screenmmheight()/4.5
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
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        x = (screen_width/2) - (self.largeur/2)
        y = (screen_height/3) - (self.hauteur/3)
        self.root.geometry('%dx%d+%d+%d' % (self.largeur, self.hauteur, x, y))
    
    
        self.cadreUsage=Frame(self.root,bg="light grey",height=int((self.root.winfo_screenheight()/6)*5),width=int((self.root.winfo_screenwidth()/6)*5))
        
        
        self.titreCas = Text(self.cadreUsage,height=1,width=15,font="-size 24",bg="light grey")
        self.titreCas.insert(END, "Cas d'usage")
        self.titreCas.config(state=DISABLED)
        self.titreCas.grid(row=1,column=1,padx=20)
        
        self.listeCas = Listbox(self.cadreUsage, width=int(self.largeur/40),height=int((self.hauteur/95)*5))
        self.listeCas.grid(row=2,column=1,pady=20,padx=20)
        
        self.boutonAjouterCas = Button(self.cadreUsage,text="Ajouter un Cas",bg="lightblue")
        self.boutonAjouterCas.grid(row=3,column=1,pady=20,padx=20)
        
        casdusage= ["Lorem", "Ipsum", "Lorem Ipsum", "Ipsum Lorem"]
        for item in casdusage:
            self.listeCas.insert(END, item)
        
        self.titrescenarii = Text(self.cadreUsage,height=1,width=15,font="-size 24",bg="light grey")
        self.titrescenarii.insert(END, "Scenarii utilisation")
        self.titrescenarii.config(state=DISABLED)
        self.titrescenarii.grid(row=1,column=2,padx=20)
        
        self.cadrescenarii = Frame(self.cadreUsage,bg="white")
        self.cadrescenarii.grid(column=2,row=1,rowspan=3)
        
        self.titreutilisateur = Text(self.cadrescenarii,height=1,width=15,font="-size 16",bg="white")
        self.titreutilisateur.insert(END, "Utilisateur")
        self.titreutilisateur.config(state=DISABLED)
        self.titreutilisateur.grid(row=1,column=1,padx=20)
        
        self.listeutilisateur = Listbox(self.cadrescenarii, width=int(self.largeur/19),height=int((self.hauteur/95)*5))
        self.listeutilisateur.grid(row=2,column=1,pady=10,padx=10)
        
        utilisateur= ["Lorem", "Ipsum", "Lorem Ipsum", "Ipsum Lorem"]
        for item in utilisateur:
            self.listeutilisateur.insert(END, item) 
        
        self.titremachine = Text(self.cadrescenarii,height=1,width=15,font="-size 16",bg="white")
        self.titremachine.insert(END, "Machine")
        self.titremachine.config(state=DISABLED)
        self.titremachine.grid(row=1,column=2,padx=20)
         
        self.listemachine = Listbox(self.cadrescenarii, width=int(self.largeur/19),height=int((self.hauteur/95)*5))
        self.listemachine.grid(row=2,column=2,pady=20,padx=20)
        
        machine= ["Lorem", "Ipsum", "Lorem Ipsum", "Ipsum Lorem"]
        for item in machine:
            self.listemachine.insert(END, item) 
            
        self.cadreExiste=True
    def fermerfenetre(self):
        print("ON FERME la fenetre")
        self.root.destroy()
    