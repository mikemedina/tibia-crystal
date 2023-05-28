from flask import render_template, request

from . import app
from .models import Spells


@app.route('/', methods=['GET'])
def show_form():
    return render_template('spell_data.html', spell_data={})


@app.route('/spell-data', methods=['GET'])
def get_spell_data():
    level = int(request.args.get('level'))
    magic_level = int(request.args.get('magic-level'))
    spells = Spells.query.all()
    spell_data = {
        spell.name: calculate_spell_damage(level, magic_level, spell)
        for spell in spells
    }
    return render_template('spell_data.html', spell_data=spell_data)


def calculate_spell_damage(level, magic_level, spell):
    twenty_percent_of_your_level = (level * 0.2)
    magic_level_times_average_spell_multiplier = (magic_level * (
            spell.x_min + spell.x_max)) / 2
    average_flat_spell_fluctuation = (spell.y_min + spell.y_max) / 2
    return int(twenty_percent_of_your_level \
        + magic_level_times_average_spell_multiplier \
        + average_flat_spell_fluctuation)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
