# -*- coding: utf-8 -*-

import os,os.path
import sys
import socket
from subprocess import Popen 
import math
from gp_analyse_vue import *
from helper import Helper as hlp
from IdMaker import Id
from gp_analyse_modele import *
from xmlrpc.client import ServerProxy


class Controleur():
    def __init__(self):
        print("IN CONTROLEUR")
        self.connectionServeurCourant()
        self.serveur = ServerProxy(self.adresseServeur)
        
        self.createurId=Id
        self.connectionServeurCourant()
        print(self.serveur)
        self.modele=Modele(self)
        self.vue=Vue(self)
        self.vue.root.mainloop()
        
    def connectionServeurCourant(self):  
        try:
            with open("../adresseServeurCourant.txt", "r") as fichier:
                self.adresseServeur = fichier.read()       
        except Exception as erreur:
            print(erreur)
            try:
                with open("../../../2018_Gestpro_client/adresseServeurCourant.txt", "r") as fichier:
                    self.adresseServeur = fichier.read()  
            except Exception as erreur:
                print(erreur)
                self.adresseServeur = "http://"
                self.adresseServeur += input("Désolé, il y a eu une erreur lors de la détection automatique de l'adresse du serveur, vous pouvez entrer le IP (ex: 10.57.47.7) manuellement: ")
                self.adresseServeur += ":9999"
        try:
            self.serveur = ServerProxy(self.adresseServeur)
        except Exception as erreur:
            print("Désolé, il y a eu un problème avec la connection au serveur, fermeture du module.")
            print(erreur)
            sys.exit(0)


if __name__ == '__main__':
    c=Controleur()