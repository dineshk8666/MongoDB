from datetime import datetime
from pymongo import MongoClient

try:
    client = MongoClient(host="localhost", port=27017)
    print "Connected Successfully"
except pymongo.errors.ConnectionFailure, e:
    print "Could not connect to MongoDB: %s" % e

# Use existing database (e.g: resturants) or create if not exist
db = client.resturants

#Use existing collection ( collections in mongodb is same as table in sql) or create new (e.g: resturant) if not exist

resturant = db.resturant

## Insert Data

resturant.insert(
        {
            "address": {
                "street": "2 Avenue",
                "zipcode": "10075",
                "building": "1480",
                "coord": [-73.9557413, 40.7720266],
                },
            "borough": "Manhattan",
            "cuisine": "Italian",
            "grades": [
                {
                    "date": datetime.strptime("2014-10-01", "%Y-%m-%d"),
                    "grade": "A",
                    "score": 11,
                },
            ],
            "name" : "Vella",
            "resturant_id" : "41704620",
            "seqNo" : 345345,
        }
   )

resturant.insert(
        {
            "address": {
                "street": "4th Avenue",
                "zipcode": "10073",
                "building": "1480",
                "coord": [-75.9557413, 80.7720266],
                },
            "borough": "Manhattan",
            "cuisine": "Mexican",
            "grades": [
                {
                    "date" : datetime.strptime("2014-01-16", "%Y-%m-%d"),
                    "grade": "B",
                    "score": 22,
                }
            ],
            "name" : "Virgun",
            "resturant_id" : "41704666",
            "seqNo": 34654564,
        }
   )


resturant.insert(
        {
            "address": {
                "street": "66 Avenue",
                "zipcode": "12274",
                "building": "1",
                "coord": [-73.9557413, 40.7720266],
                },
            "borough": "Manhattan",
            "cuisine": "Indian",
            "grades": [
                {
                    "date": datetime.strptime("2014-10-01", "%Y-%m-%d"),
                    "grade": "A",
                    "score": 11,
                },
                {
                    "date" : datetime.strptime("2014-01-16", "%Y-%m-%d"),
                    "grade": "B",
                    "score": 22,
                }
            ],
            "name" : "Menis",
            "resturant_id" : "41704620",
            "seqNo" : 254535,
        }
   )
