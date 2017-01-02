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
  select sum(case when t.attributes.`Price Range`=1 then 1 else 0 end) as One,
  sum(case when t.attributes.`Price Range`=2 then 1 else 0 end) as Two,
  sum(case when t.attributes.`Price Range`=3 then 1 else 0 end) as Three ,
  sum(case when t.attributes.`Price Range`=4 then 1 else 0 end) as Four from `mongo.274_BI`.`yelp_dataset` t
  where t.city='Montreal' and true=repeated_contains(categories,'Restaurants')
  order by count(*) asc

''')

print dumps(yelp_reviews)


# pandas dataframe
