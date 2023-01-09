from flask import Flask
from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__)
app.config.from_object("config.Config")
db = SQLAlchemy(app)
db.init_app(app)


with app.app_context():
    from routes.main import *
    from routes.plants import *
    from routes.employee import *
    from models.models import *

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)


