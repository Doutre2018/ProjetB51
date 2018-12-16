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
    def __init__(self, parent):
        self.parent = parent
        self.bd = self.parent.serveur
        self.idProject = None
        # self.connectionServeurCourant()
        # self.bd = ServerProxy(self.adresseServeur)
        # self.project = Project(self, self.parent)
        self.ProjectNameToValidate = None
        # self.project=Project(self, self.parent)
        print("Hey ho")
        self.firstGo = True;

    def createProject(self, parent, nomProjet, nomCie):
        self.parent = parent
        self.nomCie = nomCie

        # self.project = project

        if self.firstGo:
            self.firstGo = False
        else:
            print(nomProjet)
            self.ProjectNameToValidate = nomProjet
            self.NameFailure = False


            '''
            print("Nom cie" + str(self.nomCie))
            commande_cie = "SELECT id FROM Compagnie WHERE nom LIKE ('"
            commande_cie = str(self.nomCie)
            commande_cie = "');"
            ListReceiver = []
            try:
                ListReceiver[0] = self.parent.parent.serveur.requeteSelection(commande_cie)
            except:
                ListReceiver[0] = -1

            self.noCie =int(ListReceiver[0])
            print("No cie" + self.noCie + self)



            # bd= self.parent.serveur
            # print(self.ProjectNameToValidate)
            # On veut valider que pour cette compagnie ce projet a un nom unique
            commande_sel = "SELECT id FROM Projet "
            commande_sel += "WHERE Projet.nom LIKE ('"
            commande_sel += str(self.ProjectNameToValidate)
            commande_sel += "');"
            ListReceiver = []

            try:
                ListReceiver[0] = self.parent.parent.serveur.requeteSelection(commande_sel)
            except:
                ListReceiver[0] = -1

            '''

            #self.parent.idProject = int(ListReceiver[0])
            #print("Project Id is : " + self.parent.idProject)

            commande = "SELECT Projet.id FROM Projet JOIN Liaison_Util_Projet ON id_projet = id_Util JOIN Utilisateur ON utilisateur.id = id_util WHERE Projet.nom LIKE ('"  # test nom de projet existant
            commande += self.ProjectNameToValidate
            commande += "') and "
            commande += "utilisateur.id_compagnie = '"
            commande += str(self.nomCie)
            commande += "';"
            print(commande)
            try:
                ListReceiver = []

                try:
                    ListReceiver[0] = self.parent.parent.serveur.requeteSelection(commande)
                    ValidationName = False
                except:
                    ListReceiver[0] = -1
                    ValidationName = True
                print(ListReceiver[0])
                validationName = True


            except:
                validationName = False


            print(validationName)
            #number = validationName[0][0]


            if not validationName:
                self.NameFailure = True
                print("mauvais nom de projet(utilise)")
                #self.controleur.failureProjectName()
            else:
                commande = "Insert into Projet (id, nom) values (NULL, '"
                commande += self.ProjectNameToValidate
                commande += "');"
                self.parent.parent.serveur.requeteInsertionPerso(commande)

                commande_sel = "SELECT id FROM Projet "
                commande_sel += "WHERE Projet.nom LIKE ('"
                commande_sel += str(self.ProjectNameToValidate)
                commande_sel += "');"
                self.parent.idProject = self.parent.parent.serveur.requeteSelection(commande_sel)

            print("finish")
            print(self.parent.idProject)
            return 1

    def accessProject(self, parent, projectName, cieID):
        commande = "SELECT Projet.id FROM Projet JOIN Liaison_Util_Projet ON id_projet = id_Util JOIN Utilisateur ON utilisateur.id = id_util WHERE Projet.nom LIKE ('"  # test nom de projet existant
        commande += self.ProjectName
        commande += "') and "
        commande += "utilisateur.id_compagnie = '"
        commande += str(self.cieID)
        commande += "';"

        List = []
        try:
            List[0] = self.parent.parent.serveur.requeteSelection(commande)
            ValidationProject = True
        except:
            List[0] = -1
            ValidationProject = False

        if ValidationProject:
            return 0
        else:
            return 1

