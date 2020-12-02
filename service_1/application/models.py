from application import db

class Prize_Draw(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    letters = db.Column(db.String(30), nullable=False)
    numbers = db.Column(db.String(30), nullable=False)
    prize = db.Column(db.String(100), nullable=False)