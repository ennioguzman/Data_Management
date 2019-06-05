import json
from pymongo import MongoClient
import csv
import pandas as pd
import sys
import re
import itertools

client = MongoClient('localhost', 27017)
db = client.new_data
collection_JSON3 = db.data_management_collection

countries = collection_JSON3.find({}, {'Country Name' : 1, 'Year': 1})
hola = countries

collection_countries = db.data_management_countries
db.data_management_countries.insert_many(countries)
hola = db.data_management_countries.find({})
for i in hola:
    print (i)
