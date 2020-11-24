from flask import Flask, Response
import string, random

app = Flask(__name__)

@app.route('/letters', methods=['GET'])
def letters():
    letter_one = random.choice(string.ascii_letters)
    letter_two = random.choice(string.ascii_letters)
    letter_three = random.choice(string.ascii_letters)
    letters = letter_one + letter_two + letter_three
    return Response(letters, mimetext="text/plain")

if __name__ == '__main__':
    app.run(port=5002, host='0.0.0.0')