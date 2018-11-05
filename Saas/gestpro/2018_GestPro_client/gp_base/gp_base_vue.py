# -*- coding: utf-8 -*-
from tkinter import *
from tkinter import tix
from tkinter import ttk
from PIL import Image,ImageDraw, ImageTk
import os,os.path
import math
from helper import Helper as hlp

class Vue():
    def __init__(self,parent,largeur=800,hauteur=600):
        self.root=tix.Tk()
        self.root.title(os.path.basename(sys.argv[0]))
        self.root.protocol("WM_DELETE_WINDOW", self.fermerfenetre)
        self.parent=parent
        self.modele=None
        self.largeur=largeur
        self.hauteur=hauteur
        self.images={}
        self.cadreactif=None
        self.creercadres()
        self.changecadre(self.cadrebase)
        
    def changemode(self,cadre):
        if self.modecourant:
            self.modecourant.pack_forget()
        self.modecourant=cadre
        self.modecourant.pack(expand=1,fill=BOTH)            

    def changecadre(self,cadre,etend=0):
        if self.cadreactif:
            self.cadreactif.pack_forget()
        self.cadreactif=cadre
        if etend:
            self.cadreactif.pack(expand=1,fill=BOTH)
        else:
            self.cadreactif.pack()
    
        
    def creercadres(self):
        self.creercadrebase()
        #self.cadrejeu=Frame(self.root,bg="blue")
        #self.modecourant=None
                
    def creercadrebase(self):
        
        self.cadrebase=Frame(self.root)
        self.canevabase=Canvas(self.cadrebase,width=640,height=480,bg="orange")
        self.canevabase.grid()
        
        self.boutonMandat=Button(text="Mandat",bg="#3E49BB",command=none)
        self.boutonScrum=Button(text="Scrum",bg="#3E49BB",command=none)
        self.boutonAnalyse=Button(text="Analyse \nTextuelle",bg="#3E49BB",command=none)
        self.boutonCasUsage=Button(text="Cas \nd'usage",bg="#3E49BB",command=none)
        self.boutonMaquette=Button(text="Maquette",bg="#3E49BB",command=none)
        self.boutonCrc=Button(text="CRC",bg="#3E49BB",command=none)
        self.boutonBudget=Button(text="Budget",bg="#3E49BB",command=none)
        self.boutonTchat=Button(text="Tchat",bg="#3E49BB",command=none)
        self.boutonDonnee=Button(text="Modelisation \nde donnee",bg="#3E49BB",command=none)
        self.boutonTerlow=Button(text="Terlow",bg="#3E49BB",command=none)
        
        self.boutonMandat.grid(row=0,column=1)
        self.boutonScrum.grid(row=0,column=2)
        self.boutonAnalyse.grid(row=0,column=3)
        self.boutonCasUsage.grid(row=0,column=4)
        self.boutonMaquette.grid(row=0,column=5)
        self.boutonCrc.grid(row=0,column=6)
        self.boutonBudget.grid(row=0,column=7)
        self.boutonTchat.grid(row=0,column=8)
        self.boutonDonnee.grid(row=0,column=9)
        self.boutonTerlow.grid(row=0,column=10)
        
        self.canevabase.create_window(200,200,window=self.nombase,width=100,height=30)
        self.canevabase.create_window(200,400,window=btnconnecter,width=200,height=30)
    
    def salutations(self):
        pass
    def fermerfenetre(self):
        print("ON FERME la fenetre")
        self.root.destroy()
    