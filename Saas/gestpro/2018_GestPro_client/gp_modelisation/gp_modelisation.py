# -*- coding: utf-8 -*-

import os,os.path
import sys
#import Pyro4
import socket
from subprocess import Popen 
import math
#from sm_projet_modele import *
from gp_modelisation_vue import *
from gp_modelisation_model import *
from helper import Helper as hlp
from IdMaker import Id
from xmlrpc.client import ServerProxy

class Controleur():
    def __init__(self):
        self.createurId=Id
        self.serveur = ServerProxy(sys.argv[4], allow_none=True)
        self.modele=Modele(self)
        self.vue=Vue(self)
        self.vue.root.mainloop()


            
    def insertCarte(self, nomCarte):
        self.modele.insertIntoCarte(nomCarte)
        
    def insertItem(self, nom, type, contrainte, nomCarte):
        self.modele.insertIntoItem(nom, type, contrainte, nomCarte)
    
    def selectCartes(self):
        self.modele.selectAffichageCartes()
        
    def selectItemNom(self, nomCarte):
        self.modele.selectAffichageItemNom(nomCarte);
        
    def selectItemType(self, nomCarte):
        self.modele.selectAffichageItemType(nomCarte);
        
    def selectItemContrainte(self, nomCarte):
        self.modele.selectAffichageItemCon(nomCarte);
        

    
if __name__ == '__main__':
    c=Controleur()