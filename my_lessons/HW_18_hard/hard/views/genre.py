from flask_restx import Resource, Namespace

from my_lessons.HW_18_hard.hard.dao.model.genre import GenreSchema
from my_lessons.HW_18_hard.hard.implemented import genre_service

#from dao.model.genre import GenreSchema
#from implemented import genre_service

genres_ns = Namespace("genres")


@genres_ns.route("/")
class GenresView(Resource):
    def get(self):
        genres = genre_service.get_all()
        return GenreSchema(many=True).dump(genres), 200


@genres_ns.route("/<int:bid>")
class GenreView(Resource):
    def get(self, bid):
        genre = genre_service.get_one(bid)
        return GenreSchema().dump(genre), 200

