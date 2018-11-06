## -*- coding: utf-8 -*-
import sqlite3
import random
from tkinter import *
import tkinter.ttk as ttk


class Vue():
    def __init__(self,parent):
        self.parent=parent
        self.root=Tk()
        self._create_treeview()


    def _create_treeview(self):
        f = ttk.Frame(self.root)
        f.pack(side=TOP, fill=BOTH, expand=Y)
        
        # create the tree and scrollbars
        self.dataCols = ('Nom', 'Organisation')        
        self.tree = ttk.Treeview(f,columns=self.dataCols, 
                                 show = 'headings')
        
        for c in self.dataCols:
            self.tree.heading(c, text=c.title())
                              
        
        ysb = ttk.Scrollbar(orient=VERTICAL, command= self.tree.yview)
        xsb = ttk.Scrollbar(orient=HORIZONTAL, command= self.tree.xview)
        self.tree['yscroll'] = ysb.set
        self.tree['xscroll'] = xsb.set
        
        # add tree and scrollbars to frame
        self.tree.grid(in_=f, row=0, column=0, sticky=NSEW)
        ysb.grid(in_=f, row=0, column=1, sticky=NS)
        xsb.grid(in_=f, row=1, column=0, sticky=EW)
        
        # set frame resize priorities
        f.rowconfigure(0, weight=1)
        f.columnconfigure(0, weight=1)
        
    def ecristable(self,donnees):
        for i in donnees:
            self.tree.insert('', 'end', values=i)


class Modele():
    def __init__(self,parent):
        self.parent=parent
        self.noms=["jean","john","jim","jack","jones","jamie",
              "marc","matt","mike","moniq","miranda","mirna",
              "alain","denise","billye","bob","sammy",
              "dom","nancy","fleure","pascale","josee"]
        
        self.orgs=["IBM","Apple","Microsoft","Lotus","Autodesk","Ubisoft",
              "Oracle","HydroQ","Ubuntu","RedHat","NASA","SpaceX",
              "Tesla","Ford","Sony","LG","Samsung",
              "Google","Amazon","Evenko","UdeM","MIT"]
        
        self.conn = sqlite3.connect('exemplesSQLITEData.jmd')
        self.curseur = self.conn.cursor()
    
        
    def bdtestcreate(self):
        # Create table
        self.curseur.execute('''CREATE TABLE if not exists projets 
                     (nom text, organisation text) ''')
        
        self.curseur.execute('''CREATE TABLE if not exists mandats 
                     (auteur text, categorie text, nbrmots number) ''')
        self.curseur.execute('''CREATE TABLE if not exists casUsage 
                     (cas text, role text, permission number) ''')
        
        self.conn.commit()
        
    def efface(self):
        # Create table
        self.curseur.execute('''DROP TABLE projets''')
        
        self.conn.commit()
        
    
    def testBD(self):
        # Cherche definition de structure
        self.curseur.execute('''select * from sqlite_master''')
        print("Structure de BD ",self.curseur.fetchall())
        self.conn.commit()
    
    def testEcrisDB1(self,dons):
        for i in dons:
            monsql="Insert into projets values('"+i[0]+"','"+i[1]+"');"
            self.curseur.execute(monsql)
        self.conn.commit()  
        
    def creerData(self,n=1):
        ids=[]
        for i in range(n):
            n=random.choice(self.noms)
            o=random.choice(self.orgs)
            ids.append([n,o])
        print("NOUVEAU",len(ids))
        return ids
    
    def litBD(self):
        # Create table
        self.curseur.execute('''select * from projets''')
        data=self.curseur.fetchall()
        return data
        
    def patente(self):
        self.efface()
        self.bdtestcreate()
        self.testBD()
        d=self.creerData(30)
        self.testEcrisDB1(d)
        ad=self.litBD()
        return d
    
class Controleur():
    def __init__(self):
        self.modele=Modele(self)
        self.vue=Vue(self)
        d=self.modele.patente()         # Liste de tests/taches
        self.vue.ecristable(d)
        self.vue.root.mainloop()


if __name__ == '__main__':
    c=Controleur()