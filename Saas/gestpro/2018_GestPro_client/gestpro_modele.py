import random

import math
from helper import Helper as hlp

import random

import math
from helper import Helper as hlp




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
        self.firstGo = True
        self.firstGoAccess = True
        self.projectName = None
        self.cieID = None

    def createProject(self, parent, nomProjet, nomUser, nomCie):
        self.parent = parent
        self.nomCie = nomCie

        # self.project = project

        if self.firstGo:
            self.firstGo = False
        else:
            print(nomProjet)
            self.ProjectNameToValidate = nomProjet
            self.NameFailure = False

           

            commande_sel = "SELECT id FROM Projet "
            commande_sel += "WHERE Projet.nom LIKE ('"
            commande_sel += str(self.ProjectNameToValidate)
            commande_sel += "');"
            try:
                self.parent.idProject = self.parent.parent.serveur.requeteSelection(commande_sel)
            except:
                pass


            commande = "SELECT id FROM compagnie WHERE nomCompagnie LIKE = "
            commande += self.nomCie
            commande += ";"

            self.cieID = self.parent.parent.serveur.requeteSelection(commande)
            for i in self.cieID:
                for n in i:
                    self.cieID = n

            commande = "SELECT Projet.id FROM Projet JOIN Liaison_Util_Projet ON Projet.id = Liaison_Util_Projet.id_projet JOIN Utilisateur ON utilisateur.id = Liaison_Util_Projet.id_util WHERE Projet.nom LIKE ('"  # test nom de projet existant
            commande += self.ProjectNameToValidate
            commande += "') and "
            commande += "utilisateur.id_compagnie = '"
            commande += str(self.cieID)
            commande += "';"
            #print("commmande select validation nom dans table projet" + commande)

            ListReceiver = []
            validationName = True

            try:
                ListReceiver = self.parent.parent.serveur.requeteSelection(commande)
                for i in ListReceiver:
                    for n in i:
                        ListReceiver = n
                print("List receiver" + str(ListReceiver))
                validationName = False
            except Exception as exc:
                ListReceiver = -1
                validationName = True
                print("liste receiver = " + str(ListReceiver))
                # validationName = True

            print(validationName)
            # number = validationName[0][0]


            if validationName:
                self.NameFailure = True
                print("mauvais nom de projet(utilise)")
                # self.controleur.failureProjectName()
            else:
                # genere les instertion projet et table de liaison projet et utilisateur
                commande = "Insert into Projet (id, nom) values (NULL, '"
                commande += self.ProjectNameToValidate
                commande += "');"
                self.parent.parent.serveur.requeteInsertionPerso(commande)

                commandeUserID = "Select id FROM utilisateur where nomUtilisateur "
                commandeUserID += " LIKE ('"
                commandeUserID += str(nomUser)
                commandeUserID += "');"

                print("commande user id")
                print(commandeUserID)
                
                try:
                    ID_utilisateur = self.parent.parent.serveur.requeteSelection(commandeUserID)
                except:
                    pass
                
                for i in ID_utilisateur:
                    for n in i:
                        ID_utilisateur = n

                commandeIDprojet = "Select id FROM projet where nom"
                commandeIDprojet += " LIKE ('"
                commandeIDprojet += str(nomProjet)
                commandeIDprojet += "');"
                try:
                    ID_projet = self.parent.parent.serveur.requeteSelection(commandeIDprojet)
                except:
                    pass
                
                for i in ID_projet:
                    for n in i:
                        ID_projet = n

                print("id utilisateur")
                print(ID_utilisateur)

                commande_plus = "Insert into Liaison_Util_Projet (id_util, id_projet, role) Values ("
                commande_plus += str(ID_utilisateur)
                commande_plus += ", "
                commande_plus += str(ID_projet)
                commande_plus += ", 'programmeur');"

                print(commande_plus)
                try:
                    self.parent.parent.serveur.requeteInsertionPerso(commande_plus)
                except:
                    pass
                
                return 1

            

    def accessProject(self, parent, projectName, nomCie):
        self.projectName = projectName
        print(nomCie)
        self.nomCie = nomCie
        print("parameters :", projectName + "  " + nomCie)
        commande = "SELECT id FROM compagnie WHERE nomCompagnie = "
        commande += str(self.nomCie)
        commande += ";"
        #print(commande)
        #print("no Cie ")
        #print(self.parent.parent)
       
        try: 
            self.IDCie = self.parent.parent.serveur.requeteSelection(commande)
        except:
            pass
            
        print(self.IDCie)
        for i in self.IDCie:
            for n in i:
                noCIE = n
        

        # SELECT Projet.id FROM Projet JOIN Liaison_Util_Projet ON Projet.id = Liaison_Util_Projet.id_projet JOIN Utilisateur ON utilisateur.id = Liaison_Util_Projet.id_util WHERE Projet.nom LIKE ('alicia') and utilisateur.id_compagnie = '4';
        #print(self.cieID +" id and projecctname   " + self.projectName)
        commande = "SELECT Projet.id FROM Projet JOIN Liaison_Util_Projet ON projet.id = Liaison_Util_Projet.id_projet JOIN Utilisateur ON utilisateur.id = Liaison_Util_Projet.id_util WHERE projet.nom LIKE('"
        commande += self.projectName
        commande += "')  and "
        commande += "utilisateur.id_compagnie = "
        commande += str(noCIE)
        commande += ";"
        

        try:
            List = []
            
            try:
                List = self.parent.parent.serveur.requeteSelection(commande)
            except:
                pass
            for i in List:
                for n in i:
                    List = n
            
            idPro = List
            
            print(str(idPro) + " id Projet")
            if idPro > 0:
                ValidationProject = True
            else:
                ValidationProject = False

        except Exception as exc:
            List = -1
            print("oups")
            ValidationProject = False

