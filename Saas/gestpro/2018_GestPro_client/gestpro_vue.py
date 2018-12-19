# -*- coding: utf-8 -*-
from tkinter import *
from tkinter import tix
from tkinter import ttk
#from PIL import Image,ImageDraw, ImageTk
import os,os.path
import math
from helper import Helper as hlp
import signal

class Vue():
    def __init__(self,parent,monip,largeur=800,hauteur=600):

        self.root=tix.Tk()
        self.root.title(os.path.basename(sys.argv[0]))
        self.root.protocol("WM_DELETE_WINDOW", self.fermerfenetre)
        self.root.config(bg="#E4E9F3")
        self.monip=monip
        self.parent=parent
        self.modele=None
        self.nom=None
        self.fullscreen=True
        self.largeur=self.largeurDefault=largeur;
        self.hauteur=self.hauteurDefault=hauteur;
        self.largeurEcran=self.root.winfo_screenwidth()
        self.hauteurEcran=self.root.winfo_screenheight()
        self.savedNameTemp = None
        self.cieName =None

        self.root.attributes("-fullscreen", False)
        self.images={}
        self.modes={}
        self.modecourant=None
        self.cadreactif=None
        self.cadrebaseExiste=False
        self.creermenu()
        self.creercadres()
        self.changecadre(self.cadresplash)
        
        self.listBoutonActif=[]
        self.listBoutonNonActif=[self.boutonMandat,self.boutonScrum,self.boutonAnalyse,self.boutonCasUsage,self.boutonMaquette,self.boutonCrc, self.boutonTchat,self.boutonDonnee, self.boutonTerlow]

        self.placeHolderEntryNom=True
        self.placeHolderEntryMotDePasse=True
        self.placeHolderEntryNomNouveauUtilisateur=True
        self.placeHolderEntryMotDePasseNewUser=True
        self.placeHolderEntryMotDePasseNewUserConfirm=True
        self.placeHolderEntryCompagny=True


        #Bloc pour que la fenetre de connexion sois centré avec l'écran
        x = (self.largeurEcran/2)-(420/2)
        y = (self.hauteurEcran/2)-(500/2)
        self.root.geometry("+%d+%d" % (x, y))
        
    def fullScreenMode(self): 
        if(self.fullscreen):
            self.fullscreen=False
            self.largeur=self.root.winfo_screenwidth()
            self.hauteur=self.root.winfo_screenheight()
            self.root.attributes("-fullscreen", False)
        else:
             self.root.attributes("-fullscreen", True)
             self.largeur=self.largeurDefault
             self.hauteur=self.hauteurDefault
             self.root.attributes("-fullscreen", False)

    def changemode(self,cadre):
        if self.modecourant:
            self.modecourant.grid_forget()
        self.modecourant=cadre
        self.modecourant.grid(fill=BOTH)            

    def changecadre(self,cadre,etend=0):
        if self.cadreactif:
            self.cadreactif.grid_forget()
        self.cadreactif=cadre
        if etend:
            self.cadreactif.grid(fill=BOTH)
        else:
            self.cadreactif.grid()
        if self.cadreactif == self.cadrebase :
            self.root.attributes("-fullscreen", self.fullscreen)


        
    def chargercentral(self,rep):
        for i in rep:
            self.listemodules.insert(END,i)    
        self.changecadre(self.cadrebase)
            
    def popup(self,event):
        self.menu.post(event.x_root, event.y_root)
    
    def hello(self):
        pass
    
    def creercadres(self):
        self.creercadresplash()
        self.connexionProjet()
        self.nouveauProjet()
        self.creercadrebase()
        #self.creercadrecentral()
                
    def creercadresplash(self):
        self.cadresplash=Frame(self.root,bg="#E4E9F3")
        
        self.titre=Label(self.cadresplash, bg="#E5E7F4" , text="Gestionnaire de Projet MAAJM",font='arial 20')
        self.titre.grid(pady=(40,30),padx=20);
        
        self.labelNom=Label(self.cadresplash, bg="#E5E7F4" , text="Entrez votre nom d'utilisateur",font='arial 12')
        self.labelNom.grid()
        self.nomsplash=Entry(self.cadresplash,bg="white", justify=CENTER, fg="grey")
        self.nomsplash.insert(0,'Nom')
        self.nomsplash.grid(pady=(10,10),padx=100)
        self.nomsplash.bind('<FocusIn>', self.clickEntryNom)
        self.nomsplash.bind('<FocusOut>',self.puClickEntryNom)
        
        # Champ texte pour le mot de passe
        
        self.labelmotPassesplash=Label(self.cadresplash, bg="#E5E7F4" , text="Entrez votre mot de passe",font='arial 12')
        self.labelmotPassesplash.grid()
        self.entrymotPassesplash=Entry(self.cadresplash,bg="white", justify=CENTER,fg="grey")
        self.entrymotPassesplash.insert(0,"Mot de passe")
        self.entrymotPassesplash.grid(pady=(10,10),padx=100)
        self.entrymotPassesplash.bind('<FocusIn>', self.clickEntryMotDePasse)
        self.entrymotPassesplash.bind('<FocusOut>',self.puclickEntryMotDePasse)
        
        self.labelCompagnieplash=Label(self.cadresplash, bg="#E5E7F4" , text="Entrez votre nom de compagnie",font='arial 12')
        self.labelCompagnieplash.grid()
        self.entryCompagniesplash=Entry(self.cadresplash,bg="white", justify=CENTER,fg="grey")
        self.entryCompagniesplash.insert(0,"Nom de compagnie")
        self.entryCompagniesplash.grid(pady=(10,10),padx=100)
        self.entryCompagniesplash.bind('<FocusIn>', self.clickEntryCompagnie)
        self.entryCompagniesplash.bind('<FocusOut>',self.puClickEntryCompagnie)
        
        self.labelProbleme=Label(self.cadresplash ,bg="#E5E7F4",fg="#E5E7F4", text="Nom d'utilisateur ou mot de passe erroné",font='arial 1')
        self.labelProbleme.grid()
        
        self.labelIp=Label(self.cadresplash, bg="#E5E7F4" , text="Entrez l'adresse ip de votre serveur",font='arial 12',)
        self.ipsplash=Entry(self.cadresplash,bg="white",justify=CENTER,)
        self.ipsplash.insert(0, self.monip)

        # ------------------------------------                      
        
        self.labelIp.grid()
        self.ipsplash.grid()
        
        self.frameButton= Frame(self.cadresplash,bg="#E5E7F4")
        self.frameButton.grid()
        
        self.btnconnecter=Button(self.frameButton,text="Connexion",bg="#FFFFFF",command=self.chargerProjet,relief=FLAT, width=15)
        self.btnconnecter.grid(row= 5, column= 1,pady=(25,50), padx=(0,10))
        
        self.inscriptionB = Button(self.frameButton,text="Nouveau Client",bg="#FFFFFF",command=self.AllerAInscription,relief=FLAT,width=15)
        self.inscriptionB.grid(row= 5, column= 2,pady=(25,50))
                
        
    def creeNouvelleUtilisateur(self):    
        self.cadreNouvelleUtilisateur=Frame(self.root,bg="#E4E9F3")
        self.titre1=Label(self.cadreNouvelleUtilisateur,text="Creation d'un nouvel",font='arial 20',bg="#E5E7F4")
        self.titre1.grid(row= 0,pady=(40,0),padx=82)
        self.titre2=Label(self.cadreNouvelleUtilisateur,text="utilisateur",font='arial 20',bg="#E5E7F4")
        self.titre2.grid(row= 1,pady=(2,10),padx=72)
        
        #self.EntrerNomTitre= Label(self.cadreNouvelleUtilisateur,text="Veuillez entrer votre nom",font='arial 12',bg="#E5E7F4")
        #self.EntrerNomTitre.grid(pady=(20,10),padx=100) 
        self.NouveauNom= Entry(self.cadreNouvelleUtilisateur,bg="white", justify=CENTER,fg="grey",width=40)
        self.NouveauNom.grid(pady=(0,20))
        self.NouveauNom.insert(0,'Nom d''utilisateur')
        self.NouveauNom.bind('<FocusIn>', self.clickEntryNomNouveauUtilisateur)
        self.NouveauNom.bind('<FocusOut>',self.puClickEntryNomNouveauUtilisateur)
        
        #self.labelNouveauPassword= Label(self.cadreNouvelleUtilisateur,text="Veuillez entrer votre mot de passe",font='arial 12',bg="#E5E7F4")
        #self.labelNouveauPassword.grid()
        self.NouveauPassword= Entry(self.cadreNouvelleUtilisateur,bg="white",justify=CENTER,fg="grey",width=40)       # Champ texte pour le mot de passe
        self.NouveauPassword.insert(0,"Nouveau Mot de passe")
        self.NouveauPassword.grid(pady=(0,20))
        self.NouveauPassword.bind('<FocusIn>', self.clickEntryMotDePasseNewUser)
        self.NouveauPassword.bind('<FocusOut>',self.puClickEntryMotDePasseNewUser)
        
        #self.labelPasswordConfirm= Label(self.cadreNouvelleUtilisateur,text="Veuillez confirmer votre mot de passe",font='arial 12',bg="#E5E7F4")
        #self.labelPasswordConfirm.grid()
        self.PasswordConfirm= Entry(self.cadreNouvelleUtilisateur,bg="white",justify=CENTER,fg="grey",width=40)       # Champ texte pour la confirmation du mot de passe
        self.PasswordConfirm.insert(0,"Confirmer le mot de passe")
        self.PasswordConfirm.grid(pady=(0,20))
        self.PasswordConfirm.bind('<FocusIn>', self.clickEntryMotDePasseNewUserConfirm)
        self.PasswordConfirm.bind('<FocusOut>',self.puclickEntryMotDePasseNewUserConfirm)
        
        self.labelIpServuer=Label(self.cadreNouvelleUtilisateur,text="Veuillez entrer l'adresse de votre serveur",font='arial 12',bg="#E5E7F4")
        self.ipsplash=Entry(self.cadreNouvelleUtilisateur,bg="white",width=40,justify=CENTER)
        self.ipsplash.insert(0, self.monip)
        
        # ------------- DM -------------
        self.labelCompagnieplash=Label(self.cadreNouvelleUtilisateur, bg="#E5E7F4" , text="Entrez votre nom de compagnie",font='arial 12')
        self.labelCompagnieplash.grid()
        self.entryCompagniesplash=Entry(self.cadreNouvelleUtilisateur,bg="white", justify=CENTER,fg="grey")
        self.entryCompagniesplash.insert(0,"Nom de compagnie")
        self.entryCompagniesplash.grid(pady=(10,10),padx=100)
        self.entryCompagniesplash.bind('<FocusIn>', self.clickEntryCompagnie)
        self.entryCompagniesplash.bind('<FocusOut>',self.puClickEntryCompagnie)
        # ------------------------------
        
        self.labelIpServuer.grid()
        self.ipsplash.grid()

        self.confirmerIB=Button(self.cadreNouvelleUtilisateur,text="Confirmer",bg="#FFFFFF",relief=FLAT,command=self.inscription, width=15)
        self.confirmerIB.grid(row= 10, column= 0,pady=(30,35), padx=(0,122))
        
        self.annuleIB=Button(self.cadreNouvelleUtilisateur,text="Annuler",bg="#FFFFFF",relief=FLAT,command=self.retourMenuPrincipal, width=15)
        self.annuleIB.grid(row= 10,pady=(30,35) ,padx=(122,0))
        
    def connexionProjet(self):    
        self.cadreProjet=Frame(self.root,bg="#E4E9F3")
        self.titre1=Label(self.cadreProjet,text="Connexion a un Projet",font='arial 20',bg="#E5E7F4")
        self.titre1.grid(row= 0,pady=(40,0),padx=82)
        
        self.nomProjet= Entry(self.cadreProjet,bg="white", justify=CENTER,fg="grey",width=40)
        self.nomProjet.grid(pady=(0,20))
        self.nomProjet.insert(0,'Nom du Projet')
        self.nomProjet.bind('<FocusIn>', self.clickEntryNomNouveauUtilisateur)
        self.nomProjet.bind('<FocusOut>',self.puClickEntryNomNouveauUtilisateur)
        
        self.labelCompagnieplash=Label(self.cadreProjet, bg="#E5E7F4" , text="Entrez votre nom de compagnie",font='arial 12')
        self.labelCompagnieplash.grid()
        self.entryCompagniesplash=Entry(self.cadreProjet,bg="white", justify=CENTER,fg="grey")
        self.entryCompagniesplash.insert(0,"Nom de compagnie")
        self.entryCompagniesplash.grid(pady=(10,10),padx=100)
        self.entryCompagniesplash.bind('<FocusIn>', self.clickEntryCompagnie)
        self.entryCompagniesplash.bind('<FocusOut>',self.puClickEntryCompagnie)

        self.confirmerIB=Button(self.cadreProjet,text="Confirmer",bg="#FFFFFF",relief=FLAT,command=self.connexion, width=15)
        self.confirmerIB.grid(row= 10, column= 0,pady=(30,35), padx=(0,122))
        
        self.confirmerIB=Button(self.cadreProjet,text="Creer Nouveau Projet",bg="#FFFFFF",relief=FLAT,command=self.AllerANouveauProjet, width=15)
        self.confirmerIB.grid(row= 11,pady=(30,35), padx=(0,122))
        
        self.annuleIB=Button(self.cadreProjet,text="Annuler",bg="#FFFFFF",relief=FLAT,command=self.retourMenuPrincipal, width=15)
        self.annuleIB.grid(row= 10,pady=(30,35) ,padx=(122,0))    
    
    def nouveauProjet(self):    
        self.cadreNouveauProjet=Frame(self.root,bg="#E4E9F3")
        self.titre1=Label(self.cadreNouveauProjet,text="Creation d'un nouveau projet",font='arial 20',bg="#E5E7F4")
        self.titre1.grid(row= 0,pady=(40,0),padx=82)
        
        #self.EntrerNomTitre= Label(self.cadreNouvelleUtilisateur,text="Veuillez entrer votre nom",font='arial 12',bg="#E5E7F4")
        #self.EntrerNomTitre.grid(pady=(20,10),padx=100) 
        self.NouveauNomProjet= Entry(self.cadreNouveauProjet,bg="white", justify=CENTER,fg="grey",width=40)
        self.NouveauNomProjet.grid(pady=(0,20))
        self.NouveauNomProjet.insert(0,'Nom du Projet')
        self.NouveauNomProjet.bind('<FocusIn>', self.clickEntryNomNouveauUtilisateur)
        self.NouveauNomProjet.bind('<FocusOut>',self.puClickEntryNomNouveauUtilisateur)
        

        self.confirmerIB=Button(self.cadreNouveauProjet,text="Confirmer",bg="#FFFFFF",relief=FLAT,command=self.chargerProjet, width=15)
        self.confirmerIB.grid(row= 10, column= 0,pady=(30,35), padx=(0,122))
        
        self.annuleIB=Button(self.cadreNouveauProjet,text="Annuler",bg="#FFFFFF",relief=FLAT,command=self.chargerProjet, width=15)
        self.annuleIB.grid(row= 10,pady=(30,35) ,padx=(122,0))    
    def closeprocess(self):
        self.parent.fermerprocessus()
    
    def creercadrecentral(self):
        self.cadrecentral=Frame(self.root)
        self.canevacentral=Canvas(self.cadrecentral,width=640,height=580,bg="green")
        self.canevacentral.grid()
        
        self.listemodules=Listbox(bg="lightblue",borderwidth=0,relief=FLAT,width=40,height=6)
        self.ipcentral=Entry(bg="pink")
        self.ipcentral.insert(0, self.monip)
        btnconnecter=Button(text="Requerir module",bg="pink",command=self.requetemodule)
        self.canevacentral.create_window(200,100,window=self.listemodules)
        self.canevacentral.create_window(200,450,window=btnconnecter,width=150,height=30)
        
        btnquitproc=Button(text="Fermer dernier module",bg="red",command=self.closeprocess)
        self.canevacentral.create_window(200,500,window=btnquitproc,width=200,height=30)
        
    def creermenu(self):
        
        self.menubar = Menu(self.root)

        self.filemenu = Menu(self.menubar, tearoff=0)
        
        self.filemenu = Menu(self.menubar, tearoff=0)
        self.filemenu.add_command(label="Nouveau Projet", command=self.nouveauProjet)
        self.filemenu.add_command(label="Enregistrer", command=self.salutations)
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
        
        self.menubar.add_command(label="Fermer", command=self.fermerfenetre)
        self.menu = Menu(self.root, tearoff=0)
        self.menu.add_command(label="Nom", command=self.salutations)
        self.menu.add_command(label="Verbe", command=self.salutations)
        
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
       
    def creercadrebase(self):
        self.listemodules=Listbox(bg="lightblue",borderwidth=0,relief=FLAT,width=40,height=6)
        self.largeur=self.largeurEcran
        self.hauteur=self.hauteurEcran
        
        self.cadrebase=Frame(self.root, bg= "#E4E9F3")
        
        self.boutonMandat=Button(self.cadrebase,text="Mandat",bg="#234078",command=self.requeteMandat,height=4,width=int(self.largeur/65),relief=FLAT, fg="white")
        self.boutonScrum=Button(self.cadrebase,text="Scrum",bg="#234078",command=self.requeteScrum,height=4,width=int(self.largeur/65),relief=FLAT, fg="white")
        self.boutonAnalyse=Button(self.cadrebase,text="Analyse \nTextuelle",bg="#234078",command=self.requeteAnalyse,height=4,width=int(self.largeur/65),relief=FLAT, fg="white")
        self.boutonCasUsage=Button(self.cadrebase,text="Cas \nd'usage",bg="#234078",command=self.requeteCasUsage,height=4,width=int(self.largeur/65),relief=FLAT, fg="white")
        self.boutonMaquette=Button(self.cadrebase,text="Maquette",bg="#234078",command=self.requeteMaquette,height=4,width=int(self.largeur/65),relief=FLAT, fg="white")
        self.boutonCrc=Button(self.cadrebase,text="CRC",bg="#234078",command=self.requeteCrc,height=4,width=int(self.largeur/65),relief=FLAT, fg="white")
        #self.boutonBudget=Button(self.cadrebase,text="Marketing",bg="#234078",command=self.requeteBudget,height=4,width=int(self.largeur/72),relief=FLAT, fg="white")
        self.boutonTchat=Button(self.cadrebase,text="Tchat",bg="#234078",command=self.requeteTchat,height=4,width=int(self.largeur/65),relief=FLAT, fg="white")
        self.boutonDonnee=Button(self.cadrebase,text="Modelisation \nde donnee",bg="#234078",command=self.requeteModelisation,height=4,width=int(self.largeur/65),relief=FLAT, fg="white")
        self.boutonTerlow=Button(self.cadrebase,text="Terlow",bg="#234078",command=self.requeteTerlow,height=4,width=int(self.largeur/65),relief=FLAT, fg="white")

        self.boutonMandat.grid(row=0,column=1 ,padx=(0,2))
        self.boutonScrum.grid(row=0,column=2 ,padx=(0,2))
        self.boutonAnalyse.grid(row=0,column=3 ,padx=(0,2))
        self.boutonCasUsage.grid(row=0,column=4 ,padx=(0,2))
        self.boutonMaquette.grid(row=0,column=5 ,padx=(0,2))
        self.boutonCrc.grid(row=0,column=6 ,padx=(0,2))
       # self.boutonBudget.grid(row=0,column=7 ,padx=(0,2))
        self.boutonTchat.grid(row=0,column=8 ,padx=(0,2))
        self.boutonDonnee.grid(row=0,column=9 ,padx=(0,2))
        self.boutonTerlow.grid(row=0,column=10)
        
    def requeteMandat(self):
        self.ChangerCouleurBouton(self.boutonMandat)
        if(self.parent.pid):
            self.parent.fermerprocessus()

        self.requetemodule("mandat")
    def requeteScrum(self):
        self.ChangerCouleurBouton(self.boutonScrum)
        
        if(self.parent.pid):
            self.parent.fermerprocessus()
        self.requetemodule("scrum")  
    def requeteAnalyse(self):
        self.ChangerCouleurBouton(self.boutonAnalyse)
        
        if(self.parent.pid):
            self.parent.fermerprocessus()
        self.requetemodule("analyse")  
    def requeteCasUsage(self):
        self.ChangerCouleurBouton(self.boutonCasUsage)
        
        if(self.parent.pid):
            self.parent.fermerprocessus()
        self.requetemodule("casdusage")  
    def requeteMaquette(self):
        self.ChangerCouleurBouton(self.boutonMaquette)
        if(self.parent.pid):
            self.parent.fermerprocessus()
        self.requetemodule("maquette")  
    def requeteCrc(self):
        self.ChangerCouleurBouton(self.boutonCrc)
        if(self.parent.pid):
            self.parent.fermerprocessus()
        self.requetemodule("crc")  
    def requeteBudget(self):
        self.ChangerCouleurBouton(self.boutonBudget)
        if(self.parent.pid):
            self.parent.fermerprocessus()
        self.requetemodule("budget")  
    def requeteTchat(self):
        self.ChangerCouleurBouton(self.boutonTchat)
        if(self.parent.pid):
            self.parent.fermerprocessus()
        self.requetemodule("tchat")  
    def requeteModelisation(self):
        self.ChangerCouleurBouton(self.boutonDonnee)
        if(self.parent.pid):
            self.parent.fermerprocessus()
        self.requetemodule("modelisation")  
    def requeteTerlow(self):
        self.ChangerCouleurBouton(self.boutonTerlow)
        if(self.parent.pid):
            self.parent.fermerprocessus()
        self.requetemodule("terlow")  
            
    def requetemodule(self,mod):
        #mod=self.listemodules.selection_get()
        if mod:
            self.parent.requetemodule(mod)
                
    def fermerfenetre(self):
        # Ici, on pourrait mettre des actions a faire avant de fermer (sauvegarder, avertir etc)
        
        self.root.quit
        self.parent.fermefenetre()
        self.parent.fermerprocessus()
    
    def salutations(self):
        print("hello")
        
    # ---------------DM----------------- #
    def fetchCompagnies(self):
        ipserveur = self.ipsplash.get()
        return self.parent.fetchCompagnies(ipserveur)
            
    def inscription(self):
        nom = self.NouveauNom.get()                 # Nom d'utilisateur à inscrire
        motPasse = self.NouveauPassword.get()       # Mot de passe de l'utilisateur à inscrire
        mpConfirm = self.PasswordConfirm.get()      # 2e mot de passe; pour confirmation
        compagnie = self.entryCompagniesplash.get()      # Nom de la compagnie lié à l'utilisateur
        ipserveur = self.ipsplash.get()             # Addresse ip de l'utilisateur
        
        if motPasse=="Nouveau Mot de passe":
            motPasse=""
        if mpConfirm=="Confirmer le mot de passe":
            mpConfirm=""
        if compagnie == "Nom de compagnie":
            compagnie=""
        
        if self.nomConforme(nom):                   # Vérifie que le nom d'utilisateur désiré est conforme
            if self.motPasseConforme(motPasse):     # Vérifie que le mot de passe de l'utilisateur est conforme
                if motPasse == mpConfirm:           # Confirme le mot de passe désiré
                    if compagnie != "" :
                        rep = self.parent.inscription(nom, motPasse, compagnie, ipserveur)
                        print(rep)
                        self.retourMenuPrincipal()
                        
                    else:
                        self.entryCompagniesplash.delete(0, "end")
                        self.entryCompagniesplash.config(fg="red")
                        self.entryCompagniesplash.insert(0,"Le nom n'est pas comforme")
                        self.placeHolderEntryNomNouveauUtilisateur=True
                        self.confirmerIB.focus()
                        print("Nom d'utilisateur non conforme")
                    
                else:
                    self.PasswordConfirm.delete(0, "end")
                    self.PasswordConfirm.config(fg="red",show="")
                    self.PasswordConfirm.insert(0,"Mots de passe non identiques")
                    self.placeHolderEntryMotDePasseNewUserConfirm=True
                    self.confirmerIB.focus()
                    print("Mots de passe non identiques")
            else:
                self.NouveauPassword.delete(0, "end")
                self.NouveauPassword.config(fg="red",show="")
                self.NouveauPassword.insert(0,"Mot de passe non conforme")
                self.placeHolderEntryMotDePasseNewUser=True
                self.confirmerIB.focus()
                print("Mot de passe non conforme")
        else:
            self.NouveauNom.delete(0, "end")
            self.NouveauNom.config(fg="red")
            self.NouveauNom.insert(0,"Le nom n'est pas comforme")
            self.placeHolderEntryNomNouveauUtilisateur=True
            self.confirmerIB.focus()
            print("Nom d'utilisateur non conforme")
            
    def connexion(self):
        nom = self.nomsplash.get()
        motPasse = self.entrymotPassesplash.get()
        compagnie = self.entryCompagniesplash.get()
        ipserveur = self.ipsplash.get()
        
        if self.nomConforme(nom):
            if self.motPasseConforme(motPasse):
                if compagnie != "< Sélectionner votre entreprise >":
                    rep = self.parent.connexion(nom, motPasse, compagnie, ipserveur)
                    self.labelProbleme.config(fg="red",font='arial 9')
                    print(rep)
                    
                else:
                    print("Choisir une compagnie s.v.p.")
            else:
                print("Mot de passe non conforme")
        else:
            print("Nom d'utilisateur non conforme")
    
       
    def nomConforme(self, nom):             # Vérifie que le nom d'utilisateur est conforme (regex)
        if len(nom) > 12:                   # Si le nom a plus de 12 caractères
            return False
        else:
            pattern = "\w+"                 # A-Z, a-z, 0-9 et _ au moins une fois
            if (re.match(pattern, nom)):    # Compare le nom transmis au pattern
                return True
            else:
                return False
            
    def motPasseConforme(self, password):       # Vérifie que le mot de passe de l'utilisateur est conforme (regex)
        if len(password) < 8:                   # Si le mot de passe a moins de 8 caractères
            return False
        else:
            pattern = "\w+"                     # A-Z, a-z, 0-9 et _ au moins une fois
            if (re.match(pattern, password)):   # Compare le mot de passe transmi au pattern
                return True
            else:
                return False
    # --------------------------------- #   
    def chargerProjet(self):

        self.cieName = self.entryCompagniesplash.get()
        self.savedNameTemp = self.NouveauNomProjet.get()
        print("ds charger" + self.savedNameTemp, self.cieName)
        self.changecadre(self.cadreProjet)
        if self.parent.modProjet.createProject(self, self.savedNameTemp, self.nomsplash.get(), self.cieName):
            pass
        else:
            print("Erreur de creation de nom de projet (nom déjà utilisé")

        #C'est ici qu'il faut vérifé
        
        nom = self.nomsplash.get()
        motPasse = self.entrymotPassesplash.get()
        compagnie = self.entryCompagniesplash.get()
        ipserveur = self.ipsplash.get()
        
        if self.nomConforme(nom):
            if self.motPasseConforme(motPasse):
                if self.parent.modProjet.createProject(self, self.savedNameTemp, self.nomsplash.get(), self.cieName):
                    self.changecadre(self.cadreProjet)
                else:
                    print("Erreur de creation de nom de projet (nom déjà utilisé")
            else:
                print("Mot de passe non conforme")
        else:
            print("Nom d'utilisateur non conforme")
            
#        if nomestConforme:
#             if MotdepasseConforme:
#                 self.changecadre(self.cadreProjet) #Si tout ca alors il  va aller dans la prochaine étape qui est de faire afficher la connexion projet
#             else:
#                 pass
#                 
#         else:
#             pass
        
        
    def AllerAInscription(self):
        self.creeNouvelleUtilisateur()
        self.changecadre(self.cadreNouvelleUtilisateur)
    def AllerANouveauProjet(self):
        self.changecadre(self.cadreNouveauProjet)
    def retourMenuPrincipal(self):
        self.changecadre(self.cadresplash)
    
    def ChangerCouleurBouton(self, bouton):
        #Je vide la liste des bouton actif  pour les mettre dans bouton non actif      
        for b in self.listBoutonActif:
            self.listBoutonNonActif.append(b)
            self.listBoutonActif.remove(b)
            
        #J'ajoute le bouton cliquer au bouton actif et le retire de bouton non actif
        self.listBoutonActif.append(bouton)
        self.listBoutonNonActif.remove(bouton)
        
        #Je met le bouton actif d'une autre couleur et remet les bouton non actif de la bonne couleur
        for  b in self.listBoutonActif:
            b.config(bg="#FFC14C" ,fg="black")
        for b in self.listBoutonNonActif:
            b.config(bg="#234078",fg="white")  
    
    def clickEntryNom(self,evt):
        if self.placeHolderEntryNom:
            self.nomsplash.delete(0, "end")
            self.nomsplash.config(fg="black")
            self.placeHolderEntryNom=False
    
    def puClickEntryNom(self,evt):
        if  self.nomsplash.get() == '':
            self.nomsplash.insert(0, "Nom d''utilisateur")
            self.nomsplash.config(fg = "grey")
            self.placeHolderEntryNom=True
            
    def clickEntryMotDePasse(self,evt):
        if self.placeHolderEntryMotDePasse:
            self.entrymotPassesplash.delete(0, "end")
            self.entrymotPassesplash.config(fg="black",show="*")
            self.placeHolderEntryMotDePasse=False    
            
    def puclickEntryMotDePasse(self,evt):
        if  self.entrymotPassesplash.get() == '':
            self.entrymotPassesplash.insert(0, "Mot de passe")
            self.entrymotPassesplash.config(fg = "grey",show="")
            self.placeHolderEntryMotDePasse=True
            
    def clickEntryNomNouveauUtilisateur(self,evt):
        if self.placeHolderEntryNomNouveauUtilisateur:
            self.NouveauNom.delete(0, "end")
            self.NouveauNom.config(fg="black")
            self.placeHolderEntryNomNouveauUtilisateur=False
    
    def puClickEntryNomNouveauUtilisateur(self,evt):
        if  self.NouveauNom.get() == '':
            self.NouveauNom.insert(0, "Nom d''utilisateur")
            self.NouveauNom.config(fg = "grey")
            self.placeHolderEntryNomNouveauUtilisateur=True
            
    def clickEntryMotDePasseNewUser(self,evt):
        if self.placeHolderEntryMotDePasseNewUser:
            self.NouveauPassword.delete(0, "end")
            self.NouveauPassword.config(fg="black",show="*")
            self.placeHolderEntryMotDePasseNewUser=False    
            
    def puClickEntryMotDePasseNewUser(self,evt):
        if  self.NouveauPassword.get() == '':
            self.NouveauPassword.insert(0, "Nouveau Mot de passe")
            self.NouveauPassword.config(fg = "grey",show="")
            self.placeHolderEntryMotDePasseNewUser=True
            
    def clickEntryMotDePasseNewUserConfirm(self,evt):
        if self.placeHolderEntryMotDePasseNewUserConfirm:
            self.PasswordConfirm.delete(0, "end")
            self.PasswordConfirm.config(fg="black")
            self.placeHolderEntryMotDePasseNewUserConfirm=False    
            
    def puclickEntryMotDePasseNewUserConfirm(self,evt):
        if  self.PasswordConfirm.get() == '':
            self.PasswordConfirm.insert(0, "Confirmer le mot de passe")
            self.PasswordConfirm.config(fg = "grey",show="")
            self.placeHolderEntryMotDePasseNewUserConfirm=True
            
    def clickEntryCompagnie(self,evt):
        if self.placeHolderEntryCompagny:
            self.entryCompagniesplash.delete(0, "end")
            self.entryCompagniesplash.config(fg="black",show="*")
            self.placeHolderEntryCompagny=False    
            
    def puClickEntryCompagnie(self,evt):
        if  self.entryCompagniesplash.get() == '':
            self.entryCompagniesplash.insert(0, "Nom de compagnie")
            self.entryCompagniesplash.config(fg = "grey",show="")
            self.placeHolderEntryCompagny=True
    
if __name__ == '__main__':
    m=Vue(0,"127.0.0.1")
    m.root.mainloop()
    
