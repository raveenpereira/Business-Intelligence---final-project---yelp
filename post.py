#!/usr/local/bin/python
import sys, json
import json
from bson.json_util import dumps
from bson import json_util
#print "Content-type: text/html\n\n";
print 'Content-Type: application/json\n\n'
#print """<p>hehy</p>"""
from pymongo import MongoClient
name="274_BI"
collectionname="yelp_dataset_challenge"
try:
    mongoconnection = MongoClient()
    db=mongoconnection['274_BI']
    collection=db['yelp_dataset_challenge']
    #print"syayy"
except Exception as e:
    print('Error: Unable to Connect')

myjson = json.load(sys.stdin)
# Do something with 'myjson' object

var my_variable = myjson.city;

pipeline = [
{"$match": {"city":[myjson.city]}},
{"$group" : {"_id": "$attributes.Price Range","value":{"$sum":1}}},
{"$project": {"value":1}}
]
a= db.yelp_dataset.aggregate(pipeline)
print dumps(a)

#print json.dumps(myjson)
