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
    def __init__(self,parent,largeur=800,hauteur=600):
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
        self.root.attributes("-fullscreen", True)
        self.root.protocol("WM_DELETE_WINDOW", self.fermerfenetre)
        self.parent=parent
        self.modele=None
        self.largeurDefault=largeur/7
        self.hauteurDefault=hauteur/4.5
        self.largeur=self.root.winfo_screenwidth()/7
        self.hauteur=self.root.winfo_screenmmheight()/4.5
        self.cadrebaseExiste=False
        self.images={}
        self.cadreactif=None
        self.fullscreen=True
        self.creermenu()
        self.creercadres()
        self.changecadre(self.cadrebase)
        
    def changemode(self,cadre):
        if self.modecourant:
            self.modecourant.pack_forget()
        self.modecourant=cadre
        self.modecourant.pack(expand=1,fill=BOTH)            

    def changecadre(self,cadre,etend=0):
        if self.cadreactif:
            self.cadreactif.grid_forget()
        self.cadreactif=cadre
        if etend:
            self.cadreactif.grid(expand=1,fill=BOTH)
        else:
            self.cadreactif.grid()
    
        
    def creercadres(self):
        self.creercadrebase()
        #self.cadrejeu=Frame(self.root,bg="blue")
        #self.modecourant=None
        
    def requetemodule(self,mod):
        rep=self.serveur.requetemodule(mod)
        if rep:
            print(rep[0])
            cwd=os.getcwd()
            lieuApp="/gp_"+rep[0]
            lieu=cwd+lieuApp
            print(lieu)
            if not os.path.exists(lieu):
                os.mkdir(lieu) #plante s'il exist deja
            reso=rep[1]
            print(rep[1])
            for i in rep[2]:
                if i[0]=="fichier":
                    nom=reso+i[1]
                    rep=self.serveur.requetefichier(nom)
                    fiche=open(lieu+"/"+i[1],"wb")
                    fiche.write(rep.data)
                    fiche.close()
            chaineappli="."+lieuApp+lieuApp+".py"

            self.pid = Popen([sys.executable, chaineappli,self.monnom,self.monip,self.nodeport],shell=0) 
        else:
            print("RIEN") 
            
    def creermenu(self):

        self.menubar = Menu(self.root)

        self.filemenu = Menu(self.menubar, tearoff=0)
        
        self.filemenu = Menu(self.menubar, tearoff=0)
        self.filemenu.add_command(label="Nouveau Projet", command=self.salutations)
        self.filemenu.add_command(label="Ouvrir", command=self.salutations)
        self.filemenu.add_command(label="Enregistrer", command=self.salutations)
        self.filemenu.add_command(label="Enregistrer sous ...", command=self.salutations)
        self.filemenu.add_separator()
        self.filemenu.add_command(label="Fermer", command=self.root.quit)
        self.menubar.add_cascade(label="Fichier", menu=self.filemenu)
        
        self.editmenu = Menu(self.menubar, tearoff=0)
        self.editmenu.add_command(label="Undo", command=self.salutations)
        self.editmenu.add_command(label="Redo", command=self.salutations)
        self.editmenu.add_separator()
        self.editmenu.add_command(label="Copier", command=self.salutations)
        self.editmenu.add_command(label="Couper", command=self.salutations)
        self.editmenu.add_command(label="Coller", command=self.salutations)
        self.menubar.add_cascade(label="Edition", menu=self.editmenu)
        
        self.aidemenu = Menu(self.menubar, tearoff=0)
        self.aidemenu.add_command(label="Read-Me 1", command=self.salutations)
        self.aidemenu.add_command(label="Read-Me 2", command=self.salutations)
        self.aidemenu.add_command(label="Read-Me 3", command=self.salutations)
        self.aidemenu.add_command(label="Read-Me 4", command=self.salutations)
        self.aidemenu.add_command(label="Read-Me 5", command=self.salutations)
        self.menubar.add_cascade(label="Aide", menu=self.aidemenu)
        
        self.affichagemenu = Menu(self.menubar, tearoff=0)
        self.affichagemenu.add_command(label="FullScreen", command=self.fullScreenMode)
        self.menubar.add_cascade(label="Affichage", menu=self.affichagemenu)
        
        self.menubar.add_command(label="Fermer", command=self.root.quit)
        self.menu = Menu(self.root, tearoff=0)
        self.menu.add_command(label="Nom", command=self.salutations)
        self.menu.add_command(label="Verbe", command=self.salutations)
        
        #self.frame = Frame(self.root, width=512, height=512)
        #self.frame.pack()
        #self.frame.bind("<Button-3>", self.popup)
        self.root.config(menu=self.menubar) 
    def fullScreenMode(self): 
        if(self.fullscreen):
            self.fullscreen=False
            self.largeur=self.largeurDefault
            self.hauteur=self.hauteurDefault
            self.root.attributes("-fullscreen", False)
            self.creercadres()
            self.changecadre(self.cadrebase)
        else:
             self.fullscreen=True
             self.largeur=self.root.winfo_screenwidth()/7
             self.hauteur=self.root.winfo_screenmmheight()/4.5
             self.root.attributes("-fullscreen", True)
             self.creercadres()
             self.changecadre(self.cadrebase)
    def destroyCadreBase(self):
        self.cadrebase.destroy()
        self.boutonAnalyse.destroy()
        self.affichagemenu.destroy()
        self.boutonBudget.destroy()
        self.boutonCasUsage.destroy()
        self.boutonCrc.destroy()
        self.boutonDonnee.destroy()
        self.boutonMandat.destroy()
        self.boutonMaquette.destroy()
        self.boutonProjet1.destroy()
        self.boutonProjet2.destroy()                        
        self.boutonProjet3.destroy()
        self.boutonScrum.destroy()
        self.boutonTchat.destroy()
        self.boutonTerlow.destroy()                      
              
    def creercadrebase(self):
        
        if(self.cadrebaseExiste):
            destroyCadreBase()
        self.cadrebase=Frame(self.root)
        self.boutonProjet1=Button(text="Projet 1",bg="#00BCD9",command=None,height=int(self.hauteur/3),width=int(self.largeur/11))
        self.boutonProjet2=Button(text="Projet 2",bg="#00BCD9",command=None,height=int(self.hauteur/3),width=int(self.largeur/11))
        self.boutonProjet3=Button(text="Projet 3",bg="#00BCD9",command=None,height=int(self.hauteur/3),width=int(self.largeur/11))

        self.boutonMandat=Button(text="Mandat",bg="#0B416C",command=None,height=4,width=int(self.largeur/11))
        self.boutonScrum=Button(text="Scrum",bg="#0072BB",command=None,height=4,width=int(self.largeur/11))
        self.boutonAnalyse=Button(text="Analyse \nTextuelle",bg="#2AABE2",command=None,height=4,width=int(self.largeur/11))
        self.boutonCasUsage=Button(text="Cas \nd'usage",bg="#01A89E",command=None,height=4,width=int(self.largeur/11))
        self.boutonMaquette=Button(text="Maquette",bg="#22B473",command=None,height=4,width=10)
        self.boutonCrc=Button(text="CRC",bg="#38B64A",command=None,height=4,width=int(self.largeur/11))
        self.boutonBudget=Button(text="Budget",bg="#8CC83E",command=None,height=4,width=int(self.largeur/11))
        self.boutonTchat=Button(text="Tchat",bg="#DAE121",command=None,height=4,width=int(self.largeur/11))
        self.boutonDonnee=Button(text="Modelisation \nde donnee",bg="#FAEF20",command=None,height=4,width=int(self.largeur/11))
        self.boutonTerlow=Button(text="Terlow",bg="#FFB242",command=None,height=4,width=int(self.largeur/11))
        
        self.boutonProjet1.grid(row=1,column=0,rowspan=5)
        self.boutonProjet2.grid(row=6,column=0,rowspan=5)
        self.boutonProjet3.grid(row=11,column=0,rowspan=5)

        self.boutonMandat.grid(row=0,column=1)
        self.boutonScrum.grid(row=0,column=2)
        self.boutonAnalyse.grid(row=0,column=3)
        self.boutonCasUsage.grid(row=0,column=4)
        self.boutonMaquette.grid(row=0,column=5)
        self.boutonCrc.grid(row=0,column=6)
        self.boutonBudget.grid(row=0,column=7)
        self.boutonTchat.grid(row=0,column=8)
        self.boutonDonnee.grid(row=0,column=9)
        self.boutonTerlow.grid(row=0,column=10)
        

        self.scroll = Scrollbar(self.root)
        self.mandatTexte = Text(self.root,bg="#09436B",height=int(self.hauteur/4),foreground="white")
        self.scroll.grid(row=1,column=3,rowspan=4)
        self.mandatTexte.grid(row=1,column=3,columnspan=6)
        self.scroll.config(command=self.mandatTexte.yview)
        self.mandatTexte.config(yscrollcommand=self.scroll.set)
        self.mandatTexte.insert(INSERT, "MANDAT :")
        self.mandatTexte.config(state=DISABLED)

        #self.fontTitle = tkFont.Font(family="Helvetica",size=36,weight="bold")
        self.projetTexte = Entry(self.root,foreground="black",font="-size 34", width=32,background="#526EFF",justify='center')
        self.projetTexte.grid(row=5,column=2,columnspan=8)
        self.projetTexte.insert(INSERT, self.projetName)
        self.projetTexte.config(state=DISABLED)
        
        self.listeSprint = Listbox(self.root,width=30, font="-size 16",height=int(self.hauteur/6))
        self.listeSprint.grid(row=6,column=4,rowspan=4,columnspan=4)
        for sprint in self.dicodesprint.keys():
                 self.listeSprint.insert(END,"Sprint " + str(sprint) + "................."+self.dicodesprint[sprint])
        
        
        self.listeTexte = Entry(self.root,foreground="black", font="-size 16",width=80,background="#526EFF",justify='center')
        self.listeTexte.grid(row=10,column=2,columnspan=8)
        self.listeTexte.insert(INSERT, "Membre \t\t\t\t Travail sur")
        self.listeTexte.config(state=DISABLED)
        
        self.listeMembre = Listbox(self.root,width=30, font="-size 16",height=int(self.hauteur/5))
        self.listeMembre.grid(row=11,column=3,rowspan=5,columnspan=4)
        for membre in self.utilisateursEtRole.keys():
                 self.listeMembre.insert(END,membre )
        self.listeOccupation = Listbox(self.root,width=30, font="-size 16",height=int(self.hauteur/5))
        self.listeOccupation.grid(row=11,column=6,rowspan=5,columnspan=4)
        for membre in self.utilisateursEtRole.keys():
                 self.listeOccupation.insert(END,self.utilisateursEtRole[membre])
        self.cadrebaseExiste=True
    def accesScrum(self):
        ad="http://"+ipserveur+":"+self.nodeport
        self.serveur=ServerProxy(ad)
        mod = self.serveur.requetemodule()
        self.requetemodule(mod)    
    def salutations(self):
        pass
    def fermerfenetre(self):
        print("ON FERME la fenetre")
        self.root.destroy()
    