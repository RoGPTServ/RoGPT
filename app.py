from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()  # Parse the JSON from the request
    if not data or 'message' not in data:
        return jsonify({"error": "Invalid input"}), 400
    message = data['message']
    return jsonify({"reply": f"Received: {message}"})
