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
  SELECT sum(case when t.attributes.`Alcohol`<>'none' then 1 else 0 end) as Alcohol,
  sum(case when t.attributes.`Good For Groups`='true' then 1 else 0 end) as `Good For Groups`,
  sum(case when t.attributes.`Accepts Credit Cards`='true' then 1 else 0 end) as `Accept Credit Cards` ,
  sum(case when t.attributes.`Wi-Fi`='free' then 1 else 0 end) as `Wi-Fi`,
   sum(case when t.attributes.`Take-out`='true' then 1 else 0 end) as `Take-Out`,
   sum(case when t.attributes.`Coat Check`='true' then 1 else 0 end) as `Coat Check`,
   sum(case when t.attributes.`Takes Reservations`='true' then 1 else 0 end) as `Takes Reservations`,
   sum(case when t.attributes.`Wheelchair Accessible`='true' then 1 else 0 end) as `Wheelchair Accessible`,
   sum(case when t.attributes.`Outdoor Seating`='true' then 1 else 0 end) as `Outdoor Seating`,
   sum(case when t.attributes.`Dogs Allowed`='true' then 1 else 0 end) as `Dogs Allowed`,
   sum(case when t.attributes.`Smoking`='outdoor' then 1 else 0 end) as `Smoking`,
   sum(case when t.attributes.`Waiter Service`='true' then 1 else 0 end) as `Waiter Service`,
   sum(case when t.attributes.`Caters`='true' then 1 else 0 end) as `Caters`,
   sum(case when t.attributes.`Has TV`='true' then 1 else 0 end) as `Has TV`,
    sum(case when t.attributes.`Drive-Thru`='true' then 1 else 0 end) as `Drive Thru`

   from `mongo.274_BI`.`yelp_dataset`t where  t.stars>3.5 and t.city='Charlotte'
''')

print dumps(yelp_reviews)


# pandas dataframe
