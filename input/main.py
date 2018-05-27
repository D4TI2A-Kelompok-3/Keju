from flask import Flask, jsonify
from flask import request
app = Flask(__name__)

@app.route('/input/ttl', methods=['GET','POST'])
def ttl():
	return request.form['ttl'] 