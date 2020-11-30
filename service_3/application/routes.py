from flask import request, Response
import requests
from application import app
import random

@app.route('/get/numbers', methods=['GET'])
def get_numbers():
    number_one = str(random.randint(0,9))
    number_two = str(random.randint (0,9))
    number_three = str(random.randint (0,9))
    numbers = number_one + number_two + number_three
    return Response(numbers, mimetype="text/plain")