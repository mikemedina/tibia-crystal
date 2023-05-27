from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS


app = Flask(__name__)
app.debug = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///crystal.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS '] = False
CORS(app)

db = SQLAlchemy(app)

import models

@app.route('/')
def hello():
    spells = models.Spell.query.all()
    spell_data = [
        {
            'name': spell.name,
            'xMax': spell.x_max,
            'yMax': spell.y_max,
            'xMin': spell.x_min,
            'yMin': spell.y_min
        }
        for spell in spells
    ]
    return render_template('index.html')


@app.route('/spell-data', methods=['GET'])
def spell_data():
    level = request.args.get('level')
    magic_level = request.args.get('magic-level')

    # Perform any necessary processing with the received data
    # ...

    # Return a response
    return '{"message": "' + 'Received data: Level={}, Magic Level={}'.format(level, magic_level) + '"}'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

