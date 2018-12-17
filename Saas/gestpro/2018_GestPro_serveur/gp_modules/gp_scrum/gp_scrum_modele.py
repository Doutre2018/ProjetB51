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
<<<<<<< HEAD
        self.accompli = None
        self.aFaire = None
        self.probleme = None
=======
        #self.accompli
        #self.aFaire
        #self.probleme
>>>>>>> 5ca2e1500dba67f6a9f2a656ce4f497582daccb9
        
        
    def insertScrum(self, dateScrum):
        self.BD.requeteInsertionDate("INSERT INTO Scrum(id_projet, date) VALUES(?,?)", [str(self.numProjet)], [dateScrum] )
    
    def insertMembresScrum(self):
        #membres = self.BD.requeteSelection("SELECT nomUtilisateur FROM utilisateur WHERE id")
        pass
   
    def selectScrum(self, date):
        pass
    
    def selectMembres(self, nom):
        self.accompli = self.BD.requeteSelection("SELECT accompli FROM MembreScrum WHERE nom = '" + str(nom) + "');")
        self.aFaire = self.BD.requeteSelection("SELECT aFaire FROM MembreScrum WHERE nom = '" + str(nom) + "');")
        self.probleme = self.BD.requeteSelection("SELECT probleme FROM MembreScrum WHERE nom = '" + str(nom) + "');")