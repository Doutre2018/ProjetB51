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
        self.baseDonnee = BaseDonnees()
        daemon.register_function(self.requeteInsertion)
        daemon.register_function(self.requeteSelection)
        daemon.register_function(self.requeteMiseAJour)
        daemon.register_function(self.requeteInsertionPerso)
        daemon.register_introspection_functions()
        
    def creerclient(self,nom):
        if nom in self.clients.keys(): # on assure un nom unique
            return [0,"Erreur de nom"]
        # tout va bien on cree le client et lui retourne la seed pour le random
        c=Client(nom)
        self.clients[nom]=c
        return [1,"Bienvenue",list(self.modulesdisponibles.keys())]
    
    # -------------------DM------------------- #
    def listeNoms(self):
        liste = []
        f = open("inscriptionTest.txt", "r")        # Ouvre le fichier contenant les noms d'utilisateurs
        data = f.readlines()                        # Sépare les noms par ligne
        
        for line in data:
            n = line.rstrip('\n')                   # Enlève les changements de ligne ('\n') de chaque noms
            liste.append(n)                         # Ajoute les noms dans la liste
            
        return liste                                # Retourne la liste de nom
    
    def nomUnique(self, nom):
        liste = self.listeNoms()
        for n in liste:                         # Parcours les noms dans la liste
            if n == nom:                        # Compare le nom à la liste de nom
                return False                    # Nom existe déjà, donc pas unique 
        
        f = open("inscriptionTest.txt", "a")
        f.write(nom + "\n")
        f.close()
        return True                             # Si le nom n'est pas trouvé dans la liste
    # ---------------------------------------- #
            
    #méthode tampon pour insert les données dans la table de la BD du serveur selon le format suivant: nomTable = "string représentant nom", liste valeurs = [10, 'texte1', 50.3]
    def requeteInsertion(self, nomTable, listeValeurs ):
        self.baseDonnee.insertion(nomTable, listeValeurs)
        return True
    
    def requeteInsertionPerso(self,commande):
        self.baseDonnee.insertionPerso(commande)
        return True
    
   #méthode tampon pour mettre à jour des données d'une table. Il faut passer une string représentant l'ensemble de la requête update dans la fonction
    def requeteMiseAJour(self,stringUpdate):
        self.baseDonnee.miseAJour(stringUpdate)
        return True
    
    #méthode tampon qui retourne une liste. Chaque élément de la liste correspond à une rangée du select demandé.
    def requeteSelection(self, stringSelect):
        return self.baseDonnee.selection(stringSelect)
    
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
    def nomUnique(self, nom):
        if self.modele.nomUnique(nom):
            return True
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
        self.modele.baseDonnee.connecteur.close()
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
        self.insertion('stocks', [1])
       # self.connecteur.close()
        
    
    def genererListeTables(self):
        listeTables = [ 
            ['stocks', ['price', 'integer', '']],
            ['Serveurs', ['id','integer','PRIMARY KEY'], ['IP','integer',''], ['nom','text','UNIQUE']],
            ['Utilisateur', ['id','integer','PRIMARY KEY'], ['nomUtilisateur','text','UNIQUE'], ['motDePasse','text',''], ['chemin_acces_csv','text','']],
            ['Projet', ['id','integer','PRIMARY KEY'], ['nom','text','UNIQUE']],
            ['Liaison_Util_Projet', ['role','text','']],
            ['AnalyseTextuelle', ['id','integer','PRIMARY KEY'], ['ligne','integer',''],['colonne','integer','']],
            ['TypeMot', ['id','integer','PRIMARY KEY'], ['nom','text','']],
            ['LigneChat', ['id','integer','PRIMARY KEY'], ['date','date',''],['texte','text','']],
            ['CasUsage', ['id','integer','PRIMARY KEY'],['ligne','text',''],['texte','text','']],
            ['Scenarii', ['id','integer','PRIMARY KEY'],['ligne','text','']],
            ['FonctionsCRC', ['id','integer','PRIMARY KEY'],['fonction','text','']],
            ['CollaboCRC', ['id','integer','PRIMARY KEY']],
            ['FilDeDiscussion', ['id','integer','PRIMARY KEY']],
            ['TypeForme', ['id','integer','PRIMARY KEY'], ['nom','text','']],
            ['Objet_Maquette', ['i d','integer','PRIMARY KEY'], ['hauteur','real',''], ['largeur','real',''], ['fill_couleur','real','NULL']],
            ['ColonnesScenarii', ['id','integer','PRIMARY KEY'], ['nom','text',''], ['numero_position','integer','']],
            ['Cartes', ['id','integer','PRIMARY KEY'], ['classe','text',''], ['ordre','integer','']],
            ['AttributsCRC', ['id','integer','PRIMARY KEY'], ['nomAttributs','text','']],
            ['Sprint', ['id','integer','PRIMARY KEY'], ['ordre','integer',''], ['date','date','']],
            ['Tache_Sprint', ['id','integer','PRIMARY KEY'], ['description','text',''], ['nom','text',''], ['duree','integer','']],
            ['Taches_Terlow', ['id','integer','PRIMARY KEY'], ['ordre','integer',''], ['texte','text','DEFAULT NULL']],
            ['Colonnes_Terlow', ['id','integer','PRIMARY KEY'], ['type','text','']],
            ['Objet_Texte', ['id','integer','PRIMARY KEY'], ['texte','text','']],
            ['Position',['id','integer','PRIMARY KEY'],['x','real','NOT NULL'],['y','real','NOT NULL']]
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
            ['CollaboCRC', 'idClasse1','INTEGER', 'Cartes', 'id'],
            ['CollaboCRC', 'idClasse2','INTEGER', 'Cartes', 'id'],
            ['FonctionsCRC', 'id_classe','INTEGER', 'Cartes', 'id'],
            ['Scenarii', 'id_casUsage','INTEGER', 'CasUsage', 'id'],
            ['Scenarii', 'id_colonne','INTEGER', 'ColonnesScenarii', 'id'],
            ['AttributsCRC', 'id_classe','INTEGER', 'Cartes', 'id'],
            ['Cartes', 'id_carte_heritage','INTEGER', 'Cartes', 'id'],
            ['Cartes', 'idResponsable','INTEGER', 'Utilisateur', 'id'],
            ['Cartes', 'id_projet','INTEGER', 'Projet', 'id'],
            ['Objet_Maquette', 'id_position','INTEGER', 'Position', 'id'],
            ['Objet_Maquette', 'id_type','INTEGER', 'TypeForme', 'id'],
            ['Taches_Terlow', 'id_projet','INTEGER', 'Projet', 'id'],
            ['Taches_Terlow', 'id_colonne_terlow','INTEGER', 'Colonnes_Terlow', 'id'],
            ['Objet_Texte', 'id_position','INTEGER', 'Position', 'id'],
            ['Tache_Sprint','id_sprint','INTEGER', 'Sprint', 'id'],
            ['Sprint', 'id_projet', 'INTEGER',  'Projet', 'id'],
            ]
        return listeConst
        
    def creerTables(self, listeTables, listeConst):
        try:
            for table in listeTables:
                stringDropTable = "DROP TABLE "
                stringDropTable += table[0]
                #stringDropTable += " CASCADE CONSTRAINTS;"
                self.curseur.execute(stringDropTable)
        except:
            pass
        finally:
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
    
    
    def selection(self, stringSelect = ""):
        listeData=[]
        for rangee in self.curseur.execute(stringSelect):
            print(rangee)
            listeData.append(rangee)
        return listeData
            
    def alterTable(self,listeConst):
        for contrainte in listeConst:
            stringAlterTable = "ALTER TABLE " + contrainte[0] + " ADD COLUMN " + contrainte[1] + " " + contrainte[2] + " REFERENCES " + contrainte[3] + "(" + contrainte[4] + ");"
            self.curseur.execute(stringAlterTable)
    
    def insertionPerso(self,commande):
        self.curseur.execute(commande)
        
if __name__ == "__main__":
    controleurServeur=ControleurServeur()
    daemon.register_instance(controleurServeur)  
    daemon.serve_forever()
