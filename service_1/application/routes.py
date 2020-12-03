from flask import render_template, url_for, Response
from application import app, db
from application.models import Prize_Draw
import requests

@app.route('/')
@app.route('/index', methods=['GET'])
def index():
    prizes_data = Prize_Draw.query.all()
    return render_template('index.html', prizes=prizes_data)

@app.route('/prizedraw', methods=['GET'])
def prizedraw():
    letters = requests.get("http://service_2:5001/get/letters")
    numbers = requests.get("http://service_3:5002/get/numbers")
    prize = requests.post("http://service_4:5003/post/prize", json={'letters':letters.text, 'numbers': numbers.text})

    data = Prize_Draw(letters=letters.text, numbers=numbers.text, prize=prize.text)
    db.session.add(data)
    db.session.commit()

    return render_template('prizedraw.html',letters=letters.text, numbers=numbers.text, prize=prize.text)
