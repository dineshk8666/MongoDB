import datetime
from app import mongo

class Seller(mongo.Document):
    email = db.EmailField(unique=True)
    password = db.StringField(default=True)
    active = db.BooleanField(default=True)
    isAdmin = db.BooleanField(default=False)
    timestamp = db.DateTimeField(default=datetime.datetime.now())
