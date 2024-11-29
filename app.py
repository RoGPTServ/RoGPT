from flask import Flask, request, jsonify
import openai

app = Flask(__name__)  # Initialize the Flask app

# Replace with your OpenAI API key
openai.api_key = "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"

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()  # Get JSON data from the POST request

    if not data or 'message' not in data:
        return jsonify({"error": "Invalid input"}), 400

    user_message = data['message']

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",  # Replace with your desired model
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": user_message}
            ]
        )
        reply = response['choices'][0]['message']['content']
        return jsonify({"response": reply})
    except Exception as e:
        print(f"Error: {e}")  # Log the error for debugging
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)  # Specify the port for Render
