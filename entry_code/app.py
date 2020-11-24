from flask import Flask, Response, request
import requests
app = Flask(__name__)

@app.route('/entry_code', methods=['GET'])
def entry_code():
    letters = requests.get(letters:5002/letters)
    numbers = request.get(numbers:5003/numbers)
    entry_code = letters + numbers
    return Response(entry_code, mimetext="text/plain")
   
@app.route('/prize', methods=['POST'])
def prize():
    entry_code = request.data.decode('utf-8')
    count = 0
    prize_code = "Bzk371"
    while count < 10:
        if entry_code == prize_code:
            prize = "You won a big prize"
        elif count == 10:
            prize = "You won a small prize"
        else:
            print("You have not won a prize")
            count = count + 1
        return Response(prize, mimetext="text/plain")

if __name__ == '__main__':
    app.run(port=5001, debug=True)
  