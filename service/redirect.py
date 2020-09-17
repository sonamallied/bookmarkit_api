import pymongo
import json
from flask import jsonify
from flask_restful import Resource
from flask import jsonify, request
from flask_api import status
from Models.Model import URLRep
import sys
import hashlib
import datetime



def redirectUrl(shorturl):
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["bookmarkit"]
    mycol = mydb["approved"]
    output = []

    for x in mycol.find({"shorturl": shorturl}, {'_id': False}):
        output.append(x);

    print(output);

    return output

