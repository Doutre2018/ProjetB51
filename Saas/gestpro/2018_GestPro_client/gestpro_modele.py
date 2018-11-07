class Modele():
    def __init__(self,parent,joueurs,dd):
        self.parent=parent
        self.conn = sqlite3.connect('SAAS.db') #establish connection...
        self.curseur = self.conn.cursor()
        self.createurId=self.parent.createurId
        self.nomProjetValidation = None
        self.projects = Project(self, parent);
        
        
        
        
class Project():                                            
    def __init__(self, parent, controlleur):
        self.parent = parent
        self.controlleur = controlleur
        
        
        self.id = controlleur.trouverIP()
        self.nom = None
        ######print#####
        testZeroProject = 0
        print(testZeroProject)
        self.curseur.execute('''select COUNT(id) from project''') #if project table is empty, fill with Default name project
        testZeroProject = self.curseur.fetchall()
        print(testZeroProject)
        
        
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
        
                