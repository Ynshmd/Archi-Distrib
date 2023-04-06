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


for x in mycol.find({},{ "ï»¿date"	:1,"temperature"	:1,"temp_degre":1,	"dep":1	,"depnum":1,	"region":1	,"regionnum":1	,"mois":1 }):
   
    
    plt.bar(x["ï»¿date"], x['temp_degre'])

 
    
plt.rcParams['figure.figsize']=(20, 10)    
plt.title('Temperature derniers jours')
plt.xlabel('Date')
plt.ylabel('degre')
plt.xticks(rotation = 45)
plt.show()







