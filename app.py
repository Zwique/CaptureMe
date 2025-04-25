from flask import Flask, request, render_template, jsonify
from flask_cors import CORS
import threading
import time
import subprocess
import requests
import logging

from camera import save_photo
from qr_code import generate_qr_code
from utils import get_access_url

logging.basicConfig(level=logging.INFO)

def get_ngrok_url():
    try:
        response = requests.get("http://127.0.0.1:4040/api/tunnels")
        tunnels = response.json().get("tunnels", [])

        if tunnels:
            return tunnels[0].get("public_url")
        else:
            raise Exception("No tunnels found.")
    except Exception as e:
        logging.error(f"Error retrieving Ngrok URL: {str(e)}")
        return None

def start_ngrok():
    ngrok_process = subprocess.Popen(['ngrok', 'http', '1000'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    time.sleep(5)
    return get_ngrok_url(), ngrok_process

PORT = 1000
QR_CODE_FILE = "qr_code.png"

NGROK_URL, ngrok_process = start_ngrok()

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    access_url = get_access_url(NGROK_URL)
    return render_template("capture.html", access_url=access_url)

@app.route('/save_photo', methods=['POST'])
def save_photo_route():
    photo = request.files.get('photo')

    if photo:
        try:
            saved_filename = save_photo(photo)
            if saved_filename:
                return f"Photo saved as {saved_filename}"
            else:
                return jsonify({"error": "Failed to save photo."}), 500
        except Exception as e:
            logging.error(f"Error saving photo: {str(e)}")
            return jsonify({"error": "Error saving photo."}), 500
    return jsonify({"error": "No photo found in request."}), 400

def start_flask_server():
    try:
        app.run(host='0.0.0.0', port=PORT, threaded=True)
    except Exception as e:
        logging.error(f"Error starting Flask server: {str(e)}")

if __name__ == "__main__":
    logging.info("Starting Ngrok...")
    if NGROK_URL:
        logging.info(f"Ngrok Public URL: {NGROK_URL}")
    else:
        logging.error("Ngrok URL not found.")

    access_url = get_access_url(NGROK_URL)
    logging.info(f"Access the app at: {access_url}")

    server_thread = threading.Thread(target=start_flask_server, daemon=True)
    server_thread.start()

    if NGROK_URL:
        generate_qr_code(NGROK_URL)
    else:
        logging.error("QR Code not generated due to Ngrok URL issue.")

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        logging.info("Shutting down.")
        ngrok_process.terminate()
        server_thread.join()
