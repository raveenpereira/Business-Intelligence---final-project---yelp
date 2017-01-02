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
  SELECT city , count(*) totalreviews FROM
  `mongo.274_BI`.`yelp_dataset` where true=repeated_contains(categories,'Restaurants')
  group by city order by count(*) desc limit 5
''')

print dumps(yelp_reviews)


# pandas dataframe
