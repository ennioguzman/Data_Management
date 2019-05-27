import shapefile
import matplotlib.pyplot as plt
import numpy as np

# from urllib2 import urlopen
from six.moves import urllib
import json

shape = shapefile.Reader("ged181.shp")
print ('number of shapes imported:',len(shape.shapes()))
shape_ex = shape.shape(142901)
print (shape_ex)
print (shape_ex.points)
print(shape.shape.__doc__)

# name of fields
fields = shape.fields[1:] 
field_names = [field[0] for field in fields] 
# construction of a dctionary field_name:value  

for r in shape.shapeRecords():  
    atr = dict(zip(field_names, r.record))  

# geomet = shape.shape(0).shapeRecords() #will store the geometry separately
# 14.6222328,-90.5185188




def getplace(lat, lon):
    url = "http://maps.googleapis.com/maps/api/geocode/json?"
    url += "latlng=%s,%s&sensor=false" % (lat, lon)
    v = urllib.request.urlopen(url).read()
    j = json.loads(v)
    components = j['results'][0]['address_components']
    country = town = None
    for c in components:
        if "country" in c['types']:
            country = c['long_name']
        if "postal_town" in c['types']:
            town = c['long_name']
    return town, country




print(getplace(51.1, 0.1))
print(getplace(51.2, 0.1))
print(getplace(51.3, 0.1))

import reverse_geocoder as rg

coordinates = (51.5214588,-0.1729636),(14.6222328,-90.5185188),(45.4667971,9.1904984)

results = rg.search(coordinates) # default mode = 2

print (results)
