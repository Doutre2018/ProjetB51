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
        #self.connectionServeurCourant()
        self.createurId=Id
        self.serveur = ServerProxy(sys.argv[4], allow_none=True)
        self.modele=Modele(self)
        self.vue=Vue(self)
        self.vue.root.mainloop()
        
    
if __name__ == '__main__':
    c=Controleur()