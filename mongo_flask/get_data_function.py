from pymongo import MongoClient
client=MongoClient()
db=client.resturants
collection=db.resturant
def get_data(name):
    collection=db.resturant
    s=collection.find_one({'name': name})
    return s
a = get_data("Vella")
print a
