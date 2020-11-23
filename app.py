import string, random
from flask import Flask

app = Flask(__name__)

@app.route('/letters', methods=['GET'])
def letters():
  letter_one = random.choice(string.ascii_letters)
  letter_two = random.choice(string.ascii_letters)
  letter_three = random.choice(string.ascii_letters)
  letters = letter_one + letter_two + letter_three
  return letters

@app.route('/numbers', methods=['GET'])
def numbers():
  number_one = random.randint(0,9)
  number_two = random.randint (0,9)
  number_three = random.randint (0,9)
  numbers = str(number_one + number_two + number_three)
  return numbers
  
 @app.route('/entry_code', methods=['GET'])
 def entry_code():
   entry_code = letters + numbers
   return entry_code
   
 @app.route('/prize_code', methods=['GET'])
 def prize():
   count = 0
   prize_code = "Bzk371"
   while count < 10:
      if entry_code = prize_code:
        prize = "You won a big prize"
        return prize
      elif count = 10:
        prize = "You won a small prize"
        return prize
      else:
        print("You have not won a prize")
        count = count + 1
   
 if __name__ == '__main__':
    app.run(port=5000, debug=True)
  
