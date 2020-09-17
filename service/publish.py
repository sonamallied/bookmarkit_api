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


#mydict = { "name": "John", "address": "Highway 37" }


def send(_json):
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["bookmarkit"]
    mycol = mydb["request"]

    result = mycol.insert(_json)

    #print(result)
    return result

def get_md5_bytes_as_base62(urlstring):
    digestStr = hashlib.md5(urlstring.encode('utf-8')).hexdigest()

    #Above is 32 char (2 char per byte so 128 bit hash)

    #Lets take only first 10 digits for shortness
    digestStr = digestStr[:10]

    md5int = int(digestStr, 16)

    #Add current micro seconds to bring uniqueness
    md5int += datetime.datetime.now().microsecond
    return base62_encode_i(md5int)

def base62_encode_i(dec):
    s = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    ret = ''
    while dec > 0:
        ret = s[dec % 62] + ret
        dec = int(dec/62)
    return ret


def approve(_json):
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["bookmarkit"]
    mycol = mydb["approved"]

    #json_data = request.get_json(force=True)
    longurl = _json["longUrl"]
    shorturl = "http://localhost:5000/" + get_md5_bytes_as_base62(longurl)
    print(shorturl)

    json_data = {
        "chikcletName" : _json["chikcletName"],
        "longurl" : _json["longUrl"],
        "shorturl" : shorturl,
        "guid": _json["guid"]
    }

    print(json_data)

    result = mycol.insert(json_data)

    # print(result)
    return result

def delete(guid) :
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["bookmarkit"]
    mycol = mydb["request"]
    mycol.remove({"guid": guid})


    # credentials = pika.PlainCredentials('rabbitmqAdm', 'u_pick_it')
    # connection = pika.BlockingConnection(
    #     pika.ConnectionParameters('e004021.ellucian.com',5672,'/',credentials))
    # channel = connection.channel()
    #
    # channel.queue_declare(queue='bookmark_request_queue')
    #
    # channel.basic_publish(exchange='', routing_key='bookmark_request_queue', body=json.dumps(_json))
    # print(" [x] Sent "+json.dumps(_json))
    # connection.close()

