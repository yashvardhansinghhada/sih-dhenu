import os
import requests
from flask import Flask, request, jsonify
from openai import OpenAI

app = Flask(__name__)

# API Key and Endpoint
API_URL = "https://api.dhenu.ai/v1"
# Fetch from environment variables

@app.route('/chat', methods=['POST'])
def chat():
    try:
        # Get user message from the request
        data = request.get_json()
        user_message = data.get("message")

        if not user_message:
            return jsonify({"error": "Message is required"}), 400

        # Prepare the API request


        # Send request to Dhenu API
        client = OpenAI(base_url="https://api.dhenu.ai/v1", api_key=dh-d_mYtfQEWSKSMCfPBVcjoNHuEStalCfnE1vKTiUy2vs)
        stream = client.chat.completions.create(
            model="dhenu2-in-8b-preview",
            messages=[
                {"role": "user",
                 "content": user_message
                 }
            ],
        )
        response = stream.choices[0].message.content

        return jsonify({"reply": response})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=9000)
