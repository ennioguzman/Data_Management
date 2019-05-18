import json
from pymongo import MongoClient
import csv
import pandas as pd
import sys
import re



client = MongoClient('localhost', 27017)
db = client.test_database
collection2 = db.collection2



df = pd.read_csv("happiness_2017.csv")
records_ = df.to_dict(orient = 'records')

r = json.dumps(records_)
loaded_r = json.loads(r)

# print(loaded_r)


collection2.insert(loaded_r)

Ciao = db.collection2.find({})


for i in Ciao:
    print (i)
client.close()