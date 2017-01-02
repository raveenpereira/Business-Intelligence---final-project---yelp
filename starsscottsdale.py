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
  select sum(case when t.stars=1.0 then 1 else 0 end) as `1`,
  sum(case when t.stars=2.0 then 1 else 0 end) as `2`,
  sum(case when t.stars=2.5 then 1 else 0 end) as `3`,
   sum(case when t.stars=3.0 then 1 else 0 end) as `4`,
   sum(case when t.stars=3.5 then 1 else 0 end) as `5`,
   sum(case when t.stars=4.0 then 1 else 0 end) as `6`,
   sum(case when t.stars=4.5 then 1 else 0 end) as `7`,
   sum(case when t.stars=5.0 then 1 else 0 end) as `8`
   from `mongo.274_BI`.`yelp_dataset`t where t.city='Pittsburgh' and true=repeated_contains(categories,'Restaurants')

''')

print dumps(yelp_reviews)


# pandas dataframe
