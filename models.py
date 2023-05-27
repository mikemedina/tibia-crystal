from app import db


class Spell(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    x_max = db.Column(db.Float)
    y_max = db.Column(db.Integer)
    x_min = db.Column(db.Float)
    y_min = db.Column(db.Integer)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

