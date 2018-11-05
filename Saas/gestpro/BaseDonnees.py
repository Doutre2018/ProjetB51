import sqlite3
import os

class  BaseDonnees():
    def __init__(self):
        if os.path.exists("SAAS.db"):
            os.remove("SAAS.db")
        else:
            print("Creation du fichier SAAS.db initial")
        self.connecteur = sqlite3.connect('SAAS.db')
        self.curseur = self.connecteur.cursor()
        self.creerTables(self.genererListeTables(),self.genererListeConst())
        self.connecteur.close()
        
    
    def genererListeTables(self):
        listeTables = [ 
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
            ['Objet_Maquette', ['id','integer','PRIMARY KEY'], ['hauteur','real',''], ['largeur','real',''], ['fill_couleur','real','NULL']],
            ['ColonnesScenarii', ['id','integer','PRIMARY KEY'], ['nom','text',''], ['numero_position','integer','']],
            ['Cartes', ['id','integer','PRIMARY KEY'], ['classe','text',''], ['ordre','integer','']],
            ['AttributsCRC', ['id','integer','PRIMARY KEY'], ['nomAttributs','text','']],
            ['Sprint', ['id','integer','PRIMARY KEY'], ['ordre','integer',''], ['date','date','']],
            ['Tache_Sprint', ['id','integer','PRIMARY KEY'], ['description','text',''], ['nom','text',''], ['duree','integer','']],
            ['Taches_Terlow', ['id','integer','PRIMARY KEY'], ['ordre','integer',''], ['texte','text','DEFAULT NULL']],
            ['Colonnes_Terlow', ['id','integer','PRIMARY KEY'], ['type','text','']],
            ['TypeDonneeScenario', ['id','integer','PRIMARY KEY'], ['texte','text','']],
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
            ['Scenarii', 'id_donnees','INTEGER', 'TypeDonneeScenario', 'id'],
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
                stringDropTable += " CASCADE CONSTRAINTS;"
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
        for rangee in self.curseur.execute(stringSelect):
            print(rangee)
            
    def alterTable(self,listeConst):
        for contrainte in listeConst:
            stringAlterTable = "ALTER TABLE " + contrainte[0] + " ADD COLUMN " + contrainte[1] + " " + contrainte[2] + " REFERENCES " + contrainte[3] + "(" + contrainte[4] + ");"
            self.curseur.execute(stringAlterTable)
           
        
if __name__ == "__main__":
    baseDonnees = BaseDonnees()