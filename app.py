import openai

openai.api_key = "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"

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()

    if not data or 'message' not in data:
        return jsonify({"error": "Invalid input"}), 400

    user_message = data['message']

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",  # Replace with your model (e.g., gpt-3.5-turbo or gpt-4)
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": user_message}
            ]
        )
        reply = response['choices'][0]['message']['content']
        return jsonify({"response": reply})
    except Exception as e:
        return jsonify({"error": str(e)}), 500
