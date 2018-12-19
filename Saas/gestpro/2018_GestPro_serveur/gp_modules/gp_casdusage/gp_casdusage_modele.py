import os,os.path
import sys
import socket
from subprocess import Popen 
import math
from gp_casdusage_vue import *
from helper import Helper as hlp
from IdMaker import Id
from _overlapped import NULL

class Modele():
    def __init__(self, parent):
        self.parent = parent
        self.BD=parent.serveur
        print("Bienvenue dans le modele ..")
        self.numProjet="1"
        self.scrum = []
        self.membres = []
        self.accompli = None
        self.aFaire = None
        self.probleme = None
        
        
    def insertCas(self, ligne, texte):
        
        self.BD.requeteInsertionPerso("INSERT INTO CasUsage(id_projet, ligne,texte) VALUES('" + str(self.numProjet) + "','" + str(ligne) + "','" + str(texte) + "');")
    
    def insertScenarii(self, ligne, usager, machine ):
        idCas = self.BD.requeteSelection("SELECT id FROM CasUsage WHERE texte = '" + str(ligne[0]) + "';")
        idCas = idCas[0]
        idCas = idCas[0]
        
        self.BD.requeteInsertionPerso("INSERT INTO Scenarii(id_projet, id_casUsage,ligne,id_colonne) VALUES('" + str(self.numProjet) + "','" + str(idCas) + "','" + str(usager) + "','" + str(1) + "');")
        self.BD.requeteInsertionPerso("INSERT INTO Scenarii(id_projet, id_casUsage,ligne,id_colonne) VALUES('" + str(self.numProjet) + "','" + str(idCas) + "','" + str(machine) + "','" + str(2) + "');")
   
    def selectScenarii(self, ligne):
        idCas = self.BD.requeteSelection("SELECT id FROM CasUsage WHERE texte = '" + str(ligne[0]) + "';")
        #idUsager = self.BD.requeteSelection("SELECT id FROM ColonnesScenarri WHERE id = '" + str(1) + "';")
        #idMachine = self.BD.requeteSelection("SELECT id FROM ColonnesScenarri WHERE id = '" + str(2) + "';")
        idCas = idCas[0]
        idCas = idCas[0]

        idUsager=1
        idMachine=2
        print("SELECT ligne FROM Scenarii WHERE id_projet = '" + str(self.numProjet) + "' AND id_colonne = '" + str(idUsager) + "' ;")
        print("SELECT ligne FROM Scenarii WHERE id_projet = '" + str(self.numProjet) + "' AND id_colonne = '" + str(idMachine) + "' ;")
        self.casUsagers = self.BD.requeteSelection("SELECT ligne FROM Scenarii WHERE id_projet = '" + str(self.numProjet) + "' AND id_casUsage = '" + str(idCas)+ "' AND id_colonne = '" + str(idUsager) + "' ;")
        self.casMachines = self.BD.requeteSelection("SELECT ligne FROM Scenarii WHERE id_projet = '" + str(self.numProjet) + "' AND id_casUsage = '" + str(idCas)+ "' AND id_colonne = '" + str(idMachine) + "' ;")
        print(idCas)
        print(idUsager)
        print(idMachine)

        print(self.casUsagers)
        print(self.casMachines)
        print()

    def selectCas(self):
        self.Cas = self.BD.requeteSelection("SELECT texte FROM CasUsage WHERE id_projet = '" + str(self.numProjet) + "';")

        