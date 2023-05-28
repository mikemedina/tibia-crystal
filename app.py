from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS


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

all_spells = [
    Spells(name='Avalanche Rune', vocation="druid", x_max=2.85, y_max=16, x_min=1.2, y_min=7),
    Spells(name='Energy Strike', vocation="druid", x_max=2.203, y_max=14, x_min=1.403, y_min=8),
    Spells(name='Eternal Winter', vocation="druid", x_max=11, y_max=50, x_min=5.5, y_min=25),
    Spells(name='Explosion Rune', vocation="druid", x_max=3.2, y_max=19, x_min=1.6, y_min=9),
    Spells(name='Fireball Rune', vocation="druid", x_max=3, y_max=17, x_min=1.81, y_min=12),
    Spells(name='Heal Friend', vocation="druid", x_max=14.4, y_max=90, x_min=6.3, y_min=45),
    Spells(name='Heavy Magic Missile Rune', vocation="druid", x_max=1.59, y_max=10, x_min=0.81, y_min=5),
    Spells(name='Ice Wave', vocation="druid", x_max=2, y_max=12, x_min=0.81, y_min=5),
    Spells(name='Intense Healing', vocation="druid", x_max=6, y_max=37, x_min=3.6, y_min=22),
    Spells(name='Light Healing', vocation="druid", x_max=1.8, y_max=11, x_min=1.4, y_min=8),
    Spells(name='Light Magic Missile Rune', vocation="druid", x_max=0.81, y_max=4, x_min=0.4, y_min=3),
    Spells(name='Mass Healing', vocation="druid", x_max=9.6, y_max=125, x_min=4.6, y_min=100),
    Spells(name='Physical Strike', vocation="druid", x_max=2.203, y_max=14, x_min=1.403, y_min=8),
    Spells(name='Stalagmite Rune', vocation="druid", x_max=1.59, y_max=10, x_min=0.81, y_min=5),
    Spells(name='Stone Shower Rune', vocation="druid", x_max=2.6, y_max=16, x_min=1, y_min=6),
    Spells(name='Strong Ice Strike', vocation="druid", x_max=4.4, y_max=28, x_min=2.8, y_min=16),
    Spells(name='Strong Ice Wave', vocation="druid", x_max=7.6, y_max=48, x_min=4.5, y_min=20),
    Spells(name='Sudden Death Rune', vocation="druid", x_max=7.4, y_max=48, x_min=4.3, y_min=32),
    Spells(name='Terra Wave', vocation="druid", x_max=6.75, y_max=30, x_min=3.25, y_min=5),
    Spells(name='Ultimate Healing', vocation="druid", x_max=12.9, y_max=90, x_min=6.8, y_min=42),
    Spells(name='Ultimate Ice Strike', vocation="druid", x_max=7.3, y_max=55, x_min=4.5, y_min=35),
    Spells(name='Wrath of Nature', vocation="druid", x_max=9, y_max=40, x_min=3, y_min=32)
]

@app.route('/')
def hello():
    # TODO: Remove query
    with app.app_context():
        db.create_all()
        for spell in all_spells:
            db.session.add(spell)
        db.session.commit()
    spells = Spells.query.all()
    return jsonify([spell_to_dict(spell) for spell in spells])
    #return render_template('index.html')

@app.route('/spell-data', methods=['GET'])
def calculate_spell_damage():
    level = int(request.args.get('level'))
    magic_level = int(request.args.get('magic-level'))
    spell = Spells.query.filter_by(name='Avalanche').first()
    damage = (level * 0.2) + ((magic_level * (spell.x_min + spell.x_max)) / 2) + ((spell.y_min + spell.y_max) / 2)

    spell_data = {
        'damage': damage
    }
 
    print(f'Calculated that Avalanche would do '
          f'{spell_data["damage"]} damage at level {level} '
          f'and magic level {magic_level}')

    return render_template('index.html', spell_data=spell_data)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

