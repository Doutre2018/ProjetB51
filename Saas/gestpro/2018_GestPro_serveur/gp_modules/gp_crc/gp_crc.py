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
        self.listeIDCartes=self.selectIdCarte()
        for i in self.listeIDCartes:
            self.listeAttributs.append(selectAttributDeCarte(i))
        
    def insertCarte(self,listeValeur):
        self.serveur.insertionPerso("""INSERT INTO Cartes(id_projet,classe, id_carte_heritage, ordre) VALUES(  """ + listeValeur[0] + """, """ + listeValeur[1] + """, """ + listeValeur[2] + """, """ + listeValeur[3] + """, """ + listeValeur[4] + """ )""")
    
    def selectClassesCartes(self):
        commande ="""SELECT classe FROM Cartes"""
        #Retourne une liste de String de cartes
        return self.serveur.selection(commande)
    
    def selectIdCarte(self,classe):
        commande ="""SELECT id FROM Cartes WHERE classe="""
        commande+=classe
        ID = self.serveur.selection(commande)
        return ID
    
    def selectAttributDeCarte(self,idCarte):
        commande = """SELECT nomAttributs FROM AttributsCRC WHERE id_classe="""
        commande+=idCarte
        #Retourne une liste de String des attributs d'UNE carte
        return self.serveur.selection(commande)
    
    def insertAttributsDeCarte(self,listeValeur):
        self.serveur.insertionPerso("""INSERT INTO AttributsCRC(nomAttributs) VALUES(""" + listeValeur[0] + """) WHERE id_classe= """ + listeValeur[1] + """;""")
        
    def selectResponsableCarte(self,id_classe):
        commande="""SELECT nom FROM Utilisateur"""
        return self.serveur.selection(commande)
    
if __name__ == '__main__':
    c=Controleur()