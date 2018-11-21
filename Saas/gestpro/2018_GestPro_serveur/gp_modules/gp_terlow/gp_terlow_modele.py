# -*- encoding: utf-8 -*-

from datetime import datetime

class Modele():
    def __init__(self, referenceControleur):
        self.referenceControleur = referenceControleur
    
    def fetchDataBD(self):
        pass
    
    def creationColonne(self):
        pass
 
    def suppressionColonne(self):
        pass
    
    def creationCarte(self):
        pass
    
    def suppressionCarte(self):
        pass
    
#r�f�rence db
#['Taches_Terlow', ['id','INTEGER','PRIMARY KEY AUTOINCREMENT'], ['ordre','INTEGER',''], ['texte','text','DEFAULT NULL']],
#['Colonnes_Terlow', ['id','INTEGER','PRIMARY KEY AUTOINCREMENT'], ['type','text','']],

class Colonne():
    def __init__(self, ordre, titre, listeCartes):
        self.ordre = ordre
        self.titre = titre
        self.listeCartes = listeCartes


class Carte():
    def __init__(self, ordre, texte, dateCreation, estimationTemps = 0, datePrevueFin = None):
        self.ordre = ordre
        self.texte = texte
        self.dateCreation = dateCreation
        self.estimationTemps = estimationTemps
        self.datePrevueFin = datePrevueFin
        
    
    #voir lien suivant pour gestion dates: https://www.pythoncentral.io/advanced-sqlite-usage-in-python/
        
        
        
#section pour tests locaux
if __name__ == "__main__":
    pass