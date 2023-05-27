from app import app, db
import models

def populate_spells():
    all_spells = [
        {
            'name': 'Avalanche Rune',
            'x_max': 2.85,
            'y_max': 16,
            'x_min': 1.2,
            'y_min': 7
        },
        {
            'name': 'Energy Strike',
            'x_max': 2.203,
            'y_max': 14,
            'x_min': 1.403,
            'y_min': 8
        },
        {
            'name': 'Eternal Winter',
            'x_max': 11,
            'y_max': 50,
            'x_min': 5.5,
            'y_min': 25
        },
        {
            'name': 'Explosion Rune',
            'x_max': 3.2,
            'y_max': 19,
            'x_min': 1.6,
            'y_min': 9
        },
        {
            'name': 'Fireball Rune',
            'x_max': 3,
            'y_max': 17,
            'x_min': 1.81,
            'y_min': 12
        },
        {
            'name': 'Heal Friend',
            'x_max': 14.4,
            'y_max': 90,
            'x_min': 6.3,
            'y_min': 45
        },
        {
            'name': 'Heavy Magic Missile Rune',
            'x_max': 1.59,
            'y_max': 10,
            'x_min': 0.81,
            'y_min': 5
        },
        {
            'name': 'Ice Wave',
            'x_max': 2,
            'y_max': 12,
            'x_min': 0.81,
            'y_min': 5
        },
        {
            'name': 'Intense Healing',
            'x_max': 6,
            'y_max': 37,
            'x_min': 3.6,
            'y_min': 22
        },
        {
            'name': 'Light Healing',
            'x_max': 1.8,
            'y_max': 11,
            'x_min': 1.4,
            'y_min': 8
        },
        {
            'name': 'Light Magic Missile Rune',
            'x_max': 0.81,
            'y_max': 4,
            'x_min': 0.4,
            'y_min': 3
        },
        {
            'name': 'Mass Healing',
            'x_max': 9.6,
            'y_max': 125,
            'x_min': 4.6,
            'y_min': 100
        },
        {
            'name': 'Physical Strike',
            'x_max': 2.203,
            'y_max': 14,
            'x_min': 1.403,
            'y_min': 8
        },
        {
            'name': 'Stalagmite Rune',
            'x_max': 1.59,
            'y_max': 10,
            'x_min': 0.81,
            'y_min': 5
        },
        {
            'name': 'Stone Shower Rune',
            'x_max': 2.6,
            'y_max': 16,
            'x_min': 1,
            'y_min': 6
        },
        {
            'name': 'Strong Ice Strike',
            'x_max': 4.4,
            'y_max': 28,
            'x_min': 2.8,
            'y_min': 16
        },
        {
            'name': 'Strong Ice Wave',
            'x_max': 7.6,
            'y_max': 48,
            'x_min': 4.5,
            'y_min': 20
        },
        {
            'name': 'Sudden Death Rune',
            'x_max': 7.4,
            'y_max': 48,
            'x_min': 4.3,
            'y_min': 32
        },
        {
            'name': 'Terra Wave',
            'x_max': 6.75,
            'y_max': 30,
            'x_min': 3.25,
            'y_min': 5
        },
        {
            'name': 'Ultimate Healing',
            'x_max': 12.9,
            'y_max': 90,
            'x_min': 6.8,
            'y_min': 42
        },
        {
            'name': 'Ultimate Ice Strike',
            'x_max': 7.3,
            'y_max': 55,
            'x_min': 4.5,
            'y_min': 35
        },
        {
            'name': 'Wrath of Nature',
            'x_max': 9,
            'y_max': 40,
            'x_min': 3,
            'y_min': 32
        }
    ]

    # Create the tables
    with app.app_context():
        db.create_all()

    # Populate the spells
    with app.app_context():
        for spell_data in all_spells:
            spell = models.Spell(**spell_data)
            db.session.add(spell)

        db.session.commit()


if __name__ == '__main__':
    populate_spells()

