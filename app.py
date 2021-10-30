from flask import Flask, jsonify, request
from merge import *
app = Flask(__name__)

@app.route('/address', methods = ['POST'])
def addressFormatter():
    data = request.get_json()
    lis=[data['house'],data['street'],data['landmark'],data['locality'],data['vtc'],data['district'],data['state'],data['sub district'],data['pincode']]
    
    return jsonify(merge(lis))

if __name__ == '__main__':
    app.run(debug=True)