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

print(getcwd())


text = dictreader
pattern = 'roi?\w' # find 'an' either with or without a following word character

for match in re.finditer(pattern, text):
    sStart = match.start()
    sEnd = match.end()

    sGroup = match.group()

    print('Match "{}" found at: [{},{}]'.format(sGroup, sStart,sEnd))
