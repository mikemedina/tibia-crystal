from flask import Flask
from flask_cors import CORS
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///crystal.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS '] = False

CORS(app, origins=['http://localhost:5000', 'http://127.0.0.1:5000'])
db = SQLAlchemy(app)
migrate = Migrate(app, db)
