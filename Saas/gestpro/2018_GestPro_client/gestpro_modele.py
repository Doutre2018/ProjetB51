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
        self.IDCie = []
        # self.connectionServeurCourant()
        # self.bd = ServerProxy(self.adresseServeur)
        # self.project = Project(self, self.parent)
        self.ProjectNameToValidate = None
        # self.project=Project(self, self.parent)
        print("Hey ho")
        self.firstGo = True;
        self.projectName =None
        self.cieID = None

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
            print("TEEEEEEEEST")
            print("nom cie ds create " + str(self.nomCie))
            commande = "SELECT id FROM compagnie WHERE nomCompagnie LIKE ('"
            commande += self.nomCie
            commande += "');"

            self.cieID = self.parent.parent.serveur.requeteSelection(commande)


            commande = "SELECT Projet.id FROM Projet JOIN Liaison_Util_Projet ON id_projet = id_Util JOIN Utilisateur ON utilisateur.id = id_util WHERE Projet.nom LIKE ('"  # test nom de projet existant
            commande += self.ProjectNameToValidate
            commande += "') and "
            commande += "utilisateur.id_compagnie = '"
            commande += str(self.cieID)
            commande += "';"
            print(commande)

            ListReceiver = []
            validationName = True

            try:
                ListReceiver = self.parent.parent.serveur.requeteSelection(commande)
                print(ListReceiver)
                validationName = False
            except Exception as exc:
                ListReceiver = -1
                validationName = True

                print(ListReceiver)
                #validationName = True

            print(validationName)
            #number = validationName[0][0]


            if validationName:
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

    def accessProject(self, parent, projectName, nomCie):
        self.projectName = projectName
        print(nomCie)
        self.nomCie = nomCie

        commande = "SELECT id FROM compagnie WHERE nomCompagnie LIKE ('"
        commande += self.nomCie
        commande += "');"
        ListTake = []
        self.IDCie = self.parent.parent.serveur.requeteSelection(commande)
        print("no Cie ")
        print(self.IDCie)
        noCIE = self.IDCie[0][0]
        print("number cie =" + str(noCIE))

    #print(self.cieID +" id and projecctname   " + self.projectName)
        commande = "SELECT Projet.id FROM Projet JOIN Liaison_Util_Projet ON projet.id = id_projet JOIN Utilisateur ON utilisateur.id = id_util WHERE Projet.nom LIKE ('"  # test nom de projet existant
        commande += self.projectName
        commande += "') and "
        commande += "utilisateur.id_compagnie = "
        commande += str(noCIE)
        commande += ";"
        print(commande)
        List = []
        test = "SELECT id_compagnie FROM utilisateur WHERE nomUtilisateur = 'jopet';"

        test2 = "SELECT nom FROM projet WHERE id = 12"
        Listetest = []
        Listetest = self.parent.parent.serveur.requeteSelection(test2)
        print(Listetest[0][0])

        List=self.parent.parent.serveur.requeteSelection(test)
        print(List[0][0])
        print("up is cie id in user")

        test4 = "SELECT nom FROM Projet where "
        test4 += self.projectName
        test4 += " = nom;"

        try:
            List = []
            print("1")
            List = self.parent.parent.serveur.requeteSelection(test4)
            print("2")
            idPro = List[0][0]
            print("3")
            print(str(idPro) + "id Projet")
            if idPro > 0:
                ValidationProject = True
            else:
                ValidationProject = False

        except Exception as exc:
            List = -1
            print("oups")
            ValidationProject = False

        if ValidationProject:
            return 1
        else:
            return 0

