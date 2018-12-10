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
        print("Bienvenue dans le modele ..")


    def sauvegarde(self):
        pass
         #for objet in self.listeObjetMaquette :
         #   #Donnes : Type, PosX,PosY,X,Y,Bordure,Interieur,texte de string, Font, Id
       #     self.BD.requeteInsertionPerso("INSERT INTO objet[0]
         #   objet[1]
        #    objet[2]
        #    objet[3]
        #    objet[4]
         #   objet[5]
        #    objet[6]
         #   objet[7]
       #     objet[8]
        #    objet[9]
          #  objet[10]
        #
    def InsertInto(self,ligne, colonne, numProjet, type, mot):
        
        
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
        
        
        
        
        