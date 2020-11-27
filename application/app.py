from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    entry_code = requests.get("https://entry_code:5001/entry_code")
    prize = requests.post("https://prize:5001/prize", data = prize.text)
    render_template('index.html', entry_code="entry_code.txt", prize="prize.text")
    
if __name__ == '__main__':
    app.run(port=5000, host='0.0.0.0')

