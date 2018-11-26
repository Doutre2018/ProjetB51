# -*- encoding: utf-8 -*-

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
        self.id = parent.project.id
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
        
    def fetchCas(self, parent):
        #self.conn = sqlite3.connect('exemplesSQLITEData.jmd') #establish connection...
        #self.curseur = self.conn.cursor()
        
        #self.curseur.execute('''"select COUNT(id) from CasUsage where projet.id = ?", self.projectID''')
           
        #countCases = self.curseur.fetchall()
        
        nbCasUsage = self.parent.serveur.requeteSelection('''"select COUNT(id) from CasUsage where projet.id = ?", self.projectID''')
        
        
        ListeContenu = []
        ListeContenu.append("test")
        
        for i in range(nbCasUsage):
            #self.parent.serveur.requeteInsertion("Projet", ListeInsert)    
            ListeContenu.append(self.parent.serveur.requeteSelection('''"select texte from CasUsage JOIN Projet ON Projet.id = CasUsage.id_projet where CasUsage.id = ?", i'''))
            
            '''
            self.curseur.execute(select texte from CasUsage JOIN Projet ON Projet.id = CasUsage.id_projet where CasUsage.id = ?, i)
            self.ListeTitleCase[i] = self.curseur.fetchall
            self.parent.Vue.afficherScenarii(self.ListeTitleCase)
            '''
        
        
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