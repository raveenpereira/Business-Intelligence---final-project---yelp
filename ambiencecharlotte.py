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
      SELECT sum(case when t.attributes.Ambience.romantic='true' then 1 else 0 end) as Romantic,
      sum(case when t.attributes.Ambience.intimate='true' then 1 else 0 end) as Intimate,
      sum(case when t.attributes.Ambience.classy='true' then 1 else 0 end) as Classy,
      sum(case when t.attributes.Ambience.hipster='true' then 1 else 0 end) as Hipster,
      sum(case when t.attributes.Ambience.divey='true' then 1 else 0 end) as Divey,
      sum(case when t.attributes.Ambience.touristy='true' then 1 else 0 end) as Touristy,
      sum(case when t.attributes.Ambience.trendy='true' then 1 else 0 end) as Trendy,
      sum(case when t.attributes.Ambience.upscale='true' then 1 else 0 end) as Upscale,
      sum(case when t.attributes.Ambience.casual='true' then 1 else 0 end) as Casual
       from `mongo.274_BI`.`yelp_dataset`t where  true=repeated_contains(categories,'American')and t.stars>3.5 and t.city='Phoenix'


''')

print dumps(yelp_reviews)


# pandas dataframe
