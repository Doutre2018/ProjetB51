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
        self.scrums = []
        self.lesMembres = []
        self.dateScrums = []
        self.selectScrums(self.numProjet)
        
        
    def insertScrum(self, dateScrum):
        self.BD.requeteInsertionDate("INSERT INTO Scrum(id_projet, date) VALUES(?,?)", [str(self.numProjet)], [dateScrum])
    
    def insertMembreScrum(self, nom, scrumActif):
        for i in scrumActif:
            scrumActif = i
        self.BD.requeteInsertionPerso("INSERT INTO MembreScrum(nom, id_scrum) VALUES('" + str(nom) + "', '" + str(scrumActif+1) + "');")
   
    def insertDonneesMembre(self, accompli, aFaire, probleme, nom):
        idMembre = self.BD.requeteSelection("SELECT id FROM MembreScrum WHERE nom = '" + str(nom) + "';")
        for i in idMembre:
            for k in i:
                idMembre = k
        self.BD.requeteInsertionPerso("INSERT INTO DonneesMembreScrum(accompli, aFaire, probleme, id_membre) VALUES('" + str(accompli) + "', '" + str(aFaire) + "', '" + str(probleme) + "', '" + str(idMembre) + "');")
    
    def selectMembres(self, nom):
        idMembre = self.BD.requeteSelection("SELECT id FROM MembreScrum WHERE nom = '" + str(nom) + "';")
        self.accompli = self.BD.requeteSelection("SELECT accompli FROM DonneesMembreScrum WHERE id_membre = '" + str(idMembre) + "');")
        self.aFaire = self.BD.requeteSelection("SELECT aFaire FROM DonneesMembreScrum WHERE id_membre = '" + str(idMembre) + "');")
        self.probleme = self.BD.requeteSelection("SELECT probleme FROM DonneesMembreScrum WHERE id_membre = '" + str(idMembre) + "');")
        
    def selectScrums(self, numProjet):
        self.scrums = self.BD.requeteSelection("SELECT id FROM Scrum WHERE id_projet = '" + str(numProjet) + "';")
        self.dateScrums = self.BD.requeteSelection("SELECT date FROM Scrum WHERE id_projet = '" + str(numProjet) + "';")
        print(self.scrums)
        #for i in scrums:
        #    self.lesMembres.append(self.BD.requeteSelection("SELECT nom FROM MembreScrum WHERE id_scrum = '" + str(numScrum) + "';"))
        #self.lesMembres = self.BD.requeteSelection("SELECT nom FROM MembreScrum WHERE id_scrum = '" + str(numScrum) + "';")
        
        