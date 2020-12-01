from flask import request, Response
import requests
from application import app

@app.route('/get/entry_code', methods=['GET', 'POST'])
def get_entry_code():
    letters = request.data.decode('utf-8')
    numbers = request.data.decode('utf-8')
    entry_code = letters + numbers
    return Response(entry_code, mimetype="text/plain")
   
@app.route('/post/prize', methods=['POST'])
def post_prize():
    entry_code = request.data.decode('utf-8')
    prize_code = "Bzk371"
    if entry_code == prize_code:
        prize = "You won a big prize"
        return Response(prize, mimetype="text/plain")
    else:
        prize = "You have not won a prize"
        return Response(prize, mimetype="text/plain")