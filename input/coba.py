from flask import Flask,request,jsonify,json
app = Flask(__name__)

vars = [{'ttl':'01 Feb 2018'}]

def coba(a):
    var = {'ttl' : request.json['ttl']}

    vars.append(var)
    return jsonify({'vars' : vars})