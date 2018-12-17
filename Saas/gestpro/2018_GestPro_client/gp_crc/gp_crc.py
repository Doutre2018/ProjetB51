# -*- coding: utf-8 -*-

import os,os.path
import sys
#import Pyro4
import socket
from subprocess import Popen 
import math
#from sm_projet_modele import *
from gp_crc_vue import *
from helper import Helper as hlp
from IdMaker import Id
from xmlrpc.client import ServerProxy
#import sqlite3



class Controleur():
    def __init__(self):
        cwd = os.getcwd()
<<<<<<< HEAD
        self.serveur = ServerProxy(sys.argv[4], allow_none=True)
=======
        self.connectionServeurCourant()
>>>>>>> ecb373ea65a770e60aa9a9550f4bf918c45fcdc0
        liste = self.serveur.requeteSelection("select price from stocks")
        self.createurId=Id
        self.modele=Modele(self)
        self.vue=Vue(self)
        self.vue.root.mainloop()

class Modele():
    def __init__(self,parent):
        self.parent=parent
        self.serveur=parent.serveur
        self.listeCartes=self.selectClassesCartes()
        #self.listeIDCartes=self.selectIdCarte()
        #for i in self.listeIDCartes:
            #self.listeAttributs.append(selectAttributDeCarte(i))
            
    def selectClassesCartes(self):
        commande ="SELECT classe FROM Cartes"
        #Retourne une liste de String de cartes
        return self.serveur.requeteSelection(commande)
    
    def selectIdCarte(self,classe):
        commande ="SELECT id FROM Cartes WHERE classe="
        commande+= "'" + classe + "'"
        ID = self.serveur.requeteSelection(commande)
        return ID
    
    def selectIdCartePlus(self,classe,id_user):
        pass
    
    def selectAttributDeCarte(self,idCarte):
        commande = "SELECT nomAttributs FROM AttributsCRC WHERE id_classe="
        commande+=str(idCarte)
        #Retourne une liste de String des attributs d'UNE carte
        return self.serveur.requeteSelection(commande)
    
    def selectCollaboDeCarte(self,idCarte):
        commande = "SELECT textCollabo FROM CollaboCRC WHERE id_classe="
        commande+=str(idCarte)
        #Retourne une liste de String des attributs d'UNE carte
        return self.serveur.requeteSelection(commande)
    
    def selectFonctionsDeCarte(self,idCarte):
        commande = "SELECT fonction FROM FonctionsCRC WHERE id_classe="
        commande+=str(idCarte)
        #Retourne une liste de String des attributs d'UNE carte
        return self.serveur.requeteSelection(commande)
    
    def selectObjetsDeCarte(self,idCarte):
        commande = "SELECT objet FROM ObjetsCRC WHERE id_classe="
        commande+=str(idCarte)
        #Retourne une liste de String des attributs d'UNE carte
        return self.serveur.requeteSelection(commande)
    
    def selectCarteHeritage(self,idCarte):
        commande = "SELECT carte_heritage FROM Cartes WHERE id="
        commande+=str(idCarte)
        #Retourne une liste de String des attributs d'UNE carte
        return self.serveur.requeteSelection(commande)
    
    def selectCarteResponsable(self,idCarte):
        commande = "SELECT nom_responsable FROM Cartes WHERE id="
        commande+=str(idCarte)

        #Retourne une liste de String des attributs d'UNE carte
        return self.serveur.requeteSelection(commande)
    
    def selectResponsableCarte(self,id_classe):
        commande="SELECT nom FROM Utilisateur;"
        return self.serveur.requeteSelection(commande)
    
    #Les insertions
    def insertCarte(self,listeValeur):
        self.serveur.requeteInsertionPerso("INSERT INTO Cartes(id_projet, classe, carte_heritage, ordre, nom_responsable) VALUES(  " + str(listeValeur[0]) + ",'" + str(listeValeur[1]) + "','" + str(listeValeur[2]) + "'," + str(listeValeur[3]) + ",'" + str(listeValeur[4]) + "');")
    
    def insertAttributsDeCarte(self,texte,id):
        self.serveur.requeteInsertionPerso("INSERT INTO AttributsCRC(nomAttributs, id_classe) VALUES('" + texte + "', " + id + ");")
 
    def insertCollaboDeCarte(self,id,texte):
        self.serveur.requeteInsertionPerso("INSERT INTO CollaboCRC(id_classe,textCollabo) VALUES(" + id + ",'"+ texte +"') ;")
            
    def insertFonctionDeCarte(self,listeValeur):
        self.serveur.requeteInsertionPerso("INSERT INTO FonctionsCRC(id_classe,fonction) VALUES(" + str(listeValeur[0]) + ","+ str(listeValeur[1]) +");")
        
    def insertObjetDeCarte(self,listeValeur):
        self.serveur.requeteInsertionPerso("INSERT INTO ObjetsCRC(id_classe,objet) VALUES(" + str(listeValeur[0]) + ","+ str(listeValeur[1]) +");")
    
    #Les UPDATE
    def updateCarte(self,idCarte):
        pass                                                                                                                    
    # --------------- DM ---------------
    def updateCRC(self, idCarte, listeCartes):
        commande = "UPDATE Cartes" 
        commande += " SET classe = '" + listeCartes[0] + "', carte_heritage = '" + listeCartes[1] + "', nom_responsable = '" + listeCartes[2] + "'"
        commande += " WHERE id = " + idCarte
        self.serveur.requeteMiseAJour(commande)
        
    def updateAttributsCRC(self, id, texte):
        commande = "UPDATE AttributsCRC SET nomAttributs = '" + texte + "' WHERE id_classe = " + id
        self.serveur.requeteMiseAJour(commande)
        
    def updateFonctionCRC(self, id, texte):
        commande = "UPDATE FonctionsCRC SET fonction = '" + texte + "' WHERE id_classe = " + id
        self.serveur.requeteMiseAJour(commande)
        
    def updateObjetCRC(self, id, texte):
        commande = "UPDATE ObjetsCRC SET objet = '" + texte + "' WHERE id_classe = " + id
        self.serveur.requeteMiseAJour(commande)
        
    def updateCollabCRC(self, id, texte):
        commande = "UPDATE CollaboCRC SET textCollabo = '" + texte + "' WHERE id_classe = " + id
        self.serveur.requeteMiseAJour(commande)
    # ----------------------------------                                                                                        
    def supprimerAttributsDeCarte(self,idCarte):
        commande="DELETE FROM AttributsCRC WHERE id_classe="
        commande+=str(idCarte)
        self.serveur.requeteInsertionPerso(commande)
        
    def supprimerCollaboDeCarte(self,idCarte):
        commande="DELETE FROM CollaboCRC WHERE id_classe="
        commande+=str(idCarte)
        self.serveur.requeteInsertionPerso(commande)
        
    def supprimerFonctionDeCarte(self,idCarte):
        commande="DELETE FROM FonctionsCRC WHERE id_classe="
        commande+=str(idCarte)
        self.serveur.requeteInsertionPerso(commande)     
        
    def supprimerCarte(self,nomCarte):
        commande="DELETE FROM Cartes WHERE classe='"
        commande=commande+str(nomCarte)+"';"
        self.serveur.requeteInsertionPerso(commande)
    
if __name__ == '__main__':
    c=Controleur()