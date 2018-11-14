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
                          "Verbe supplementaire"]
        self.creerType()
        self.numProjet
        self.typeDonnee
    
        
    def InsertInto(self,ligne, colonne, nomProjet, type):
        self.numProjet = BD.selection("SELECT id FROM Projet WHERE nom = " + nomProjet)
        self.typeDonnee = BD.selection("SELECT id FROM TypeMot WHERE nom = " + type)
        BD.insertionPerso("INSERT INTO AnalyseTextuelle(ligne, colonne, id_projet, id_type) VALUES( " + ligne + ", " + colonne + ", " + numProjet + ", " + typeDonnee + " )") 
        
        
    def creerType(self):
        #self.lesTypes = self.BD.selection("SELECT nom FROM TypeMot")
        for type in self.listeType :
            if type in lesTypes:
                pass
            else:
                BD.insertionPerso("INSERT INTO TypeMot(nom) VALUES(" + type + " )")
                
        print("SELECT * FROM TypeMot")
            
        
        
        
        
        