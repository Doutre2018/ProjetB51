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
from _overlapped import NULL

class Modele():
    def __init__(self, parent):
        self.parent = parent
        self.BD=parent.serveur
        print("Bienvenue dans le modele ..")
        self.listeType = ["Nom-explicite",
                          "Verbe implicite",
                          "Adjectif supplementaire",
                          "Adjectif implicite",
                          "Adjectif explicite",
                          "Nom implicite",
                          "Nom supplementaire",
                          "Verbe explicite",
                          "Verbe supplementaire"]
<<<<<<< HEAD
=======
        #self.creerType()
        #self.numProjet
        #self.typeDonnee
>>>>>>> 5ed4b1e2bf07c711a742a4480e48d71936b48b78
        self.creerType()
        self.numProjet=1
        self.lesTypes = []
        self.lesVerbesImp = []
        self.lesNomsImp = []
        self.lesAdjectifsImp =[]
        self.lesVerbesSup = []
        self.lesNomsSup = []
        self.lesAdjectifSup =[]
        self.lesVerbesEx = []
        self.lesNomsEx =[]
        self.lesAdjectifsEx =[]
        self.selectAffichage()


    
        
<<<<<<< HEAD
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
        
        
            
=======
    #def InsertInto(self,ligne, colonne, nomProjet, type):
        #self.numProjet = BD.requeteSelection("SELECT id FROM Projet WHERE nom = " + nomProjet)
    #    typeDonnee = BD.requeteSelection("SELECT id FROM TypeMot WHERE nom = " + type)
    #    self.BD.requeteInsertionPerso("INSERT INTO AnalyseTextuelle(ligne, colonne, id_projet, id_type) VALUES( " + ligne + ", " + colonne + ", " + self.numProjet + ", " + typeDonnee + " )")
        
        
    def creerType(self):
        self.lesTypes = self.BD.requeteSelection("SELECT nom FROM TypeMot;")
        if not self.lesTypes:
            print("Entre")
            for type in self.listeType :
                    self.BD.requeteInsertionPerso("INSERT INTO TypeMot(nom) VALUES('" + type + "' );")
                    
    def selectAffichage(self):
        self.lesVerbesImp = self.BD.requeteSelection("SELECT ligne,colonne FROM AnalyseTextuelle WHERE id_type IN (SELECT nom FROM TypeMot WHERE nom = '" + self.listeType[1] + "');")
        self.lesNomsEx = self.BD.requeteSelection("SELECT ligne,colonne FROM AnalyseTextuelle WHERE id_type IN (SELECT nom FROM TypeMot WHERE nom = '" + self.listeType[0] + "');")
        self.lesAdjectifSup = self.BD.requeteSelection("SELECT ligne,colonne FROM AnalyseTextuelle WHERE id_type IN (SELECT nom FROM TypeMot WHERE nom = '" + self.listeType[2] + "');")
        self.lesAdjectifsImp = self.BD.requeteSelection("SELECT ligne,colonne FROM AnalyseTextuelle WHERE id_type IN (SELECT nom FROM TypeMot WHERE nom = '" + self.listeType[3] + "');")
        self.lesAdjectifsEx = self.BD.requeteSelection("SELECT ligne,colonne FROM AnalyseTextuelle WHERE id_type IN (SELECT nom FROM TypeMot WHERE nom = '" + self.listeType[4] + "');")
        self.lesNomsImp = self.BD.requeteSelection("SELECT ligne,colonne FROM AnalyseTextuelle WHERE id_type IN (SELECT nom FROM TypeMot WHERE nom = '" + self.listeType[5] + "');")
        self.lesNomsSup = self.BD.requeteSelection("SELECT ligne,colonne FROM AnalyseTextuelle WHERE id_type IN (SELECT nom FROM TypeMot WHERE nom = '" + self.listeType[6] + "');")
        self.lesVerbesEx = self.BD.requeteSelection("SELECT ligne,colonne FROM AnalyseTextuelle WHERE id_type IN (SELECT nom FROM TypeMot WHERE nom = '" + self.listeType[7] + "');")
        self.lesVerbesSup = self.BD.requeteSelection("SELECT ligne,colonne FROM AnalyseTextuelle WHERE id_type IN (SELECT nom FROM TypeMot WHERE nom = '" + self.listeType[8] + "');")
>>>>>>> 5ed4b1e2bf07c711a742a4480e48d71936b48b78
        
        
        
        
        