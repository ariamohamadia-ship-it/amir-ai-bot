import os
from flask import Flask, request
import requests

app = Flask(__name__)

TOKEN = os.environ.get("BOT_TOKEN")

@app.route("/")
def home():
    return "AmirAI Bot is alive!"

@app.route("/" + TOKEN, methods=["POST"])
def webhook():
    try:
        data = request.get_json()
        if data and "message" in data:
            chat_id = data["message"]["chat"]["id"]
            text = data["message"].get("text", "")
            url = "https://api.telegram.org/bot" + TOKEN + "/sendMessage"
            payload = {"chat_id": chat_id, "text": "📩 دریافت شد: " + text}
            requests.post(url, json=payload)
        return "OK", 200
    except Exception as e:
        print("Error:", e)
        return "OK", 200

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
