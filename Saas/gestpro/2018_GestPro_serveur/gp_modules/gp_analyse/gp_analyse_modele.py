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
        self.listeType = ["Nom explicite",
                          "Verbe implicite",
                          "Adjectif supplementaire",
                          "Adjectif implicite",
                          "Adjectif explicite",
                          "Nom implicite",
                          "Nom supplementaire",
                          "Verbe explicite",
                          "Verbe supplementaire"]
        #self.creerType()
        #self.numProjet
        #self.typeDonnee
        self.creerType()
        self.numProjet
        self.typeDonnee
        self.lesTypes = []
        self.lesVerbesImp = []
        self.lesNomsImp = []
        self.lesAdjectifsImp =[]
        self.lesVerbesSup = []
        self.lesNomsSup = []
        self.lesAdjectifSup =[]
        self.lesVerbesEx = []
        self.lesNomsEx
        self.lesAdjectifsEx
        self.selectAffichage()


    
        
    def InsertInto(self,ligne, colonne, nomProjet, type):
        self.numProjet = BD.selection("SELECT id FROM Projet WHERE nom = " + nomProjet)
        self.typeDonnee = BD.selection("SELECT id FROM TypeMot WHERE nom = " + type)
        BD.insertionPerso("INSERT INTO AnalyseTextuelle(ligne, colonne, id_projet, id_type) VALUES( " + ligne + ", " + colonne + ", " + numProjet + ", " + typeDonnee + " )") 
        
        
    def creerType(self):
        try:
            self.lesTypes = self.BD.selection("SELECT nom FROM TypeMot")
        except:
            for type in self.listeType :
                    BD.insertionPerso("INSERT INTO TypeMot(nom) VALUES(" + type + " )")
                    
    def selectAffichage(self):
        self.lesVerbesImp = self.BD.selection("SELECT ligne,colonne")
        
        
            
        
        
        
        
        