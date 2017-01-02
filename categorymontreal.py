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

city="Las Vegas"

yelp_reviews = drill.query('''
  select categories[0] as category, count(categories[0]) as number from `dfs.yelp`.`yelp_academic_dataset_business.json`
   where true=repeated_contains(categories,'Restaurants') and city='Montreal' group by categories[0]
    order by count(categories[0]) desc limit 5

''')

print dumps(yelp_reviews)


# pandas dataframe
