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
<<<<<<< HEAD
=======
        self.bd = BD()
>>>>>>> f08a15c066688db539cd4bee089a338cc2d957a1
        self.listeType = ["Nom explicite",
                          "Verbe implicite",
                          "Adjectif supplementaire",
                          "Adjectif implicite",
                          "Adjectif explicite",
                          "Nom implicite",
                          "Nom supplementaire",
                          "Verbe explicite",
<<<<<<< HEAD
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
=======
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
>>>>>>> f08a15c066688db539cd4bee089a338cc2d957a1
            
        
        
        
        
        