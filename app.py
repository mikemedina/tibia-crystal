from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app = Flask(__name__)
app.debug = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///crystal.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS '] = False

db = SQLAlchemy(app)

import models

@app.route('/')
def hello():
	spells = models.Spell.query.all()
	spell_data = [{ 'name': spell.name, 'xMax': spell.x_max, 'yMax': spell.y_max, 'xMin': spell.x_min, 'yMin': spell.y_min } for spell in spells]
	return jsonify(spell_data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

