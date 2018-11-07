# -*- coding: utf-8 -*-

import os,os.path
import sys
#import Pyro4
import socket
from subprocess import Popen 
from xmlrpc.client import ServerProxy
import math
#from sm_projet_modele import *
from gp_casdusage_vue import *
from helper import Helper as hlp
from IdMaker import Id

class Controleur():
    def __init__(self):
        print("IN CONTROLEUR")
        self.connectionServeurCourant()
        self.serveur = ServerProxy(self.adresseServeur)
        self.createurId=Id
        self.modele=None
        self.vue=Vue(self)
        self.vue.root.mainloop()
        
    def connectionServeurCourant(self):  
        with open("../adresseServeurCourant.txt", "r") as fichier:
            self.adresseServeur = fichier.read()
                
if __name__ == '__main__':
    c=Controleur()