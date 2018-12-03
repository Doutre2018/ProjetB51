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
import sqlite3
import csv
from datetime import datetime
import atexit


#s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#s.connect(("gmail.com",80))
#monip=s.getsockname()[0]
IP = socket.gethostbyname(socket.getfqdn())
print("MON IP SERVEUR",IP)
#s.close()

#daemon = Pyro4.core.Daemon(host=monip,port=9999) 
daemon= SimpleXMLRPCServer((IP,9999), logRequests = False)


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
                                 "scrum":"gp_scrum",
                                 "analyse":"gp_analyse",
                                 "casdusage":"gp_casdusage",
                                 "maquette":"gp_maquette",
                                 "crc":"gp_crc",
                                 "budget":"gp_budget",
                                 "tchat":"gp_tchat",
                                 "modelisation":"gp_modelisation",
                                 "terlow":"gp_terlow",
                                 "inscription":"gp_inscription"}
        self.clients={}
        self.baseDonnees = BaseDonnees()
        self.adresseServeur = "http://"+str(IP) + ":" + str(9999)
        daemon.register_function(self.getAdresse)
        daemon.register_function(self.requeteInsertion)
        daemon.register_function(self.requeteSelection)
        daemon.register_function(self.requeteMiseAJour)
        daemon.register_function(self.requeteInsertionPerso)
        daemon.register_function(self.requeteFichier)
        daemon.register_function(self.logErreur)
        daemon.register_introspection_functions()
        
    def creerclient(self,nom):
        #if nom in self.clients.keys(): # on assure un nom unique
        #    return [0,"Erreur de nom"]
        # tout va bien on cree le client et lui retourne la seed pour le random
        c=Client(nom)
        self.clients[nom]=c
        return [1,"Bienvenue",list(self.modulesdisponibles.keys())]
    
    # -------------------DM------------------- #
    def inscription(self, nom, motPasse):
        if self.nomUnique(nom):                       # Vérifie que le nom d'utilisateur est unique
            commande = "INSERT INTO Utilisateur(nomUtilisateur, motDePasse, chemin_acces_csv) VALUES ('" + nom + "', '" + motPasse + "', NULL)"
            self.requeteInsertionPerso(commande)      # Insert dans la DB du nouvel utilisateur
            rep = nom + " inscrit!"
            return  rep
        
        else:
            rep = nom + " n'est pas disponible"
            return rep
    
    def nomUnique(self, nom):
        commande = "SELECT nomUtilisateur FROM Utilisateur WHERE nomUtilisateur = '" + nom + "'"
        sql = self.requeteSelection(commande)        # Requête de SELECT à la BD pour chercher le nom transmis
        if sql:
            return False                             # Si le nom est trouvé dans la BD (rep non vide)
        else:
            return True                              # Si le nom n'est pas dans la BD (rep vide)
        
    def userExiste(self, nom, motPasse):
        commande = "SELECT motDePasse FROM Utilisateur WHERE nomUtilisateur = '" + nom + "'"
        sql = self.requeteSelection(commande)       # Requête à la BD pour chercher le mot de passe associé au nom d'utilisateur
        
        if sql:                                     # Si le nom d'utilisateur a été trouvé
            temp = sql[0]                           # Change le tuple en liste
            if motPasse in temp:                    # Cherche le mot de passe transmis dans la liste
                return True
            
        return False                                # Si au moins une condition n'est pas bonne

        # ???
        #self.requeteInsertionPerso("INSERT INTO Utilisateur(nomUtilisateur, motDePasse, chemin_acces_csv) VALUES (" + "'" + nom + "'" + ", NULL, NULL)")      # Insert dans la DB du nouvel utilisateur
        #return True                             # Si le nom n'est pas trouvé dans la liste
    
    def nomExiste(self, nom):
        liste = self.listeNoms()
        for n in liste:                         # Parcours les noms dans la liste
            if n == nom:                        # Compare le nom à la liste de nom
                return True                     # Nom existe déjà, donc pas unique 

        return False                            # Si le nom n'est pas trouvé dans la liste
    # ---------------------------------------- #
            
    #méthode tampon pour insert les données dans la table de la BD du serveur selon le format suivant: nomTable = "string représentant nom", liste valeurs = [10, 'texte1', 50.3]
    def requeteInsertion(self, nomTable, listeValeurs ):
        self.baseDonnees.connecteur = sqlite3.connect('SAAS.db')
        self.baseDonnees.curseur = self.baseDonnees.connecteur.cursor()
        self.baseDonnees.insertion(nomTable, listeValeurs)
        self.baseDonnees.connecteur.close()
        return True
    
    def requeteInsertionPerso(self,commande):
        self.baseDonnees.connecteur = sqlite3.connect('SAAS.db')
        self.baseDonnees.curseur = self.baseDonnees.connecteur.cursor()
        self.baseDonnees.insertionPerso(commande)
        self.baseDonnees.connecteur.close()
        return True
    
   #méthode tampon pour mettre à jour des données d'une table. Il faut passer une string représentant l'ensemble de la requête update dans la fonction
    def requeteMiseAJour(self,stringUpdate):
        self.baseDonnees.connecteur = sqlite3.connect('SAAS.db')
        self.baseDonnees.curseur = self.baseDonnees.connecteur.cursor()
        self.baseDonnees.miseAJour(stringUpdate)
        self.baseDonnees.connecteur.close()
        return True
    
    #méthode tampon qui retourne une liste. Chaque élément de la liste correspond à une rangée du select demandé.
    def requeteSelection(self, stringSelect):
        listeSelect  = self.baseDonnees.selection(stringSelect)
        return listeSelect
    
    def getAdresse(self):
        return self.adresseServeur
    
    def requeteFichier(self, cheminFichier):
        with open(cheminFichier, "rb") as handle:
            return xmlrpc.client.Binary(handle.read())

    def logErreur(self,date, adresseIP, message):
        with open("log.csv", 'a+', newline = '') as handler:
            writer = csv.writer(handler, delimiter = ';') 
            row =[date,  adresseIP,  message]
            writer.writerow(row)
        return True
            
class ControleurServeur(object):
    def __init__(self):
        rand=random.randrange(1000)+1000
        self.modele=ModeleService(self,rand)

     
    def checkBase(self):
        pass
            
    def loginauserveur(self,nom):
        rep=self.modele.creerclient(nom)
        return rep
    
    # ------------------DM-------------------- #
    def inscription(self, nom, motPasse):
        return self.modele.inscription(nom, motPasse)
    
    def connexion(self, nom, motPasse):
        if self.modele.userExiste(nom, motPasse):       # Vérifie le nom d'utilisateur et mot de passe
            return self.loginauserveur(nom)
        else:
            return False
    # ---------------------------------------- #

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
        timerFermeture = Timer(1,self.fermer).start()
        return "ferme"
    
    def jequitte(self,nom):
        del self.modele.clients[nom]
        del self.modele.cadreDelta[nom]
        if not self.modele.clients:
            self.quitter()
        return 1
    
    def fermer(self):
        daemon.shutdown()

class  BaseDonnees():
    def __init__(self):
        #if os.path.exists("SAAS.db"):
            #os.remove("SAAS.db")
        #else:
            #print("Creation du fichier SAAS.db initial")
        self.connecteur = sqlite3.connect('SAAS.db')
        self.curseur = self.connecteur.cursor()
        self.creerTables(self.genererListeTables(),self.genererListeConst())
        #self.insertion('stocks', [1])
        self.connecteur.commit()
        self.selection("select * from stocks")
        self.connecteur.close()

        
    
    def genererListeTables(self):
        listeTables = [ 
            ['stocks', ['price', 'INTEGER', '']],
            ['Serveurs', ['id','INTEGER','PRIMARY KEY AUTOINCREMENT'], ['IP','INTEGER',''], ['nom','text','UNIQUE']],
            ['Utilisateur', ['id','INTEGER','PRIMARY KEY AUTOINCREMENT'], ['nomUtilisateur','text','UNIQUE'], ['motDePasse','text',''], ['chemin_acces_csv','text','']],
            ['Projet', ['id','INTEGER','PRIMARY KEY AUTOINCREMENT'], ['nom','text','UNIQUE']],
            ['Liaison_Util_Projet', ['role','text','']],
            ['AnalyseTextuelle', ['id','INTEGER','PRIMARY KEY AUTOINCREMENT'], ['ligne','INTEGER',''],['colonne','INTEGER',''],['mot','text','']],
            ['TypeMot', ['id','INTEGER','PRIMARY KEY AUTOINCREMENT'], ['nom','text','']],
            ['LigneChat', ['id','INTEGER','PRIMARY KEY AUTOINCREMENT'], ['date','date',''],['texte','text','']],
            ['CasUsage', ['id','INTEGER','PRIMARY KEY AUTOINCREMENT'],['ligne','text',''],['texte','text','']],
            ['Scenarii', ['id','INTEGER','PRIMARY KEY AUTOINCREMENT'],['ligne','text','']],
            ['FonctionsCRC', ['id','INTEGER','PRIMARY KEY AUTOINCREMENT'],['fonction','text','']],
            ['CollaboCRC', ['id','INTEGER','PRIMARY KEY AUTOINCREMENT'],['textCollabo','text','']],
            ['FilDeDiscussion', ['id','INTEGER','PRIMARY KEY AUTOINCREMENT']],
            ['TypeForme', ['id','INTEGER','PRIMARY KEY AUTOINCREMENT'], ['nom','text','']],
            ['Objet_Maquette', ['id','INTEGER','PRIMARY KEY AUTOINCREMENT'], ['hauteur','real',''], ['largeur','real',''], ['fill_couleur','real','NULL']],
            ['ColonnesScenarii', ['id','INTEGER','PRIMARY KEY AUTOINCREMENT'], ['nom','text',''], ['numero_position','INTEGER','']],
            ['Cartes', ['id','INTEGER','PRIMARY KEY AUTOINCREMENT'], ['classe','text',''], ['ordre','INTEGER',''],['carte_heritage','text',''],['nom_responsable','text','']],
            ['AttributsCRC', ['id','INTEGER','PRIMARY KEY AUTOINCREMENT'], ['nomAttributs','text','']],
            ['Sprint', ['id','INTEGER','PRIMARY KEY AUTOINCREMENT'], ['ordre','INTEGER',''], ['date','date','']],
            ['Tache_Sprint', ['id','INTEGER','PRIMARY KEY AUTOINCREMENT'], ['description','text',''], ['nom','text',''], ['duree','INTEGER','']],
            ['Taches_Terlow', ['id','INTEGER','PRIMARY KEY AUTOINCREMENT'], ['ordre','INTEGER',''], ['texte','text','DEFAULT NULL']],
            #['Colonnes_Terlow', ['id','INTEGER','PRIMARY KEY AUTOINCREMENT'], ['ordre', 'INTEGER', ''], ['titre','text','']],
            ['Objet_Texte', ['id','INTEGER','PRIMARY KEY AUTOINCREMENT'], ['texte','text','']],
            ['Position',['id','INTEGER','PRIMARY KEY AUTOINCREMENT'],['x','real','NOT NULL'],['y','real','NOT NULL']],
            ['Compagnie',['id','INTEGER','PRIMARY KEY AUTOINCREMENT'],['nomCompagnie','text','NOT NULL']]
            ]
        return listeTables
    
    def genererListeConst(self):
        listeConst = [
            ['LigneChat', 'id_utilisateur','INTEGER', 'Utilisateur', 'id'],
            ['LigneChat', 'id_filDiscussion','INTEGER', 'filDeDiscussion', 'id'],
            ['AnalyseTextuelle', 'id_type','INTEGER', 'TypeMot', 'id'],
            ['AnalyseTextuelle', 'id_projet','INTEGER', 'Projet', 'id'],
            ['Liaison_Util_Projet', 'id_util','INTEGER', 'Utilisateur', 'id'],
            ['Liaison_Util_Projet', 'id_projet','INTEGER', 'Projet', 'id'],
            ['FilDeDiscussion', 'id_projet','INTEGER', 'Projet', 'id'],
            ['CollaboCRC', 'id_classe','INTEGER', 'Cartes', 'id'],
            ['FonctionsCRC', 'id_classe','INTEGER', 'Cartes', 'id'],
            ['Scenarii', 'id_casUsage','INTEGER', 'CasUsage', 'id'],
            ['Scenarii', 'id_colonne','INTEGER', 'ColonnesScenarii', 'id'],
            ['AttributsCRC', 'id_classe','INTEGER', 'Cartes', 'id'],
            ['Cartes', 'id_projet','INTEGER', 'Projet', 'id'],
            ['Objet_Maquette', 'id_position','INTEGER', 'Position', 'id'],
            ['Objet_Maquette', 'id_type','INTEGER', 'TypeForme', 'id'],
            ['Taches_Terlow', 'id_projet','INTEGER', 'Projet', 'id'],
            ['Taches_Terlow', 'id_colonne_terlow','INTEGER', 'Colonnes_Terlow', 'id'],
            ['Objet_Texte', 'id_position','INTEGER', 'Position', 'id'],
            ['Tache_Sprint','id_sprint','INTEGER', 'Sprint', 'id'],
            ['Sprint', 'id_projet', 'INTEGER',  'Projet', 'id'],
            ['Utilisateur', 'id_compagnie', 'INTEGER',  'Compagnie', 'id'],
            ]
        return listeConst
        
    def creerTables(self, listeTables, listeConst):
        for table in listeTables:
            stringCreate = "CREATE TABLE IF NOT EXISTS " + table[0] + "(" 
            for indiceEntrees in range(len(table)):
                if indiceEntrees > 0:
                    stringCreate +=  table[indiceEntrees][0] + " " + table[indiceEntrees][1] + " " + table[indiceEntrees][2]
                    if indiceEntrees < len(table)-1:
                        stringCreate += ", "
            stringCreate += ")"
            self.curseur.execute(stringCreate)
        self.alterTable(listeConst)
        self.curseur.execute("CREATE TABLE IF NOT EXISTS Colonnes_Terlow (id INTEGER PRIMARY KEY AUTOINCREMENT, ordre INTEGER, titre text, CONSTRAINT ordre_unique UNIQUE (ordre)) ")
                
    
    
    def insertion(self, nomTable = "", listeValeurs=[]):
        stringInsert = "INSERT INTO " + nomTable + " VALUES("
        for indiceEntree in range(len(listeValeurs)):
            if isinstance(listeValeurs[indiceEntree],str):
                listeValeurs[indiceEntree] = "'"+listeValeurs[indiceEntree]+"'"
                stringInsert += listeValeurs[indiceEntree]
            else:
                stringInsert += str(listeValeurs[indiceEntree])
            if indiceEntree < len(listeValeurs)-1:
                stringInsert += ", "
        stringInsert += ")"
        self.curseur.execute(stringInsert)
    
    
    def selection(self, stringSelect):
        connecteur = sqlite3.connect('SAAS.db')
        curseur = connecteur.cursor()
        listeData=[]
        for rangee in curseur.execute(stringSelect):
            listeData.append(rangee)
        connecteur.close()
        return listeData
            
    def alterTable(self,listeConst):
        try:
            for contrainte in listeConst:
                stringAlterTable = "ALTER TABLE " + contrainte[0] + " ADD COLUMN " + contrainte[1] + " " + contrainte[2] + " REFERENCES " + contrainte[3] + "(" + contrainte[4] + ");"
                self.curseur.execute(stringAlterTable)
        except:
            pass
            #print("contraintes existent")
    
    def insertionPerso(self,commande):
        self.curseur.execute(commande)
        self.connecteur.commit()
        
if __name__ == "__main__":
    controleurServeur=ControleurServeur()
    #atexit.register(controleurServeur.fermer)
    daemon.register_instance(controleurServeur)  
    daemon.serve_forever()
