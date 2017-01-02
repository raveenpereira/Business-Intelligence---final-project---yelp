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
  select sum(case when t.attributes.`Noise Level`='average' then 1 else 0 end) as Average,
  sum(case when t.attributes.`Noise Level`='loud' then 1 else 0 end) as Loud,
  sum(case when t.attributes.`Noise Level`='very_loud' then 1 else 0 end) as `Very Loud`,
  sum(case when t.attributes.`Noise Level`='quiet' then 1 else 0 end) as `Quiet`
   from `mongo.274_BI`.`yelp_dataset`t where t.city='Montreal' and true=repeated_contains(categories,'Restaurants')

''')

print dumps(yelp_reviews)


# pandas dataframe
