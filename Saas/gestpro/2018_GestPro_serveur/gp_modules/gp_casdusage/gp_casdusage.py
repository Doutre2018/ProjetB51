# -*- coding: utf-8 -*-

import os,os.path
import sys
#import Pyro4
import socket
from subprocess import Popen 
import math
#from sm_projet_modele import *
from gp_casdusage_model import *
from gp_casdusage_vue import *
from helper import Helper as hlp
from IdMaker import Id

class Controleur():
    def __init__(self):
        print("IN CONTROLEUR")
        self.createurId=Id
        self.modele = Scenarii(self)
        self.vue=Vue(self)
        self.vue.root.mainloop()
        
    def fetchCases(self):
        return self.modele.fetchCas()
        ListeRetourne = []
        afficheCasUsage(ListeRetourne)
    
if __name__ == '__main__':
    c=Controleur()