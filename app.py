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
	ttl = [
	{
		"tempat":"bandung",
		"tanggal_lahir":"13 mei 1999" 
	},
	{ 
		"tempat":"sydney",
		"tanggal_lahir":"13 mei 1999" 
	},
	{ 
		"tempat":"bandung",
		"tanggal_lahir":"1 januari 1997" 
	},
	{
		"tempat":"bandung",
		"tanggal_lahir":"7 Juni 1998"
	},
	{
		"tempat":"Sao paulo",
		"tanggal_lahir":"5 Februari 1992"
	}
]
	return jsonify({'list tempat tanggal_lahir':ttl})

@app.route('/input/dd/<b>', methods=['POST','GET'])
def aa(b):
    return jsonify(CB.din(b))