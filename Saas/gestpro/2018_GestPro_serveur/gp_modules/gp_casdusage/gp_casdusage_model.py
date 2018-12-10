# -*- coding: utf-8 -*-


#gestion de probleme server closed database


import random
import sqlite3
import math
from xmlrpc.client import ServerProxy
from helper import Helper as hlp
from test.test_importlib.util import case_insensitive_tests
from cgitb import text

class Scenarii():
    def __init__(self, parent):
        self.parent = parent
        
        self.ListeTitleCase = []        # liste grand cas selectionnables
        self.DetailsUser = [[]]
        self.DetailsMachine = [[]]
        self.connectionServeurCourant()
        self.serveur = ServerProxy(self.adresseServeur)
        self.selectedCase = 0           # le Cas selectionne
        self.projectID = parent.projectID
        self.lignes = 0
        
    
        
       
    def connectionServeurCourant(self):  
        with open("adresseServeurCourant.txt", "r") as fichier:
            self.adresseServeur = fichier.read()  
        
    def fetchCas(self):
        commande = "select COUNT(id) from CasUsage where projet.id = "
        commande += self.projectID + ";"
        nbCasUsage = self.serveur.requeteSelection(commande)
        
        #self.serveur.requeteInsertionPerso("INSERT INTO FonctionsCRC(id_classe,fonction) VALUES(" + str(listeValeur[0]) + ","+ str(listeValeur[1]) +");")
        ListeContenu = []
        ListeContenu.append("test")             #DEBUG ONLY
        
        for i in range(nbCasUsage):
            #self.parent.serveur.requeteInsertion("Projet", ListeInsert)    
            commande = "select texte from CasUsage JOIN Projet ON Projet.id = CasUsage.id_projet where CasUsage.id = "
            commande = i + ";"
            ListeContenu.append(self.serveur.requeteSelection(commande))         #cree liste consultable
            
        return ListeContenu    
            
            
#self.curseur.execute('''Select MAX(ligne) from Scenarii JOIN CasUsage ON Scenarii.id_casUsage = CasUsage.id JOIN Projet ON Projet.id = CasUsage.id_projet''')
       # maxLines = self.curseur.fetchall()

        #TxtColScenarii = [[]]
        '''
        for k in range(3):
            for j in range(maxLines):
                self.curseur.execute(Select texte from TypeDonn�Sc�nario JOIN Scenarii ON TypeDonn�eSc�nario.id = Scenarii.id_donnees where id_colonne = ?, k)
                TxtColScenarii[k][j].append(self.curseur.fetchall())
        '''    
        return ListeContenu
        
    def newDataEnteredScenarii(self, textColonne, ScenariiNo, colonneNo, currentCase, lineNb):
            self.currentProject = self.projectID
            self.currentCase = currentCase;
            for k in range(3):
                self.curseur.execute('''insert into Scenarii values (NULL, ?,  ?,  ?, ?''', self.currentCase, lineNb, textColonne, k)
        #current project
        
    def effaceData(self, eraseLine):
        self.eraseline = eraseline
        for i in range(lignes):
            self.serveur.dequeteMiseAJour("UPDATE ")
            
            

    def newDataEnteredCase(self, nomCase, lineAt):
        self.lineAt = lineAt
        self.name = nomCase
        self.curseur.execute(''' insert into CasUsage values (NULL, ?, ?, ?)''', self.projectID, self.lineAt, self.name)
        
        #va falloir pitcher mes inserts dans serveur
        
        
        
        
        
   
        
        
        
        
        
        
       
        #affichage nouveau case
        #affichage fil new data
        #effacer new data
        #effacer cas (tout le data...)
        #positionement new data entry
        #line over line suivi (tracking)
        #nextLine write