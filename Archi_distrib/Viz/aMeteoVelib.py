import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import csv
from dateutil import parser
import json 
import seaborn as sns
from pymongo import MongoClient 


CONNECTION_STRING="mongodb://127.0.0.1:27017/?directConnection=true&serverSelectionTimeoutMS=2000&appName=mongosh+1.6.1"
client = MongoClient(CONNECTION_STRING)


print("Connexion établie")

mydb = client["Projet"]
mycol = mydb["Meteo"]
mydb2 = client["Projet"]
mycol2 = mydb2["Velib"]



d_moyennes = dict({})  


    
fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2, figsize=(15, 5))
plt.suptitle('Prix des véhicules / Pib du Departement', fontsize=16)
for x in mycol.find({},{ "ï»¿date"	:1,"temperature"	:1,"temp_degre":1,	"dep":1	,"depnum":1,	"region":1	,"regionnum":1	,"mois":1 }): 
    
    ax1.bar(x["ï»¿date"], x['temp_degre'],color='black')

for x in mycol2.find({},{ "Identifiant station" :1	,"Nom station" :1,	"Station en fonctionnement" :1	,
                         "Capacité de la station":1,	"Nombre bornettes libres":1,	"Nombre total vélos disponibles":1,	
                         "Vélos mécaniques disponibles":1,	"Vélos électriques disponibles":1	,"Borne de paiement disponible":1,	
                         "Retour vélib possible":1	,"Actualisation de la donnée":1,	"Coordonnées géographiques":1	,
                         "Nom communes équipées": 1,	"Code INSEE communes équipées":1
 }):
   
    ax2.bar(x['Nom communes équipées'], x['Nombre total vélos disponibles'],color='red')
ax1.set_title('Meteo')
ax2.set_title('Velib')
plt.subplots_adjust(left=0.2, wspace=0.2, top=0.85) # ajuster la position et l'espacement des graphes
plt.xticks(rotation = 90)
plt.show()