# -*- encoding: utf-8 -*-

from datetime import datetime

class Modele():
    def __init__(self, referenceControleur):
        self.referenceControleur = referenceControleur
        #self.tests()
        self.data = self.fetchDataBD()
        self.listeColonnes = []
        self.creationColonne()
        #self.testPrint()
        #self.suppressionColonne(2)
       # self.testPrint()
    
    def tests(self):
        self.referenceControleur.serveur.requeteInsertionPerso("DELETE FROM Colonnes_Terlow")
        self.referenceControleur.serveur.requeteInsertionPerso("INSERT INTO Colonnes_Terlow (ordre, titre) VALUES (1, 'test1')")
        self.referenceControleur.serveur.requeteInsertionPerso("INSERT INTO Colonnes_Terlow (ordre, titre) VALUES (2, 'test2')")
        self.referenceControleur.serveur.requeteInsertionPerso("INSERT INTO Colonnes_Terlow (ordre, titre) VALUES (3, 'test3')")
        self.referenceControleur.serveur.requeteInsertionPerso("INSERT INTO Colonnes_Terlow (ordre, titre) VALUES (4, 'test4')")
        
    #méthode qui va chercher les données pour la création des colonnes
    def fetchDataBD(self):
        data = self.referenceControleur.serveur.requeteSelection("SELECT * FROM Colonnes_Terlow")
        print(data)
        return data
        
    def creationColonne(self):
        for colonne in self.data:
            self.listeColonnes.append(Colonne(colonne[0], colonne[1], colonne[2]))

    def suppressionColonne(self, numColonneASupprimer):
        for i, colonne in enumerate(self.listeColonnes):
            if colonne.ordre == numColonneASupprimer:
                del self.listeColonnes[i]
                break
        for i, colonne in enumerate(self.listeColonnes):
            colonne.ordre = i+1
            
            
    def testPrint(self):
        for i, colonne in enumerate(self.listeColonnes):
            print("colonne", i+1)
            print("id=", colonne.id)
            print("ordre = ", colonne.ordre)
            print ("titre = ", colonne.titre)
                
                
                
    
    def creationCarte(self):
        pass
    
    def suppressionCarte(self):
        pass
    
#['Taches_Terlow', ['id','INTEGER','PRIMARY KEY AUTOINCREMENT'], ['ordre','INTEGER',''], ['texte','text','DEFAULT NULL']],
#['Colonnes_Terlow', ['id','INTEGER','PRIMARY KEY AUTOINCREMENT'], ['type','text','']],

class Colonne():
    def __init__(self, id, ordre, titre, listeCartes = []):
        self.id = id
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