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
    if barcode == "barcode":
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
    if barcode == "seba":
            letters = string.digits
            name = "demo " + (''.join(random.choice(letters) for i in range(6)))
            return {
                        "inspectionName": name,
                        "productor": "Fruta Sol",
                        "planta": "Curico",
                        "cosecha": "1672752255000",
                        "recepcion": "1672838655000",
                        "codeVariety": "Common Red Apple",
                        "processKey": "APPLES",
                        "standardKey": "DEFAULT"
                    }
    if barcode == "cristobal":
            letters = string.digits
            name = "demo " + (''.join(random.choice(letters) for i in range(6)))
            return {
                        "inspectionName": name,
                        "prod": "Productor Manzanas",
                        "npallet": "300",
                        "fdc": "1672752255000",
                        "codeVariety": "Common Red Apple",
                        "processKey": "proceso",
                        "standardKey": "USDA"
                    }
    if barcode == "Cherry Summit":
            letters = string.digits
            name = "Cherry Summit"
            return {
                        "inspectionName": name,
                        "productor": "Agricolas Farias",
                        "nproductor": 48,
                        "cosecha": "1681704000",
                        "recepcion": "1681704000",
                        "kgtotal": 25
                    }
    if barcode == "BlueBerry Convention":
            letters = string.digits
            name = "BlueBerry Convention"
            return {
                        "inspectionName": name,
                        "productor": "Agricolas Farias",
                        "nproductor": 48,
                        "cosecha": "1681704000",
                        "recepcion": "1681704000",
                        "kgtotal": 25
                    }
    if barcode == "pineapple":
            letters = string.digits
            name = "Pineapples - PS:  " + (''.join(random.choice(letters) for i in range(6)))
            return {
                        "inspectionName": name,
                        "ggnumber": 94544324,
                        "grower": "Grower C",
                        "customer": "Walmart",
                        "codeVariety": "commonpa",
                        "processKey": "pineapples_ps_process",
                        "standardKey": "stand_ps_pineapples"
                    }
    if barcode == "apple":
            letters = string.digits
            name = "Apples - PS:  " + (''.join(random.choice(letters) for i in range(6)))
            return {
                        "inspectionName": name,
                        "ggnumber": 51345534,
                        "grower": "Grower A",
                        "customer": "EDEKA",
                        "codeVariety": "commonrapple",
                        "processKey": "p_apple_ps",
                        "standardKey": "stand_ps_apples"
                    }
    if barcode == "cherry":
            letters = string.digits
            name = "Cherries - PS:  " + (''.join(random.choice(letters) for i in range(6)))
            return {
                        "inspectionName": name,
                        "ggnumber": 43125623,
                        "grower": "Grower B",
                        "customer": "M&S",
                        "codeVariety": "and",
                        "processKey": "cherries_ps_process",
                        "standardKey": "stand_ps_cherries"
                    }
    if barcode == "grape":
            letters = string.digits
            name = "Grapes - PS:  " + (''.join(random.choice(letters) for i in range(6)))
            return {
                        "inspectionName": name,
                        "ggnumber": 31254236,
                        "grower": "Grower C",
                        "customer": "Amazon",
                        "codeVariety": "THOMPSON",
                        "processKey": "p_grape_ps",
                        "standardKey": "stand_ps_graes"
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
    
