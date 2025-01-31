from flask import Flask, request, jsonify
import requests
import os
from dotenv import load_dotenv

# Load API key from .env file
load_dotenv()
HUGGINGFACE_API_KEY = os.getenv("HUGGINGFACE_API_KEY")

MODEL = "deepseek-ai/DeepSeek-R1"
API_URL = f"https://api-inference.huggingface.co/models/{MODEL}"

app = Flask(__name__)

@app.route("/proxy", methods=["POST"])
def proxy_request():
    data = request.json
    headers = {"Authorization": f"Bearer {HUGGINGFACE_API_KEY}"}
    
    response = requests.post(API_URL, json=data, headers=headers)
    return jsonify(response.json())

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
