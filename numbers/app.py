from flask import Flask, Response
import random

app = Flask(__name__)

@app.route('/numbers', methods=['GET'])
def numbers():
    number_one = random.randint(0,9)
    number_two = random.randint (0,9)
    number_three = random.randint (0,9)
    numbers = str(number_one + number_two + number_three)
    return Response(numbers, mimetext="text/plain")

if __name__ == '__main__':
  app.run(port=5003, host='0.0.0.0')