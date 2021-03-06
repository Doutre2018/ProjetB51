# -*- coding: utf-8 -*-

import os,os.path
import sys
#import Pyro4
import socket
from subprocess import Popen 
import math
#from sm_projet_modele import *
from gp_scrum_vue import *
from gp_scrum_modele import *
from helper import Helper as hlp
from IdMaker import Id
from xmlrpc.client import ServerProxy

class Controleur():
    def __init__(self):
        print("IN CONTROLEUR")
        self.createurId=Id
        self.serveur = ServerProxy(sys.argv[4], allow_none=True)
        self.modele=Modele(self)
        self.vue=Vue(self)
        self.vue.root.mainloop()
        
    def insertNewScrum(self, dateScrum):
        self.modele.insertScrum(dateScrum)
    
    def insertNewMembre(self, nom, idScrum):
        self.modele.insertMembreScrum(nom, idScrum)
        
    def insertDataMembre(self, accompli, aFaire, probleme, nom):
        self.modele.insertDonneesMembre(accompli, aFaire, probleme, nom)
        
    def selectDataMembre(self, nom):
        self.modele.selectMembres(nom)
    
    def afficherMembres(self, idscrum):
        self.modele.selectMembre(idscrum)
        
    
if __name__ == '__main__':
    c=Controleur()