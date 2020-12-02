from flask import request, Response
import requests
from application import app

@app.route('/get/prize', methods=['GET', 'POST'])
def get_prize():
    numbers = request.data.decode('utf-8')
    if numbers == "371":
        prize = "You won a big prize"
    else:
        prize = "You have not won a prize"
    return Response(prize, mimetype="text/plain")