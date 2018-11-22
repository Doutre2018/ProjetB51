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
        self.parent=parent
        self.modele=None
        
        self.largeurDefault=largeur
        self.hauteurDefault=hauteur
        self.largeurEcran=self.root.winfo_screenwidth()
        self.hauteurEcran=self.root.winfo_screenmmheight()
        
        self.cadrecrcExiste=False

        self.images={}
        self.cadreactif=None
        self.creercadres()
        self.changecadre(self.cadreAnalyse)


        
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
        self.creercadreAnalyse()
        #self.cadrejeu=Frame(self.root,bg="blue")
        #self.modecourant=None
                         
              
    def creercadreAnalyse(self):
        #permet d'intégrer l'application dans l'application de base
        self.root.overrideredirect(True) #Enleve la bordure
        self.root.geometry('%dx%d+%d+%d' % (self.largeurDefault, self.hauteurDefault, (self.largeurEcran/2)-(self.largeurDefault/2),(self.hauteurEcran/2)))

        self.cadreAnalyse=Frame(self.root)

        self.lTitreCRC= Label(self.cadreAnalyse, text= "Analyse",font= "arial, 20")
        self.lTitreCRC.grid(padx=100 ,row=0, column=0,  columnspan=2)
        
        
        self.lVerbe = Label(self.cadreAnalyse, text= "Verbe",font= "arial, 12")
        self.lVerbe.grid(row=1, column=1,)
        self.lNom = Label(self.cadreAnalyse, text= "Nom",font= "arial, 12")
        self.lNom.grid(row=1, column=2,)
        self.lAjectif = Label(self.cadreAnalyse, text= "Ajectif",font= "arial, 12")
        self.lAjectif.grid(row=1, column=3,)
        
        
        self.lexplicite = Label(self.cadreAnalyse, text= "Explicite",font= "arial, 12")
        self.lexplicite.grid(row=3, column=0,)
        self.lImplicite = Label(self.cadreAnalyse, text= "Implicite",font= "arial, 12")
        self.lImplicite.grid(row=5, column=0,)
        self.lSuplementaire = Label(self.cadreAnalyse, text= "Suplementaire",font= "arial, 12")
        self.lSuplementaire.grid(row=7, column=0,)
        
        self.BVerbeExplicite= Label(self.cadreAnalyse, text ="+", font= "arial, 16")
        self.BVerbeExplicite.grid(row=2, column=1)
        self.BVerbeImplicite= Label(self.cadreAnalyse, text ="+", font= "arial, 16")
        self.BVerbeImplicite.grid(row=4, column=1)
        self.BVerbeSuplementaire=Label(self.cadreAnalyse, text ="+", font= "arial, 16")
        self.BVerbeSuplementaire.grid(row=6, column=1)
        self.BNomExplicite =Label(self.cadreAnalyse, text ="+", font= "arial, 16")
        self.BNomExplicite.grid(row=2, column= 2);
        self.BNomImplicite =Label(self.cadreAnalyse, text ="+", font= "arial, 16")
        self.BNomImplicite.grid(row=4, column= 2);
        self.BNomSuplementaire =Label(self.cadreAnalyse, text ="+", font= "arial, 16")
        self.BNomSuplementaire.grid(row=6, column= 2);
        self.BAdjectifExplicite =Label(self.cadreAnalyse, text ="+", font= "arial, 16")
        self.BAdjectifExplicite.grid(row=2, column= 3);
        self.BAjdectifImplicite =Label(self.cadreAnalyse, text ="+", font= "arial, 16")
        self.BAjdectifImplicite.grid(row=4, column= 3);
        self.BAjdectifSuplementaire =Label(self.cadreAnalyse, text ="+", font= "arial, 16")
        self.BAjdectifSuplementaire.grid(row=6, column= 3);
        
        self.BVerbeExplicite.bind("<ButtonRelease-1>",self.NouveauVerbeExplicite)
        self.BVerbeImplicite.bind("<ButtonRelease-1>",self.NouveauVerbeImplicite)
        self.BVerbeSuplementaire.bind("<ButtonRelease-1>",self.NouveauVerbeSuplementaire)
        
        self.BNomExplicite.bind("<ButtonRelease-1>",self.NouveauNomExplicite)
        self.BNomImplicite.bind("<ButtonRelease-1>",self.NouveauNomImplicite)
        self.BNomSuplementaire.bind("<ButtonRelease-1>",self.NouveauNomSuplementaire)
        
        self.BAdjectifExplicite.bind("<ButtonRelease-1>",self.NouveauAjectifExplicite)
        self.BAjdectifImplicite.bind("<ButtonRelease-1>",self.NouveauAjectifImplicite)
        self.BAjdectifSuplementaire.bind("<ButtonRelease-1>",self.NouveauAjectifSupplementaire)
        
        
        self.lBVerbeExplicite = Listbox(self.cadreAnalyse,selectmode=SINGLE,height=7)
        self.lBVerbeExplicite.grid(row=3, column= 1);
        self.lBVerbeImplicite = Listbox(self.cadreAnalyse,selectmode=SINGLE,height=7)
        self.lBVerbeImplicite.grid(row=5, column= 1);
        self.lBVerbeSuplementaire = Listbox(self.cadreAnalyse,selectmode=SINGLE,height=7)
        self.lBVerbeSuplementaire.grid(row=7, column= 1);
        self.lBNomExplicite = Listbox(self.cadreAnalyse,selectmode=SINGLE,height=7)
        self.lBNomExplicite.grid(row=3, column= 2);
        self.lBNomImplicite = Listbox(self.cadreAnalyse,selectmode=SINGLE,height=7)
        self.lBNomImplicite.grid(row=5, column= 2);
        self.lBNomSuplementaire = Listbox(self.cadreAnalyse,selectmode=SINGLE,height=7)
        self.lBNomSuplementaire.grid(row=7, column= 2);
        self.lBAdjectifExplicite = Listbox(self.cadreAnalyse,selectmode=SINGLE,height=7)
        self.lBAdjectifExplicite.grid(row=3, column= 3);
        self.lBAjdectifImplicite = Listbox(self.cadreAnalyse,selectmode=SINGLE,height=7)
        self.lBAjdectifImplicite.grid(row=5, column= 3);
        self.lBAjdectifSuplementaire = Listbox(self.cadreAnalyse,selectmode=SINGLE,height=7)
        self.lBAjdectifSuplementaire.grid(row=7, column= 3);



        self.cadrecrcExiste=True

    def fermerfenetre(self):
        print("ON FERME la fenetre")
        self.root.destroy()
      
    def NouveauVerbeExplicite(self,evt):  
        self.frameNouveauVerbeExplicite =Toplevel(self.root)
        self.lTitre=Label(self.frameNouveauVerbeExplicite, text="Nouveau Verbe Explicite",font= "arial, 20")
        self.lTitre.grid();
        self.entryNew = Entry(self.frameNouveauVerbeExplicite)
        self.entryNew.grid()
        
        self.bAjouter= Button(self.frameNouveauVerbeExplicite, text="Ajouter" ,command=self.AjouterNouveauVerbeExplicite)
        self.bAjouter.grid();     
        
    def NouveauVerbeImplicite(self,evt): 
        self.frameNouveauVerbeImplicite =Toplevel(self.root) 
        self.lTitre=Label(self.frameNouveauVerbeImplicite, text="Nouveau Verbe Implicite",font= "arial, 20")
        self.lTitre.grid();
        self.entryNew = Entry(self.frameNouveauVerbeImplicite)
        self.entryNew.grid()
           
        self.bAjouter= Button(self.frameNouveauVerbeImplicite, text="Ajouter" ,command=self.AjouterNouveauVerbeImplicite)
        self.bAjouter.grid();   
        
    def NouveauVerbeSuplementaire(self,evt):  
        self.frameNouveauVerbeSuplementaire =Toplevel(self.root)
        self.lTitre=Label(self.frameNouveauVerbeSuplementaire, text="Nouveau Verbe supplementaire",font= "arial, 20")
        self.lTitre.grid();
        self.entryNew = Entry(self.frameNouveauVerbeSuplementaire)
        self.entryNew.grid()
         
        self.bAjouter= Button(self.frameNouveauVerbeSuplementaire, text="Ajouter" ,command=self.AjouterNouveauVerbeSupplementaire)
        self.bAjouter.grid();   
        
    def NouveauNomExplicite(self,evt):  
        self.frameNouveauNomExplicite =Toplevel(self.root)
        self.lTitre=Label(self.frameNouveauNomExplicite, text="Nouveau nom explicite",font= "arial, 20")
        self.lTitre.grid();
        self.entryNew = Entry(self.frameNouveauNomExplicite)
        self.entryNew.grid()
         
        self.bAjouter= Button(self.frameNouveauNomExplicite, text="Ajouter" ,command=self.AjouterNouveauNomExplicite)
        self.bAjouter.grid();  
    
    def NouveauNomImplicite(self,evt): 
        self.frameNouveauNomImplicite =Toplevel(self.root) 
        self.lTitre=Label(self.frameNouveauNomImplicite, text="Nouveau Nom Implicite",font= "arial, 20")
        self.lTitre.grid();
        self.entryNew = Entry(self.frameNouveauNomImplicite)
        self.entryNew.grid()
           
        self.bAjouter= Button(self.frameNouveauNomImplicite, text="Ajouter" ,command=self.AjouterNouveauNomImplicite)
        self.bAjouter.grid(); 
     
    def NouveauNomSuplementaire(self,evt):  
        self.frameNouveauNomSuplementaire =Toplevel(self.root)
        self.lTitre=Label(self.frameNouveauNomSuplementaire, text="Nouveau Nom supplementaire",font= "arial, 20")
        self.lTitre.grid();
        self.entryNew = Entry(self.frameNouveauNomSuplementaire)
        self.entryNew.grid()
         
        self.bAjouter= Button(self.frameNouveauNomSuplementaire, text="Ajouter" ,command=self.AjouterNouveauNomSupplementaire)
        self.bAjouter.grid();      
   
    def NouveauAjectifExplicite(self,evt):  
        self.frameNouveauAjectifExplicite =Toplevel(self.root)
        self.lTitre=Label(self.frameNouveauAjectifExplicite, text="Nouvelle adjectif explicite",font= "arial, 20")
        self.lTitre.grid();
        self.entryNew = Entry(self.frameNouveauAjectifExplicite)
        self.entryNew.grid()
         
        self.bAjouter= Button(self.frameNouveauAjectifExplicite, text="Ajouter" ,command=self.AjouterNouveauAdjectifExplicite)
        self.bAjouter.grid();   
       
    def NouveauAjectifImplicite(self,evt):  
        self.frameNouveauAjectifImplicite =Toplevel(self.root)
        self.lTitre=Label(self.frameNouveauAjectifImplicite, text="Nouvelle adjectif implicite",font= "arial, 20")
        self.lTitre.grid();
        self.entryNew = Entry(self.frameNouveauAjectifImplicite)
        self.entryNew.grid()
         
        self.bAjouter= Button(self.frameNouveauAjectifImplicite, text="Ajouter" ,command=self.AjouterNouveauAdjectifImplicite)
        self.bAjouter.grid();  
        
    def NouveauAjectifSupplementaire(self,evt):  
        self.frameNouveauAjectifSupplementaire =Toplevel(self.root)
        self.lTitre=Label(self.frameNouveauAjectifSupplementaire, text="Nouvelle adjectif supplementaire",font= "arial, 20")
        self.lTitre.grid();
        self.entryNew = Entry(self.frameNouveauAjectifSupplementaire)
        self.entryNew.grid()
         
        self.bAjouter= Button(self.frameNouveauAjectifSupplementaire, text="Ajouter" ,command=self.AjouterNouveauAdjectifSupplementaire)
        self.bAjouter.grid();  
        
        
       
       
       
        
    def AjouterNouveauVerbeExplicite(self):  
        self.newInsert=self.entryNew.get();
        self.lBVerbeExplicite.insert(END, self.newInsert)
        self.frameNouveauVerbeExplicite.destroy()
        
    def AjouterNouveauVerbeImplicite(self):  
        self.newInsert=self.entryNew.get();
        self.lBVerbeImplicite.insert(END, self.newInsert)
        self.frameNouveauVerbeImplicite.destroy()
       
    def AjouterNouveauVerbeSupplementaire(self):  
        self.newInsert=self.entryNew.get();
        self.lBVerbeSuplementaire.insert(END, self.newInsert)
        self.frameNouveauVerbeSuplementaire.destroy()
        
    def AjouterNouveauNomExplicite(self):  
        self.newInsert=self.entryNew.get();
        self.lBNomExplicite.insert(END, self.newInsert)
        self.frameNouveauNomExplicite.destroy()
        
    def AjouterNouveauNomImplicite(self):  
        self.newInsert=self.entryNew.get();
        self.lBNomImplicite.insert(END, self.newInsert)
        self.frameNouveauNomImplicite.destroy()
    
    def AjouterNouveauNomSupplementaire(self):  
        self.newInsert=self.entryNew.get();
        self.lBNomSuplementaire.insert(END, self.newInsert)
        self.frameNouveauNomSuplementaire.destroy()
        
    def AjouterNouveauAdjectifExplicite(self):  
        self.newInsert=self.entryNew.get();
        self.lBAdjectifExplicite.insert(END, self.newInsert)
        self.frameNouveauAjectifExplicite.destroy()
        
    def AjouterNouveauAdjectifImplicite(self):  
        self.newInsert=self.entryNew.get();
        self.lBAjdectifImplicite.insert(END, self.newInsert)
        self.frameNouveauAjectifImplicite.destroy()
        
    def AjouterNouveauAdjectifSupplementaire(self):  
        self.newInsert=self.entryNew.get();
        self.lBAjdectifSuplementaire.insert(END, self.newInsert)
        self.frameNouveauAjectifSupplementaire.destroy()