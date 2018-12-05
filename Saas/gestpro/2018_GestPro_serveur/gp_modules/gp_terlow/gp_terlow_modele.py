# -*- encoding: utf-8 -*-

from datetime import datetime

class Modele():
    def __init__(self, referenceControleur):
        self.referenceControleur = referenceControleur
        #self.tests()
        self.referenceControleur.serveur.requeteInsertionDate("INSERT INTO Cartes_Terlow (id_colonne, ordre, texte, dateCreation) VALUES (?, ?, ?, ?)", [1,1,"'test carte'"], "maintenant") 
        print(self.referenceControleur.serveur.requeteSelection("select * from Cartes_Terlow"))
        self.listeColonnes = []
        self.generationColonnes()
        self.creationColonne("test nouvelle creation")
        self.generationCartes()
        self.testPrint()
        
    def tests(self):
        self.referenceControleur.serveur.requeteInsertionPerso("DELETE FROM Colonnes_Terlow")
        self.referenceControleur.serveur.requeteInsertionPerso("INSERT INTO Colonnes_Terlow (ordre, titre) VALUES (1, 'test1')")
        self.referenceControleur.serveur.requeteInsertionPerso("INSERT INTO Colonnes_Terlow (ordre, titre) VALUES (2, 'test2')")
        self.referenceControleur.serveur.requeteInsertionPerso("INSERT INTO Colonnes_Terlow (ordre, titre) VALUES (3, 'test3')")
        self.referenceControleur.serveur.requeteInsertionPerso("INSERT INTO Colonnes_Terlow (ordre, titre) VALUES (4, 'test4')")
        #self.referenceControleur.serveur.requeteInsertionDate(["INSERT INTO Cartes_Terlow (id_colonne, ordre, texte, dateCreation) VALUES (?, ?, ?, ?)", 1,1,"'test carte'", "maintenant"]) 
        
        
    def creationColonne(self, titre):
        if self.listeColonnes:
            ordre = self.listeColonnes[-1].ordre +1
        else:
            ordre = 1
        print("ordre nouvelle colonne", ordre)
        tupleValeurs = (ordre,titre,)
        self.referenceControleur.serveur.requeteInsertionPerso("INSERT INTO Colonnes_Terlow (ordre, titre) VALUES (?, ?)", tupleValeurs )
        self.generationColonnes()
    
    
    def creationCarte(self):
        pass
    
    def generationColonnes(self):
        try:
            data = self.referenceControleur.serveur.requeteSelection("SELECT * FROM Colonnes_Terlow")
            if data:
                self.listeColonnes.clear()
                for colonne in data:
                    self.listeColonnes.append(Colonne(colonne[0], colonne[1], colonne[2], []))
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
            #stringSelect = "SELECT * FROM Cartes_Terlow WHERE id_colonne = ?" 
            #dataCartes = self.referenceControleur.serveur.requeteSelection(stringSelect, colonne.id )
            stringSelect = "SELECT * FROM Cartes_Terlow WHERE id_colonne = " + str(colonne.id )
            dataCartes = self.referenceControleur.serveur.requeteSelection(stringSelect )
            if dataCartes:
                print("colonne id = ", colonne.id, "dataCartes = ", dataCartes)
                for carte in dataCartes:
                    colonne.listeCartes.append(Carte(carte[0], carte[1], carte[2],  carte[3], carte[4] ))
                    print("appending")
                
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
            for carte in colonne.listeCartes:
                print("-------- cartes: -------")
                print("carte id=", carte.id)
                print("carte -> id_colonne = ", carte.id_colonne)
                print("carte ordre = ", carte.ordre)
                print ("carte texte = ", carte.texte)
                print("carte date = ", carte.dateCreation)
                

class Colonne():
    def __init__(self, id, ordre, titre, listeCartes):
        self.id = id
        self.ordre = ordre
        self.titre = titre
        self.listeCartes = listeCartes

class Carte():
    def __init__(self, id, id_colonne, ordre, texte, dateCreation = None, estimationTemps = None, datePrevueFin = None):
        self.id = id
        self.id_colonne = id_colonne
        self.ordre = ordre
        self.texte = texte
        self.dateCreation = dateCreation
        self.estimationTemps = estimationTemps
        self.datePrevueFin = datePrevueFin
        
    
    #voir lien suivant pour gestion dates: https://www.pythoncentral.io/advanced-sqlite-usage-in-python/
        
        
        
#section pour tests locaux
if __name__ == "__main__":
    pass