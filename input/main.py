from flask import Flask
from flask import request
app = Flask(__name__)

# If /json route receives header "application/json"
@app.route('/json', methods=['GET','POST'])
def json():

	  app.logger.debug("JSON received...")
      app.logger.debug(request.json)
    
    if request.json:
        mydata = request.json
        
        return "mengembalikan json tempat tanggal_lahir %s" % mydata.get("ttl")

    else:
        return "no json received"