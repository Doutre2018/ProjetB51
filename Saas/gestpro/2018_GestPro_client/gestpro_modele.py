from xmlrpc.client import ServerProxy


class Modele():
    #def __init__(self,parent,joueurs,dd):
    def __init__(self,parent,joueurs,dd):
        print("Hey ho")
        self.parent=parent
        self.connectionServeurCourant()
        self.serveur = ServerProxy(self.adresseServeur)
        #self.conn = sqlite3.connect('SAAS.db') #establish connection...
       # self.curseur = self.conn.cursor()
       
       # self.createurId=self.parent.createurId
        self.nomProjetValidation = None
        self.projects=[]
        self.projects.append(Project(self, self.parent))
        
    def connectionServeurCourant(self):  
        with open("adresseServeurCourant.txt", "r") as fichier:
            self.adresseServeur = fichier.read()  
        
        
class Project():                                            
    def __init__(self, parent, controleur):
        self.parent = parent
        self.controleur = controleur
        ###################### self.id = controleur.trouverIP()
        self.nom = None
        ######print#####
        testZeroProject = 0
        print(testZeroProject)
        #self.curseur.execute('''select COUNT(id) from project''') #if project table is empty, fill with Default name project
        #testZeroProject = self.curseur.fetchall()
        #self.controleur.serveur
        print(self.parent.serveur)
        ListeResult = [10, 'attempt']
        valueBool = self.parent.serveur.requeteInsertion("projet", ListeResult)
        print(valueBool)
        ListeSel = []
        ListeSel.append(self.parent.serveur.requeteSelection('''Select * from projet'''))
        print("post Select")
        
        
        if testZeroProject:
            pass
        else:
            parent.nomProjetValidation = 'Default Project Name'
            ######print test######
            print("test project creation")
            createProject(parent, modele)
                
            
        if(createProject(self, parent)):
            return True
        else:
            return False
        
    def createProject(self, project, modele):
        self.modele = modele
        self.project = project
        self.ProjectNameToValidate = modele.nomProjetValidation
        self.NameFailure = False
        
       
        self.curseur.execute('''select DISTINCT id from project''')
        total = self.curseur.fetchall()
        
        for compteur in range(total):
            self.curseur.execute('''select DISTINCT name from project where id = (?)''', compteur)
            nameInDB=self.curseur.fetchall()
            if self.ProjectNameToValidate == nameInDB:
                self.NameFailure = True
                return NameFailure
            else:
                self.curseur.execute('''insert into project values (NULL, (?))''', self.ProjectNameToValidate)  #ajouter autres vars de projet
                
   
if __name__=="__main__":
    mod=Modele(1, 2, 2)       
                