from flask import Flask
from flask import request
app = Flask(__name__)

@app.route('/postjson', methods=['POST'])
def postjson():
	print (request.is_json)
	content = request.get_json()
    print (content)
    return 'JSON posted'