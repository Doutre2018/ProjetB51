 # -*- coding: utf-8 -*-

import os,os.path
import sys
#import Pyro4
import socket
import sqlite3
from subprocess import Popen 
import math
#frommgestpro_client_main import Controleur as ControleurClient
#from sm_projet_modele import *
from gp_tchat_vue import *
from helper import Helper as hlp
from IdMaker import Id
from xmlrpc.client import ServerProxy

class Controleur():
    def __init__(self):
        print("IN CONTROLEUR")
        self.monNom = sys.argv[1]
        #print(self.monNom)
        self.createurId=Id
        self.serveur = ServerProxy(sys.argv[4], allow_none=True)
        self.recevoirFichiers()
        self.modele=Modele(self, self.monNom)
        self.vue=Vue(self)
        self.reloadMessageBD()
        self.vue.root.mainloop()
        
    def reloadMessageBD(self):
        self.vue.ajoutMessageBD()
        self.vue.root.after(20,self.reloadMessageBD)
        
    def recevoirFichiers(self):
        # pour utiliser, entrez le nom des fichiers que vous voulez dans la liste chemins (1 à n chemins) 
        listeChemins = ["chat.jpg", "chat2.jpg"]
        for chemin in listeChemins:
            try:
                with open(chemin, "wb") as handle:
                    handle.write(self.serveur.requeteFichier(chemin).data)
            except Exception as erreur: 
                try:
                    self.serveur.logErreur(socket.gethostbyname(socket.getfqdn()), erreur)
                except:
                    pass
                
class Modele():
    def __init__(self,parent, usager):
        self.parent=parent
        self.serveur=parent.serveur
        #self.usager = self.serveur.fetchNomUtilisateurCourant() #//modif simon 10:59
        self.usager = usager
        self.compagnie = self.serveur.fetchNomCompagnie()
        self.FilDeDiscussionCourant = 0 #Tant qu'il n'y a pas de module Projet
        self.idProjetCourant = None
        self.idUsager=self.idUtilisateurCourant()
        for i in self.idUsager:
            for n in i:
                self.idUsager=n
    def fetchNomTchateur(self):
        return self.monNom
    
    def idUtilisateurCourant(self):
        commande="SELECT id FROM Utilisateur WHERE nomUtilisateur='"+self.usager+"';"
        return self.serveur.requeteSelection(commande)
    
    #Insertions
    def insertLigneChat(self,texte):
        self.serveur.requeteInsertionPerso("INSERT INTO LigneChat(texte,id_filDiscussion,id_utilisateur) VALUES('"+texte+"',"+str(self.FilDeDiscussionCourant)+","+str(self.idUsager)+");")
        
    def insertFilDiscussion(self):
        self.serveur.requeteInsertionPerso("INSERT INTO FilDeDiscussion(id_projet) VALUES("+str(self.idProjetCourant)+");")

    #Select
    def selectFilDiscussion(self):
        pass
    
    def selectIdLignesChat(self):
        commande = "SELECT id FROM LigneChat;"
        return self.serveur.requeteSelection(commande)
    
    def selectToutesTextesLignesChat(self):
        commande = "SELECT texte FROM LigneChat;"
        self.serveur.requeteSelection(commande)
    
    def selectTexteLigneChat(self,id):
        commande = "SELECT texte FROM LigneChat WHERE id="
        for i in self.serveur.requeteSelection(commande+str(id)):
            for n in i:
                rep = n
        commande += " ORDER BY id DESC LIMIT 30"
        return rep
    
    def selectNomUtilisateurDeLigneChat(self,id):
        for i in self.triNomAvecIdUtilisateur(self.selectUtilisateurDeLigneChat(id)):
            for n in i:
                nom = n
        return nom
    
    def selectUtilisateurDeLigneChat(self,id):
        commande = "SELECT id_utilisateur FROM LigneChat WHERE id="
        return self.serveur.requeteSelection(commande+str(id))
        
    def selectTousUtilisateursLigneChat(self):
        commande = "SELECT id_utilisateur FROM LigneChat;"
        try:
            return self.serveur.requeteSelection(commande)
        except Exception as erreur:
            try:
                self.serveur.logErreur(socket.gethostbyname(socket.getfqdn()), erreur)
            except:
                pass
        
    def triNomAvecIdUtilisateur(self,idUsager):
        commande = "SELECT nomUtilisateur FROM Utilisateur WHERE id="
        try:
            for i in idUsager:
                for n in i:
                    idUsager=n
            return self.serveur.requeteSelection(commande+str(idUsager))
        except sqlite3.Error as erreur:
                try:
                    self.serveur.logErreur(socket.gethostbyname(socket.getfqdn()), erreur)
                    return None
                except:
                    return None
            
    
if __name__ == '__main__':
    c=Controleur()