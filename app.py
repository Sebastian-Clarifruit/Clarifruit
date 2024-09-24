from flask import Flask, request, json, jsonify
import time
import random
import string

app = Flask(__name__)

def hello_world():
    return 'Hello, World!'


@app.route('/test')
def barcode_info():
    barcode = request.args.get('barcode')
    
  

    if barcode == "abcd1234":
        letters = string.digits
        name = "Strawberry Fields"
        return {
            "inspectionName": name,
            "coo": "USA",
            "grower": "Field 1",
            "lot": "2404",
            "packdate": "1709607600000",       
        }
    else:
        return jsonify({"error": "No Stock - Barcode not exist",
                        "message": "There is no stock on pallet reference"}), 422


@app.route('/foo', methods=['POST'])
def print_payload():
    payload = request.get_json()
    print(payload)
    return 'Payload received and printed'
    if __name__ == '__main__':
        app.run()


@app.route('/barcode_issue')
def index():
    return jsonify("Error: Barcode is not exists"), 422
