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
        self.monip=monip
        self.parent=parent
        self.modele=None
        self.nom=None
        self.fullscreen=True
        self.largeurDefault=largeur;
        self.hauteurDefault=hauteur;
        if self.fullscreen :
            self.largeur=self.root.winfo_screenwidth()
            self.hauteur=self.root.winfo_screenheight()
            
        else:
            self.largeur=self.largeurDefault
            self.hauteur=self.hauteurDefault

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
        self.listBoutonNonActif=[self.boutonMandat,self.boutonScrum,self.boutonAnalyse,self.boutonCasUsage,self.boutonMaquette,self.boutonCrc, self.boutonBudget,self.boutonTchat,self.boutonDonnee, self.boutonTerlow]

        self.placeHolderEntryNom=True;


        #Bloc pour que la fenetre de connexion sois centré avec l'écran
        largeurEcran = self.root.winfo_screenwidth()
        hauteurEcran = self.root.winfo_screenheight()
        x = (largeurEcran/2)-(420/2)
        y = (hauteurEcran/2)-(500/2)
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
        
        self.creeNouvelleUtilisateur()
        self.creercadrebase()
        #self.creercadrecentral()
                
    def creercadresplash(self):
        self.cadresplash=Frame(self.root,bg="#E4E9F3")
        
        self.titre=Label(self.cadresplash, bg="#E5E7F4" , text="Gestionnaire de Projet MAAJM",font='arial 20')
        self.titre.grid(pady=(40,30),padx=20);
        
        self.labelNom=Label(self.cadresplash, bg="#E5E7F4" , text="Entrez votre nom d'utilisateur",font='arial 12')
        self.labelNom.grid()
        self.nomsplash=Entry(self.cadresplash,bg="white", justify=CENTER, fg="grey")
        self.nomsplash.insert(0,'Entrez votre nom')
        self.nomsplash.grid(pady=(10,10),padx=100)
        self.nomsplash.bind('<FocusIn>', self.clickEntryNom)
        self.nomsplash.bind('<FocusOut>',self.puClickEntryNom)
        
        # Champ texte pour le mot de passe
        
        self.labelmotPassesplash=Label(self.cadresplash, bg="#E5E7F4" , text="Entrez votre mot de passe",font='arial 12')
        self.labelmotPassesplash.grid()
        self.entrymotPassesplash=Entry(self.cadresplash,bg="white", justify=CENTER,)
        self.entrymotPassesplash.insert(0,"")
        self.entrymotPassesplash.grid(pady=(10,10),padx=100)
        
        
        self.labelIp=Label(self.cadresplash, bg="#E5E7F4" , text="Entrez l'adresse ip de votre serveur",font='arial 12',)
        self.labelIp.grid()
        self.ipsplash=Entry(self.cadresplash,bg="white",justify=CENTER,)
        self.ipsplash.insert(0, self.monip)
        self.ipsplash.grid()
                
        self.frameButton= Frame(self.cadresplash,bg="#E5E7F4")
        self.frameButton.grid()
        
        self.btnconnecter=Button(self.frameButton,text="Connexion",bg="#FFFFFF",command=self.connexion,relief=FLAT, width=15)
        self.btnconnecter.grid(row= 5, column= 1,pady=(25,50), padx=(0,10))
        
        self.inscriptionB = Button(self.frameButton,text="Nouveau Client",bg="#FFFFFF",command=self.AllerAInscription,relief=FLAT,width=15)
        self.inscriptionB.grid(row= 5, column= 2,pady=(25,50))
                
        
    def creeNouvelleUtilisateur(self):    
        self.cadreNouvelleUtilisateur=Frame(self.root,bg="#E4E9F3")
        self.titre1=Label(self.cadreNouvelleUtilisateur,text="Creation d'un nouvelle",font='arial 20',bg="#E5E7F4")
        self.titre1.grid(row= 0,pady=(40,0),padx=72)
        self.titre2=Label(self.cadreNouvelleUtilisateur,text="utilisateur",font='arial 20',bg="#E5E7F4")
        self.titre2.grid(row= 1,pady=(2,10),padx=72)
        
        self.EntrerNomTitre= Label(self.cadreNouvelleUtilisateur,text="Veuillez entrer votre nom",font='arial 12',bg="#E5E7F4")
        self.EntrerNomTitre.grid(pady=(20,10),padx=100)
        
        self.NouveauNom= Entry(self.cadreNouvelleUtilisateur,bg="white")
        self.NouveauNom.grid(pady=(0,20))
        
        self.labelNouveauPassword= Label(self.cadreNouvelleUtilisateur,text="Veuillez entrer votre mot de passe",font='arial 12',bg="#E5E7F4")
        self.labelNouveauPassword.grid()
        self.NouveauPassword= Entry(self.cadreNouvelleUtilisateur,bg="white")       # Champ texte pour le mot de passe
        self.NouveauPassword.grid(pady=(0,20))
        
        self.labelPasswordConfirm= Label(self.cadreNouvelleUtilisateur,text="Veuillez confirmer votre mot de passe",font='arial 12',bg="#E5E7F4")
        self.labelPasswordConfirm.grid()
        self.PasswordConfirm= Entry(self.cadreNouvelleUtilisateur,bg="white")       # Champ texte pour la confirmation du mot de passe
        self.PasswordConfirm.grid(pady=(0,20))
        
        self.labelIpServuer=Label(self.cadreNouvelleUtilisateur,text="Veuillez entrer l'adresse de votre serveur",font='arial 12',bg="#E5E7F4")
        self.labelIpServuer.grid()
        self.ipsplash=Entry(self.cadreNouvelleUtilisateur,bg="white")
        self.ipsplash.insert(0, self.monip)
        self.ipsplash.grid()

        self.confirmerIB=Button(self.cadreNouvelleUtilisateur,text="Confirmé",bg="#FFFFFF",relief=FLAT,command=self.inscription, width=15)
        self.confirmerIB.grid(row= 10, column= 0,pady=(25,20), padx=(0,122))
        
        self.annuleIB=Button(self.cadreNouvelleUtilisateur,text="Annuler",bg="#FFFFFF",relief=FLAT,command=self.retourMenuPrincipal, width=15)
        self.annuleIB.grid(row= 10,pady=(25,20) ,padx=(122,0))
        
        
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
        
        #self.frame = Frame(self.root, width=512, height=512)
        #self.frame.grid()
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
       
    def creercadrebase(self):
        self.listemodules=Listbox(bg="lightblue",borderwidth=0,relief=FLAT,width=40,height=6)
        if(self.cadrebaseExiste):
            self.destroyCadreBase()
        else:
            #self.largeurDefault=int(self.largeur/7)
            #self.hauteurDefault=int(self.hauteur/4.5)
            self.largeur=self.root.winfo_screenwidth()/7
            self.hauteur=self.root.winfo_screenmmheight()
        
        self.cadrebase=Frame(self.root, bg= "#E4E9F3")
        self.listeProjet=Listbox(self.cadrebase,height=int(self.hauteur-4), width = int(self.largeur/11),bg="#234078")
        self.listeProjet.grid(row=1,column=0,rowspan=15)
        self.listeProjet.insert(END, "a list entry")
        #self.boutonProjet1=Button(self.cadrebase,text="Projet 1",bg="#00BCD9",command=None,height=int(self.hauteur/3),width=int(self.largeur/11))
       # self.boutonProjet2=Button(self.cadrebase,text="Projet 2",bg="#00BCD9",command=None,height=int(self.hauteur/3),width=int(self.largeur/11))
        #self.boutonProjet3=Button(self.cadrebase,text="Projet 3",bg="#00BCD9",command=None,height=int(self.hauteur/3),width=int(self.largeur/11))

        self.boutonMandat=Button(self.cadrebase,text="Mandat",bg="#234078",command=self.requeteMandat,height=4,width=int(self.largeur/11),relief=FLAT, fg="white")
        self.boutonScrum=Button(self.cadrebase,text="Scrum",bg="#234078",command=self.requeteScrum,height=4,width=int(self.largeur/11),relief=FLAT, fg="white")
        self.boutonAnalyse=Button(self.cadrebase,text="Analyse \nTextuelle",bg="#234078",command=self.requeteAnalyse,height=4,width=int(self.largeur/11),relief=FLAT, fg="white")
        self.boutonCasUsage=Button(self.cadrebase,text="Cas \nd'usage",bg="#234078",command=self.requeteCasUsage,height=4,width=int(self.largeur/11),relief=FLAT, fg="white")
        self.boutonMaquette=Button(self.cadrebase,text="Maquette",bg="#234078",command=self.requeteMaquette,height=4,width=int(self.largeur/11),relief=FLAT, fg="white")
        self.boutonCrc=Button(self.cadrebase,text="CRC",bg="#234078",command=self.requeteCrc,height=4,width=int(self.largeur/11),relief=FLAT, fg="white")
        self.boutonBudget=Button(self.cadrebase,text="Budget",bg="#234078",command=self.requeteBudget,height=4,width=int(self.largeur/11),relief=FLAT, fg="white")
        self.boutonTchat=Button(self.cadrebase,text="Tchat",bg="#234078",command=self.requeteTchat,height=4,width=int(self.largeur/11),relief=FLAT, fg="white")
        self.boutonDonnee=Button(self.cadrebase,text="Modelisation \nde donnee",bg="#234078",command=self.requeteModelisation,height=4,width=int(self.largeur/11),relief=FLAT, fg="white")
        self.boutonTerlow=Button(self.cadrebase,text="Terlow",bg="#234078",command=self.requeteTerlow,height=4,width=int(self.largeur/11),relief=FLAT, fg="white")
        
        #self.boutonProjet1.grid(row=1,column=0,rowspan=5)
        #self.boutonProjet2.grid(row=6,column=0,rowspan=5)
        #self.boutonProjet3.grid(row=11,column=0,rowspan=5)

        self.boutonMandat.grid(row=0,column=1 ,padx=(0,2))
        self.boutonScrum.grid(row=0,column=2 ,padx=(0,2))
        self.boutonAnalyse.grid(row=0,column=3 ,padx=(0,2))
        self.boutonCasUsage.grid(row=0,column=4 ,padx=(0,2))
        self.boutonMaquette.grid(row=0,column=5 ,padx=(0,2))
        self.boutonCrc.grid(row=0,column=6 ,padx=(0,2))
        self.boutonBudget.grid(row=0,column=7 ,padx=(0,2))
        self.boutonTchat.grid(row=0,column=8 ,padx=(0,2))
        self.boutonDonnee.grid(row=0,column=9 ,padx=(0,2))
        self.boutonTerlow.grid(row=0,column=10)
        
    def nouveauProjet(self):
        self.fenetreCreationProjet = Toplevel(self.root, bg="#F8C471"  )
        self.fenetreCreationProjet.wm_title("Creer un Projet")
        
        self.texteCreationProjet = Label(self.fenetreCreationProjet, text="Nom du nouveau projet :", bg="#F8C471")
        self.texteCreationProjet.grid(row=1,column=1, padx=50, pady=(30,10))
        
        self.entreeCreationProjet = Entry(self.fenetreCreationProjet)
        self.entreeCreationProjet.grid(row=2,column=1, padx=50, pady=(0,10))
        
        self.boutonCreationProjet = Button(self.fenetreCreationProjet, text="Creer Projet", bg="#E67E22",command=self.creerProjet)
        self.boutonCreationProjet.grid(row=3,column=1, padx=50, pady=(0,30))
    def creerProjet(self):
        pass   
    
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
    def inscription(self):
        nom = self.NouveauNom.get()                 # Nom d'utilisateur à inscrire
        motPasse = self.NouveauPassword.get()       # Mot de passe de l'utilisateur à inscrire
        mpConfirm = self.PasswordConfirm.get()      # 2e mot de passe; pour confirmation
        ipserveur = self.ipsplash.get()             # Addresse ip de l'utilisateur
        
        if self.nomConforme(nom):                   # Vérifie que le nom d'utilisateur désiré est conforme
            if self.motPasseConforme(motPasse):     # Vérifie que le mot de passe de l'utilisateur est conforme
                if motPasse == mpConfirm:           # Confirme le mot de passe désiré
                    rep = self.parent.inscription(nom, motPasse, ipserveur)
                    print(rep)
                    self.retourMenuPrincipal()
                    
                else:
                    print("Mots de passe non identiques")
            else:
                print("Mot de passe non conforme")
        else:
            print("Nom d'utilisateur non conforme")
            
    def connexion(self):
        nom = self.nomsplash.get()
        motPasse = self.entrymotPassesplash.get()
        ipserveur = self.ipsplash.get()
        
        if self.nomConforme(nom):
            if self.motPasseConforme(motPasse):
                rep = self.parent.connexion(nom, motPasse, ipserveur)
                print(rep)
                
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
        
    def AllerAInscription(self):
        self.changecadre(self.cadreNouvelleUtilisateur)
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
            self.nomsplash.insert(0, "Entrez votre nom")
            self.nomsplash.config(fg = "grey")
            self.placeHolderEntryNom=True
    
if __name__ == '__main__':
    m=Vue(0,"127.0.0.1")
    m.root.mainloop()
    
