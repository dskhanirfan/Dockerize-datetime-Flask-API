from flask import Flask,jsonify
from datetime import datetime
app = Flask(__name__)

@app.route("/")
def hello():
	now = datetime.now()
	return jsonify( {"Date and Time: ": now})

if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0')