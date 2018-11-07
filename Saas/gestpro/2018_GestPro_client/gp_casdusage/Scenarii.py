import random
import sqlite3
import math
from helper import Helper as hlp
from test.test_importlib.util import case_insensitive_tests
from cgitb import text

class Scenarii():
    def __init__(self, parent):
        self.id = parent.project.id
        self.ListeTitleCase = []        # liste grand cas selectionnables
        self.DetailsUser = []
        self.DetailsMachine = []
        self.selectedCase = 0           # le Cas selectionné
        self.projectID = parent.projectID
       
        
        
    def affichageTableau(self):
        self.conn = sqlite3.connect('exemplesSQLITEData.jmd') #establish connection...
        self.curseur = self.conn.cursor()
        
        self.curseur.execute('''select COUNT(id) from CasUsage where projet.id = ?''', self.projectID)
           
        countCases = self.curseur.fetchall()
        for i in range(countCases):
            self.curseur.execute('''select texte from CasUsage JOIN Projet ON Projet.id = CasUsage.id_projet where CasUsage.id = ?''', i)
            self.ListeTitleCase[i] = self.curseur.fetchall
            parent.Vue.afficherScenarii(self.ListeTitleCase)
        
        self.curseur.execute('''Select MAX(ligne) from Scenarii JOIN CasUsage ON Scenarii.id_casUsage = CasUsage.id JOIN Projet ON Projet.id = CasUsage.id_projet''')
        maxLines = self.curseur.fetchall() 
        for k in range(3):
            for j in range(maxLines):
                self.curseur.execute('''Select texte from TypeDonnéScénario JOIN Scenarii ON TypeDonnéeScénario.id = Scenarii.id_donnees where id_colonne = ?''', k)
                TxtColScenariiself[k][j].append(self.curseur.fetchall())
            
        
    def newDataEnteredScenarii(self, textColonne, ScenariiNo, colonneNo, currentCase, lineNb):
        if(ScenariiSelected):
            self.currentProject = self.projectID
            self.currentCase = currentCase;
            for k in range(3):
                self.curseur.execute('''insert into Scenarii values (NULL, ?,  ?,  ?, ?''', self.currentCase, lineNb, textColonne, k)
        

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