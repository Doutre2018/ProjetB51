# -*- coding: utf-8 -*-

from xmlrpc.client import ServerProxy
from _winapi import NULL


#------------------------------------------------------JFL------------------------------------------------------------------------------#

class ModeleProject():
    #def __init__(self,parent,joueurs,dd):
    def __init__(self,parent):
        print("Hey ho")
        self.parent=parent
        self.connectionServeurCourant()
        self.serveur = ServerProxy(self.adresseServeur)
        self.project = Project(self, self.parent)
        self.nomProjetValidation = None
        self.projects=[]            #pertinence d'une liste avec bd?
        self.projects.append(Project(self, self.parent))
        
    def connectionServeurCourant(self):  
        with open("adresseServeurCourant.txt", "r") as fichier:
            self.adresseServeur = fichier.read()  

class Project():
    def __init__(self, parent, controleur):

        self.controleur = controleur
        self.modele = parent
        self.nom = None
        self.bd = self.modele.serveur
        ######print#####
        testZeroProject = 0

    def testZero(self):
        #print(testZeroProject)
        commande = """SELECT COUNT(id) from Projet"""
        commande += self.ProjectNameToValidate
        testZeroProject = self.bd.selection(commande)
        if testZeroProject > 0:
            pass
        else:
            #parent.nomProjetValidation = 'Default Project Name'
            nom = 'Default Project Name'
            self.createProject(self, nom)
        if(self.createProject(self, nom)):
            return True
        else:
            return False
    
    
    def createProject(self, parent, nomProjet):
        # self.project = project
        self.ProjectNameToValidate = nomProjet
        self.NameFailure = False
        #bd= self.parent.serveur
        print(self.ProjectNameToValidate)
        #On veut valider que pour cette compagnie ce projet a un nom unique
        commande = """SELECT COUNT(id) from Projet JOIN Liaison_Util_Projet ON id_projet = id_Util JOIN Utilisateur ON utilisateur.id = id_util where nom LIKE ("""     #test nom de projet existant
        commande += self.ProjectNameToValidate
        commande += """) and """
        commande += "utilisateur.id_compagnie = 1);"                          #hardcoded value 1 until finalization
        #self.bd.selection(commande)

        
        
        if (0):#self.bd.selection(commande)) > 0:                                    #return false si projet avec nouveau nom
            self.NameFailure = True             
            print("mauvais nom de projet(utilise)")
            self.controleur.failureProjectName()
        else:
            commande = "Insert into Projet (id, nom) values (NULL, "
            commande += self.ProjectNameToValidate
            commande += ");"
            self.bd.insertionperso(commande)


        """
            #test fonctionnalite
        commande_sel = "Select COUNT(nom) from Projet "
        commande_sel += "where Projet.nom LIKE ("
        commande_sel += self.ProjectNameToValidate
        commande_sel += ")"
        
        print(requeteSelection(self, commande_sel))
        """

"""
if __name__ == '__main__':
    modele = ModeleProject(self)

"""

  

				