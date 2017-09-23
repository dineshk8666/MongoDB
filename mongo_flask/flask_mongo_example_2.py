# mongo.py

from flask import Flask
from flask import jsonify
from flask import request
from flask_pymongo import PyMongo

app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'resturants'
app.config['MONGO_URI'] = 'mongodb://localhost:27017/resturants'

mongo = PyMongo(app)


@app.route('/star', methods=['GET'])
def get_all_stars():
    resturant = mongo.db.resturant
    output = []
    for s in resturant.find():
        output.append({'name': s['name'], 'seqNo': s['seqNo'], "address":s["address"]})
    return jsonify({'result': output})

@app.route('/star/<name>', methods=['GET'])
def get_one_star(name):
    resturant = mongo.db.resturant
    s = resturant.find_one({'name' : name})
    if s:
        output = {'name' : s['name'], 'seqNo' : s['seqNo'], 'address':s['address']}
    else:
        output = "No such name"
    return jsonify({'result' : output})

@app.route('/star', methods=['POST'])
def add_star():
    rest = mongo.db.resturant
    name = request.json['name']
    seqNo = request.json['seqNo']
    resturant_id = request.jsnon['resturant_id']
    rest_id = resturant.insert({'name': name, 'seqNo': seqNo, 'resturant_id': resturant_id})
    new_rest = resturant.find_one({'_id': rest_id })
    output = {'name' : new_rest['name'], 'seqNo' : new_rest['seqNo'], 'resturant_id':new_rest['resturant_id']}
    return jsonify({'result' : output})
if __name__ == "__main__":
    app.run(debug=True)
