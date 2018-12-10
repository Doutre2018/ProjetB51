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
        self.connectionServeurCourant()
        self.recevoirFichiers()
        self.modele=Modele(self)
        self.vue=Vue(self)
        self.reloadMessageBD()
        self.vue.root.mainloop()
        
    def reloadMessageBD(self):
        self.vue.ajoutMessageBD()
        self.vue.root.after(100,self.reloadMessageBD)
        
    def connectionServeurCourant(self):  
        try:
            with open("adresseServeurCourant.txt", "r") as fichier:
                self.adresseServeur = fichier.read()       
        except Exception as erreur:
            print(erreur)
            try:
                with open("../../../2018_Gestpro_client/adresseServeurCourant.txt", "r") as fichier:
                    self.adresseServeur = fichier.read()  
            except Exception as erreur:
                print(erreur)
                self.adresseServeur = "http://"
                self.adresseServeur += input("Désolé, il y a eu une erreur lors de la détection automatique de l'adresse du serveur, vous pouvez entrer le IP (ex: 10.57.47.7) manuellement: ")
                self.adresseServeur += ":9999"
        try:
            self.serveur = ServerProxy(self.adresseServeur)
        except Exception as erreur:
            print("Désolé, il y a eu un problème avec la connection au serveur, fermeture du module.")
            print(erreur)
            sys.exit(0)
        
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
        
    def idUtilisateurCourant(self):
        commande="SELECT id FROM Utilisateur WHERE nomUtilisateur='"+self.usager+"';"
        return self.serveur.requeteSelection(commande)
    
    #Insertions
    def insertLigneChat(self,texte):
        self.serveur.requeteInsertionPerso("INSERT INTO LigneChat(texte,id_filDiscussion,id_utilisateur) VALUES('"+str(texte)+"',"+str(self.FilDeDiscussionCourant)+","+str(self.idUsager)+");")
        
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
        self.serveur.requeteSelection(commande)
        
    def triNomAvecIdUtilisateur(self,idUsager):
        commande = "SELECT nomUtilisateur FROM Utilisateur WHERE id="
        self.serveur.requeteSelection(commande+str(isUsager))
    
if __name__ == '__main__':
    c=Controleur()