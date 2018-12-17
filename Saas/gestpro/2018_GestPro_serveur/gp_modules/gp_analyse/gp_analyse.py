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
        self.modele=Modele(self)
        self.vue=Vue(self)
        self.vue.root.mainloop()
        

    def insertion(self,ligne,nomProjet, type, mot):
        self.modele.InsertInto(ligne,nomProjet, type, mot)

    
    def afficher(self):
        self.modele.selectAffichage(self)
        
    def supprimer(self, type, nom):
        self.modele.deleteItem(type, nom)


if __name__ == '__main__':
    c=Controleur()