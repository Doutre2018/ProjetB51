# -*- coding: utf-8 -*-

import os,os.path
import sys
#import Pyro4
import socket
from subprocess import Popen 
import math
#from sm_projet_modele import *
from gp_mandat_vue import *
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
        
class Modele():
    def __init__(self,parent):
        self.parent=parent
        self.serveur=parent.serveur
        
    def selectSprint(self):
        commande = "SELECT nom FROM Sprint"
        return self.serveur.requeteSelection(commande)
    
    def selectIdSprint(self,nom):
        commande = "SELECT id FROM Sprint WHERE nom='"
        commande+=str(nom)+"'"
        return self.serveur.requeteSelection(commande)
    
    def insertSprint(self,nom):
        return self.serveur.requeteInsertionPerso("INSERT INTO Sprint(nom) VALUES('" + str(nom) + "');")
    
    def insertMembreSprint(self,membre,idSprint):
        return self.serveur.requeteInsertionPerso("INSERT INTO MembreSprint(nomMembre,id_sprint) VALUES('" + str(membre) + "',"+str(idSprint)+");")
    
    def deleteSprint(self,idSprint):
        print(idSprint)
        commande="DELETE FROM Sprint WHERE id="
        commande+=str(idSprint)
        self.serveur.requeteInsertionPerso(commande)
if __name__ == '__main__':
    c=Controleur()