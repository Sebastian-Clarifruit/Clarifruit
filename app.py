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
    
    if barcode == "a1":
        letters = string.digits
        name = "4x6pk Red Bell Pep Bags (Costco Morris USA)"
        return {
            "inspectionName": name,
        }

    if barcode == "abcd1234":
        letters = string.digits
        name = "Sales Demo" + (''.join(random.choice(letters) for i in range(6)))
        return {
            "inspectionName": name,
            "coo": "USA",
            "grower": "Demo Grower",
            "customer": "Demo Client",
            "arrivaldate": "1709607600000",
            "ggnumber": 12345,       
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
    if barcode == "21002754":
        letters = string.digits
        name = barcode
        return {
            "inspectionName": name,
            "exp": "SOC. COOP. AGR. ZEOLI FRUIT",
            "coo": "ITALY",
            "vess": "MSC SAMANTHA",
            "cont": "MSDU 985028/4",
            "eta": "08-03-2024",
        }


    if barcode == "3620215":
        letters = string.digits
        name = barcode
        return {
            "inspectionName": name,
            "exp": "FRUITION SA",
            "coo": "GREECE",
            "vess": "MSC SAMANTHA",
            "cont": "TTNU 820993/1",
            "eta": "08-03-2024",
        }
    if barcode == "3550252":
        letters = string.digits
        name = barcode
        return {
            "inspectionName": name,
            "exp": "FRUTTA FRIULI SCA",
            "coo": "ITALY",
            "vess": "MSC NIOVI VIII",
            "cont": "MNBU 438520/2",
            "eta": "08-03-2024",
        }
    if barcode == "3620216":
        letters = string.digits
        name = barcode
        return {
            "inspectionName": name,
            "exp": "FRUITION SA",
            "coo": "GREECE",
            "vess": "MSC SAMANTHA",
            "cont": "TRIU 895471/2",
            "eta": "08-03-2024",
        }
    if barcode == "3420229":
        letters = string.digits
        name = barcode
        return {
            "inspectionName": name,
            "exp": "VITULA FRUIT SRL",
            "coo": "ITALY",
            "vess": "MSC SAMANTHA",
            "cont": "MSDU 983085/8",
            "eta": "08-03-2024",
        }
    if barcode in range_1t:
        letters = string.digits
        name = barcode
        return {
            "inspectionName": name,
            "tlt": "3420229",
            "lab": "VIOLEA GREEN",
            "siz": 36,
            "gro": "VITULA FRUIT SRL",
        } 
    if barcode in range_2t:
        letters = string.digits
        name = barcode
        return {
            "inspectionName": name,
            "tlt": "3420229",
            "lab": "VIOLEA GREEN",
            "siz": 33,
            "gro": "VITULA FRUIT SRL",
        } 
    if barcode in range_3t:
        letters = string.digits
        name = barcode
        return {
            "inspectionName": name,
            "tlt": "3420229",
            "lab": "VIOLEA GREEN",
            "siz": 30,
            "gro": "VITULA FRUIT SRL",
        }
    if barcode in range_4t:
        letters = string.digits
        name = barcode
        return {
            "inspectionName": name,
            "tlt": "3420229",
            "lab": "VIOLEA ORGANIC",
            "siz": 27,
            "gro": "VITULA FRUIT SRL",
        }
    if barcode in list_1:
        letters = string.digits
        name = barcode
        return {
            "inspectionName": name,
            "tlt": "3620216",
            "lab": "VIOLEA",
            "siz": 25,
            "gro": "FRUITION SA",
        } 
    if barcode in list_2:
        letters = string.digits
        name = barcode
        return {
            "inspectionName": name,
            "tlt": "3620216",
            "lab": "VIOLEA",
            "siz": 27,
            "gro": "FRUITION SA",
        }
    if barcode in range_5t:
        letters = string.digits
        name = barcode
        return {
            "inspectionName": name,
            "tlt": "3550252",
            "lab": "KIWISTAR",
            "siz": 23,
            "gro": "FRUTTA FRIULI SCA",
        }
    if barcode in range_6t:
        letters = string.digits
        name = barcode
        return {
            "inspectionName": name,
            "tlt": "3550252",
            "lab": "KIWISTAR",
            "siz": 27,
            "gro": "FRUTTA FRIULI SCA",
        }
    if barcode in range_7t:
        letters = string.digits
        name = barcode
        return {
            "inspectionName": name,
            "tlt": "3550252",
            "lab": "KIWISTAR",
            "siz": 30,
            "gro": "FRUTTA FRIULI SCA",
        }   
    if barcode in range_8t:
        letters = string.digits
        name = barcode
        return {
            "inspectionName": name,
            "tlt": "3550252",
            "lab": "KIWISTAR",
            "siz": 33,
            "gro": "FRUTTA FRIULI SCA",
        }
    if barcode in range_9t:
        letters = string.digits
        name = barcode
        return {
            "inspectionName": name,
            "tlt": "3550252",
            "lab": "KIWISTAR",
            "siz": 39,
            "gro": "FRUTTA FRIULI SCA",
        }
    if barcode == range_10t:
        letters = string.digits
        name = barcode
        return {
            "inspectionName": name,
            "tlt": "3550252",
            "lab": "KIWISTAR",
            "siz": 42,
            "gro": "FRUTTA FRIULI SCA",
        }
    if barcode in list_3:
        letters = string.digits
        name = barcode
        return {
            "inspectionName": name,
            "tlt": "3620215",
            "lab": "VIOLEA",
            "siz": 25,
            "gro": "FRUITION SA",
        }
    if barcode in list_4:
        letters = string.digits
        name = barcode
        return {
            "inspectionName": name,
            "tlt": "3620215",
            "lab": "VIOLEA",
            "siz": 27,
            "gro": "FRUITION SA",
        }
    if barcode in range_11t:
        letters = string.digits
        name = barcode
        return {
            "inspectionName": name,
            "tlt": "21002754",
            "lab": "KIWISTAR",
            "siz": 39,
            "gro": "SOC. COOP. AGR. ZEOLI FRUIT",
        }
    if barcode in range_12t:
        letters = string.digits
        name = barcode
        return {
            "inspectionName": name,
            "tlt": "21002754",
            "lab": "KIWISTAR",
            "siz": 36,
            "gro": "SOC. COOP. AGR. ZEOLI FRUIT",
        }
    if barcode == range_13t:
        letters = string.digits
        name = barcode
        return {
            "inspectionName": name,
            "tlt": "21002754",
            "lab": "KIWISTAR",
            "siz": 42,
            "gro": "SOC. COOP. AGR. ZEOLI FRUIT",
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
