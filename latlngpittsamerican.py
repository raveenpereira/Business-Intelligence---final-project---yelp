#!/usr/local/bin/python
from pydrill.client import PyDrill
import json
from bson.json_util import dumps
from bson import json_util
#print "Content-type: application/json\n\n";
print "Content-type: text/html\n\n";
#print """<p>hehy</p>"""
#drill = PyDrill(host='localhost', port=8047)
from pymongo import MongoClient
drill = PyDrill(host='localhost', port=8047)

if not drill.is_active():
    raise ImproperlyConfigured('Please run Drill first')

yelp_reviews = drill.query('''
  select avg(t.latitude) as latitude, avg(t.longitude) as longitude from `mongo.274_BI`.`yelp_dataset`t
  where true=repeated_contains(categories,'American')and t.stars>3.5 and t.city='Pittsburgh'
''')

print dumps(yelp_reviews)


# pandas dataframe
