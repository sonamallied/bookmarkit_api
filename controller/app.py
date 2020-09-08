from flask import Flask
from flask_cors import CORS
from flask import jsonify,request

app = Flask(__name__)
CORS(app)

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
        resp = jsonify(_chikcletName)
        resp.status_code = 200

        return resp
    else:

        return not_found()


@app.errorhandler(404)
def not_found(error=None):
    message = {
        'status':404,
        'message':'Not found' + request.url

    }
    resp = jsonify(message)
    resp.status_code =404
    return  resp


if __name__ == "__main__":
    app.run(debug=True);