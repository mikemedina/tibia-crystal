from flask import Flask, render_template, request
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///crystal.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS '] = False

CORS(app, origins=['http://localhost:5000', 'http://127.0.0.1:5000'])
db = SQLAlchemy(app)


class Spells(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    vocation = db.Column(db.String(10))
    x_max = db.Column(db.Float)
    y_max = db.Column(db.Integer)
    x_min = db.Column(db.Float)
    y_min = db.Column(db.Integer)


def spell_to_dict(spell):
    return {
        'name': spell.name,
        'vocation': spell.vocation,
        'xMax': spell.x_max,
        'yMax': spell.y_max,
        'xMin': spell.x_min,
        'yMin': spell.y_min
    }


@app.route('/')
def hello():
    return render_template('index.html')


@app.route('/spell-data', methods=['GET'])
def calculate_spell_damage():
    level = int(request.args.get('level'))
    magic_level = int(request.args.get('magic-level'))
    spell = Spells.query.filter_by(name='Avalanche').first()
    damage = (level * 0.2) + (
                (magic_level * (spell.x_min + spell.x_max)) / 2) + (
                         (spell.y_min + spell.y_max) / 2)

    spell_data = {
        'damage': damage
    }

    print(f'Calculated that Avalanche would do '
          f'{spell_data["damage"]} damage at level {level} '
          f'and magic level {magic_level}')

    return render_template('index.html', spell_data=spell_data['damage'])


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
