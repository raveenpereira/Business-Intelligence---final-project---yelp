#!/usr/local/bin/python
from pydrill.client import PyDrill
import json
import cgi
import sys
from bson.json_util import dumps
from bson import json_util
print "Content-type: application/json\n\n";
#sys.stdout.write("Content-Type: application/json\n\n")
#print "Content-type: text/html\n\n";
#print """<p>hehy</p>"""
#drill = PyDrill(host='localhost', port=8047)
from pymongo import MongoClient
drill = PyDrill(host='localhost', port=8047)

if not drill.is_active():
    raise ImproperlyConfigured('Please run Drill first')

#city =
city=cgi.FieldStorage().value
#print [city]


city1=json.loads(city)
#print city1["data"]


query="select t.name,t.latitude,t.longitude,t.stars from `mongo.274_BI`.`yelp_dataset`t where true=repeated_contains(categories,'"+city1["data"]+"')and t.stars>3.5 and t.city='"+city1["data2"]+"' limit 15"
#print query
#yelp_reviews = drill.query('''
#         select t.name,t.latitude,t.longitude,t.stars from `mongo.274_BI`.`yelp_dataset`t where
#           true=repeated_contains(categories,'American')and t.stars>3.5 and t.city='Charlotte' limit 15


#''')
yelp_reviews=drill.query(query)

print dumps(yelp_reviews)



# pandas dataframe
