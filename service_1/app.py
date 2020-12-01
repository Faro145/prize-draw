from application import app
from application import db
from application.models import Prize_Draw

db.create_all()

if __name__ == "__main__":
    app.run(port=5000, debug=True, host='0.0.0.0')

from application import routes
