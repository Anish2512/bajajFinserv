from flask import Flask, request, jsonify

app = Flask(__name__)

USER_ID = "AnishPatro_25122003"
EMAIL = "anishpatro25@gmail.com"
ROLL_NUMBER = "21BCE5059"

# Route for GET method
@app.route('/bfhl', methods=['GET'])
def get_operation_code():
    return jsonify({"operation_code": 1}), 200

# Route for POST method
@app.route('/bfhl', methods=['POST'])
def process_data():
    data = request.json.get('data', [])
    numbers = []
    alphabets = []
    highest_lowercase_alphabet = []

    for item in data:
        if item.isdigit():
            numbers.append(item)
        elif item.isalpha():
            alphabets.append(item)
            if item.islower():
                if not highest_lowercase_alphabet or item > highest_lowercase_alphabet[0]:
                    highest_lowercase_alphabet = [item]

    response = {
        "is_success": True,
        "user_id": USER_ID,
        "email": EMAIL,
        "roll_number": ROLL_NUMBER,
        "numbers": numbers,
        "alphabets": alphabets,
        "highest_lowercase_alphabet": highest_lowercase_alphabet
    }

    return jsonify(response), 200

if __name__ == '__main__':
    app.run(debug=True)
