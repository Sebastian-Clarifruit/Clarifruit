from flask import Flask, request, json, jsonify
import time
import random
import string

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/test')
def barcode_info():
    barcode = request.args.get('barcode')
    if barcode == "tzahi":
        letters = string.digits
        name = "demo " + (''.join(random.choice(letters) for i in range(6)))
        return {
                    "inspectionName": name,
                    "ggnumber": 987654321,
                    "itemweight": 500,
                    "grower": "Fran",
                    "coo": "Mexico",
                    "codeVariety": "Thompson",
                    "processKey": "GRAPES",
                    "standardKey": "DEFAULT"
                }
        
    if barcode == "Nature Fresh":
        letters = string.digits
        name = "Nature Fresh Trial" + (''.join(random.choice(letters) for i in range(6)))
        return {
                    "inspectionName": name,
                    "coo": "USA",
                    "warehouse": "NFFSALESDC",
                    "insty": " Entrance Control",
                    "shipmen": "Conventional",
                    "insppo": "Arrival",
                    "shi": "N/A",
                    "shire": 12345,
                    "cnee": "Nature Fresh Farms",
                    "cneeref": 1111,
                    "loca": "NFFSALESDC, Production",
                    "ve": "Maersk",
                    "sample": 100,
                    "codeVariety": "BeefSteak",
                    "processKey": "lot",
                    "standardKey": "DEFAULT"
                }
            
        
    if barcode == "Bjs Grapes":
        letters = string.digits
        name = "Bjs Grapes" + (''.join(random.choice(letters) for i in range(6)))
        return {
                    "inspectionName": name,
                    "COO": "USA",
                    "PD": "1709607600000",
                    "IN": "BJ's",
                    "codeVariety": "CO",
                }
    if barcode == "Bjs Oranges":
        letters = string.digits
        name = "Bjs Oranges" + (''.join(random.choice(letters) for i in range(6)))
        return {
                    "inspectionName": name,
                    "COO": "USA",
                    "PD": "1709607600000",
                    "IN": "BJ's",
                    "codeVariety": "CO",
                }
        if barcode == "abcd1234":
        letters = string.digits
        name = "FDM" + (''.join(random.choice(letters) for i in range(6)))
        return {
                    "inspectionName": name,
                    "COO": "Costa Rica",
                    "arrivaldate": "1709607600000",
                    "IN": "FDM",
                    "codeVariety": "SG",
                }
  
    else:
        return jsonify({"error":"No Stock - Barcode not exist",
                        "message":"There is no stock on pallet reference"}), 422
                        
                                                            
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
    
