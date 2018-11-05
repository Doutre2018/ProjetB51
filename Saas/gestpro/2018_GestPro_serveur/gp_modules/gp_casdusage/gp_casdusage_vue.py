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
    def __init__(self,parent,largeur=800,hauteur=600):
                
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
        
        self.cadreUsage=Frame(self.root,bg="light grey",height=int((self.root.winfo_screenheight()/6)*5),width=int((self.root.winfo_screenwidth()/6)*5))
        
        self.titreCas = Text(self.cadreUsage,height=1,width=15,font="-size 24",bg="light grey")
        self.titreCas.insert(END, "Cas d'usage")
        self.titreCas.config(state=DISABLED)
        self.titreCas.grid(row=1,column=1,padx=20)
        
        self.listeCas = Listbox(self.cadreUsage, width=int(self.largeur/35),height=int((self.hauteur/60)*5))
        self.listeCas.grid(row=2,column=1,pady=20,padx=20)
        
        self.boutonAjouterCas = Button(self.cadreUsage,text="Ajouter un Cas",bg="lightblue")
        self.boutonAjouterCas.grid(row=3,column=1,pady=20,padx=20)
        
        casdusage= ["Lorem", "Ipsum", "Lorem Ipsum", "Ipsum Lorem"]
        for item in casdusage:
            self.listeCas.insert(END, item)
        
        self.cadreExiste=True
    def fermerfenetre(self):
        print("ON FERME la fenetre")
        self.root.destroy()
    