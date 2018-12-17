import os,os.path
import sys
import socket
from subprocess import Popen 
import math
from helper import Helper as hlp
from IdMaker import Id
from _overlapped import NULL

class Modele():
    def __init__(self, parent):
        self.parent = parent
        self.BD=parent.serveur


    def sauvegarde(self,listeObjet):
        for objet in listeObjet :
           self.BD.requeteInsertionPerso("INSERT INTO Objet_Maquette(Type, PosX,PosY,X,Y,Bordure,Interieur,Texte, Font) VALUES('" + str(objet[0]) +"','"+ str(objet[1]) +"','"+ str(objet[2]) +"','"+ str(objet[3]) +"','"+ str(objet[4]) +"','"+ str(objet[5]) +"','"+ str(objet[6]) +"','"+ str(objet[7]) +"','"+ str(objet[8]) + "');")
            
                    
    def selectAffichage(self):
            self.listeObjets = []
            for idtab in self.BD.requeteSelection("SELECT id FROM Objet_Maquette") :
                objet = []
                id = idtab[0]
                objet.append(str((self.BD.requeteSelection("SELECT Type FROM Objet_Maquette WHERE id ='" + str(id) + "';"))))
                objet.append(self.BD.requeteSelection("SELECT PosX FROM Objet_Maquette WHERE id ='" + str(id) + "';"))
                objet.append((self.BD.requeteSelection("SELECT PosY FROM Objet_Maquette WHERE id ='" + str(id) + "';")))
                objet.append((self.BD.requeteSelection("SELECT X FROM Objet_Maquette WHERE id ='" + str(id) + "';")))
                objet.append((self.BD.requeteSelection("SELECT Y FROM Objet_Maquette WHERE id ='" + str(id) + "';")))
                objet.append((self.BD.requeteSelection("SELECT Bordure FROM Objet_Maquette WHERE id ='" + str(id) + "';")))
                objet.append((self.BD.requeteSelection("SELECT Interieur FROM Objet_Maquette WHERE id ='" + str(id) + "';")))
                objet.append((self.BD.requeteSelection("SELECT Texte FROM Objet_Maquette WHERE id ='" + str(id) + "';")))
                objet.append((self.BD.requeteSelection("SELECT Font FROM Objet_Maquette WHERE id ='" + str(id) + "';")))

                print(objet)
                for i in range(0,len(objet)):
                    value = objet[i]
                    objet[i]=value[0]
                for i in range(0,len(objet)):
                    value = objet[i]
                    objet[i]=value[0]
                
            
                objet.append(id)    
                print(objet)
                print()
                self.listeObjets.append(objet)   
                