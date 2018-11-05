# -*- encoding: utf-8 -*-

#import Pyro4
from xmlrpc.server import SimpleXMLRPCServer

import xmlrpc.client

import os,os.path
from threading import Timer
import sys
import socket
import time
import random


s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("gmail.com",80))
monip=s.getsockname()[0]
print("MON IP SERVEUR",monip)
s.close()

#daemon = Pyro4.core.Daemon(host=monip,port=9999) 
daemon= SimpleXMLRPCServer((monip,9999), logRequests = False)

class Client(object):
    def __init__(self,nom):
        self.nom=nom
        
class ModeleService(object):
    def __init__(self,parent,rdseed):
        self.parent=parent
        self.rdseed=rdseed
        self.modulesdisponibles={"projet":"gp_projet",
                                 "sql":"gp_sql",
                                 "mandat":"gp_mandat",

                                 "inscription":"gp_inscription"}
        self.clients={}
        
    def creerclient(self,nom):
        if nom in self.clients.keys(): # on assure un nom unique
            return [0,"Erreur de nom"]
        # tout va bien on cree le client et lui retourne la seed pour le random
        c=Client(nom)
        self.clients[nom]=c
        return [1,"Bienvenue",list(self.modulesdisponibles.keys())]
            
class ControleurServeur(object):
    def __init__(self):
        rand=random.randrange(1000)+1000
        self.modele=ModeleService(self,rand)
        
    def loginauserveur(self,nom):
        rep=self.modele.creerclient(nom)
        return rep

    def requetemodule(self,mod):
        if mod in self.modele.modulesdisponibles.keys():
            cwd=os.getcwd()
            if os.path.exists(cwd+"/gp_modules/"):
                dirmod=cwd+"/gp_modules/"+self.modele.modulesdisponibles[mod]+"/"
                if os.path.exists(dirmod):
                    listefichiers=[]
                    for i in os.listdir(dirmod):
                        if os.path.isfile(dirmod+i):
                            val=["fichier",i]
                        else:
                            val=["dossier",i]
                            
                        listefichiers.append(val)
                    return [mod,dirmod,listefichiers]
            
    def requetefichier(self,lieu):
        fiche=open(lieu,"rb")
        contenub=fiche.read()
        fiche.close()
        return xmlrpc.client.Binary(contenub)
            
        
    def quitter(self):
        t=Timer(1,self.fermer)
        t.start()
        return "ferme"
    
    def jequitte(self,nom):
        del self.modele.clients[nom]
        del self.modele.cadreDelta[nom]
        if not self.modele.clients:
            self.quitter()
        return 1
    
    def fermer(self):
        print("FERMETURE DU SERVEUR")
        daemon.shutdown()

controleurServeur=ControleurServeur()
daemon.register_instance(controleurServeur)  
 
print("Serveur XML-RPC actif")
daemon.serve_forever()