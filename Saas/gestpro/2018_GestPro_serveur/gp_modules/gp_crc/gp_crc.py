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

parentPath = os.path.abspath("../..")
if parentPath not in sys.path:
    sys.path.insert(0,parentPath)
from gestpro_serveur import BaseDonnees

class Controleur():
    def __init__(self):
        print("IN CONTROLEUR")
        self.createurId=Id
        self.modele=None
        self.vue=Vue(self)
        self.vue.root.mainloop()
        
class Modele():
    def __init__(self):
        self.bd = BaseDonnees
        self.nombreCartes=0
        for i in selectClassesCartes():
            self.nombreCartes+=1        
    
    def insertCarte (self,listeValeur,nom="Cartes"):
        self.bd.insertion(nom,listeValeur)
    
    def selectClassesCartes(self):
        commande ="""SELECT classe FROM Cartes"""
        #Retourne une liste de String de cartes
        return self.bd.selection(commande)
    
    def selectIdCarte(self,classe):
        commande ="""SELECT id FROM Cartes WHERE classe="""
        commande+=classe
        ID = self.bd.selection(commande)
        return ID
    
    def selectAttributDeCarte(self,idCarte):
        commande = """SELECT nomAttributs FROM AttributsCRC WHERE id_classe="""
        commande+=idCarte
        #Retourne une liste de String des attributs d'UNE carte
        return self.bd.selection(commande)
    
    def insertAttributsDeCarte(self,id_classe):
        listeValeur
        self.bd.insertion("AttributsCRC")
    
if __name__ == '__main__':
    c=Controleur()