# -*- coding: utf-8 -*-

import os,os.path
import sys
#import Pyro4
import socket
from subprocess import Popen 
import math
#from sm_projet_modele import *
from gp_crc_vue import *
from helper import Helper as hlp
from IdMaker import Id
from xmlrpc.client import ServerProxy
#import sqlite3



class Controleur():
    def __init__(self):
        print("IN CONTROLEUR")
        cwd = os.getcwd()
        self.connectionServeurCourant()
        print(self.serveur)
        liste = self.serveur.requeteSelection("select price from stocks")
        print(liste)
        self.createurId=Id
        self.modele=Modele(self)
        self.vue=Vue(self)
        self.vue.root.mainloop()
        
    def connectionServeurCourant(self):  
        try:
            with open("../adresseServeurCourant.txt", "r") as fichier:
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

class Modele():
    def __init__(self,parent):
        self.parent=parent
        self.serveur=parent.serveur
        self.listeCartes=self.selectClassesCartes()
        #self.listeIDCartes=self.selectIdCarte()
        #for i in self.listeIDCartes:
            #self.listeAttributs.append(selectAttributDeCarte(i))
        
    def insertCarte(self,listeValeur):
        self.serveur.requeteInsertionPerso("""INSERT INTO Cartes(id_projet, classe, id_carte_heritage, ordre) VALUES(  """ + str(listeValeur[0]) + """, """ + str(listeValeur[1]) + """, """ + str(listeValeur[2]) + """, """ + str(listeValeur[3]) + """);""")
    
    def selectClassesCartes(self):
        commande ="SELECT classe FROM Cartes"
        #Retourne une liste de String de cartes
        return self.serveur.requeteSelection(commande)
    
    def selectIdCarte(self,classe):
        commande ="""SELECT id FROM Cartes WHERE classe="""
        commande+=classe
        ID = self.serveur.requeteSelection(commande)
        return ID
    
    def selectAttributDeCarte(self,idCarte):
        commande = """SELECT nomAttributs FROM AttributsCRC WHERE id_classe="""
        commande+=idCarte
        #Retourne une liste de String des attributs d'UNE carte
        return self.serveur.requeteSelection(commande)
    
    #Les insertions
    def insertAttributsDeCarte(self,listeValeur):
        self.serveur.requeteInsertionPerso("""INSERT INTO AttributsCRC(nomAttributs) VALUES(""" + str(str(listeValeur[0])) + """) WHERE id_classe= """ + str(listeValeur[1]) + """;""")
        
    def insertCollaboDeCarte(self,listeValeur):
        self.serveur.requeteInsertionPerso("""INSERT INTO CollaboCRC(id_classe,textCollabo) VALUES(""" + str(listeValeur[0]) + ""","""+ str(listeValeur[1]) +""") ;""")
    
    def insertFonctionDeCarte(self,listeValeur):
        self.serveur.requeteInsertionPerso("""INSERT INTO FonctionsCRC(id_classe,fonction) VALUES(""" + str(listeValeur[0]) + ""","""+ str(listeValeur[1]) +""");""")
                                                                                                                                      
    def selectResponsableCarte(self,id_classe):
        commande="""SELECT nom FROM Utilisateur"""
        return self.serveur.requeteSelection(commande)
    
if __name__ == '__main__':
    c=Controleur()