import pymongo
from pymongo import MongoClient

try:
    client = MongoClient(host="localhost", port=27017)
    print "connected Successfully"
except pymongo.errors.ConnectionFailure, e:
    print "Could not connect to MongoDB: %s" % e
    
db = client.OM
