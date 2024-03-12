from flask import Flask, request, json, jsonify
import time
import random
import string

app = Flask(__name__)

range_1 = range(80224001,80224004)
range_1t = list(map(str, range_1))
range_2 = range(80224005,80224008)
range_2t = list(map(str, range_2))
range_3 = range(80224009,80224016)
range_3t = list(map(str, range_3))
range_4 = range(80224017,80224021)
range_4t = list(map(str, range_4))
list_1 = ["SUL240131024","SUL240131022","SUL240131025","SUL240131026","SUL240131027","SUL240131029","SUL240131031","SUL240131032","SUL240131034","SUL240131036","SUL240131037","SUL240131039","SUL240131041","SUL240131042"]
list_2 = ["SUL240131023","SUL240131028","SUL240131030","SUL240131033","SUL240131035","SUL240131038","SUL240131040"]
range_5 = range(967,969)
range_5t = list(map(str, range_5))
range_6 = range(970,972)
range_6t = list(map(str, range_6))
range_7 = range(973,976)
range_7t = list(map(str, range_7))
range_8 = range(977,984)
range_8t = list(map(str, range_8))
range_9 = range(985,986)
range_9t = list(map(str, range_9))
range_10t = 987
list_3 = ["SUL240131001","SUL240131002","SUL240131004","SUL240131005","SUL240131006","SUL240131007","SUL240131010","SUL240131011","SUL240131012","SUL240131014","SUL240131015","SUL240131016","SUL240131017","SUL240131018","SUL240131020"]
list_4 = ["SUL240131003","SUL240131008","SUL240131009","SUL240131013","SUL240131019","SUL240131021","SUL240131040"]
range_11 = range(16236,16248)
range_11t = list(map(str, range_11))
range_12 = range(16249,16255)
range_12t = list(map(str, range_12))
range_13t = 16256
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
    if barcode == range_11t:
        letters = string.digits
        name = barcode
        return {
            "inspectionName": name,
            "tlt": "21002754",
            "lab": "KIWISTAR",
            "siz": 39,
            "gro": "SOC. COOP. AGR. ZEOLI FRUIT",
        }
    if barcode == range_12t:
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

