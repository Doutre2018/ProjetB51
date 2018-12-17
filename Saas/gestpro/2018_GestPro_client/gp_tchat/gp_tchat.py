# -*- coding: utf-8 -*-

import os,os.path
import sys
#import Pyro4
import socket
from subprocess import Popen 
import math
#from sm_projet_modele import *
from gp_tchat_vue import *
from helper import Helper as hlp
from IdMaker import Id
from xmlrpc.client import ServerProxy

class Controleur():
    def __init__(self):
        print("IN CONTROLEUR")
        self.createurId=Id
        self.serveur = ServerProxy(sys.argv[4], allow_none=True)
        self.recevoirFichiers()
        self.modele=Modele(self)
        self.vue=Vue(self)
        self.reloadMessageBD()
        self.vue.root.mainloop()
        
    def reloadMessageBD(self):
        self.vue.ajoutMessageBD()
        self.vue.root.after(100,self.reloadMessageBD)
        
    def recevoirFichiers(self):
        # pour utiliser, entrez le nom des fichiers que vous voulez dans la liste chemins (1 à n chemins) 
        listeChemins = ["chat.jpg"]
        for chemin in listeChemins:
            try:
                with open(chemin, "wb") as handle:
                    handle.write(self.serveur.requeteFichier(chemin).data)
            except Exception as erreur: 
                print("Problème lors du téléchargement du fichier", chemin, '\n', erreur)
                
class Modele():
    def __init__(self,parent):
        self.parent=parent
        self.serveur=parent.serveur
        self.usager = self.serveur.fetchNomUtilisateurCourant()
        self.compagnie = self.serveur.fetchNomCompagnie()
        self.FilDeDiscussionCourant = 0 #Tant qu'il n'y a pas de module Projet
        self.idProjetCourant = None
        self.idUsager=self.idUtilisateurCourant()
        for i in self.idUsager:
            for n in i:
                self.idUsager=n
        
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
    
    def selectToutesLignesChat(self):
        commande = "SELECT texte FROM LigneChat;"
        self.serveur.requeteSelection(commande)
        
    def selectTousUtilisateursLigneChat(self):
        commande = "SELECT id_utilisateur FROM LigneChat;"
        return self.serveur.requeteSelection(commande)
        
    def triNomAvecIdUtilisateur(self,idUsager):
        commande = "SELECT nomUtilisateur FROM Utilisateur WHERE id="
        return self.serveur.requeteSelection(commande+str(idUsager))
    
if __name__ == '__main__':
    c=Controleur()