import pymongo
import json
from pymongo import MongoClient
try:
    client = MongoClient()
    print "Connected Successfully"
except pymongo.error.ConnectionFailure, e:
    print "Could not connect to MongoDB: %s" % e

db=client.resturants
resturant=db.resturant
data=resturant.find_one({"name":"Vella"})
print data
print "\n\n"

"""
update() method replaces the whole document so be careful! If instead we want to modify specific fields of the document we can use MongoDB's update operators like set, inc, push, pull and many more.
"""
"""
updated_data=resturant.update({"name":"Vella"},{"seqNo":234526})
data=resturant.find({"seqNo":234526})
print list(data)
"""

## Update Operators:
"""
"set" operator: Just update specific field not full doc and create the field if not exist, but it create field only when there is find match. Like in below example if name=vella exist, if add newField=testting, but if name=vella doesnt exit, it wont updat or add the doc
"""
updated_data=resturant.update({"name":"Vella"},{"$set":{"seqNo":234526,"newField":"testing"}})
data=resturant.find({"name":"Vella"})
print list(data)

"""
"upsert": upsert is used to add new record if match doesnt found. Means, if name="vellaa" not available it will crate the new record with all fields
"""
updated_data=resturant.update({"name":"Vellaa"},{"$set":{"seqNo":734526}},upsert=True)
data=resturant.find({"name":"Vellaa"})
print list(data)

"""
multi=True
By default, only first match record will be updated, so if we want to update all the recirds with matches, multi=True, can be added
"""

updated_data=resturant.update({"name":"Vellaa"},{"$set":{"seqNo":734526,"newField":"testing",}},upsert=True,multi=True)
data=resturant.find({"name":"Vellaa"})
print list(data)

"""
inc : this operator increase the value of the field by n number, and  if the field doesn't exist, it created and assign the given value
"""

"""
unset: It deletes the specified field if it find from the matching record , else no effect on record
"""

"""
rename: it rename the specified key of a record. To use this given key_name should exist
e.g: {"$rename":{"seqNo":"seqnumber"}

No changes for the value of the key in a record. multi=True can be uses to replace all the key "seqNo" to "seqnumber"
"""



"""
push and pop and pull
"""
