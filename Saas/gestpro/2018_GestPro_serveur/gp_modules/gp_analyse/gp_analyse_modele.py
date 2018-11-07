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

parentPath = os.path.abspath("../..")
if parentPath not in sys.path:
    sys.path.insert(0, parentPath)
from gestpro_serveur import BaseDonnees as BD

class Modele():
    def __init__(self, parent):
        print("Bienvenue dans le modele ..")
        self.creerType()
        self.listeType = ["Nom explicite",
                          "Verbe implicite",
                          "Adjectif supplementaire",
                          "Adjectif implicite",
                          "Adjectif explicite",
                          "Nom implicite",
                          "Nom supplementaire",
                          "Verbe explicite",
                          "Verbe supplementaire",]
        self.lesTypes = self.bd.selection("SELECT nom FROM TypeMot")
        
        
    def creerType(self):
        for type in listeType:
            if type in lesTypes:
                pass
            else:
                BD.curseur.execute("INSERT INTO TypeMot(nom) VALUES(" + type + " )")
            
        
        
        
        
        