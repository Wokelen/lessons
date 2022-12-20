#from setup_db import db
from marshmallow import Schema, fields

from my_lessons.HW_18_hard.hard.setup_db import db


class Genre(db.Model):
    __tablename__ = 'genre'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)

class GenreSchema(Schema):
    id = fields.Int()
    name = fields.Str()