import os
from flask import Flask
from flask import jsonify, request

from flask_pymongo import PyMongo


app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'OMDB'
app.config['MONGO_URL'] = 'mongodb://localhost:27017/OMDB'
app.debug = os.environ.get('DEBUG', False)

db = PyMongo(app)


## Refer Below code to connect multiple mongoDb
"""
app = Flask(__name__)

# connect to MongoDB with the defaults
mongo1 = PyMongo(app)

# connect to another MongoDB database on the same host
app.config['MONGO2_DBNAME'] = 'dbname_two'
mongo2 = PyMongo(app, config_prefix='MONGO2')

# connect to another MongoDB server altogether
app.config['MONGO3_HOST'] = 'another.host.example.com'
app.config['MONGO3_PORT'] = 27017
app.config['MONGO3_DBNAME'] = 'dbname_three'
mongo3 = PyMongo(app, config_prefix='MONGO3')

"""

"""
@app.route('/star', methods =['POST'])
def add_start():
    star = mongo.db.stars
    data = request.json ## Json data added during post requwst to test
    print data
    name = data['name']
    distance = data['distance']
    star_id = star.insert({'name':name, 'distance':distance})
    new_star = star.find_one({'_id': star_id})
    output = {'name' : new_star['name'], 'distance': new_star['distance']}
    return jsonify({'result':output})

@app.route('/star', methods=['GET'])
def get_all_stars():
    star = mongo.db.stars
    output = []
    for s in star.find():
        output.append({'name':s['name'], 'distance':s['distance']})
    return jsonify({'result':output})

@app.route('/star/', methods=['GET'])
def get_one_star(name):
    star=mondo.db.stars
    s = star.find_one({'name':name})
    if s:
        output = {'name': s['name'], 'distance': s['distance']}
    else:
        print "No Such Match"
    return jsonify({'result': output})


if __name__ == '__main__':
    app.run(debug=True)

"""
