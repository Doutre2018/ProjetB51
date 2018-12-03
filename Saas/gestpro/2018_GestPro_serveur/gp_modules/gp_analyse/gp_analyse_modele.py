import os,os.path
import sys
import socket
from subprocess import Popen 
import math
from gp_analyse_vue import *
from helper import Helper as hlp
from IdMaker import Id
from _overlapped import NULL

class Modele():
    def __init__(self, parent):
        self.parent = parent
        self.BD=parent.serveur
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
        self.numProjet="1"
        self.lesTypes
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


    
        
    def InsertInto(self,ligne, colonne, numProjet, type, mot):
        typeDonnee = self.BD.requeteSelection("SELECT id FROM TypeMot WHERE nom = '" + type + "';")
        print(mot)
        for i in typeDonnee:
            for n in i:
                typeDonnee = n
        self.BD.requeteInsertionPerso("INSERT INTO AnalyseTextuelle(ligne, colonne, id_projet, id_type, mot) VALUES( '" + str(ligne) + "', '" + str(colonne) + "', '" + str(self.numProjet) + "', '" + str(typeDonnee) + "', '" + str(mot) + "');")
        self.selectAffichage()
        
        
    def creerType(self):
        self.lesTypes = self.BD.requeteSelection("SELECT nom FROM TypeMot;")
        if not self.lesTypes:
            for type in self.listeType :
                    self.BD.requeteInsertionPerso("INSERT INTO TypeMot(nom) VALUES('" + type + "' );")
                    
    def selectAffichage(self):
        self.lesVerbesImp = self.BD.requeteSelection("SELECT ligne,colonne FROM AnalyseTextuelle WHERE id_type = (SELECT id FROM TypeMot WHERE nom = '" + self.listeType[1] + "');")
        self.lesNomsEx = self.BD.requeteSelection("SELECT ligne,colonne FROM AnalyseTextuelle WHERE id_type = (SELECT id FROM TypeMot WHERE nom = '" + self.listeType[0] + "');")
        self.lesAdjectifSup = self.BD.requeteSelection("SELECT ligne,colonne FROM AnalyseTextuelle WHERE id_type = (SELECT id FROM TypeMot WHERE nom = '" + self.listeType[2] + "');")
        self.lesAdjectifsImp = self.BD.requeteSelection("SELECT ligne,colonne FROM AnalyseTextuelle WHERE id_type = (SELECT id FROM TypeMot WHERE nom = '" + self.listeType[3] + "');")
        self.lesAdjectifsEx = self.BD.requeteSelection("SELECT ligne,colonne FROM AnalyseTextuelle WHERE id_type = (SELECT id FROM TypeMot WHERE nom = '" + self.listeType[4] + "');")
        self.lesNomsImp = self.BD.requeteSelection("SELECT ligne,colonne FROM AnalyseTextuelle WHERE id_type = (SELECT id FROM TypeMot WHERE nom = '" + self.listeType[5] + "');")
        self.lesNomsSup = self.BD.requeteSelection("SELECT ligne,colonne FROM AnalyseTextuelle WHERE id_type = (SELECT id nom FROM TypeMot WHERE nom = '" + self.listeType[6] + "');")
        self.lesVerbesEx = self.BD.requeteSelection("SELECT mot FROM AnalyseTextuelle WHERE id_type = (SELECT id FROM TypeMot WHERE nom = '" + self.listeType[7] + "');")
        self.lesVerbesSup = self.BD.requeteSelection("SELECT mot FROM AnalyseTextuelle WHERE id_type = (SELECT id FROM TypeMot WHERE nom = '" + self.listeType[8] + "');")
        
        
        
        
        