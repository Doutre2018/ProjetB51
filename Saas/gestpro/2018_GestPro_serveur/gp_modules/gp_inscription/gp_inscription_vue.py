# -*- coding: utf-8 -*-
from tkinter import *
from tkinter import tix
from tkinter import ttk
from PIL import Image,ImageDraw, ImageTk
import os,os.path
import math
from helper import Helper as hlp

import re       # Regex

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
        
        # -------------DM---------------- #
        self.nomUtilisateur = None
        # ------------------------------- #
        
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
        btnconnecter=Button(text="Créer",bg="white",command=self.fetchNom)
        #self.canevalogin.create_window(200,200,window=self.orglogin,width=100,height=30)
        self.canevalogin.create_window(200,300,window=self.nomlogin,width=100,height=30)
        self.canevalogin.create_window(200,400,window=btnconnecter,width=100,height=30)
    
    '''    
    def salutations(self):
        print("HOURRA SA MARCHE")
    '''    
    
    # ---------------DM----------------- #     
    def fetchNom(self):                     # Méthode pour prendre le nom de l'utilisateur du textbox
        temp = self.nomlogin.get()          # Prend le string de la textbox "self.nomlogin"
        
        if self.nomConforme(temp):
            print("conforme")
        
        else:
            print("Nom d'utilisateur invalide")
       
    def nomConforme(self, nom):             # Vérifie que le nom d'utilisateur est conforme (regex)
        if len(nom) > 12:                   # Si le nom a plus de 12 caractères
            return False
        else:
            pattern = "\w+"                 # A-Z, a-z, 0-9 et _ au moins une fois
            if (re.match(pattern, nom)):    # Compare le nom transmis au pattern
                return True
            else:
                return False
            
    def nomUnique(self, nom):               # Vérifie que le nom d'utilisateur n'existe pas déjà dans la BD
        pass
    # --------------------------------- #
        
    def fermerfenetre(self):
        print("ONFERME la fenetre")
        self.root.destroy()
    