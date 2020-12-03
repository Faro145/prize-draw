from flask import request, Response
from application import app

@app.route('/post/prize', methods=['GET', 'POST'])
def post_prize():
    data = request.get_json()
    if data['letters'] == "EqH" and data['numbers'] == "371":
        prize = "You won a big prize"
    elif data['letters'] == "EqH" or data['numbers'] == "371" :
        prize = "You won a small prize"
    else:
        prize = "You have not won a prize"
    return Response(prize, mimetype="text/plain")
