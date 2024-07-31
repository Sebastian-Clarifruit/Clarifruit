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
    
    if barcode == "(01)10664924899116(13)22108(10)PFLB-45":
        letters = string.digits
        name = "4x6 ct Mix Bell Pep Bags"
        return {
            "inspectionName": name,
            "packageKey": "3576",
            "upc": "684924040054",
        }

    if barcode == "abcd1234":
        letters = string.digits
        name = "Sales Demo" + (''.join(random.choice(letters) for i in range(6)))
        return {
            "inspectionName": name,
            "coo": "USA",
            "grower": "Demo Grower",
            "customer": "Demo Client",
            "arrivaldate": "1718807418296",
            "ggnumber": 12345,
            "in": "BJ's",
            "pd": "1718807418296", 
            "supp": "Affinor",
            "br": "Bj's",
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
            "coo": "Costa Rica",
            "arrivaldate": "1709607600000",
            "grower": "FDM",
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
