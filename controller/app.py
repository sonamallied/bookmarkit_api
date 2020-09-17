from flask import Flask
from flask_cors import CORS
from flask import jsonify,request

from service import publish
from service import consume
from service import redirect
from resources.URLGenerator import URLGen
from resources.URLRedirect import URLRedirect
from flask import Blueprint
from flask_restful import Api
import json








app = Flask(__name__)
CORS(app)

api_bp = Blueprint('api', __name__)
api = Api(api_bp)

@app.route("/about")
def about():
   about = {
      "name" : "BookmarkIt_API",
      "version" : "1.0"
   }
   return about


@app.route('/requestChikclet',methods=['POST'])

def requestChikclet():
    print(request.json)
    _json =request.json
    _longUrl= _json['longUrl']
    _chikcletName = _json['chikcletName']



    if _longUrl and _chikcletName and request.method == 'POST':
        # id = mycol.insert_one({'name':_name,'email':_email,'pwd':_pwd})
        print("_longUrl",_longUrl);
        publish.send(_json)
        resp = jsonify("Successful")
        resp.status_code = 200

        return resp
    else:

        return not_found()


@app.route('/receiveFromQueue',methods=['GET'])
def receiveFromQueue():
        #consume.receive()
     #response = consume.receive()
     #response.status_code = 200
     #print(response)
    response = consume.receive()
    response.status_code = 200  # or 400 or whatever
    return response
     #return jsonify((response))


@app.route('/approve',methods=['POST'])
def approve():
    print(request.json)
    _json =request.json
    _longUrl= _json['longUrl']
    _chikcletName = _json['chikcletName']
    _guid = _json['guid']


    if _longUrl and _chikcletName and _guid and request.method == 'POST':
        # id = mycol.insert_one({'name':_name,'email':_email,'pwd':_pwd}
        publish.approve(_json)

        publish.delete(_guid)

        resp = jsonify("Successful")
        resp.status_code = 200

        return resp
    else:

        return not_found()


@app.route('/getApprovedData',methods=['GET'])
def getApprovedData():

    response = consume.approvedData()
    response.status_code = 200  # or 400 or whatever
    return response
     #return jsonify((response))


@app.errorhandler(404)
def not_found(error=None):
    message = {
        'status':404,
        'message':'Not found' + request.url

    }
    resp = jsonify(message)
    resp.status_code =404
    return  resp


@app.route('/URLGen',methods=['POST'])
def URLGene():
    api.add_resource(URLGen)
    return "hi"

@app.route('/<shorturl>',methods=['GET'])
def sendUrl(shorturl):
    str= "http://localhost:5000/"+shorturl
    print(str)
    print(shorturl)
    #return "hi"
    response = jsonify(redirect.redirectUrl(str))

    return response


#api.add_resource(URLGen, '/URLGen')
#api.add_resource(URLRedirect, '/URLRedirect')



if __name__ == "__main__":
    app.run(debug=True);