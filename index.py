#!/usr/local/bin/python
import json
from bson.json_util import dumps
from bson import json_util
print "Content-type: text/html\n\n";
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


pipeline = [
{"$match": {"city":"Las Vegas"}},
{"$group" : {"_id": "$attributes.Price Range","value":{"$sum":1}}},
{"$project": {"value":1}}
]
a= db.yelp_dataset.aggregate(pipeline)
print dumps(a)
#for a in db.yelp_dataset.find({"business_id" : "5UmKMjUEUNdYWqANhGckJw"}):
 #  print json.dumps(a,indent=4, default=json_util.default)


#for c in db.yelp_dataset.find({"attributes" :{"Delivery" : "false"}}):
#    print json.dumps(c,indent=4, default=json_util.default)

#for c in db.yelp_dataset.find({"attributes" :{ "Delivery" : "false"}}):
    #print c
    #print json.dumps(c,indent=4, default=json_util.default)

#for b in db.yelp_dataset.aggregate([{"$match":{"state":"PA"}}, {"$group":{"_id":0,"stars":{"$avg":"$stars"}}}, {"$project":{"_id":0,"stars":1}}]):
#    print b
mongoconnection.close()
