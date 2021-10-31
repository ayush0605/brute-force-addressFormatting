from flask import Flask, jsonify, request
from merge import *
from mergeLang import *
app = Flask(__name__)

@app.route('/')
def home():
    return 'Address Formatting API. Deployed on : The API is deployed on heroku. The url is : https://brute-force-address.herokuapp.com/. The endpoints are /address (it doesnot considers language) and /addressLang (it considers language code as langcode in JSON input)'

@app.route('/address', methods = ['POST'])
def addressFormatter():
    data = request.get_json()
    lis=[data['house'],data['street'],data['landmark'],data['locality'],data['vtc'],data['district'],data['state'],data['sub district'],data['pincode']]
    
    return jsonify(merge(lis))

#This considers languages and then declutters the address. It expects langcode in JSON input
@app.route('/addressLang', methods = ['POST'])
def addressFormatterLang():
    data = request.get_json()
    if 'langcode' in data:
        langcode = data['langcode']
    else:
        langcode = '00'

    lis=[data['house'],data['street'],data['landmark'],data['locality'],data['vtc'],data['district'],data['state'],data['sub district'],data['pincode'],langcode]
    
    return jsonify(mergeLang(lis))

if __name__ == '__main__':
    app.run(debug=True)