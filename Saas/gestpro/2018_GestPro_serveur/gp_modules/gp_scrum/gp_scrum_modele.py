import os,os.path
import sys
import socket
from subprocess import Popen 
import math
from gp_scrum_vue import *
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
        
        
    def insertScrum(self, dateScrum):
        self.BD.requeteInsertionDate("INSERT INTO Scrum(id_projet, date) VALUES(?,?)", [str(self.numProjet)], [dateScrum])
    
    def insertMembreScrum(self, nom, scrumActif):
        for i in scrumActif:
            scrumActif = i
        self.BD.requeteInsertionPerso("INSERT INTO MembreScrum(nom, id_scrum) VALUES('" + str(nom) + "', '" + str(scrumActif+1) + "');")
   
    def insertDonneesMembre(self, accompli, aFaire, probleme, nom):
        print(accompli)
        print(aFaire)
        print(probleme)
        print(nom)
        idMembre = requeteSelection("SELECT id FROM MembreScrum WHERE nom = '" + str(nom) + "';")
        self.BD.requeteInsertionPerso("INSERT INTO DonneesMembreScrum(accompli, aFaire, probleme, id_membre) VALUES('" + str(accompli) + "', '" + str(aFaire) + "', '" + str(probleme) + "', '" + str(idMembre) + "');")
    
    def selectMembres(self, nom):
        idMembre = requeteSelection("SELECT id FROM MembreScrum WHERE nom = '" + str(nom) + "';")
        self.accompli = self.BD.requeteSelection("SELECT accompli FROM DonneesMembreScrum WHERE id_membre = '" + str(idMembre) + "');")
        self.aFaire = self.BD.requeteSelection("SELECT aFaire FROM DonneesMembreScrum WHERE id_membre = '" + str(idMembre) + "');")
        self.probleme = self.BD.requeteSelection("SELECT probleme FROM DonneesMembreScrum WHERE id_membre = '" + str(idMembre) + "');")
        
    def selectScrums(self, numProjet):
        self.numScrum = self.BD.requeteSelection("SELECT id FROM Scrum WHERE id_projet = '" + str(numProjet) + "';")
        print(numScrum)
        #self.lesMembres = self.BD.requeteSelection("SELECT nom FROM MembreScrum WHERE id_scrum = '" + str(numScrumActif) + "';")
        
        