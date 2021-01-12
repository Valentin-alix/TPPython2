#!/usr/bin/env python
import pandas as pd
import csv

"""with open('departements-france.csv', newline='') as csvfile:
 spamreader = csv.reader(csvfile, delimiter=' ',
quotechar='|')
 for row in spamreader:
   print(', '.join(row))"""
   
df = pd.read_csv("departements-france.csv")
type(df)
df.head()
df.describe
df[‘servers’]
df[‘servers’][0]
df[df[‘size’]>10]
