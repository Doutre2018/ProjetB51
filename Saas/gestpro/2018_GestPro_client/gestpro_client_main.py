# -*- coding: utf-8 -*-

import os,os.path
import sys
from xmlrpc.client import ServerProxy
import socket
from subprocess import Popen 
import math
from gestpro_modele import *
from gestpro_vue import *
from helper import Helper as hlp
from IdMaker import Id

class Controleur():
    def __init__(self):
        print("IN CONTROLEUR")
        self.createurId=Id
        self.modele=None
        self.serveur=None
        self.monip=self.trouverIP()
        self.nodeport="9999"
        self.vue=Vue(self,self.monip)
        self.vue.root.mainloop()
        
    def trouverIP(self): # fonction pour trouver le IP en 'pignant' gmail
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # on cree un socket
        s.connect(("gmail.com",80))    # on envoie le ping
        monip=s.getsockname()[0] # on analyse la reponse qui contient l'IP en position 0 
        s.close() # ferme le socket
        return monip
    
    # ----------------DM------------------------ #
    def nomUnique(self, ipserveur, nom):
        if ipserveur and nom:
            ad = "http://"+ipserveur+":"+self.nodeport
            self.serveur=ServerProxy(ad)
            
            if self.serveur.nomUnique(nom):
                return True
            else:
                return False
            
    def nomExiste(self, ipserveur, nom):
        if ipserveur and nom:
            ad = "http://"+ipserveur+":"+self.nodeport
            self.serveur=ServerProxy(ad)
            
            if self.serveur.nomExiste(nom):
                return True
            else:
                return False
    # ------------------------------------------ #
    
    def loginclient(self,ipserveur,nom):
        if ipserveur and nom:
            ad="http://"+ipserveur+":"+self.nodeport
            self.serveur=ServerProxy(ad)
            self.monnom=nom
            rep=self.serveur.loginauserveur(self.monnom)    # on averti le serveur de nous inscrire
            print("reponse du serveur",rep)
            self.vue.chargercentral(rep[2])
            self.serveur.requeteSelection("select * from stocks")
                    
    def requetemodule(self,mod):
        rep=self.serveur.requetemodule(mod)
        if rep:
            print(rep[0])
            cwd=os.getcwd()
            lieuApp="/gp_"+rep[0]
            lieu=cwd+lieuApp
            print(lieu)
            if not os.path.exists(lieu):
                os.mkdir(lieu) #plante s'il exist deja
            reso=rep[1]
            print(rep[1])
            for i in rep[2]:
                if i[0]=="fichier":
                    nom=reso+i[1]
                    rep=self.serveur.requetefichier(nom)
                    fiche=open(lieu+"/"+i[1],"wb")
                    fiche.write(rep.data)
                    fiche.close()
            chaineappli="."+lieuApp+lieuApp+".py"

            self.pid = Popen([sys.executable, chaineappli,self.monnom,self.monip,self.nodeport],shell=0) 
        else:
            print("RIEN")
            
    def fermerprocessus(self):
        self.pid.kill()
        
    def connecteservice(self,rep):  # initalisation locale de la simulation, creation du modele, generation des assets et suppression du layout de lobby
        if rep[1][0][0]=="connecte":
            #print("REP",rep)
            self.modele=Modele(self,rep[1][0][1],rep[1][0][2]) # on cree le modele
            self.vue.afficherinitpartie(self.modele)

            
    def fermeserveur(self):
        if self.serveur:
            self.serveur.jequitte(self.monnom)
    
    def fermefenetre(self):
        print("Client GestPro quitte")
        self.vue.root.destroy()
        
        
if __name__=="__main__":
    c=Controleur()
    print("End GestPro")