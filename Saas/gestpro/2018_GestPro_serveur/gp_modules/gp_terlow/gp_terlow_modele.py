# -*- encoding: utf-8 -*-

from datetime import datetime

class Modele():
    def __init__(self, referenceControleur):
        self.referenceControleur = referenceControleur
        #self.tests()
        self.listeColonnes = []
        self.generationColonnes()
        self.generationCartes()
        #self.testPrint()
        #self.suppressionColonne(2)
       # self.testPrint()
    
    def tests(self):
        self.referenceControleur.serveur.requeteInsertionPerso("DELETE FROM Colonnes_Terlow")
        self.referenceControleur.serveur.requeteInsertionPerso("INSERT INTO Colonnes_Terlow (ordre, titre) VALUES (1, 'test1')")
        self.referenceControleur.serveur.requeteInsertionPerso("INSERT INTO Colonnes_Terlow (ordre, titre) VALUES (2, 'test2')")
        self.referenceControleur.serveur.requeteInsertionPerso("INSERT INTO Colonnes_Terlow (ordre, titre) VALUES (3, 'test3')")
        self.referenceControleur.serveur.requeteInsertionPerso("INSERT INTO Colonnes_Terlow (ordre, titre) VALUES (4, 'test4')")
            
    def generationColonnes(self):
        try:
            data = self.referenceControleur.serveur.requeteSelection("SELECT * FROM Colonnes_Terlow")
            #print(data)
            for colonne in data:
                self.listeColonnes.append(Colonne(colonne[0], colonne[1], colonne[2]))
        except Exception as erreur:
            print(erreur)   # ->log
       

    def suppressionColonne(self, numColonneASupprimer):
        for i, colonne in enumerate(self.listeColonnes):
            if colonne.ordre == numColonneASupprimer:
                del self.listeColonnes[i]
                break
        for i, colonne in enumerate(self.listeColonnes):
            colonne.ordre = i+1
            
    #à tester
    def generationCartes(self):
        for colonne in self.listeColonnes:
            #stringSelect = "SELECT * FROM Cartes_Terlow WHERE id_colonne = " + colonne.id
            dataCartes = self.referenceControleur.serveur.requeteSelection("SELECT * FROM Cartes_Terlow WHERE id_colonne = " + colonne.id)
            if dataCartes:
                for carte in dataCartes:
                    colonne.listeCartes.append(Carte(carte[0], carte[1], carte[2],  carte[3], carte[4], carte[5]))
                
    #à tester
    #méthode tente de supprimer la carte correspondante, si tout fonctionne, elle retourne true       
    def suppressionCarte(self, numColonneDeCarte, numCarteASupprimer): #p-ê passer l'objet directement?
        for i, colonne in enumerate(self.listeColonnes):
            if colonne.ordre == numColonneDeCarte:
                for j, carte in enumerate(colonne.listeCartes):
                    if carte.ordre == numCarteASupprimer:
                        del colonne.listeCartes[j]
                        return True
        return False
                    
    def testPrint(self):
        for i, colonne in enumerate(self.listeColonnes):
            print("colonne", i+1)
            print("id=", colonne.id)
            print("ordre = ", colonne.ordre)
            print ("titre = ", colonne.titre)

class Colonne():
    def __init__(self, id, ordre, titre, listeCartes = []):
        self.id = id
        self.ordre = ordre
        self.titre = titre
        self.listeCartes = listeCartes

class Carte():
    def __init__(self, id, ordre, texte, dateCreation, estimationTemps = None, datePrevueFin = None):
        self.id = id
        self.ordre = ordre
        self.texte = texte
        self.dateCreation = dateCreation
        self.estimationTemps = estimationTemps
        self.datePrevueFin = datePrevueFin
        
    
    #voir lien suivant pour gestion dates: https://www.pythoncentral.io/advanced-sqlite-usage-in-python/
        
        
        
#section pour tests locaux
if __name__ == "__main__":
    pass