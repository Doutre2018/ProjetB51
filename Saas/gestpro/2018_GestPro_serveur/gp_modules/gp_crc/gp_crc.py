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


class Controleur():
    def __init__(self):
        print("IN CONTROLEUR")
        self.connectionServeurCourant()
        self.serveur = ServerProxy(self.adresseServeur)
        print(self.serveur)

        self.createurId=Id
        self.modele=None
        self.vue=Vue(self)
        self.vue.root.mainloop()
        
    def connectionServeurCourant(self):  
        with open("../../../2018_Gestpro_client/adresseServeurCourant.txt", "r") as fichier:
            self.adresseServeur = fichier.read()  

class Modele():
    def __init__(self):
        #self.bd = BaseDonnees
        self.nombreCartes=0
        for i in selectClassesCartes():
            self.nombreCartes+=1        
    
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
    
    def insertAttributsDeCarte(self,id_classe):
        #listeValeur
        bd.insertion("AttributsCRC")
    
if __name__ == '__main__':
    c=Controleur()