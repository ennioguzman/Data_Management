import json
from pymongo import MongoClient
import csv
import pandas as pd
import sys
import re

# en este archivo se convinan dos datasets para hacer un database, un archivo es tipo json y otro archivo es tipo csv
# el proyecto se trabaja en mongodb

client = MongoClient('localhost', 27017)
db = client.test_database
collection_JSON = db.collection_JSON
collection_CSV = db.collection_CSV

#Open CSV
df = pd.read_csv("happiness_2017.csv")
records_ = df.to_dict(orient = 'records')
r = json.dumps(records_)
loaded_r = json.loads(r)
collection_CSV.insert(loaded_r)

# Open JSON
with open('birth_rate_and_others.json') as f:
    file_data = json.load(f)
collection_JSON.insert(file_data)

print(db.collection_JSON.find({}))
print(db.collection_CSV.find({}))


ciao_csv = db.collection_CSV.find()
ciao_json = db.collection_JSON.find()
print('collection')


Country = [db.collection_CSV.distinct('Country'), 
            db.collection_CSV.distinct('Happiness Rank'),
            db.collection_CSV.distinct('Happiness Score'),
            db.collection_CSV.distinct('Whisker high'),
            db.collection_CSV.distinct('Whisker low'),
            db.collection_CSV.distinct('Economy GDP per Capita'),
            db.collection_CSV.distinct('Family'),
            db.collection_CSV.distinct('Health Life Expectancy'),
            db.collection_CSV.distinct('Freedom'),
            db.collection_CSV.distinct('Generosity'),
            db.collection_CSV.distinct('Trust Government Corruption'),
            db.collection_CSV.distinct('Dystopia Residual')
            ]  

country2 = db.collection_CSV.find({ 'Country' : Country[0][1] })
# print(country2[0])

Ciao = db.collection_JSON.find()

with open('person.txt', 'w') as f:
    for row in Ciao:
        f.write("%s\n" % str(row))


# for i in Ciao:
#     print (i)


# db.collection_JSON.update({'Country Name': 'Denmark'}, { '$set': { 'Happiness Rank': "Corrado level"}  })
# for i in country2:
#     print (i)

# for i in Country[]:
#      print(i[2])



# print(Country)
# for i in ciao_csv:
#     print (i)
# Ciao = db.collection_CSV.find({ 'Country Name' : Country[0][1] })
# Ciao = db.collection_JSON.find({})
# for i in Ciao:
#     print (i)

client.close()
