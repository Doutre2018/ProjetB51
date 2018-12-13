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
    def __init__(self,parent,largeur=800,hauteur=700):

        self.root=tix.Tk()
        self.root.title(os.path.basename(sys.argv[0]))
        self.root.attributes("-fullscreen", False)
        self.root.protocol("WM_DELETE_WINDOW", self.fermerfenetre)
        self.root.config(bg="#E4E9F3")
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
        
        self.lectureBD()


    def lectureBD(self):
        for mot in self.parent.modele.lesVerbesEx:
            self.lBVerbeExplicite.insert(END, mot)
        for mot in self.parent.modele.lesVerbesImp:
            self.lBVerbeImplicite.insert(END, mot)
        for mot in self.parent.modele.lesNomsImp:
            self.lBNomImplicite.insert(END, mot)
        for mot in self.parent.modele.lesAdjectifsImp:
            self.lBAjdectifImplicite.insert(END, mot)
        for mot in self.parent.modele.lesVerbesSup:
            self.lBVerbeSuplementaire.insert(END, mot)
        for mot in self.parent.modele.lesNomsSup:
            self.lBNomSuplementaire.insert(END, mot)
        for mot in self.parent.modele.lesAdjectifSup:
            self.lBAjdectifSuplementaire.insert(END, mot)
        for mot in self.parent.modele.lesNomsEx:
            self.lBNomExplicite.insert(END, mot)
        for mot in self.parent.modele.lesAdjectifsEx:
            self.lBAdjectifExplicite.insert(END, mot)
        
        
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

        self.cadreAnalyse=Frame(self.root,bg="#E4E9F3")
        self.cadreAnalyse.grid(padx=(100,0))

        self.lTitreCRC= Label(self.cadreAnalyse, text= "Analyse Textuelle",font= "arial, 30",bg="#E4E9F3")
        self.lTitreCRC.grid(padx=100 ,row=0, column=1,  columnspan=4,pady=(0,20))
        
        
        self.lVerbe = Label(self.cadreAnalyse, text= "Verbe",font= "arial, 12",bg="#E4E9F3")
        self.lVerbe.grid(row=1, column=1,)
        self.lNom = Label(self.cadreAnalyse, text= "Nom",font= "arial, 12",bg="#E4E9F3")
        self.lNom.grid(row=1, column=2,)
        self.lAjectif = Label(self.cadreAnalyse, text= "Ajectif",font= "arial, 12",bg="#E4E9F3")
        self.lAjectif.grid(row=1, column=3,)
        
        
        self.lexplicite = Label(self.cadreAnalyse, text= "Explicite",font= "arial, 12",bg="#E4E9F3")
        self.lexplicite.grid(row=3, column=0,)
        self.lImplicite = Label(self.cadreAnalyse, text= "Implicite",font= "arial, 12",bg="#E4E9F3")
        self.lImplicite.grid(row=5, column=0,)
        self.lSuplementaire = Label(self.cadreAnalyse, text= "Suplementaire",font= "arial, 12",bg="#E4E9F3")
        self.lSuplementaire.grid(row=7, column=0,)
        
        self.BVerbeExplicite= Label(self.cadreAnalyse, text ="+", font= "arial, 16",bg="#E4E9F3")
        self.BVerbeExplicite.grid(row=2, column=1,padx=(0,30))
        self.DelVerbeExplicite= Label(self.cadreAnalyse, text ="-", font= "arial, 16",bg="#E4E9F3")
        self.DelVerbeExplicite.grid(row=2, column=1,padx=(30,0))
        
        self.BVerbeImplicite= Label(self.cadreAnalyse, text ="+", font= "arial, 16",bg="#E4E9F3")
        self.BVerbeImplicite.grid(row=4, column=1,padx=(0,30))
        self.DelVerbeImplicite= Label(self.cadreAnalyse, text ="-", font= "arial, 16",bg="#E4E9F3")
        self.DelVerbeImplicite.grid(row=4, column=1,padx=(30,0))
        
        self.BVerbeSuplementaire=Label(self.cadreAnalyse, text ="+", font= "arial, 16",bg="#E4E9F3")
        self.BVerbeSuplementaire.grid(row=6, column=1,padx=(0,30))
        self.DelVerbeSuplementaire=Label(self.cadreAnalyse, text ="-", font= "arial, 16",bg="#E4E9F3")
        self.DelVerbeSuplementaire.grid(row=6, column=1,padx=(30,0))
        
        self.BNomExplicite =Label(self.cadreAnalyse, text ="+", font= "arial, 16",bg="#E4E9F3")
        self.BNomExplicite.grid(row=2, column= 2,padx=(0,30));
        self.DelNomExplicite =Label(self.cadreAnalyse, text ="-", font= "arial, 16",bg="#E4E9F3")
        self.DelNomExplicite.grid(row=2, column= 2,padx=(30,0));
        
        self.BNomImplicite =Label(self.cadreAnalyse, text ="+", font= "arial, 16",bg="#E4E9F3")
        self.BNomImplicite.grid(row=4, column= 2,padx=(0,30));
        self.DelNomImplicite =Label(self.cadreAnalyse, text ="-", font= "arial, 16",bg="#E4E9F3")
        self.DelNomImplicite.grid(row=4, column= 2,padx=(30,0));
        
        self.BNomSuplementaire =Label(self.cadreAnalyse, text ="+", font= "arial, 16",bg="#E4E9F3")
        self.BNomSuplementaire.grid(row=6, column= 2,padx=(0,30));
        self.DelNomSuplementaire =Label(self.cadreAnalyse, text ="-", font= "arial, 16",bg="#E4E9F3")
        self.DelNomSuplementaire.grid(row=6, column= 2,padx=(30,0));
        
        self.BAdjectifExplicite =Label(self.cadreAnalyse, text ="+", font= "arial, 16",bg="#E4E9F3")
        self.BAdjectifExplicite.grid(row=2, column= 3,padx=(0,30));
        self.DelAdjectifExplicite =Label(self.cadreAnalyse, text ="-", font= "arial, 16",bg="#E4E9F3")
        self.DelAdjectifExplicite.grid(row=2, column= 3,padx=(30,0));
        
        self.BAjdectifImplicite =Label(self.cadreAnalyse, text ="+", font= "arial, 16",bg="#E4E9F3")
        self.BAjdectifImplicite.grid(row=4, column= 3,padx=(0,30));
        self.DelAjdectifImplicite =Label(self.cadreAnalyse, text ="-", font= "arial, 16",bg="#E4E9F3")
        self.DelAjdectifImplicite.grid(row=4, column= 3,padx=(30,0));
        
        self.BAjdectifSuplementaire =Label(self.cadreAnalyse, text ="+", font= "arial, 16",bg="#E4E9F3")
        self.BAjdectifSuplementaire.grid(row=6, column= 3,padx=(0,30));
        self.DelAjdectifSuplementaire =Label(self.cadreAnalyse, text ="-", font= "arial, 16",bg="#E4E9F3")
        self.DelAjdectifSuplementaire.grid(row=6, column= 3,padx=(30,0));
        
        self.BVerbeExplicite.bind("<ButtonRelease-1>",self.NouveauVerbeExplicite)
        self.BVerbeImplicite.bind("<ButtonRelease-1>",self.NouveauVerbeImplicite)
        self.BVerbeSuplementaire.bind("<ButtonRelease-1>",self.NouveauVerbeSuplementaire)
        
        self.BNomExplicite.bind("<ButtonRelease-1>",self.NouveauNomExplicite)
        self.BNomImplicite.bind("<ButtonRelease-1>",self.NouveauNomImplicite)
        self.BNomSuplementaire.bind("<ButtonRelease-1>",self.NouveauNomSuplementaire)
        
        self.BAdjectifExplicite.bind("<ButtonRelease-1>",self.NouveauAjectifExplicite)
        self.BAjdectifImplicite.bind("<ButtonRelease-1>",self.NouveauAjectifImplicite)
        self.BAjdectifSuplementaire.bind("<ButtonRelease-1>",self.NouveauAjectifSupplementaire)
        
        
        
        
        self.DelVerbeExplicite.bind("<ButtonRelease-1>",self.SupVerbeExplicite)
        self.DelVerbeImplicite.bind("<ButtonRelease-1>",self.SupVerbeImplicite)
        self.DelVerbeSuplementaire.bind("<ButtonRelease-1>",self.SupVerbeSuplementaire)
        
        self.DelNomExplicite.bind("<ButtonRelease-1>",self.SupNomExplicite)
        self.DelNomImplicite.bind("<ButtonRelease-1>",self.SupNomImplicite)
        self.DelNomSuplementaire.bind("<ButtonRelease-1>",self.SupNomSuplementaire)
        
        self.DelAdjectifExplicite.bind("<ButtonRelease-1>",self.SupAjectifExplicite)
        self.DelAjdectifImplicite.bind("<ButtonRelease-1>",self.SupAjectifImplicite)
        self.DelAjdectifSuplementaire.bind("<ButtonRelease-1>",self.SupAjectifSupplementaire)
        
        
        self.lBVerbeExplicite = Listbox(self.cadreAnalyse,selectmode=SINGLE,height=9,width=25)
        self.lBVerbeExplicite.grid(row=3, column= 1,pady=(0,10));
        self.lBVerbeImplicite = Listbox(self.cadreAnalyse,selectmode=SINGLE,height=9,width=25)
        self.lBVerbeImplicite.grid(row=5, column= 1,padx=(5,5),pady=(0,10));
        self.lBVerbeSuplementaire = Listbox(self.cadreAnalyse,selectmode=SINGLE,height=9,width=25)
        self.lBVerbeSuplementaire.grid(row=7, column= 1,pady=(0,10));
        self.lBNomExplicite = Listbox(self.cadreAnalyse,selectmode=SINGLE,height=9,width=25)
        self.lBNomExplicite.grid(row=3, column= 2,pady=(0,10));
        self.lBNomImplicite = Listbox(self.cadreAnalyse,selectmode=SINGLE,height=9,width=25)
        self.lBNomImplicite.grid(row=5, column= 2,padx=(5,5),pady=(0,10));
        self.lBNomSuplementaire = Listbox(self.cadreAnalyse,selectmode=SINGLE,height=9,width=25)
        self.lBNomSuplementaire.grid(row=7, column= 2,pady=(0,10));
        self.lBAdjectifExplicite = Listbox(self.cadreAnalyse,selectmode=SINGLE,height=9,width=25)
        self.lBAdjectifExplicite.grid(row=3, column= 3,pady=(0,10));
        self.lBAjdectifImplicite = Listbox(self.cadreAnalyse,selectmode=SINGLE,height=9,width=25)
        self.lBAjdectifImplicite.grid(row=5, column= 3,padx=(5,5),pady=(0,10));
        self.lBAjdectifSuplementaire = Listbox(self.cadreAnalyse,selectmode=SINGLE,height=9,width=25)
        self.lBAjdectifSuplementaire.grid(row=7, column= 3,pady=(0,10));



        self.cadrecrcExiste=True

    def fermerfenetre(self):
        print("ON FERME la fenetre")
        self.root.destroy()
      
    def NouveauVerbeExplicite(self,evt):  
        self.frameNouveauVerbeExplicite =Toplevel(self.root)
        
        largeurEcran = self.root.winfo_screenwidth()
        hauteurEcran = self.root.winfo_screenheight()
        x = (largeurEcran/2)-(220/2)
        y = (hauteurEcran/2)-(220/2)
        self.frameNouveauVerbeExplicite.geometry("+%d+%d" % (x, y))
        
        self.frameNouveauVerbeExplicite.config(bg="#234078")
        self.lTitre=Label(self.frameNouveauVerbeExplicite, text="Nouveau Verbe Explicite",font= "arial, 20",bg="#234078",fg="white")
        self.lTitre.grid(pady=(5,10),padx=10);
        self.entryNew = Entry(self.frameNouveauVerbeExplicite)
        self.entryNew.grid()
        
        
        self.bAjouter= Button(self.frameNouveauVerbeExplicite, text="Ajouter" ,command=self.AjouterNouveauVerbeExplicite,bg="white", relief=FLAT)
        self.bAjouter.grid(pady=10);     
        
    def NouveauVerbeImplicite(self,evt): 
        self.frameNouveauVerbeImplicite =Toplevel(self.root)
        
        largeurEcran = self.root.winfo_screenwidth()
        hauteurEcran = self.root.winfo_screenheight()
        x = (largeurEcran/2)-(220/2)
        y = (hauteurEcran/2)-(220/2)
        self.frameNouveauVerbeImplicite.geometry("+%d+%d" % (x, y))
         
        self.frameNouveauVerbeImplicite.config(bg="#234078")
        self.lTitre=Label(self.frameNouveauVerbeImplicite, text="Nouveau Verbe Implicite",font= "arial, 20",bg="#234078",fg="white")
        self.lTitre.grid(pady=(5,10),padx=10);
        self.entryNew = Entry(self.frameNouveauVerbeImplicite)
        self.entryNew.grid()
           
        self.bAjouter= Button(self.frameNouveauVerbeImplicite, text="Ajouter" ,command=self.AjouterNouveauVerbeImplicite,bg="white", relief=FLAT)
        self.bAjouter.grid(pady=10);   
        
    def NouveauVerbeSuplementaire(self,evt):  
        self.frameNouveauVerbeSuplementaire =Toplevel(self.root)
        
        largeurEcran = self.root.winfo_screenwidth()
        hauteurEcran = self.root.winfo_screenheight()
        x = (largeurEcran/2)-(220/2)
        y = (hauteurEcran/2)-(220/2)
        self.frameNouveauVerbeImplicite.geometry("+%d+%d" % (x, y))
        
        self.frameNouveauVerbeSuplementaire.config(bg="#234078")
        self.lTitre=Label(self.frameNouveauVerbeSuplementaire, text="Nouveau Verbe supplementaire",font= "arial, 20",bg="#234078",fg="white")
        self.lTitre.grid(pady=(5,10),padx=10);
        self.entryNew = Entry(self.frameNouveauVerbeSuplementaire)
        self.entryNew.grid()
         
        self.bAjouter= Button(self.frameNouveauVerbeSuplementaire, text="Ajouter" ,command=self.AjouterNouveauVerbeSupplementaire,bg="white", relief=FLAT)
        self.bAjouter.grid(pady=10);   
        
    def NouveauNomExplicite(self,evt):  
        self.frameNouveauNomExplicite =Toplevel(self.root)
        
        largeurEcran = self.root.winfo_screenwidth()
        hauteurEcran = self.root.winfo_screenheight()
        x = (largeurEcran/2)-(220/2)
        y = (hauteurEcran/2)-(220/2)
        self.frameNouveauNomExplicite.geometry("+%d+%d" % (x, y))
        
        self.frameNouveauNomExplicite.config(bg="#234078")
        self.lTitre=Label(self.frameNouveauNomExplicite, text="Nouveau nom explicite",font= "arial, 20",bg="#234078",fg="white")
        self.lTitre.grid(pady=(5,10),padx=10);
        self.entryNew = Entry(self.frameNouveauNomExplicite)
        self.entryNew.grid()
         
        self.bAjouter= Button(self.frameNouveauNomExplicite, text="Ajouter" ,command=self.AjouterNouveauNomExplicite,bg="white", relief=FLAT)
        self.bAjouter.grid(pady=10);  
    
    def NouveauNomImplicite(self,evt): 
        self.frameNouveauNomImplicite =Toplevel(self.root)
        
        largeurEcran = self.root.winfo_screenwidth()
        hauteurEcran = self.root.winfo_screenheight()
        x = (largeurEcran/2)-(220/2)
        y = (hauteurEcran/2)-(220/2)
        self.frameNouveauNomImplicite.geometry("+%d+%d" % (x, y))
         
        self.frameNouveauNomImplicite.config(bg="#234078")
        self.lTitre=Label(self.frameNouveauNomImplicite, text="Nouveau Nom Implicite",font= "arial, 20",bg="#234078",fg="white")
        self.lTitre.grid(pady=(5,10),padx=10);
        self.entryNew = Entry(self.frameNouveauNomImplicite)
        self.entryNew.grid()
           
        self.bAjouter= Button(self.frameNouveauNomImplicite, text="Ajouter" ,command=self.AjouterNouveauNomImplicite,bg="white", relief=FLAT)
        self.bAjouter.grid(pady=10); 
     
    def NouveauNomSuplementaire(self,evt):  
        self.frameNouveauNomSuplementaire =Toplevel(self.root)
        
        largeurEcran = self.root.winfo_screenwidth()
        hauteurEcran = self.root.winfo_screenheight()
        x = (largeurEcran/2)-(220/2)
        y = (hauteurEcran/2)-(220/2)
        self.frameNouveauNomSuplementaire.geometry("+%d+%d" % (x, y))
        
        self.frameNouveauNomSuplementaire.config(bg="#234078")
        self.lTitre=Label(self.frameNouveauNomSuplementaire, text="Nouveau Nom supplementaire",font= "arial, 20",bg="#234078",fg="white")
        self.lTitre.grid(pady=(5,10),padx=10);
        self.entryNew = Entry(self.frameNouveauNomSuplementaire)
        self.entryNew.grid()
         
        self.bAjouter= Button(self.frameNouveauNomSuplementaire, text="Ajouter" ,command=self.AjouterNouveauNomSupplementaire,bg="white", relief=FLAT)
        self.bAjouter.grid(pady=10);      
   
    def NouveauAjectifExplicite(self,evt):  
        self.frameNouveauAjectifExplicite =Toplevel(self.root)
        
        largeurEcran = self.root.winfo_screenwidth()
        hauteurEcran = self.root.winfo_screenheight()
        x = (largeurEcran/2)-(220/2)
        y = (hauteurEcran/2)-(220/2)
        self.frameNouveauAjectifExplicite.geometry("+%d+%d" % (x, y))
        
        self.frameNouveauAjectifExplicite.config(bg="#234078")
        self.lTitre=Label(self.frameNouveauAjectifExplicite, text="Nouvelle adjectif explicite",font= "arial, 20",bg="#234078",fg="white")
        self.lTitre.grid(pady=(5,10),padx=10);
        self.entryNew = Entry(self.frameNouveauAjectifExplicite)
        self.entryNew.grid()
         
        self.bAjouter= Button(self.frameNouveauAjectifExplicite, text="Ajouter" ,command=self.AjouterNouveauAdjectifExplicite,bg="white", relief=FLAT)
        self.bAjouter.grid(pady=10);   
       
    def NouveauAjectifImplicite(self,evt):  
        self.frameNouveauAjectifImplicite =Toplevel(self.root)
        
        largeurEcran = self.root.winfo_screenwidth()
        hauteurEcran = self.root.winfo_screenheight()
        x = (largeurEcran/2)-(220/2)
        y = (hauteurEcran/2)-(220/2)
        self.frameNouveauAjectifImplicite.geometry("+%d+%d" % (x, y))
        
        self.frameNouveauAjectifImplicite.config(bg="#234078")
        self.lTitre=Label(self.frameNouveauAjectifImplicite, text="Nouvelle adjectif implicite",font= "arial, 20",bg="#234078",fg="white")
        self.lTitre.grid(pady=(5,10),padx=10);
        self.entryNew = Entry(self.frameNouveauAjectifImplicite)
        self.entryNew.grid()
         
        self.bAjouter= Button(self.frameNouveauAjectifImplicite, text="Ajouter" ,command=self.AjouterNouveauAdjectifImplicite,bg="white", relief=FLAT)
        self.bAjouter.grid(pady=10);  
        
    def NouveauAjectifSupplementaire(self,evt):  
        self.frameNouveauAjectifSupplementaire =Toplevel(self.root)
        
        largeurEcran = self.root.winfo_screenwidth()
        hauteurEcran = self.root.winfo_screenheight()
        x = (largeurEcran/2)-(220/2)
        y = (hauteurEcran/2)-(220/2)
        self.frameNouveauAjectifSupplementaire.geometry("+%d+%d" % (x, y))
        
        self.frameNouveauAjectifSupplementaire.config(bg="#234078")
        self.lTitre=Label(self.frameNouveauAjectifSupplementaire, text="Nouvelle adjectif supplementaire",font= "arial, 20",bg="#234078",fg="white")
        self.lTitre.grid(pady=(5,10),padx=10);
        self.entryNew = Entry(self.frameNouveauAjectifSupplementaire)
        self.entryNew.grid()
         
        self.bAjouter= Button(self.frameNouveauAjectifSupplementaire, text="Ajouter" ,command=self.AjouterNouveauAdjectifSupplementaire,bg="white", relief=FLAT)
        self.bAjouter.grid(pady=10);
        
        
       
       
       
        
    def AjouterNouveauVerbeExplicite(self):  
        self.newInsert=self.entryNew.get();
        self.lBVerbeExplicite.insert(END, self.newInsert)
        self.parent.insertion(1,1,1,"Verbe explicite",self.newInsert)
        self.frameNouveauVerbeExplicite.destroy()
        
    def AjouterNouveauVerbeImplicite(self):  
        self.newInsert=self.entryNew.get();
        self.lBVerbeImplicite.insert(END, self.newInsert)
        self.parent.insertion(1,1,1,"Verbe implicite",self.newInsert)
        self.frameNouveauVerbeImplicite.destroy()
       
    def AjouterNouveauVerbeSupplementaire(self):  
        self.newInsert=self.entryNew.get();
        self.lBVerbeSuplementaire.insert(END, self.newInsert)
        self.parent.insertion(1,1,1,"Verbe supplementaire",self.newInsert)
        self.frameNouveauVerbeSuplementaire.destroy()
        
    def AjouterNouveauNomExplicite(self):  
        self.newInsert=self.entryNew.get();
        self.lBNomExplicite.insert(END, self.newInsert)
        self.parent.insertion(1,1,1,"Nom explicite",self.newInsert)
        self.frameNouveauNomExplicite.destroy()
        
    def AjouterNouveauNomImplicite(self):  
        self.newInsert=self.entryNew.get();
        self.lBNomImplicite.insert(END, self.newInsert)
        self.parent.insertion(1,1,1,"Nom implicite",self.newInsert)
        self.frameNouveauNomImplicite.destroy()
    
    def AjouterNouveauNomSupplementaire(self):  
        self.newInsert=self.entryNew.get();
        self.lBNomSuplementaire.insert(END, self.newInsert)
        self.parent.insertion(1,1,1,"Nom supplementaire",self.newInsert)
        self.frameNouveauNomSuplementaire.destroy()
        
    def AjouterNouveauAdjectifExplicite(self):  
        self.newInsert=self.entryNew.get();
        self.lBAdjectifExplicite.insert(END, self.newInsert)
        self.parent.insertion(1,1,1,"Adjectif explicite",self.newInsert)
        self.frameNouveauAjectifExplicite.destroy()
        
    def AjouterNouveauAdjectifImplicite(self):  
        self.newInsert=self.entryNew.get();
        self.lBAjdectifImplicite.insert(END, self.newInsert)
        self.parent.insertion(1,1,1,"Adjectif implicite",self.newInsert)
        self.frameNouveauAjectifImplicite.destroy()
        
    def AjouterNouveauAdjectifSupplementaire(self):  
        self.newInsert=self.entryNew.get();
        self.lBAjdectifSuplementaire.insert(END, self.newInsert)
        self.parent.insertion(1,1,1,"Adjectif supplementaire",self.newInsert)
        self.frameNouveauAjectifSupplementaire.destroy()
        
        
        
        
    def SupVerbeExplicite(self,evt):  
        a=()
        a=self.lBVerbeExplicite .curselection()
        
        if a==():
            pass
        else:
           self.lBVerbeExplicite.delete(a)
        
    def SupVerbeImplicite(self,evt): 
        a=()
        a=self.lBVerbeImplicite.curselection()
        
        if a==():
            pass
        else:
           self.lBVerbeImplicite .delete(a) 
        
    def SupVerbeSuplementaire(self,evt):  
        a=()
        a=self.lBVerbeSuplementaire .curselection()
        
        if a==():
            pass
        else:
           self.lBVerbeSuplementaire.delete(a)
        
    def SupNomExplicite(self,evt):  
        a=()
        a=self.lBNomExplicite .curselection()
        
        if a==():
            pass
        else:
           self.lBNomExplicite.delete(a)   
    
    def SupNomImplicite(self,evt): 
        a=()
        a=self.lBNomImplicite .curselection()
        
        if a==():
            pass
        else:
           self.lBNomImplicite.delete(a)  
     
    def SupNomSuplementaire(self,evt):  
        a=()
        a=self.lBNomSuplementaire .curselection()
        
        if a==():
            pass
        else:
           self.lBNomSuplementaire.delete(a)      
   
    def SupAjectifExplicite(self,evt):  
        a=()
        a=self.lBAdjectifExplicite .curselection()
        
        if a==():
            pass
        else:
           self.lBAdjectifExplicite.delete(a)  
       
    def SupAjectifImplicite(self,evt):  
        a=()
        a=self.lBAjdectifImplicite .curselection()
        
        if a==():
            pass
        else:
           self.lBAjdectifImplicite.delete(a)
        
    def SupAjectifSupplementaire(self,evt):  
        a=()
        a=self.lBAjdectifSuplementaire .curselection()
        
        if a==():
            pass
        else:
           self.lBAjdectifSuplementaire.delete(a) 