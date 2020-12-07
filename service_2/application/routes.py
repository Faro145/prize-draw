from flask import request, Response
import requests
from application import app
import random, string

@app.route('/get/letters', methods=['GET'])
def get_letters():
    #letter_one = random.choice(string.ascii_letters)
    #letter_two = random.choice(string.ascii_letters)
    #letter_three = random.choice(string.ascii_letters)
    letter_one = random.choice(string.ascii_lowercase)
    letter_two = random.choice(string.ascii_lowercase)
    letter_three = random.choice(string.ascii_lowercase)
    letters = letter_one + letter_two + letter_three
    return Response(letters, mimetype="text/plain")
