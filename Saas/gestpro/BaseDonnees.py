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
            ]
        return listeTables
    
    def genererListeConst(self):
        listeConst = [
            ['table a modifier', 'nom de la contrainte', 'laForeign Key', 'la table de reference', 'variable de reference'],
            ['table a modifier', 'nom de la contrainte', 'laForeign Key', 'la table de reference', 'variable de reference'],
            ['table a modifier', 'nom de la contrainte', 'laForeign Key', 'la table de reference', 'variable de reference'],
            ['table a modifier', 'nom de la contrainte', 'laForeign Key', 'la table de reference', 'variable de reference'],
            ['table a modifier', 'nom de la contrainte', 'laForeign Key', 'la table de reference', 'variable de reference'],
            ['table a modifier', 'nom de la contrainte', 'laForeign Key', 'la table de reference', 'variable de reference'],
            ['table a modifier', 'nom de la contrainte', 'laForeign Key', 'la table de reference', 'variable de reference'],
            ['table a modifier', 'nom de la contrainte', 'laForeign Key', 'la table de reference', 'variable de reference'],
            ['table a modifier', 'nom de la contrainte', 'laForeign Key', 'la table de reference', 'variable de reference'],
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
            stringCreateConst = "ALTER TABLE " + contrainte[0] + " ADD CONSTRAINT " + contrainte[1] + " FOREIGN KEY(" + contrainte[2] + ") REFERENCES " + contrainte[3] + "(" + contrainte[4] + ");"
            self.curseur.execute(stringCreateConst)
           
        
if __name__ == "__main__":
    baseDonnees = BaseDonnees()