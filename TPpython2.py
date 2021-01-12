#!/usr/bin/env python
import pandas as pd
import csv
import re
from os import getcwd, chdir, mkdir, path, makedirs, listdir, remove

file_path = "departements-france.csv"

with open('departements-france.csv', newline='') as csvfile:
 spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
 
 for row in spamreader:
    print(row)

    r_path = row[3]
    d_path = r_path + "/" + row[1]
    if len(listdir(r_path)) == 0:
       print("il n'y a pas de département")
    else :
       print("il y a déjà un département")
       print("voulez-vous abandonner ou vider le dossier ? (a/v)")
       nn = input()
       if (nn == "v"):
            files = listdir(r_path)
            for i in range(0, len(files)):
               remove(r_path+'/'+files[i])

    if(path.exists(r_path) == False):
       makedirs(r_path)

    if(path.exists(d_path) == False):
       makedirs(d_path)


print(getcwd())

"""path.isfile('departements-france.csv')
test = path.isfile('departements-france.csv')
if test:
      print("cest bon")
df = pd.read_csv('departements-france.csv', index_col='code_departement')
print(df['code_region'])
dossier_cible = df['code_region']
mkdir(dossier_cible)"""

"""type(df)
df.head()
df.describe
df[‘servers’]
df[‘servers’][0]
df[df[‘size’]>10]"""
