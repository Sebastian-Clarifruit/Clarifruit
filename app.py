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
    if barcode == "IFPA 2023":
            letters = string.digits
            name = "IFPA 2023 " + (''.join(random.choice(letters) for i in range(6)))
            return {
                        "inspectionName": name,
                        "grower": "Grower A",
                        "ggnumber": "515",
                        "arrivaldate": "1697727235000",
                        "temp": "16"
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
    if barcode == "Demo España":
            letters = string.digits
            name = "Proceso Manzanas"
            return {
                        "inspectionName": name,
                        "productor": "Agricolas Farias",
                        "nproductor": 48,
                        "planta": "Planta Norte",
                        "cosecha": "1681838430000",
                        "recepcion": "1681838430000",
                        "kgtotal": 25
                    }
    if barcode == "Francisca":
            letters = string.digits
            name = "Proceso Manzanas"
            return {
                        "inspectionName": name,
                        "productor": "Agricolas Farias",
                        "nproductor": 48,
                        "planta": "Planta Norte",
                        "cosecha": "1681838430000",
                        "recepcion": "1681838430000",
                        "kgtotal": 25
                    }
    if barcode == "USDA":
            letters = string.digits
            name = "USDA Demo Sample"
            return {
                        "inspectionName": name,
                        "ggnumber": 001234,
                        "grower": "Grower B",
                        "coo": "Chile",
                        "customer": "USDA",
                        "arrivaldate": "1705460400000"
                    }
    if barcode == "Tomate":
            letters = string.digits
            name = "Demo Tomate"
            return {
                        "inspectionName": name,
                        "productor": "Agricolas Farias",
                        "cosecha": "1681838430000",
                        "recepcion": "1681838430000",
                        "kgtotal": 25,
                        "ncajas": 48
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
    
