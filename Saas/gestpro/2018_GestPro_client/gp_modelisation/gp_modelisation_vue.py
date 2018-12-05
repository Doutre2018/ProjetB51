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
    def __init__(self,parent,largeur=1600,hauteur=900):
       
        self.root=tix.Tk()
        self.root.title(os.path.basename(sys.argv[0]))
        self.root.protocol("WM_DELETE_WINDOW", self.fermerfenetre)
        self.parent=parent
        self.modele=None
        self.largeurDefault=largeur
        self.hauteurDefault=hauteur
        self.largeurEcran=self.root.winfo_screenwidth()
        self.hauteurEcran=self.root.winfo_screenmmheight()
        self.cadremodelisationExiste=False
        self.nbTable=0
        self.nomTableCreer=[]
        self.images={}
        self.cadreactif=None
        self.creercadres()
        self.changecadre(self.cadremodelisation)
        
        
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
        self.creercadremodelisation()
        #self.cadrejeu=Frame(self.root,bg="blue")
        #self.modecourant=None
    
            
        
              
    def creercadremodelisation(self):
        self.cadremodelisation=Frame(self.root)
        self.root.overrideredirect(True) #Enleve la bordure
        self.root.geometry('%dx%d+%d+%d' % (self.largeurDefault, self.hauteurDefault, (self.largeurEcran/2)-(self.largeurDefault/2),(self.hauteurEcran/2)))
        
        self.boutonAjoutTable = Button(self.cadremodelisation, text="Creer Table", width = 20, height = 3, command = self.creerTable)
        self.boutonAjoutTable.grid(row=0,column=0)
        
        self.cadremodelisationExiste=True
    
    def creerTable(self):
        self.nbChamps = 0
        self.creationTable =Toplevel(self.cadremodelisation)
        textNom = Label(self.creationTable,text="Nom de la table")
        textNom.grid(row=0,column=1)
        #self.nomTableCreer.append(StringVar())

        self.nomTableCreer = Entry(self.creationTable)
        self.nomTableCreer.grid(row=0,column=2)
        textNom = Label(self.creationTable,text="Nom du Champ",width=15)
        textNom.grid(row=1,column=1)
        textType = Label(self.creationTable,text="Type du Champ",width=15)
        textType.grid(row=1,column=2)
        textAutre = Label(self.creationTable,text="Autre",width=15)
        textAutre.grid(row=1,column=3)


        self.nomsChampsCreer=[]
        self.typeChampsCreer=[]
        self.autreChampsCreer=[]
        
        boutonAjoutChamps = Button(self.creationTable, width = 15, height = 1, text= "Ajouter Champs", command = self.ajouterChampsNouveau)
        boutonAjoutChamps.grid(row=self.nbChamps+3)
        boutonCreer = Button(self.creationTable, width = 15, height = 1, text = "Ajouter", command  = self.ajouterTable)
        boutonCreer.grid(row=self.nbChamps+4,column=0, pady=10)
    def ajouterChampsNouveau(self):
        
        self.nomsChampsCreer.append(StringVar())
        nomChamp =Entry(self.creationTable, width = 20,textvariable = self.nomsChampsCreer[self.nbChamps] )
        nomChamp.grid(row=self.nbChamps+2,column=1)
        
        self.typeChampsCreer.append(StringVar())
        typeChamp=Entry(self.creationTable, width = 20,textvariable = self.typeChampsCreer[self.nbChamps])
        typeChamp.grid(row=self.nbChamps+2,column=2)
        
        self.autreChampsCreer.append(StringVar())
        autreChampEntry=Entry(self.creationTable, width = 20,textvariable = self.autreChampsCreer[self.nbChamps])
        autreChampEntry.grid(row=self.nbChamps+2,column=3)


        self.nbChamps+=1
    def ajouterTable(self):        
        textNom = Label(self.cadremodelisation,text="Nom de la table")
        textNom.grid(column=self.nbTable*3,row=1)
        
        nomTable = Label(self.cadremodelisation,text=str(self.nomTableCreer.get()),borderwidth=2, relief="groove")
        nomTable.grid(column=self.nbTable*3+1,row=1)
        
        
        textNom = Label(self.cadremodelisation,text="Nom du Champ",width=15)
        textNom.grid(row=2,column=(self.nbTable*3))
        textType = Label(self.cadremodelisation,text="Type du Champ",width=15)
        textType.grid(row=2,column=(self.nbTable*3)+1)
        textAutre = Label(self.cadremodelisation,text="Autre",width=15)
        textAutre.grid(row=2,column=(self.nbTable*3)+2)
        j = 0
        
        for i in range(len(self.nomsChampsCreer)) :
            nomduchamp = Label(self.cadremodelisation, width = 20, text= self.nomsChampsCreer[i].get(),borderwidth=2, relief="groove")
            nomduchamp.grid(column=(self.nbTable*3), row=i+3,padx=(20,0))
        for i in range(len(self.typeChampsCreer)) :
            nomduchamp = Label(self.cadremodelisation, width = 20, text= self.typeChampsCreer[i].get(),borderwidth=2, relief="groove")
            nomduchamp.grid(column=(self.nbTable*3)+1, row=i+3)
        for i in range(len(self.autreChampsCreer)) :
            nomduchamp = Label(self.cadremodelisation, width = 20, text= str(self.autreChampsCreer[i].get()),borderwidth=2, relief="groove")
            nomduchamp.grid(column=(self.nbTable*3)+2, row=i+3,padx=(0,20))
            j = i
        
        notable = self.nbTable
        nomschamps=self.nomsChampsCreer
        typeschamps=self.typeChampsCreer
        autreschamps=self.autreChampsCreer
        boutonModifier = Button(self.cadremodelisation, text="modifier", width = 15, command = lambda:self.modifierTable(boutonModifier,notable,nomTable,nomschamps,typeschamps,autreschamps))
        boutonModifier.grid(column=(self.nbTable*3),row=j+4)
        self.nbTable+=1
        self.creationTable.destroy()

    def modifierTable(self,boutonModifier,noTable,nom,nomsChamps,typesChamps,autresChamps):
        boutonModifier.grid_forget()
        self.nbChamps = len(nomsChamps)
        self.nomsChampsCreer=nomsChamps
        self.typeChampsCreer=typesChamps
        self.autreChampsCreer=autresChamps
        
        self.modifTable =Toplevel(self.cadremodelisation)
        
        textNom = Label(self.modifTable,text="Nom de la table")
        textNom.grid(row=0,column=1)
        self.nomTableCreer = Entry(self.modifTable)
        self.nomTableCreer.grid(row=0,column=2)
        self.nomTableCreer.insert(0,nom.cget("text"))
        textNom = Label(self.modifTable,text="Nom du Champ",width=15)
        textNom.grid(row=1,column=1)
        textType = Label(self.modifTable,text="Type du Champ",width=15)
        textType.grid(row=1,column=2)
        textAutre = Label(self.modifTable,text="Autre",width=15)
        textAutre.grid(row=1,column=3)
        
        for i in range(len(self.nomsChampsCreer)) :
            nomduchamp = Entry(self.modifTable, width = 20, text= self.nomsChampsCreer[i].get(),borderwidth=2, relief="groove")
            nomduchamp.grid(column=1, row=i+2,padx=(20,0))
            nomduchamp.insert(0,str(nomsChamps[i].get()))

            typeduchamp = Entry(self.modifTable, width = 20, text= self.typeChampsCreer[i].get(),borderwidth=2, relief="groove")
            typeduchamp.grid(column=2, row=i+2)
            typeduchamp.insert(0,str(typesChamps[i].get()))

            autre = Entry(self.modifTable, width = 20, text= str(self.autreChampsCreer[i].get()),borderwidth=2, relief="groove")
            autre.grid(column=3, row=i+2,padx=(0,20))
            autre.insert(0,str(autresChamps[i].get()))
            
            boutonEnlever = Button(self.modifTable,width =1, text = 'X', command = lambda:self.enleverChampsModifier(i, nomduchamp,typeduchamp,autre,boutonEnlever))
            boutonEnlever.grid(column=4,row=i+2)
            j = i
            
        boutonAjoutChamps = Button(self.modifTable, width = 15, height = 1, text= "Ajouter Champs", command = self.ajouterChampsModifier)
        boutonAjoutChamps.grid(row=self.nbChamps+3)
        boutonCreer = Button(self.modifTable, width = 15, height = 1, text = "Modifier", command  = lambda:self.ajoutmodificationTable(noTable))
        boutonCreer.grid(row=self.nbChamps+4,column=0, pady=10)
    def ajouterChampsModifier(self):
        
        self.nomsChampsCreer.append(StringVar())
        nomChamp =Entry(self.modifTable, width = 20,textvariable = self.nomsChampsCreer[self.nbChamps] )
        nomChamp.grid(row=self.nbChamps+2,column=1)
        
        self.typeChampsCreer.append(StringVar())
        typeChamp=Entry(self.modifTable, width = 20,textvariable = self.typeChampsCreer[self.nbChamps])
        typeChamp.grid(row=self.nbChamps+2,column=2)
        
        self.autreChampsCreer.append(StringVar())
        autreChampEntry=Entry(self.modifTable, width = 20,textvariable = self.autreChampsCreer[self.nbChamps])
        autreChampEntry.grid(row=self.nbChamps+2,column=3)

        self.nbChamps+=1
    def enleverChampsModifier(self,position,champ1,champ2,champ3,bouton):
        
        #NE MARCHE PAS VRAIMENT ENCORE
            #Possibilité de supprimer UNE ligne
            #Fait bugger le reste
            #Pas possible de supprimer d'autre ligne
        champ1.grid_forget()
        champ2.grid_forget()
        champ3.grid_forget()
        bouton.grid_forget()
        
        self.nomsChampsCreer.pop(position)
        self.typeChampsCreer.pop(position)
        self.autreChampsCreer.pop(position)
        
    def ajoutmodificationTable(self, noTable):
        textNom = Label(self.cadremodelisation,text="Nom de la table")
        textNom.grid(column=noTable*3,row=1)
        
        nomTable = Label(self.cadremodelisation,text=str(self.nomTableCreer.get()),borderwidth=2, relief="groove")
        nomTable.grid(column=noTable*3+1,row=1)
        
        
        textNom = Label(self.cadremodelisation,text="Nom du Champ",width=15)
        textNom.grid(row=2,column=(noTable*3))
        textType = Label(self.cadremodelisation,text="Type du Champ",width=15)
        textType.grid(row=2,column=(noTable*3)+1)
        textAutre = Label(self.cadremodelisation,text="Autre",width=15)
        textAutre.grid(row=2,column=(noTable*3)+2)
        j = 0
        
        for i in range(len(self.nomsChampsCreer)) :
            nomduchamp = Label(self.cadremodelisation, width = 20, text= self.nomsChampsCreer[i].get(),borderwidth=2, relief="groove")
            nomduchamp.grid(column=(noTable*3), row=i+3,padx=(20,0))

            typeduchamp = Label(self.cadremodelisation, width = 20, text= self.typeChampsCreer[i].get(),borderwidth=2, relief="groove")
            typeduchamp.grid(column=(noTable*3)+1, row=i+3)

            autrechamp = Label(self.cadremodelisation, width = 20, text= str(self.autreChampsCreer[i].get()),borderwidth=2, relief="groove")
            autrechamp.grid(column=(noTable*3)+2, row=i+3,padx=(0,20))
            j = i
        
        boutonModifier = Button(self.cadremodelisation, text="modifier", width = 15, command = lambda:modifierTable(boutonModifier,noTable,self.nomTableCreer.get(),self.nomsChampsCreer,self.typeChampsCreer,self.autreChampsCreer))
        boutonModifier.grid(column=(noTable*3),row=j+4)
        self.creationTable.destroy()

    def fermerfenetre(self):
        print("ON FERME la fenetre")
        self.root.destroy()
    