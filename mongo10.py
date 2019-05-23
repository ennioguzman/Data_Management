# Se convinan un dataset tipo CSV y uno tipo JSON y se adicionan a una base de datos...

import json
from pymongo import MongoClient
import csv
import pandas as pd
import sys
import re
import itertools

client = MongoClient('localhost', 27017)
db = client.test_database
collection_JSON = db.data_management_collection

# Open JSON
with open('birth_rate_and_others.json') as f:
    file_data = json.load(f)
collection_JSON.insert(file_data)

#laod the csv file
happiness_2007 = pd.read_csv("happiness_2017.csv")

# load the data and pass to a dataframe
happiness_2007_data = pd.DataFrame.from_csv("happiness_2017.csv")

# get the names of the countries
rows = list(happiness_2007_data.columns.tolist())
happiness_2007_data_countries = happiness_2007.Country.tolist()

for temp_country in happiness_2007_data_countries:
    specific_data = happiness_2007_data.loc[temp_country,:]
    for dato in range(len(rows)):
        if temp_country=="Ecuador":
            print (str(rows[dato]) + " - " + str(specific_data[dato]) + " - " + temp_country)
            db.collection_JSON.update({'Country': temp_country}, { '$set': {rows[dato]: specific_data[dato]}  })

    # print (temp_country)

Ciao = db.collection_JSON.find({})

with open('Ciao_Corrado.txt', 'w') as f:
    for row in Ciao:
        f.write("%s\n" % str(row))
    


