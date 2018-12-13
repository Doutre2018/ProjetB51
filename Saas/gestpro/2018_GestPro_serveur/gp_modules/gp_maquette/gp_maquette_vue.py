# -*- coding: utf-8 -*-
from tkinter import *
from tkinter import tix
from tkinter import ttk
#from PIL import Image,ImageDraw, ImageTk
import os,os.path
import math
from helper import Helper as hlp
from msilib.schema import Font
from IdMaker import Id
from tkinter.colorchooser import *


class Vue():
    def __init__(self,parent,modele,largeur=1600,hauteur=1000):

        #Donnes : Type, PosX,PosY,X,Y,Bordure,Interieur,texte de string, Font, Id
        listederectangle = ["rectangle",150,150,200,300,"black","black","","",Id.prochainid()]
        listedecercle = ["ovale",500,500,200,300,"black","black","","",Id.prochainid()]
        listedetexte = ["texte",500,500,0,0,"white","black","Hello","Arial 12",Id.prochainid()]
        self.textSize=12
        self.couleurCourante="#FFC14C"
        self.bordureCourante="black"

        self.root=tix.Tk()
        self.root.title(os.path.basename(sys.argv[0]))
        self.root.attributes("-fullscreen", False)
        self.root.protocol("WM_DELETE_WINDOW", self.fermerfenetre)
        self.root.config(bg="#E4E9F3")
        self.parent=parent
        self.modele=modele
        self.largeur=self.largeurDefault=largeur
        self.hauteur=self.hauteurDefault=hauteur
        self.largeurEcran=self.root.winfo_screenwidth()
        self.hauteurEcran=self.root.winfo_screenmmheight()
        self.cadreExiste=False
        self.previousX=None
        self.objetSelectionner = None
        
        self.images={}
        self.cadreactif=None
        self.listeObjetMaquette = self.modele.listeObjets
        
        
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
        self.menubar.add_command(label="Choisir Couleur", command=self.getColor)

        
        self.menu = Menu(self.root, tearoff=0)
        self.menu.add_command(label="Nom", command=self.salutations)
        self.menu.add_command(label="Verbe", command=self.salutations)
        self.menu.config(bg="#E4E9F3")

        
        #self.frame = Frame(self.root, width=512, height=512)
        #self.frame.grid()
        #self.frame.bind("<Button-3>", self.popup)
        self.root.config(menu=self.menubar)           
    def creercadreMaquette(self):
        #permet d'intégrer l'application dans l'application de base
        self.root.overrideredirect(True) #Enleve la bordure
        self.root.geometry('%dx%d+%d+%d' % (self.largeurDefault, self.hauteurDefault, (self.largeurEcran/2)-(self.largeurDefault/2),(self.hauteurEcran/2-30)))

        self.canevasMaquette=Canvas(self.root,width=self.largeur,height=self.hauteur-120,bg="#E4E9F3")
        self.canevasMaquette.create_rectangle((10,10,self.largeur-10,100),fill="#234078")
        self.canevasMaquette.create_rectangle((10,110,self.largeur-10,self.hauteur-10),outline="black",fill="white")
        self.boutontrectangle = self.canevasMaquette.create_rectangle((200,20,260,80),outline="black", fill=self.couleurCourante,tags=(Id.prochainid(),"bouton","rectangle"))
        self.boutontovale = self.canevasMaquette.create_oval(((int(self.largeur/3))+200,20,(int(self.largeur/3))+260,80),outline="black", fill=self.couleurCourante,tags=(Id.prochainid(),"bouton","ovale"))
        self.boutontTexte = self.canevasMaquette.create_text(int((self.largeur/3)*2)+200,55,text="T",font="Arial 60",fill="#FFC14C",tags=(Id.prochainid(),"bouton","texte"))
        self.canevasMaquette.bind("<Button>",self.creerNouvelObjet)
        self.canevasMaquette.bind("<B1-Motion>",self.bougerObjet)
        self.canevasMaquette.bind("<Button-2>",self.detruitObjet)
        self.canevasMaquette.bind("<B3-Motion>",self.aggrandirObjet)
        self.canevasMaquette.bind("<Double-Button-1>",self.modifierTexte)

        self.creerObjet()
        
    def creerNouvelObjet(self,evt):
        t=self.canevasMaquette.gettags(CURRENT)
        print(t)
        if t :
            if t[0] != "current" and t[1] == "bouton":
                    nouvelid = Id.prochainid()
                    if t[2]=="rectangle":
                        self.listeObjetMaquette.append( ["rectangle",(self.largeur/2)-50,(self.hauteur/2)-50,(self.largeur/2+50),((self.hauteur/2)+50),self.bordureCourante,self.couleurCourante,"","",nouvelid])
                    if t[2]=="ovale":
                        self.listeObjetMaquette.append( ["ovale",(self.largeur/2)-50,(self.hauteur/2)-50,(self.largeur/2+50),((self.hauteur/2)+50),self.bordureCourante,self.couleurCourante,"","",nouvelid])

                    if t[2]=="texte":
                        self.listeObjetMaquette.append(["texte",(self.largeur/2),(self.hauteur/2),0,0,self.bordureCourante,self.couleurCourante,"Nouveau Texte","Arial 12",nouvelid])
                    self.creerObjet()
                    
    def bougerObjet(self,evt):
        t=self.canevasMaquette.gettags(CURRENT)
        if t :
            if  t[0] != "current" and t[1] == "objet" :
                    print(t[0] +" " + t[1] + " " + t[2] )

                    self.objetSelectionner=t[0]

                    if t[2]=="texte":
                        self.canevasMaquette.coords(t[0],evt.x, evt.y)
                        diffx = 0
                        diffy = 0
                    else:
                        x0, y0, x1, y1 = self.canevasMaquette.coords(t[0])
                        diffx = x1-x0
                        diffy = y1-y0

                        self.canevasMaquette.coords(t[0],evt.x-(diffx/2), evt.y-(diffy/2),evt.x+(diffx/2),evt.y+(diffy/2))
                    for objet in self.listeObjetMaquette :
                        if (objet[9]==t[0]) :
                            objet[1]=evt.x-(diffx/2)
                            objet[2]=evt.y-(diffy/2)
                            objet[3]=evt.x+(diffx/2)
                            objet[4]=evt.y+(diffy/2)
                            
                    self.objetSelectionnerX=evt.x
                    self.objetSelectionnerY=evt.y

    def aggrandirObjet(self,evt):
        t=self.canevasMaquette.gettags(CURRENT)
        
        if t :
            if  t[0] != "current" and t[1] == "objet" :
                    print(t[0] +" " + t[1] + " " + t[2] )

                    if t[2] == "texte" :
                        size=""
                        font = self.canevasMaquette.itemcget(t[0],'font')
                        i=0
                        for iFont in font:
                            if(i>=6):
                                size += iFont
                                print(size)
                            i+=1
                            
                        self.textSize= int(size)
                        if(self.previousX==None):
                            self.previousX=evt.x
                        if(self.previousX>evt.x):
                            self.textSize-=1
                        if(self.previousX<evt.x):
                            self.textSize+=1
                        size = str(self.textSize)
                        font = "Arial "
                        for i in size:
                            font += i
                        self.canevasMaquette.itemconfig(t[0], font=font)
                        for objet in self.listeObjetMaquette :
                            if (objet[9]==t[0]) :
                                objet[8]=font
                        self.previousX=evt.x

                    else:
                        x0, y0, x1, y1 = self.canevasMaquette.coords(t[0])
                        self.canevasMaquette.coords(t[0], x0,y0,evt.x,evt.y)
                        for objet in self.listeObjetMaquette :
                            if (objet[9]==t[0]) :
                                objet[1]=x0
                                objet[2]=y0
                                objet[3]=evt.x
                                objet[4]=evt.y
                                
    def detruitObjet(self,evt):
        t=self.canevasMaquette.gettags(CURRENT)
        if t :
            if  t[0] != "current" and t[1] == "objet" :
                    print(t[0] +" " + t[1] + " " + t[2] )

                    for objet in self.listeObjetMaquette :
                        if (objet[9]==t[0]) :
                            self.listeObjetMaquette.remove(objet)
                    self.canevasMaquette.delete(t[0])
            
    def changerTexte(self):
        self.canevasMaquette.itemconfig(self.idTexte, text=self.entreeModificationMot.get())
        for objet in self.listeObjetMaquette :
            if (objet[9]==self.idTexte) :
                objet[7]=self.entreeModificationMot.get()
        self.fenetreModificationMot.destroy()


    def modifierTexte(self,evt):
        t=self.canevasMaquette.gettags(CURRENT)
        if t :
            if  t[0] != "current" and t[1] == "objet" and t[2]=="texte":
                self.idTexte = t[0]
                self.fenetreModificationMot = Toplevel(self.root, bg="#F8C471"  )
                self.fenetreModificationMot.wm_title("Creer un Cas d'utilisation")
                
                self.texteModificationMot = Label(self.fenetreModificationMot, text="Mot a entrer :", bg="#F8C471")
                self.texteModificationMot.grid(row=1,column=1, padx=50, pady=(30,10))
                
                self.entreeModificationMot = Entry(self.fenetreModificationMot)
                self.entreeModificationMot.grid(row=2,column=1, padx=50, pady=(0,10))
                
                self.boutonModificationMot = Button(self.fenetreModificationMot, text="Modifier Mot", bg="#E67E22",command=self.changerTexte)
                self.boutonModificationMot.grid(row=3,column=1, padx=50, pady=(0,30))

    def creerObjet(self):
        self.canevasMaquette.delete("objet")
        for objet in self.listeObjetMaquette:
            print(objet)
            if(objet[0]=="rectangle"):
                self.canevasMaquette.create_rectangle((objet[1],objet[2],objet[3],objet[4]),outline=objet[5],fill=objet[6],tags=((objet[9]),"objet","rectangle"))
            if(objet[0]=="ovale"):
                self.canevasMaquette.create_oval((objet[1],objet[2],objet[3],objet[4]),outline=objet[5],fill=objet[6],tags=((objet[9]),"objet","ovale"))
            if(objet[0]=="texte"):
                self.canevasMaquette.create_text(objet[1],objet[2],text=objet[7],fill=objet[6],tags=((objet[9]),"objet","texte"),font=(objet[8]))
    def getColor(self):
        self.couleurCourante = askcolor()[1]
        print(self.couleurCourante)
    def sauvegarde(self):
        self.parent.sauvegarde(self.listeObjetMaquette)
       
    def salutations(self):
        print("hello")
    def fermerfenetre(self):
        print("ON FERME la fenetre")
        self.root.destroy()
    