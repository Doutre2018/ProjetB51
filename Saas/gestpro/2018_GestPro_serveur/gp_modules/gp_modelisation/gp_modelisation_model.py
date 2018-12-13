import os,os.path
import sys
import socket
from subprocess import Popen 
import math
from gp_modelisation_vue import *
from helper import Helper as hlp
from IdMaker import Id
from _overlapped import NULL

class Modele():
    def __init__(self, parent):
        self.parent = parent
        self.BD=parent.serveur
        self.numProjet="1"
        self.cartes = []
        self.noms = []
        self.types = []
        self.conts = []
        self.selectAffichageCartes()
            
    def insertIntoCarte(self, nomCarte):
        self.BD.requeteInsertionPerso("INSERT INTO CartesDonnees(nom, id_projet) VALUES('" + str(nomCarte) + "', '" + str(self.numProjet) + "');")
        
    def insertIntoItem(self, nom, type, contrainte, nomCarte):
        idCarte = self.BD.requeteSelection("SELECT id FROM CartesDonnees WHERE nom = '" + str(nomCarte) + "';")
        for i in idCarte:
            for n in i:
                idCarte = n
        self.BD.requeteInsertionPerso("INSERT INTO ItemDonnees(nom, type, contrainte, id_carte) VALUES('" + str(nom) + "', '" + str(type) + "', '" + str(contrainte) + "', '" + str(idCarte) + "');")
    
    def selectAffichageCartes(self):
        self.cartes = self.BD.requeteSelection("SELECT nom FROM CartesDonnees WHERE id_projet = 1")
    
    def selectAffichageItemNom(self, nomCarte):
        self.noms = self.BD.requeteSelection("SELECT nom FROM ItemDonnees WHERE id_carte = (SELECT id FROM CartesDonnees WHERE nom = '" + nomCarte + "');")
        
    def selectAffichageItemType(self, nomCarte):
        self.types = self.BD.requeteSelection("SELECT type FROM ItemDonnees WHERE id_carte = (SELECT id FROM CartesDonnees WHERE nom = '" + str(nomCarte) + "');")

    def selectAffichageItemCon(self, nomCarte):
        self.conts = self.BD.requeteSelection("SELECT contrainte FROM ItemDonnees WHERE id_carte = (SELECT id FROM CartesDonnees WHERE nom = '" + str(nomCarte) + "');")
        