#!/usr/bin/env python
import pandas as pd
import csv
import re
from os import getcwd, chdir, mkdir, path, makedirs, listdir, remove


#Partie région - départements
with open('departements-france.csv', newline='') as csvfile:
 spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
 
 for row in spamreader:
    print(row)

    r_path = row[3]
    d_path = r_path + "/" + row[1]


    if(path.exists(r_path) == False):
       makedirs(r_path)

    if(path.exists(d_path) == False):
       makedirs(d_path)

#Partie Batiment

regex = "^roi$"
bat_file_path = "liste-des-immeubles-proteges-au-titre-des-monuments-historiques.csv"
with open(bat_file_path, newline='') as csvfile:
 dictreader = csv.DictReader(csvfile, delimiter=';', quotechar='"')
 
 for row in dictreader:
    print(row["tico"], row["reg"], row["dpt_lettre"])
    
    if(row["tico"].__contains__(',') == False):
       correctFileName = row["tico"]
       correctFileName = correctFileName.replace('"', '')
       correctFileName = correctFileName.replace('/', '')
       lin_file_path = row["reg"] + "/" + row["dpt_lettre"] + "/" + correctFileName +".csv"

       if(path.exists(row["reg"]) == True & path.exists(row["reg"] + "/" + row["dpt_lettre"]) == True):
          if(path.exists(lin_file_path) == False):
             with open(lin_file_path, 'w', newline='') as csvsubfile:
                fieldnames = ['nom', 'description', 'date_construction', 'date_protection', 'histoire', 'commune', 'departement', 'region']
                dictwriter = csv.DictWriter(csvsubfile, fieldnames)
                dictwriter.writeheader()
                dictwriter.writerow({'nom' : row["tico"], 'description' : row["desc"], 'date_construction' : row["sclx"], 'date_protection' : row["dpro"], 'histoire' : row["hist"], 'commune' : row["wcom"], 'departement' : row["dpt_lettre"], 'region' : row["reg"]})
                print("added")
          else:
            print("file alrdy exists")
    else:
       print("wrong delimiter")  
       
    #monument fiche à mettre dans la boucle ci dessus  
fichier = open("tico", "wt")
ecrivainCSV = csv.writer(fichier,delimiter=";")
ecrivainCSV.writerow(["Nom","description","commune","localisation","latitude","longitude"])	# On écrit la ligne d'en-tête avec le titre des colonnes
ecrivainCSV.writerow(["tico","reg","dpt_lettre"])

fichier.close()
      

       
print(getcwd())