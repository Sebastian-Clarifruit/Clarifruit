from flask import Flask, request, jsonify
import csv

app = Flask(__name__)

# Load CSV data into memory for quick access
data = []
with open('your_file.csv', newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        data.append(row)

@app.route('/get_info', methods=['GET'])
def get_info():
    pallet_number = request.args.get('Pallet#')
    
    if not pallet_number:
        return jsonify({"error": "Pallet# is required"}), 400
    
    # Search for the pallet number in the data
    for row in data:
        if row['Pallet#'] == pallet_number:
            return jsonify(row), 200  # Directly return the row dictionary
    
    # If the pallet number is not found
    return jsonify({"error": "Pallet# not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)
