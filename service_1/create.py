from application import db
from application.models import Prize_Draw

db.drop_all()
db.create_all()