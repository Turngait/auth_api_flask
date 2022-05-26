from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from config.db_config import db_config
from middlewares.check_api_key import CheckAPIKEY
from middlewares.check_json import CheckJSON
from config.config import MASTER_API_KEY

app = Flask(__name__)
app.wsgi_app = CheckAPIKEY(app.wsgi_app, MASTER_API_KEY)
app.wsgi_app = CheckJSON(app.wsgi_app)
app.config['SQLALCHEMY_DATABASE_URI'] = db_config['mysql']
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

CORS(app)
db = SQLAlchemy(app)
