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
        print("Bienvenue dans le modele ..")


    def sauvegarde(self,listeObjet):
        for objet in listeObjet :
           self.BD.requeteInsertionPerso("INSERT INTO Objet_Maquette(Type, PosX,PosY,X,Y,Bordure,Interieur,texte, Font) VALUES('" + str(objet[0]) +"','"+ str(objet[1]) +"','"+ str(objet[2]) +"','"+ str(objet[3]) +"','"+ str(objet[4]) +"','"+ str(objet[5]) +"','"+ str(objet[6]) +"','"+ str(objet[7]) +"','"+ str(objet[8]) + "');")
            
                    
    def selectAffichage(self):
        try :
            self.listeObjets = self.BD.requeteSelection("SELECT * FROM Objet_Maquette")
        except:
            pass
        