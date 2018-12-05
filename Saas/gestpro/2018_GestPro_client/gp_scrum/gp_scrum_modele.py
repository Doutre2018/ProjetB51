import os,os.path
import sys
import socket
from subprocess import Popen 
import math
from gp_scrum_vue import *
from helper import Helper as hlp
from IdMaker import Id
from _overlapped import NULL

class Modele():
    def __init__(self, parent):
        self.parent = parent
        self.BD=parent.serveur
        print("Bienvenue dans le modele ..")
        self.numProjet="1"
        self.scrum = []
        
        
    def InsertScrum(self, date):
        pass
        #self.BD.requeteInsetionPerso("INSERT INTO Scrum(id_projet, id_date) VALUES('" + str(self.numProjet) + "', '" + str(date));")