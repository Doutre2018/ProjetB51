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

class Modele():
    def __init__(self, parent):
        print("Bienvenue dans le modele ..")
        self.bd = BD()
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
        self.creerType()
        
        
        
    def creerType(self):
        for type in self.listeType:
            if type in self.lesTypes:
                pass
            else:
                self.bd.curseur.execute("INSERT INTO TypeMot(nom) VALUES(" + type + " )")

                #self.bd.curseur.execute("")
            
        
        
        
        
        