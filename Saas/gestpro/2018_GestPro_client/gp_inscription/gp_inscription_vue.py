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
        self.changecadre(self.cadrelogin)
        
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
        self.creercadrelogin()
        #self.cadrejeu=Frame(self.root,bg="blue")
        #self.modecourant=None
                
    def creercadrelogin(self):
        self.cadrelogin=Frame(self.root)
        self.canevalogin=Canvas(self.cadrelogin,width=640,height=480,bg="gray")
        self.canevalogin.pack()
        #self.orglogin=Entry(bg="white")
        #self.orglogin.insert(0, "CVM")
        self.nomlogin=Entry(bg="white")
        self.nomlogin.insert(0, "")
        btnconnecter=Button(text="Créer",bg="white",command=self.salutations)
        #self.canevalogin.create_window(200,200,window=self.orglogin,width=100,height=30)
        self.canevalogin.create_window(200,300,window=self.nomlogin,width=100,height=30)
        self.canevalogin.create_window(200,400,window=btnconnecter,width=100,height=30)
        
    def salutations(self):
        print("HOURRA SA MARCHE")
        
    def fermerfenetre(self):
        print("ONFERME la fenetre")
        self.root.destroy()
    