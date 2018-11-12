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
import sqlite3


class Controleur():
    def __init__(self):
        print("IN CONTROLEUR")
        cwd = os.getcwd()
        if cwd is "2018_GestPro_client":
            self.connectionServeurCourant()
            self.serveur = ServerProxy(self.adresseServeur)
        connection = sqlite3.connect("SAAS.db")
        curseur = connection.cursor()
        self.createurId=Id
        self.modele=None
        self.vue=Vue(self)
        self.vue.root.mainloop()
        
    def connectionServeurCourant(self):  
        with open("../adresseServeurCourant.txt", "r") as fichier:
            self.adresseServeur = fichier.read()  

class Modele():
    def __init__(self):
        #self.bd = BaseDonnees
        self.nombreCartes=0
        for i in selectClassesCartes():
            self.nombreCartes+=1        
    
<<<<<<< HEAD
    def insertCarte(self,listeValeur):
        bd.insertionPerso("""INSERT INTO Cartes(id_projet,classe, id_carte_heritage, ordre) VALUES(  """ + listeValeur[0] + """, """ + listeValeur[1] + """, """ + listeValeur[2] + """, """ + listeValeur[3] + """, """ + listeValeur[4] + """ )""")
=======
    def insertCarte (self,listeValeur,nom="Cartes"):
        self.bd.insertion(nom,listeValeur)
>>>>>>> f08a15c066688db539cd4bee089a338cc2d957a1
    
    def selectClassesCartes(self):
        commande ="""SELECT classe FROM Cartes"""
        #Retourne une liste de String de cartes
        return bd.selection(commande)
    
    def selectIdCarte(self,classe):
        commande ="""SELECT id FROM Cartes WHERE classe="""
        commande+=classe
        ID = bd.selection(commande)
        return ID
    
    def selectAttributDeCarte(self,idCarte):
        commande = """SELECT nomAttributs FROM AttributsCRC WHERE id_classe="""
        commande+=idCarte
        #Retourne une liste de String des attributs d'UNE carte
        return bd.selection(commande)
    
    def insertAttributsDeCarte(self,id_classe):
        listeValeur
        bd.insertion("AttributsCRC")
    
if __name__ == '__main__':
    c=Controleur()