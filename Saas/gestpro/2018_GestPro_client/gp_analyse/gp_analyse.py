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
        self.connectionServeurCourant()
        self.serveur = ServerProxy(self.adresseServeur)
        
        self.createurId=Id
        self.modele=Modele(self)
        self.vue=Vue(self)
        self.vue.root.mainloop()
        
    def connectionServeurCourant(self):  
        with open("../../../2018_Gestpro_client/adresseServeurCourant.txt", "r") as fichier:
            self.adresseServeur = fichier.read() 
        
        
    
if __name__ == '__main__':
    c=Controleur()