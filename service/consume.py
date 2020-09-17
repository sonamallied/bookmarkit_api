import pymongo
import json
from flask import jsonify






def receive():
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["bookmarkit"]
    mycol = mydb["request"]
    output = []
    for x in mycol.find({}, {'_id': False}):
        output.append(x);


    return jsonify({'result' : output})



def approvedData():
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["bookmarkit"]
    mycol = mydb["approved"]
    output = []
    for x in mycol.find({}, {'_id': False}):
        output.append(x);


    return jsonify({'result' : output})
