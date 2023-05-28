from . import db


class Spells(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    vocation = db.Column(db.String(10))
    x_max = db.Column(db.Float)
    y_max = db.Column(db.Integer)
    x_min = db.Column(db.Float)
    y_min = db.Column(db.Integer)

    def __repr__(self):
        return {
            'name': self.name,
            'vocation': self.vocation,
            'xMax': self.x_max,
            'yMax': self.y_max,
            'xMin': self.x_min,
            'yMin': self.y_min
        }
