from flask import render_template, url_for, Response
from application import app, db
from application.models import Team
import requests

@app.route('/')
@app.route('/index', methods=['GET'])
def index():
    results_data = Prize_draw.query.all()
    return render_template('index.html', results=results_data)
   
@app.route('/prizedraw', methods=['GET'])
def prizedraw():
    letters = requests.get("https://letters:5001/get/letters")
    numbers = request.get("https://numbers:5002/get/numbers")
    entry_code = requests.get("https://entry_code:5003/get/entry_code")
    prize = requests.post("https://prize:5003/post/prize", data = entry_code)
    
    data = Prize_Draw(letters=letters.text, numbers=numbers.text, entry_code=entry_code.text, prize=prize.text)
    db.session.add(data)
    db.session.commit()

    return render_template('prizedraw.html')