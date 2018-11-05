import sqlite3

class  BaseDonnees():
    def __init__(self):
        self.connecteur = sqlite3.connect('SAAS.db')
        self.curseur = self.connecteur.cursor()
        self.creerTables(self.genererListeTables(),self.genererListeConst())
        self.insertion("stocks", ['date','trans', 'symbol',53.2,5.2])
        self.selection('Select * FROM stocks ')
        self.connecteur.close()
    
    def genererListeTables(self):
        listeTables = [ 
            ['Serveurs', ['id','integer','PRIMARY KEY'], ['IP','integer',''], ['nom','text','UNIQUE']],
            ['Utilisateur', ['id','integer','PRIMARY KEY'], ['nomUtilisateur','text','UNIQUE'], ['motDePasse','text',''], ['chemin_acces_csv','text','']],
            ['Projet', ['id','integer','PRIMARY KEY'], ['nom','text','UNIQUE']],
            ['Liaison_Util_Projet', ['id_util','integer','NOT NULL'], ['id_projet','integer','NOT NULL'], ['role','text',''],['PRIMARY KEY (id_util,id_projet)','','']],
            ['AnalyseTextuelle', ['id','integer','PRIMARY KEY'], ['id_projet','integer','NOT NULL'], ['ligne','integer',''],['colonne','integer',''],['id_type','integer','']],
            ['TypeMot', ['id','integer','PRIMARY KEY'], ['nom','text','']],
            ['LigneChat', ['id','integer','PRIMARY KEY'], ['date','date',''],['texte','text',''],['id_filDiscussion','integer',''],['id_utilisateur','integer','']],
            ['CasUsage', ['id','integer','PRIMARY KEY'], ['id_projet','integer',''],['ligne','text',''],['texte','text','']],
            ['Scenarii', ['id','integer','PRIMARY KEY'], ['id_casUsage','integer',''],['ligne','text',''],['id_donnees','integer',''],['id_colonne','integer','']],
            ['FonctionsCRC', ['id','integer','PRIMARY KEY'], ['id_classe','integer',''],['fonction','text','']],
            ['CollaboCRC', ['id','integer','PRIMARY KEY'], ['idClasse1','integer',''],['idClasse2','text','']],
            ['filDeDiscussion', ['id','integer','PRIMARY KEY'], ['id_Projet','integer','']],
            ['typeForme', ['id','integer','PRIMARY KEY'], ['nom','text','']],
            ['objet_Maquette', ['id','integer','PRIMARY KEY'], ['id_position','integer',''], ['id_type','integer',''], ['hauteur','real',''], ['largeur','real',''], ['fill_couleur','real','NULL']],
            ['ColonnesScenarii', ['id','integer','PRIMARY KEY'], ['nom','text',''], ['numero_position','integer','']],
            ['Cartes', ['id','integer','PRIMARY KEY'], ['id_projet','integer',''], ['id_responsable','integer','DEFAULT NULL'], ['classe','text',''], ['id_carte_heritage','integer',''], ['ordre','integer','']],
            ['AttributsCRC', ['id','integer','PRIMARY KEY'], ['id_classe','integer',''], ['nomAttributs','text','']],
            ['Sprint', ['id','integer','PRIMARY KEY'], ['id_projet','integer',''], ['ordre','integer',''], ['date','date','']],
            ['Tache_Sprint', ['id','integer','PRIMARY KEY'], ['id_sprint','integer',''], ['description','text',''], ['nom','text',''], ['duree','integer','']],
            ['Taches_Terlow', ['id','integer','PRIMARY KEY'], ['id_projet','integer',''], ['id_colonne_terlow','integer','NOT NULL'], ['ordre','integer',''], ['texte','text','DEFAULT NULL']],
            ['Colonnes_Terlow', ['id','integer','PRIMARY KEY'], ['type','text','']],
            ['TypeDonneeScenario', ['id','integer','PRIMARY KEY'], ['texte','text','']],
            ['Objet_Texte', ['id','integer','PRIMARY KEY'], ['id_position','integer',''],['texte','text','']],
            ['Position',['id','integer','PRIMARY KEY'],['x','real','NOT NULL'],['y','real','NOT NULL']]
            ]
        return listeTables
    
    def genererListeConst(self):
        listeConst = [
            ['LigneChat', 'fk_lignechat_idUtil', 'id_utilisateur', 'Utilisateur', 'id'],
            ['LigneChat', 'fk_lignechat_idFilDisc', 'id_filDiscussion', 'filDeDiscussion', 'id'],
            ['AnalyseTextuelle', 'fk_analyseTextuelle_type', 'id_type', 'TypeMot', 'id'],
            ['AnalyseTextuelle', 'fk_analyseTextuelle_projet', 'id_projet', 'Projet', 'id'],
            ['Liaison_Util_Projet', 'fk_liaison_utilisateur', 'id_util', 'Utilisateur', 'id'],
            ['Liaison_Util_Projet', 'fk_liaison_projet', 'id_projet', 'Projet', 'id'],
            ['FilDeDiscussion', 'fk_filDiscussion_projet', 'id_projet', 'Projet', 'id'],
            ['CollaboCRC', 'fk_collaboCrc_classe1', 'idClasse1', 'Cartes', 'id'],
            ['CollaboCRC', 'fk_collaboCrc_classe2', 'idClasse2', 'Cartes', 'id'],
            ['FonctionsCRC', 'fk_fonctionsCrc_classe', 'id_classe', 'Cartes', 'id'],
            ['Scenarii', 'fk_scenarii_casUsage', 'id_casUsage', 'CasUsage', 'id'],
            ['Scenarii', 'fk_scenarii_donnes', 'id_donnees', 'TypeDonneeScenario', 'id'],
            ['Scenarii', 'fk_scenarii_colonne', 'id_colonne', 'ColonnesScenarii', 'id'],
            ['Fo', 'fk_fonctionsCrc_classe', 'id_classe', 'Cartes', 'id'],
            ['FonctionsCRC', 'fk_fonctionsCrc_classe', 'id_classe', 'Cartes', 'id'],
            ['FonctionsCRC', 'fk_fonctionsCrc_classe', 'id_classe', 'Cartes', 'id'],
            ['FonctionsCRC', 'fk_fonctionsCrc_classe', 'id_classe', 'Cartes', 'id'],
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
            stringAlterTable = "ALTER TABLE " + contrainte[0] + " ADD CONSTRAINT " + contrainte[1] + " FOREIGN KEY(" + contrainte[2] + ") REFERENCES " + contrainte[3] + "(" + contrainte[4] + ");"
            self.curseur.execute(stringAlterTable)
           
        
if __name__ == "__main__":
    baseDonnees = BaseDonnees()