import random

import math
from helper import Helper as hlp

'''
class Modele():
    def __init__(self,parent,joueurs,dd):
        self.parent=parent
        self.createurId=self.parent.createurId
        self.mp = ModeleProject(self)
'''        

class ModeleProject():
    
    def __init__(self,parent):
        self.parent = parent
        self.bd = self.parent.serveur
        self.idProject = None
        #self.connectionServeurCourant()
        #self.bd = ServerProxy(self.adresseServeur)
        #self.project = Project(self, self.parent)
        self.ProjectNameToValidate = None
        #self.project=Project(self, self.parent)
        print("Hey ho")
    
            
    def createProject(self, parent, nomProjet, noCie):
        self.parent = parent
                
        # self.project = project
        print(nomProjet)
        self.ProjectNameToValidate = nomProjet
        self.noCie = 1
        self.NameFailure = False
        #bd= self.parent.serveur
        #print(self.ProjectNameToValidate)
        #On veut valider que pour cette compagnie ce projet a un nom unique
        commande = "SELECT COUNT(nom) FROM Projet JOIN Liaison_Util_Projet ON id_projet = id_Util JOIN Utilisateur ON utilisateur.id = id_util WHERE Projet.nom LIKE ('"     #test nom de projet existant
        commande += self.ProjectNameToValidate
        commande += "') and "
        commande += "utilisateur.id_compagnie = '"
        commande += str(self.noCie)
        commande += "';"                          #hardcoded value 1 until finalization
        print(commande)
        validationName = self.parent.parent.serveur.requeteSelection(commande)
        print(validationName)
        number = validationName[0][0]
        print(number)

        if number > 0:              
            self.NameFailure = True             
            print("mauvais nom de projet(utilise)")
            self.controleur.failureProjectName()
        else:
            commande = "Insert into Projet (id, nom) values (NULL, '"
            commande += self.ProjectNameToValidate
            commande += "');"
            self.parent.parent.serveur.requeteInsertionPerso(commande)
            
            
            
            commande_sel = "SELECT id FROM Projet "
            commande_sel += "WHERE Projet.nom LIKE ('"
            commande_sel += str(self.ProjectNameToValidate)
            commande_sel += "');"
            self.parent.idProject =  self.parent.parent.serveur.requeteSelection(commande_sel)
            
        print("finish")    
        print(self.parent.idProject)
        return 1
    
    
    
    