# -*- coding: utf-8 -*-

'''
f = open("inscriptionTest.txt", "a")
f.write("User1" + "\n")
f.write("User2" + "\n")
f.write("User3" + "\n")
f.close()
'''

string = "UserA"

f = open("inscriptionTest.txt", "r")
data = f.readlines()
print(data)

for line in data:
    mot = line.rstrip('\n')
    print(string)
    print(mot)
    
    if string == mot:
        print("pareil")
        break
    else:
        print("différent")