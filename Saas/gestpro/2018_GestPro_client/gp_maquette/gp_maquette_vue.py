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
    def __init__(self,parent,largeur=1200,hauteur=800):
        self.listeObjetMaquette = []
        
        listederectangle = ["rectangle",150,150,200,300,"black","red","",1]
        listedecercle = ["ovale",500,500,200,300,"black","red","",2]
        listedetexte = ["texte",500,500,0,0,"black","white","Hello",3]

        self.listeObjetMaquette.append(listederectangle)
        self.listeObjetMaquette.append(listedecercle)
        self.listeObjetMaquette.append(listedetexte)
        self.root=tix.Tk()
        self.root.title(os.path.basename(sys.argv[0]))
        self.root.attributes("-fullscreen", False)
        self.root.protocol("WM_DELETE_WINDOW", self.fermerfenetre)
        self.parent=parent
        self.modele=None
        self.largeur=self.largeurDefault=largeur
        self.hauteur=self.hauteurDefault=hauteur
        self.largeurEcran=self.root.winfo_screenwidth()
        self.hauteurEcran=self.root.winfo_screenmmheight()
        self.cadreExiste=False
        self.images={}
        self.cadreactif=None
        
        self.creermenu()

        self.creercadres()
        self.changecadre(self.canevasMaquette)
        
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
        self.creercadreMaquette()            
    def creermenu(self):
        
        self.menubar = Menu(self.root)
        self.menubar.add_command(label="Sauvegarder", command=self.sauvegarde)

        self.editmenu = Menu(self.menubar, tearoff=0)
        self.editmenu.add_command(label="Undo", command=self.salutations)
        self.editmenu.add_command(label="Redo", command=self.salutations)
        self.editmenu.add_separator()
        self.editmenu.add_command(label="Copier", command=self.salutations)
        self.editmenu.add_command(label="Couper", command=self.salutations)
        self.editmenu.add_command(label="Coller", command=self.salutations)
        self.menubar.add_cascade(label="Edition", menu=self.editmenu)
        
        self.menu = Menu(self.root, tearoff=0)
        self.menu.add_command(label="Nom", command=self.salutations)
        self.menu.add_command(label="Verbe", command=self.salutations)
        
        #self.frame = Frame(self.root, width=512, height=512)
        #self.frame.grid()
        #self.frame.bind("<Button-3>", self.popup)
        self.root.config(menu=self.menubar)           
    def creercadreMaquette(self):
        self.canevasMaquette=Canvas(self.root,width=self.largeur,height=self.hauteur)
        self.canevasMaquette.create_rectangle((10,10,self.largeur-10,100),fill="green")
        self.canevasMaquette.create_rectangle((10,110,self.largeur-10,self.hauteur-10),outline="black",fill="white")
    
        for objet in self.listeObjetMaquette:
            if(objet[0]=="rectangle"):
<<<<<<< HEAD
                self.canevasMaquette.create_rectangle((objet[1],objet[2],objet[3],objet[4]),outline=objet[5],fill=objet[6],tags=(objet[8]))
                
            if(objet[0]=="ovale"):
                self.canevasMaquette.create_oval((objet[1],objet[2],objet[3],objet[4]),outline=objet[5],fill=objet[6],tags=(objet[8]))
            if(objet[0]=="texte"):
                texte=Label(self.canevasMaquette,fg=objet[5],bg=objet[6], text=objet[7],tags=(objet[8]))
=======
                self.canevasMaquette.create_rectangle((objet[1],objet[2],objet[3],objet[4]),outline=objet[5],fill=objet[6],tags=str((objet[8])))
                
            if(objet[0]=="ovale"):
                self.canevasMaquette.create_oval((objet[1],objet[2],objet[3],objet[4]),outline=objet[5],fill=objet[6],tags=str((objet[8])))
            if(objet[0]=="texte"):
                texte=Label(self.canevasMaquette,fg=objet[5],bg=objet[6], text=objet[7],tags=str((objet[8])))
>>>>>>> f08a15c066688db539cd4bee089a338cc2d957a1
                texte.pack()
                texte.place(x=objet[1],y=objet[2])
    def sauvegarde(self):
        pass #Envoyer self.listeObjetMaquette dans BD
    def salutations(self):
        print("hello")
    def fermerfenetre(self):
        print("ON FERME la fenetre")
        self.root.destroy()
    