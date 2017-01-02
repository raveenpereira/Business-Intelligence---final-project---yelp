#!/usr/bin/python
from pymongo import MongoClient
name="274_BI"
collectionname="yelp_dataset_challenge"
try:
    mongoconnection = MongoClient()
    db=mongoconnection['274_BI']
    collection=db['yelp_dataset_challenge']
    print"syayy"
except Exception as e:
    print('Error: Unable to Connect')

for post in collection.find():
    print post

mongoconnection.close()
