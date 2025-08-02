from flask import Flask, request, jsonify
from flask_cors import CORS
import pyautogui
import time

app = Flask(__name__)
CORS(app)

@app.route('/typewrite', methods=['POST'])
def typewrite():
    data = request.get_json()
    text = data.get('text', '')
    time.sleep(5)
    pyautogui.typewrite(text)
    pyautogui.press('enter')
    return jsonify({"status": "success"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
