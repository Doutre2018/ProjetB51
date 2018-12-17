# -*- coding: utf-8 -*-
from tkinter import *
from tkinter import tix
from tkinter import ttk
#from PIL import Image,ImageDraw, ImageTk
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
        self.root.config(bg="#E4E9F3")
        self.parent=parent
        self.modele=parent.modele
        
        self.largeurDefault=largeur
        self.hauteurDefault=hauteur
        self.largeurEcran=self.root.winfo_screenwidth()
        self.hauteurEcran=self.root.winfo_screenmmheight()
        
        self.cadrecrcExiste=False

        self.images={}
        self.cadreactif=None
        self.creercadres()
        self.changecadre(self.cadrecrc)
        self.compteurBouton=3;
        self.dicBouton={}
        
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
        self.creercadrecrc()
        #self.cadrejeu=Frame(self.root,bg="blue")
        #self.modecourant=None

            
                         
              
    def creercadrecrc(self):
        #permet d'intégrer l'application dans l'application de base
        self.root.overrideredirect(True) #Enleve la bordure
        self.root.geometry('%dx%d+%d+%d' % (self.largeurDefault, self.hauteurDefault, (self.largeurEcran/2)-(self.largeurDefault/2),(self.hauteurEcran/2)))

        self.cadrecrc=Frame(self.root,bg= "#E4E9F3")
        self.cadrecrc.grid(padx=(100,0))

        self.lTitreCRC= Label(self.cadrecrc, text= "CRC",font= "arial, 30",bg= "#E4E9F3")
        self.lTitreCRC.grid(row=0, column=0,columnspan=2,pady=(20,0))

        self.ListeCRC= Listbox(self.cadrecrc,selectmode=SINGLE,width=50,height=30)
        
        #valeur=0
        #for i in self.modele.listeCartes:
           # self.listeCRC.insert(valeur+1,i)
        
        
        #self.ListeCRC.insert(0, "Modele")
        for nom in self.modele.listeCartes:
            for i in nom:
                self.ListeCRC.insert(0,i)

        self.ListeCRC.grid(row=1, column=0,rowspan=3,padx=(30,20),pady=10)

        
        self.AjouterCRC = Button(self.cadrecrc ,text= "Ajouter",command=self.ajoutCRC, height=1,width=10,relief=FLAT,bg="white")
        self.AjouterCRC.grid(row=2, column=1,pady=(0,100),padx=(0,20))
        self.SupprimerCRC = Button(self.cadrecrc ,text= "Supprimer",command=self.delCRC, height=1, width=10,relief=FLAT,bg="white")
        self.SupprimerCRC.grid(row=2, column=1,padx=(0,20))
        self.ModifCRC = Button(self.cadrecrc ,text= "Modifier",command=self.modifierCRC, height=1, width=10,relief=FLAT,bg="white")
        self.ModifCRC.grid(row=2, column=1,pady=(100,0),padx=(0,20))

        self.cadrecrcExiste=True

    def fermerfenetre(self):
        self.root.destroy()
        
    def ajoutCRC(self):
        self.carteCRC =Toplevel(self.root)
        self.carteCRC.config(bg="#234078")
        
        largeurEcran = self.root.winfo_screenwidth()
        hauteurEcran = self.root.winfo_screenheight()
        x = (largeurEcran/2)-(600/2)
        y = (hauteurEcran/2)-(500/2)
        self.carteCRC.geometry("+%d+%d" % (x, y))
        
        self.frameCarteCRC = Frame(self.carteCRC,bg="#234078")
        self.frameCarteCRC.grid()
        
        self.labelNomClasse= Label(self.frameCarteCRC, text="Classe: ",bg="#234078",fg="white",font= "arial, 20")
        self.labelNomClasse.grid(pady=(20,0))
        self.entryNomClasse= Entry(self.frameCarteCRC)
        self.entryNomClasse.grid()
        
        self.frameInterieur= Frame(self.frameCarteCRC,bg="#234078")
        self.frameInterieur.grid()
        
        #Partie du frame pour heritage et responsable
        self.frameHeriatageResponsable= Frame(self.frameInterieur,bg="#234078")
        self.frameHeriatageResponsable.grid(row=0,column=1)
        self.labelHeritage= Label(self.frameHeriatageResponsable, text="Héritage: ",bg="#234078",fg="white")
        self.labelHeritage.grid(row=0,column=1,pady=(10,0))
        self.entryHeritage=Entry(self.frameHeriatageResponsable)
        self.entryHeritage.grid(row=0, column=2,pady=(10,0))
        self.labelResponsable= Label(self.frameHeriatageResponsable, text="Responsable: ",bg="#234078",fg="white")
        self.labelResponsable.grid(row=1, column=1)
        self.entryResponsable= Entry(self.frameHeriatageResponsable)
        self.entryResponsable.grid(row=1, column=2)
        
        #Partie du frame pour les fonction, Attribut , objet
        self.frameFonction= Frame(self.frameInterieur,bg="#234078")
        self.frameFonction.grid(row=1,column=1,padx=(20,0))
        self.labelFonction= Label(self.frameFonction, text="Fonction",bg="#234078",fg="white")
        self.labelFonction.grid(row=0, column=1,padx=5)
        self.labelAttribut= Label(self.frameFonction, text="Attribut",bg="#234078",fg="white")
        self.labelAttribut.grid(row=0, column=2,padx=(0,5))
        self.labelObjet= Label(self.frameFonction, text="Objet",bg="#234078",fg="white")
        self.labelObjet.grid(row=0, column=3)
        self.textFonction = Text(self.frameFonction, height = 10, width=15)
        self.textFonction.grid(row=1, column=1,padx=(20,0))
        self.textAttribut = Text(self.frameFonction, height = 10, width=15)
        self.textAttribut.grid(row=1, column=2,padx=5)
        self.textObjet = Text(self.frameFonction, height = 10, width=15)
        self.textObjet.grid(row=1, column=3,padx=(0,5))
        
        #partie du frame pour Collaboration
        self.frameCollaboration= Frame(self.frameInterieur,bg="#234078")
        self.frameCollaboration.grid(row=0 , column= 2, rowspan=2)
        self.labelCollaboration= Label(self.frameCollaboration, text="Collaboration",bg="#234078",fg="white")
        self.labelCollaboration.grid(padx=(0,20))
        self.textCollaboration=Text(self.frameCollaboration,height = 13, width=15)
        self.textCollaboration.grid(padx=(0,20))
        
        
        #Bouton Ajouter
        self.boutonAjouter= Button(self.frameCarteCRC, text="Ajouter", command=self.nouveauCRC,bg="white",relief=FLAT)
        self.boutonAjouter.grid(pady=(10,20))

    def nouveauCRC(self):
        texteboutton=self.entryNomClasse.get()
        texteResponsable=self.entryResponsable.get()
        texteHeritage=self.entryHeritage.get()
        #AJOUT DE LA CARTE À LA BD
        #id du projet
        listeValeurCarte=[None]*5
        listeValeurCarte[0]=0
        
        #nom de la classe
        listeValeurCarte[1]=texteboutton
        #responsable
        listeValeurCarte[2]=texteHeritage
        #ordre
        listeValeurCarte[3]=0
        
        listeValeurCarte[4]=texteResponsable
        #insertion des infos de base de la carte dans la BD
        self.modele.insertCarte(listeValeurCarte)
        #id de la carte qui vient d'être ajoutée
        temp = self.modele.selectIdCarte(texteboutton)
        for n in temp:
            for i in n:
                idCarteAjoutee=str(i)
        
        texteAtt = self.textAttribut.get(1.0, "end-1c")
        self.modele.insertAttributsDeCarte(texteAtt, idCarteAjoutee)
        
        #FONCTIONS
        texteFonction = self.textFonction.get(1.0, "end-1c")
        listeValeurFonct=[None]*2
        listeValeurFonct[0]="'"+idCarteAjoutee+"'"
        listeValeurFonct[1]="'"+texteFonction+"'"
        self.modele.insertFonctionDeCarte(listeValeurFonct)
        
        #OBJETS
        texteObjet = self.textObjet.get(1.0, "end-1c")
        listeValeurObj=[None]*2
        listeValeurObj[0]="'"+idCarteAjoutee+"'"
        listeValeurObj[1]="'"+texteObjet+"'"
        self.modele.insertObjetDeCarte(listeValeurObj)
        
        #COLLABO
        texteCollabo = self.textCollaboration.get(1.0, "end-1c")
        self.modele.insertCollaboDeCarte(idCarteAjoutee,texteCollabo)
        
        self.ListeCRC.insert(self.compteurBouton, texteboutton)
        
        self.carteCRC.destroy()
        
        self.compteurBouton=self.compteurBouton+1
        
    def modifierCRC(self):
        a=()
        a=self.ListeCRC.curselection()
        
        if a==():
            pass
        else:
            b=self.ListeCRC.get(a)
        
            # ------------- DM -------------
            id = self.modele.selectIdCarte(b)
            for i in id:
                for n in i:
                    id=n
    
            attribut = self.modele.selectAttributDeCarte(id)
            for i in attribut:
                for n in i:
                    attribut=n
            nom_responsable = self.modele.selectCarteResponsable(id)
            for i in nom_responsable:
                for n in i:
                    nom_responsable=n
            heritage = self.modele.selectCarteHeritage(id)
            for i in heritage:
                for n in i:
                    heritage=n
            fonctions = self.modele.selectFonctionsDeCarte(id)
            for i in fonctions:
                for n in i:
                    fonctions=n
                    
            collabos  = self.modele.selectCollaboDeCarte(id)
            for i in collabos:
                for n in i:
                    collabos=n
                    
            objets = self.modele.selectObjetsDeCarte(id)
            for i in objets:
                for n in i:
                    objets=n
            # ------------------------------
            
            self.carteCRC =Toplevel(self.root)
            self.frameCarteCRC = Frame(self.carteCRC)
            self.carteCRC.config(bg="#234078")
            self.frameCarteCRC.grid()
            
            largeurEcran = self.root.winfo_screenwidth()
            hauteurEcran = self.root.winfo_screenheight()
            x = (largeurEcran/2)-(600/2)
            y = (hauteurEcran/2)-(500/2)
            self.carteCRC.geometry("+%d+%d" % (x, y))
            
            self.frameCarteCRC = Frame(self.carteCRC,bg="#234078")
            self.frameCarteCRC.grid()
            
            self.labelNomClasse= Label(self.frameCarteCRC, text="Classe: ",bg="#234078",fg="white",font= "arial, 20")
            self.labelNomClasse.grid(pady=(20,0))
            self.entryNomClasse= Entry(self.frameCarteCRC)
            self.entryNomClasse.grid()
            
            self.frameInterieur= Frame(self.frameCarteCRC,bg="#234078")
            self.frameInterieur.grid()
            
            #Partie du frame pour heritage et responsable
            self.frameHeriatageResponsable= Frame(self.frameInterieur,bg="#234078")
            self.frameHeriatageResponsable.grid(row=0,column=1)
            self.labelHeritage= Label(self.frameHeriatageResponsable, text="Héritage: ",bg="#234078",fg="white")
            self.labelHeritage.grid(row=0,column=1,pady=(10,0))
            self.entryHeritage=Entry(self.frameHeriatageResponsable)
            self.entryHeritage.grid(row=0, column=2,pady=(10,0))
            self.labelResponsable= Label(self.frameHeriatageResponsable, text="Responsable: ",bg="#234078",fg="white")
            self.labelResponsable.grid(row=1, column=1)
            self.entryResponsable= Entry(self.frameHeriatageResponsable)
            self.entryResponsable.grid(row=1, column=2)
            
            # ------------- DM -------------
            self.entryNomClasse.insert(0, b)
            self.entryHeritage.insert(0,heritage)
            self.entryResponsable.insert(0,nom_responsable)
            # ------------------------------
            
            #Partie du frame pour les fonction, Attribut , objet
            self.frameFonction= Frame(self.frameInterieur,bg="#234078")
            self.frameFonction.grid(row=1,column=1,padx=(20,0))
            self.labelFonction= Label(self.frameFonction, text="Fonction",bg="#234078",fg="white")
            self.labelFonction.grid(row=0, column=1,padx=5)
            self.labelAttribut= Label(self.frameFonction, text="Attribut",bg="#234078",fg="white")
            self.labelAttribut.grid(row=0, column=2,padx=(0,5))
            self.labelObjet= Label(self.frameFonction, text="Objet",bg="#234078",fg="white")
            self.labelObjet.grid(row=0, column=3)
            self.textFonction = Text(self.frameFonction, height = 10, width=15)
            self.textFonction.grid(row=1, column=1,padx=(20,0))
            self.textAttribut = Text(self.frameFonction, height = 10, width=15)
            self.textAttribut.grid(row=1, column=2,padx=5)
            self.textObjet = Text(self.frameFonction, height = 10, width=15)
            self.textObjet.grid(row=1, column=3,padx=(0,5))
            
            # ------------- DM -------------
            self.textAttribut.insert(INSERT, attribut)
            self.textFonction.insert(INSERT, fonctions)
            self.textObjet.insert(INSERT, objets)
            # ------------------------------
            
            #partie du frame pour Collaboration
            self.frameCollaboration= Frame(self.frameInterieur,bg="#234078")
            self.frameCollaboration.grid(row=0 , column= 2, rowspan=2)
            self.labelCollaboration= Label(self.frameCollaboration, text="Collaboration",bg="#234078",fg="white")
            self.labelCollaboration.grid(padx=(0,20))
            self.textCollaboration=Text(self.frameCollaboration,height = 13, width=15)
            self.textCollaboration.grid(padx=(0,20))
            
            # ------------- DM -------------
            self.textCollaboration.insert(INSERT, collabos)
            # ------------------------------
            
            #Bouton Ajouter
            a = self.ListeCRC.curselection()
            self.niaisage = self.ListeCRC.get(a)        # J'tanné
            self.boutonModifier= Button(self.frameCarteCRC, text="Modifier", command=self.modifierCarteCRC,bg="white",relief=FLAT)
            self.boutonModifier.grid(pady=(10,20))
            
        
        
        
    # ---------------- DM ----------------
    def modifierCarteCRC(self):
        classe = self.niaisage
        
        listeCarte = []
        listeCarte.append(self.entryNomClasse.get())
        listeCarte.append(self.entryHeritage.get())
        listeCarte.append(self.entryResponsable.get())
        
        id = self.modele.selectIdCarte(classe)
        
        for n in id:
            for i in n:
                id = str(i)
        
        self.modele.updateCRC(id, listeCarte)
        
        texteAtt = self.textAttribut.get("1.0", END)
        self.modele.updateAttributsCRC(id, texteAtt)
        
        texteFnc = self.textFonction.get("1.0", END)
        self.modele.updateFonctionCRC(id, texteFnc)
        
        texteObj = self.textObjet.get("1.0", END)
        self.modele.updateObjetCRC(id, texteObj)
        
        texteCollab = self.textCollaboration.get("1.0", END)
        self.modele.updateCollabCRC(id, texteCollab)
        
        self.carteCRC.destroy()
        self.ListeCRC.delete(0, END)
        listeCartes = []
        listeCartes = self.modele.selectClassesCartes()
        
        for nom in listeCartes:
            for i in nom:
                self.ListeCRC.insert(0,i)
    # ------------------------------------
        

    def delCRC(self):
        a=()
        a=self.ListeCRC.curselection()
        nomClasse = str(self.ListeCRC.get(a))
        for i in self.modele.selectIdCarte(nomClasse):
            for n in i:
                idCarteCourante=str(n)
        #Supprime la rangée de la BD pour toutess les composantes
        self.modele.supprimerAttributsDeCarte(idCarteCourante)
        self.modele.supprimerCollaboDeCarte(idCarteCourante)
        self.modele.supprimerFonctionDeCarte(idCarteCourante)
        self.modele.supprimerCarte(nomClasse)
        
        self.ListeCRC.delete(a)
    