# -*- coding: utf-8 -*-

import os,os.path
import sys
import socket
from subprocess import Popen 
import math
from gp_analyse_vue import *
from helper import Helper as hlp
from IdMaker import Id
from gp_analyse_modele import *
from xmlrpc.client import ServerProxy

class Controleur():
    def __init__(self):
        print("IN CONTROLEUR")
        self.serveur = ServerProxy(sys.argv[4], allow_none=True)
        
        self.createurId=Id
        print(self.serveur)
        self.modele=Modele(self)
        self.vue=Vue(self)
        self.vue.root.mainloop()
        
    def insertion(self,ligne,colonne,nomProjet, type, mot):
        self.modele.InsertInto(ligne,colonne,nomProjet, type, mot)
    
    def afficher(self):
        self.modele.selectAffichage(self)


if __name__ == '__main__':
    c=Controleur()