from flask import request, Response
from application import app
import requests

@app.route('/post/prize', methods=['GET', 'POST'])
def post_prize():

    entry_code = request.data.decode('utf-8')

    #if entry_code  == "EqH371":
    if entry_code  == "aqb325":
        prize = "You won a big prize"
    #elif entry_code[:3] == "EqH" or entry_code[-3:] == "371" :
    elif entry_code[0] == "a" or entry_code[3] == "3" :
        prize = "You won a small prize"
    else:
        prize = "You have not won a prize"
    return Response(prize, mimetype="text/plain")
