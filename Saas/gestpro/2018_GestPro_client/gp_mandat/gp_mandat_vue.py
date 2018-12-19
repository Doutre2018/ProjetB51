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
    def __init__(self,parent,largeur=900,hauteur=700):
        #Variable de BD
        self.projetName="Projet de Gestion de Projet"
        self.utilisateursEtRole ={"Joé":"Donnée",
                                  "Claudia":"Maquette",
                                  "Ludovic":"Maquette",
                                  "JF":"Rien",
                                  "Simon":"Rien",
                                  "Danick":"Maquette",
                                  "Marylene":"Rien",}
        self.dicodesprint={1:"29 oct. 2018",
                           2:"29 oct. 2018",
                           3:"29 oct. 2018"}
        
        
        self.root=tix.Tk()
        self.root.title(os.path.basename(sys.argv[0]))
        
        self.root.protocol("WM_DELETE_WINDOW", self.fermerfenetre)
        self.root.config(bg="#E4E9F3")
        self.parent=parent
        self.modele=parent.modele
        
        self.largeur=self.largeurDefault=largeur
        self.hauteur=self.hauteurDefault=hauteur
        self.largeurEcran=self.root.winfo_screenwidth()
        self.hauteurEcran=self.root.winfo_screenheight()

        self.cadremandatExiste=False

        self.images={}
        self.cadreactif=None
        self.fullscreen=True
        self.creercadres()
        self.changecadre(self.cadremandat)
        
        self.compteur=1
        
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
        self.creercadremandat()
              
    def creercadremandat(self):
        self.root.overrideredirect(True)
        self.cadremandat=Frame(self.root)
        self.cadremandat.grid()
        


#         self.scroll = Scrollbar(self.root)
#         self.mandatTexte = Text(self.root,bg="#09436B",height=int(self.hauteur/80),foreground="white")
#         self.scroll.grid(row=1,column=3,rowspan=4)
#         self.mandatTexte.grid(row=1,column=3,columnspan=6)
#         self.scroll.config(command=self.mandatTexte.yview)
#         self.mandatTexte.config(yscrollcommand=self.scroll.set)
#         self.mandatTexte.insert(INSERT, "MANDAT :")
#         self.mandatTexte.config(state=DISABLED)

        

        self.labelProjet= Label(self.root,font="-size 30", text=self.projetName,bg="#E4E9F3")
        self.labelProjet.grid(padx=250, pady=(20,10))
        
        
        self.labelSprint= Label(self.root,font="-size 20", text="Sprint",bg="#E4E9F3")
        self.labelSprint.grid(row=2)
        self.listeSprint = Listbox(self.root,width=30, font="-size 16",height=int(self.hauteur/91))
        self.listeSprint.grid(row=3,column=0,rowspan=3,columnspan=3)
        self.boutonAjouterSprint = Button(self.root, text="Ajouter", command=self.ajoutSprint,width=10, relief=FLAT, bg="white")
        self.boutonAjouterSprint.grid(row=11,column=0, pady=10,columnspan=3, padx=(0,200))
        self.boutonSuppSprint = Button(self.root, text="Supprimer",command=self.delete,width=10, relief=FLAT, bg="white")
        self.boutonSuppSprint.grid(row=11,column=0,columnspan=3)
        self.boutonModifierSprint = Button(self.root, text="Modifier", command=self.modifier,width=10, relief=FLAT, bg="white")
        self.boutonModifierSprint.grid(row=11,column=0, pady=10,columnspan=3,padx=(200,0))
        
        for i in self.modele.selectSprint():
            for n in i:
                self.listeSprint.insert(0,n)

        self.textMembre= Label(self.root,font="-size 14",text="Membre",bg="#E4E9F3",width=10)
        self.textMembre.grid(row=15,column=0,columnspan=3, padx=(0,240), pady=(20,0))
        self.textIntermediat =Label(self.root,font="-size 14",text="",bg="#E4E9F3",width=10)
        self.textIntermediat.grid(row=15,column=0,columnspan=3, pady=(20,0))
        self.textOccupation= Label(self.root,font="-size 14",text="Travail sur",bg="#E4E9F3",width=10)
        self.textOccupation.grid(row=15,column=0,columnspan=3, padx=(240,0), pady=(20,0))
#         
        self.listeMembre = Listbox(self.root,width=20, font="-size 16",height=int(self.hauteur/70))
        self.listeMembre.grid(row=17,column=0,rowspan=4,columnspan=3,padx=(0,250)) 
        self.listeOccupation = Listbox(self.root,width=20, font="-size 16",height=int(self.hauteur/70))
        self.listeOccupation.grid(row=17,column=0,rowspan=4,columnspan=3,padx=(250,0))
         
 
        self.boutonAjouterMembre = Button(self.root, text="Ajouter", command=self.AjouterMembre,width=10, relief=FLAT, bg="white")
        self.boutonAjouterMembre.grid(row=22,column=0, pady=10,columnspan=3, padx=(0,200))
        self.boutonSuppMembre =Button(self.root, text="Supprimer",width=10,command=self.SuppMembre, relief=FLAT, bg="white")
        self.boutonSuppMembre.grid(row=22,column=0,columnspan=3)
        self.boutonModifierMembre = Button(self.root, text="Modifier", command=self.ModifMembre,width=10, relief=FLAT, bg="white")
        self.boutonModifierMembre.grid(row=22,column=0, pady=10,columnspan=3,padx=(200,0))


        self.cadremandatExiste=True
        self.root.geometry('%dx%d+%d+%d' % (self.largeurDefault, self.hauteurDefault, (self.largeurEcran/2)-(self.largeurDefault/2),(self.hauteurEcran/2)-320))
    def salutations(self):
        pass
    def fermerfenetre(self):
        print("ON FERME la fenetre")
        self.root.destroy()
        
    def ajoutSprint(self):
        self.nouveauSprint =Toplevel(self.root)
        
        largeurEcran = self.root.winfo_screenwidth()
        hauteurEcran = self.root.winfo_screenheight()
        x = (largeurEcran/2)-(220/2)
        y = (hauteurEcran/2)-(220/2)
        self.nouveauSprint.geometry("+%d+%d" % (x, y))
        
        self.FramenouveauSprint = Frame(self.nouveauSprint,bg="#234078")
        self.FramenouveauSprint.grid()
        self.labeltitre= Label(self.FramenouveauSprint, text="Sprint "+str(self.compteur),font= "arial, 20",bg="#234078", fg="white")
        self.labeltitre.grid(row=1, column=1,columnspan=5,pady=(10,10));
        self.labeldate= Label(self.FramenouveauSprint, text="Date: ",font= "arial, 12",bg="#234078", fg="white")
        self.labeldate.grid(row=2, column=1,padx=(40,0));
        self.jour = Spinbox(self.FramenouveauSprint, width=2, relief=FLAT,from_=1, to=31,buttonuprelief=FLAT)
        self.jour.grid(row=2, column=3);
        self.comboMois= ttk.Combobox(self.FramenouveauSprint,values=[
                                    "Janvier", 
                                    "Février",
                                    "Mars",
                                    "Avril",
                                    "Mai",
                                    "Juin",
                                    "Juillet",
                                    "Aout",
                                    "Septembre",
                                    "Octobre",
                                    "Novembre",
                                    "Décembre"])
        self.comboMois.current(0)
        self.comboMois.grid(row=2, column=4, padx=(0,40))
        
        self.labelJour = Label(self.FramenouveauSprint, text="Jour",font= "arial, 10",bg="#234078", fg="white")
        self.labelJour.grid(row=3, column=3)
        self.labelJour = Label(self.FramenouveauSprint, text="Mois(Lettre)",font= "arial, 10",bg="#234078", fg="white")
        self.labelJour.grid(row=3, column=4,padx=(0,40))
        
        self.boutonOk = Button(self.FramenouveauSprint,text="Ajouter", command = self.insertion,relief=FLAT, bg="white")
        self.boutonOk.grid(row=4, column=1,columnspan=5,pady=10)
       
        
    def insertion(self):
        Date= self.jour.get() +" "+ self.comboMois.get() 
        ligneAjout= "Sprint " + str(self.compteur) +" : "+ Date
        self.listeSprint.insert(END, ligneAjout)
        self.compteur +=1
        self.modele.insertSprint(Date)
        self.nouveauSprint.destroy()
        
    def delete(self):
        a=()
        a=self.listeSprint.curselection()
        
        if a==():
            pass
        else:
            self.listeSprint.delete(a)   
        
        #Supprime la rangée de la BD
        #self.modele.supprimerCarte(nomClasse)
                
       
    
    def modifier(self):
        
        self.SelectionSprint=();
        self.SelectionSprint=self.listeSprint.curselection();
        
        if self.SelectionSprint==():
            pass
        else:
            self.nouveauSprint =Toplevel(self.root)
        
            largeurEcran = self.root.winfo_screenwidth()
            hauteurEcran = self.root.winfo_screenheight()
            x = (largeurEcran/2)-(220/2)
            y = (hauteurEcran/2)-(220/2)
            self.nouveauSprint.geometry("+%d+%d" % (x, y))
            
            self.FrameModifierSprint = Frame(self.nouveauSprint,bg="#234078")
            self.FrameModifierSprint.grid()
            self.labeltitre= Label(self.FrameModifierSprint, text="Sprint ",font= "arial, 20",bg="#234078",fg="white")
            self.labeltitre.grid(row=1, column=1,columnspan=4,pady=(10,10));
            
            self.entryNumeroSprint = Entry(self.FrameModifierSprint, width=3,relief=FLAT)
            self.entryNumeroSprint.grid(row=1, column=4)
            
            
            self.labeldate= Label(self.FrameModifierSprint, text="Date: ",font= "arial, 12",bg="#234078",fg="white")
            self.labeldate.grid(row=2, column=1,padx=(40,0));
            self.jour = Spinbox(self.FrameModifierSprint, width=2, relief=FLAT,from_=1, to=31,buttonuprelief=FLAT)
            self.jour.grid(row=2, column=3);
            self.comboMois= ttk.Combobox(self.FrameModifierSprint,values=[
                                        "Janvier", 
                                        "Février",
                                        "Mars",
                                        "Avril",
                                        "Mai",
                                        "Juin",
                                        "Juillet",
                                        "Aout",
                                        "Septembre",
                                        "Octobre",
                                        "Novembre",
                                        "Décembre"])
            self.comboMois.current(0)
            self.comboMois.grid(row=2, column=4, padx=(0,40))
            
            self.labelJour = Label(self.FrameModifierSprint, text="Jour",font= "arial, 10",bg="#234078",fg="white")
            self.labelJour.grid(row=3, column=3)
            self.labelJour = Label(self.FrameModifierSprint, text="Mois(Lettre)",font= "arial, 10",bg="#234078",fg="white")
            self.labelJour.grid(row=3, column=4,padx=(0,40))
            
    
            
            self.boutonOk = Button(self.FrameModifierSprint,text="Modifier", command = self.modifInsertion,relief=FLAT,bg="white")
            self.boutonOk.grid(row=4, column=1,columnspan=5,pady=10)  
            

        
        
    def modifInsertion(self):
       
        Date= self.jour.get() +" "+ self.comboMois.get() 
        ligneAjout= "Sprint " + self.entryNumeroSprint.get() +" : "+ Date
        
        self.listeSprint.delete(self.SelectionSprint)
        self.listeSprint.insert(self.SelectionSprint, ligneAjout)
        
        self.nouveauSprint.destroy()
        
    def AjouterMembre(self):
        self.nouveauMembre =Toplevel(self.root)
        largeurEcran = self.root.winfo_screenwidth()
        hauteurEcran = self.root.winfo_screenheight()
        x = (largeurEcran/2)-(340/2)
        y = (hauteurEcran/2)-(220/2)
        self.nouveauMembre.geometry("+%d+%d" % (x, y))
        
        self.FrameAjoutMembre = Frame(self.nouveauMembre,bg="#234078")
        self.FrameAjoutMembre.grid()
        
        self.labelMembre = Label(self.FrameAjoutMembre, text="Ajouter un Nouveau Membre",font= "arial, 20",bg="#234078",fg="white")
        self.labelMembre.grid(row=0,column=0,columnspan=3,padx= 25,pady=(20,10))
        
        
        self.labelnom= Label(self.FrameAjoutMembre, text="Nom: ",bg="#234078",fg="white")
        self.labelnom.grid(row=1, column=0,padx=(90,0))
        self.entryNom = Entry(self.FrameAjoutMembre,relief=FLAT)
        self.entryNom.grid(row=1, column=1,padx=(0,75));
        
        self.labelTravailSur= Label(self.FrameAjoutMembre, text="Travail sur: ",bg="#234078",fg="white")
        self.labelTravailSur.grid(row=2, column=0,padx=(90,0))
        self.comboModule = ttk.Combobox(self.FrameAjoutMembre,values=[
                                    "Scrum", 
                                    "Analyse Textuelle",
                                    "Maquette",
                                    "Crc",
                                    "Budget",
                                    "Modélisation de Donné",
                                    "Libre"] , justify=CENTER)
        self.comboModule.current(6)
        self.comboModule.grid(row=2, column=1,padx=(0,75),pady=10)
    
        
        self.boutonAjoutMembre= Button(self.FrameAjoutMembre, text="Ajouter",command=self.InsertionMembre,bg="white",relief=FLAT)
        self.boutonAjoutMembre.grid(row=3,column=0,columnspan=3,pady=10);
        
    def InsertionMembre(self):
        self.listeMembre.insert(END, self.entryNom.get())
        self.listeOccupation.insert(END,self.comboModule.get())
        self.nouveauMembre.destroy()
    def SuppMembre(self):
        a=()
        a=self.listeMembre.curselection()
        b=()
        b=self.listeOccupation.curselection()
        
        if a==():
            self.listeMembre.delete(b)
            self.listeOccupation.delete(b)
        else:
           self.listeMembre.delete(a)
           self.listeOccupation.delete(a) 
            
        
        #Supprime la rangée de la BD
        #self.modele.supprimerCarte(nomClasse)
    def ModifMembre(self):
        
        self.selctionMembre=() #a
        self.selctionMembre=self.listeMembre.curselection()
        self.selctionOccupation=()#b
        self.selctionOccupation=self.listeOccupation.curselection()


        if self.selctionMembre==() and self.selctionOccupation==():
            pass
        else:
            self.nouveauMembre =Toplevel(self.root)
            largeurEcran = self.root.winfo_screenwidth()
            hauteurEcran = self.root.winfo_screenheight()
            x = (largeurEcran/2)-(340/2)
            y = (hauteurEcran/2)-(220/2)
            self.nouveauMembre.geometry("+%d+%d" % (x, y))
            
            self.FrameAjoutMembre = Frame(self.nouveauMembre,bg="#234078")
            self.FrameAjoutMembre.grid()
            
            self.labelMembre = Label(self.FrameAjoutMembre, text="Modifier un membre",font= "arial, 20",bg="#234078",fg="white")
            self.labelMembre.grid(row=0,column=0,columnspan=3,padx= 25,pady=(20,10))
            
            
            self.labelnom= Label(self.FrameAjoutMembre, text="Nom: ",bg="#234078",fg="white")
            self.labelnom.grid(row=1, column=0,padx=(90,0))
            self.entryNom = Entry(self.FrameAjoutMembre)
            self.entryNom.grid(row=1, column=1,padx=(0,75));
           
            self.labelTravailSur= Label(self.FrameAjoutMembre, text="Travail sur: ",bg="#234078",fg="white")
            self.labelTravailSur.grid(row=2, column=0,padx=(90,0))
            self.comboModule = ttk.Combobox(self.FrameAjoutMembre,values=[
                                    "Scrum", 
                                    "Analyse Textuelle",
                                    "Maquette",
                                    "Crc",
                                    "Budget",
                                    "Modélisation de Donné",
                                    "Libre"] , justify=CENTER)
            self.comboModule.current(6)
            self.comboModule.grid(row=2, column=1,padx=(0,75),pady=10)
    
        
            self.boutonAjoutMembre= Button(self.FrameAjoutMembre, text="Modifier",command=self.InsertionModifMembre,bg="white",relief=FLAT)
            self.boutonAjoutMembre.grid(row=3,column=0,columnspan=3,pady=10)
        
            if  self.selctionMembre==():
                self.entryNom.insert(self.selctionOccupation, self.listeMembre.get(self.selctionOccupation))
            else:
                self.entryNom.insert(self.selctionMembre, self.listeMembre.get(self.selctionMembre))
           
                  

        
      
    
    def InsertionModifMembre(self):
        
        if self.selctionMembre==():
            self.listeMembre.delete(self.selctionOccupation)
            self.listeOccupation.delete(self.selctionOccupation)
            self.listeMembre.insert(self.selctionOccupation, self.entryNom.get())
            self.listeOccupation.insert(self.selctionOccupation,self.comboModule.get())
        else: 
            self.listeMembre.delete(self.selctionMembre)
            self.listeOccupation.delete(self.selctionMembre)
            self.listeMembre.insert(self.selctionMembre, self.entryNom.get())
            self.listeOccupation.insert(self.selctionMembre,self.comboModule.get())
            
            

        
        self.nouveauMembre.destroy()
        