from flask import Flask,request,jsonify
from input import coba as CB
app = Flask(__name__)

@app.route('/<gurih>')
def hello_world(gurih):
    return gurih

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id

@app.route('/crot', methods=['POST'])
def login():
	return request.form['anu']

@app.route('/input/ttl', methods=['POST','GET'])
def ttl():
	return jsonify(
		tempat="bandung",
		tanggal_lahir="13 mei 1999" 
	)

@app.route('/input/dd/<b>', methods=['POST'])
def aa(b):
    return jsonify(CB.din(b)) 
