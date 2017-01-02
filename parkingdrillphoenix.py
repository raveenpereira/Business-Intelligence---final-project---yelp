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
  SELECT sum(case when t.attributes.Parking.garage='true' then 1 else 0 end) as Garage,
  sum(case when t.attributes.Parking.street='true' then 1 else 0 end) as Street,
  sum(case when t.attributes.Parking.validated='true' then 1 else 0 end) as Validated,
  sum(case when t.attributes.Parking.valet='true' then 1 else 0 end) as Valet,
  sum(case when t.attributes.Parking.lot='true' then 1 else 0 end) as Lot
   FROM `mongo.274_BI`.`yelp_dataset`t where t.city = 'Phoenix' and true=repeated_contains(categories,'Restaurants')

''')

print dumps(yelp_reviews)


# pandas dataframe
