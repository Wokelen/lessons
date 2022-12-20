from flask_restx import Resource, Namespace
from easy.setup_db import db
from easy.models import Genre, GenreSchema

genre_ns = Namespace('genres')
genre_schema = GenreSchema()
genres_schema = GenreSchema(many=True)


@genre_ns.route("/")
class GenreView(Resource):
    def get(self):
        genres = db.session.query(Genre).all()
        return genres_schema.dump(genres), 200


@genre_ns.route("/<int:uid>")
class GenreView(Resource):
    def get(self, uid: int):
        try:
            genre = db.session.query(Genre).filter(Genre.id == uid).one()
            return genre_schema.dump(genre), 200
        except Exception:
            return "wrong id", 404
