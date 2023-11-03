import requests
from flask import Flask, make_response, request
from flask_cors import CORS
import json

app = Flask(__name__)
cors = CORS(app)

master_records = list()

@app.route('/get')
def get():
	global master_records
	return make_response(master_records)

@app.route('/add', methods=['POST'])
def home():
	global master_records
	json = request.json
	master_records.append(json)
	return make_response('home')

if __name__ == "__main__":
    app.run()
