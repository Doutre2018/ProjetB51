# -*- coding: utf-8 -*-

import os,os.path
import sys
#import Pyro4
import socket
from subprocess import Popen 
import math
#from sm_projet_modele import *
from gp_analyse_vue import *
from helper import Helper as hlp
from IdMaker import Id
from gp_analyse_modele import *

parentPath = os.path.abspath("../..")
if parentPath not in sys.path:
    sys.path.insert(0, parentPath)
from gestpro_serveur import BaseDonnees as BD
    

class Controleur():
    def __init__(self):
        print("IN CONTROLEUR")
        self.createurId=Id
        #self.modele=Modele(self)
        self.vue=Vue(self)
        self.vue.root.mainloop()
        
        
    
if __name__ == '__main__':
    c=Controleur()