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
    def __init__(self,parent,largeur=1600,hauteur=1000):
        self.listeObjetMaquette = []
        
        listederectangle = ["rectangle",150,150,200,300,"black","red","",1]
        listedecercle = ["ovale",500,500,200,300,"black","red","",2]
        listedetexte = ["texte",500,500,0,0,"black","white","Hello",3]
        
        self.couleurCourante="red"
        self.bordureCourante="black"
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
        
        self.objetSelectionner = None
        
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
        #permet d'intégrer l'application dans l'application de base
        self.root.overrideredirect(True) #Enleve la bordure
        self.root.geometry('%dx%d+%d+%d' % (self.largeurDefault, self.hauteurDefault, (self.largeurEcran/2)-(self.largeurDefault/2),(self.hauteurEcran/2)))

        self.canevasMaquette=Canvas(self.root,width=self.largeur,height=self.hauteur)
        self.canevasMaquette.create_rectangle((10,10,self.largeur-10,100),fill="green")
        self.canevasMaquette.create_rectangle((10,110,self.largeur-10,self.hauteur-10),outline="black",fill="white")
        self.boutontrectangle = self.canevasMaquette.create_rectangle((200,20,260,80),outline="black", fill="black",tags=("1","bouton","rectangle"))
        self.boutontovale = self.canevasMaquette.create_oval(((int(self.largeur/3))+200,20,(int(self.largeur/3))+260,80),outline="black", fill="black",tags=("1","bouton","ovale"))
        self.boutontTexte = self.canevasMaquette.create_text(int((self.largeur/3)*2)+200,55,text="T",font="Arial 50 bold",tags=("1","bouton","texte"))
        self.canevasMaquette.bind("<Button>",self.creerNouvelObjet)
        self.canevasMaquette.bind("<B1-Motion>",self.bougerObjet)
        

        self.creerObjet()
    def creerNouvelObjet(self,evt):
        t=self.canevasMaquette.gettags(CURRENT)
        print(t)
        if t :
            if t[0] != "current" and t[1] == "bouton":
                    if t[2]=="rectangle":
                        self.canevasMaquette.create_rectangle(((self.largeur/2)-50,(self.hauteur/2)-50,(self.largeur/2+50),(self.hauteur/2)+50),fill=self.couleurCourante,outline=self.bordureCourante,tags=(Id.prochainid(),"objet","rectangle"))
                    if t[2]=="ovale":
                        self.canevasMaquette.create_oval(((self.largeur/2)-50,(self.hauteur/2)-50,(self.largeur/2+50),(self.hauteur/2)+50),fill=self.couleurCourante,outline=self.bordureCourante,tags=(Id.prochainid(),"objet","ovale"))
                    if t[2]=="texte":
                        self.canevasMaquette.create_text(((self.largeur/2),(self.hauteur/2)),text="Nouveau Texte",fill=self.couleurCourante,tags=(Id.prochainid(),"objet","texte"))
            elif  t[0] != "current" and t[1] == "objet" :
                    self.objetSelectionner=t[0]
                    self.objetSelectionnerX=evt.x
                    self.objetSelectionnerY=evt.y

            else:
                print("pas d'objet")
                if self.objetSelectionner != None :                                 
                    self.canevasMaquette.move(self.objetSelectionner,evt.x-self.objetSelectionnerX,evt.y-self.objetSelectionnerY)
                    self.objetSelectionner=None
        else :
            print("no objet")
            if self.objetSelectionner != None :                                 
                    self.canevasMaquette.move(self.objetSelectionner,evt.x-self.objetSelectionnerX,evt.y-self.objetSelectionnerY)
                    self.objetSelectionner=None
    def bougerObjet(self):
        t=self.canevasMaquette.gettags(CURRENT)
        if t :
            if  t[0] != "current" and t[1] == "objet" :
                    self.objetSelectionner=t[0]
                    self.objetSelectionnerX=evt.x
                    self.objetSelectionnerY=evt.y
                    self.canevasMaquette.move(self.objetSelectionner,evt.x,evt.y)
                    self.objetSelectionner=None

            else:
                print("pas d'objet")
                if self.objetSelectionner != None :                                 
                    self.canevasMaquette.move(self.objetSelectionner,evt.x-self.objetSelectionnerX,evt.y-self.objetSelectionnerY)
                    self.objetSelectionner=None
        else :
            print("no objet")
            if self.objetSelectionner != None :                                 
                    self.canevasMaquette.move(self.objetSelectionner,evt.x-self.objetSelectionnerX,evt.y-self.objetSelectionnerY)
                    self.objetSelectionner=None
        
    def creerObjet(self):
        for objet in self.listeObjetMaquette:
            if(objet[0]=="rectangle"):
                self.canevasMaquette.create_rectangle((objet[1],objet[2],objet[3],objet[4]),outline=objet[5],fill=objet[6],tags=((objet[8]),"objet","rectangle"))
                
            if(objet[0]=="ovale"):
                self.canevasMaquette.create_oval((objet[1],objet[2],objet[3],objet[4]),outline=objet[5],fill=objet[6],tags=((objet[8]),"objet","ovale"))
            if(objet[0]=="texte"):
                self.canevasMaquette.create_text(objet[1],objet[2],text=objet[7],fill=objet[5],tags=((objet[8]),"objet","texte"))

    def sauvegarde(self):
        pass #Envoyer self.listeObjetMaquette dans BD
    def salutations(self):
        print("hello")
    def fermerfenetre(self):
        print("ON FERME la fenetre")
        self.root.destroy()
    