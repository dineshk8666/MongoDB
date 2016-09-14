import pymongo
from pymongo import MongoClient
client = MongoClient(host="localhost", port=27017)

# use db command
db = client.resturants

# useing collection ( or say table) resturant from the db resturants
collection = db.resturant

# Fild all data

print "Complete data of collection returant"
### All data in list
resturantData= collection.find()
print list(resturantData)
print "\n\n"

## Get data one-by-one on next() interation
print "one item of data list at once"
resturantData= collection.find()
print resturantData.next()
print "\n\n"

## All data on iteration
resturantData= collection.find()
for d in resturantData:
    print d

print "\n\n"

## Count the number of records in collection
resturantData= collection.find()
print "Number of records is:%s" % (resturantData.count())

print "\n\n"

# Find specific keyword search data
print "Data contains grade A from collection resturant"
gradeData = collection.find({"grades.grade" : "A"})
for grade in gradeData:
    print grade

print "\n\n"

print "Data contain name=Vella"
nameData = collection.find({"name":"Vella"})
for nd in nameData:
    print nd

print "\n\n"

## update data
## How to update data for 2nd field, not the first find
print "Update data of field"
name=collection.find_one({"name":"Menis"})
name["name"] = "Menus"
print "%s\n\n" % name
name["grades"][1]["grade"] = "D"
print name["grades"][1]["grade"]
print "\n\n"


## If data avilable in given list, get data
print list(collection.find({"cuisine":{"$in":["I","Mexican","Indian","Russian",]}}))
print "\n\n"

## If data not availabe in given list, get those data
print list(collection.find({"cuisine":{"$nin":["Mexican","Indian","Russian",]}}))
print "\n\n"


## Sort data
print "sorted list of records and make limited list"
cursor = collection.find().sort('seqNo', pymongo.DESCENDING).limit(2)
for c in cursor:
    print c['seqNo']
print "\n\n"

## skip(n) will first skip the top n number of records and then limit to 2
## for e.g: if there are 500 records, sort().limit(10).skip(100) means , first sort the list , then skip the top 100 records and then print next 10 , means from 101 to 110 
print "sorted and skipped and limited"
cursor = collection.find().sort('seqNo', pymongo.DESCENDING).limit(2).skip(1)
for c in cursor:
    print c['seqNo']
print "\n\n"


## To pick the specific fields from the record

print "Only specific field from a record\n"
cursor = collection.find_one({"seqNo":{"$gt" : 345342}}, {"cuisine":1, "_id":0})
print cursor

cursor = collection.find_one({"seqNo":{"$gt" : 345342}}, {"seqNo":1,"cuisine":1, "_id":0})
print cursor
print "\n\n" 

print "Distint value of the fields"
print collection.distinct("name")
print collection.distinct("cuisine")
print collection.distinct("grades.grade")
print collection.find({"seqNo":{"$gt":10000}}).distinct("name")

print "\n\n" 
print "Removing data from collection resturant"
for d in collection.find():
    print "removing entry %s" % d
    collection.remove(d)
print "\n\n"
