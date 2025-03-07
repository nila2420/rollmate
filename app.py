from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# ESP8266 IP Address (Change this to your ESP8266's IP from Serial Monitor)
ESP_IP = "http://192.168.157.197"

def send_command(command):
    """Send HTTP request to ESP8266"""
    url = f"{ESP_IP}/{command}"
    try:
        response = requests.get(url, timeout=2)
        print(f"Sent: {command}, Response: {response.text}")
        return f"Sent: {command}, Response: {response.text}"
    except requests.exceptions.RequestException:
        print("Failed to connect to ESP8266")
        return "Failed to connect to ESP8266"

# Routes
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/command/<cmd>")
def command(cmd):
    return send_command(cmd)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000,debug=True)