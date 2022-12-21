from setup_db  import db
from models import MovieSchema, Movie
from flask_restx import Resource, Namespace
from flask import request

movie_ns = Namespace('movies')
movie_schema = MovieSchema()
movies_schema = MovieSchema(many=True)


@movie_ns.route("/")
class MovieView(Resource):
    def get(self):
        movies = db.session.query(Movie).all()
        director_id = request.args.get("director_id")
        if director_id:
            movies = db.session.query(Movie).filter(Movie.director_id == director_id)
        genre_id = request.args.get("genre_id")
        if genre_id:
            movies = db.session.query(Movie).filter(Movie.genre_id == genre_id)
        return movies_schema.dump(movies), 200

    def post(self):
        req_json = request.json
        new_movie = Movie(**req_json)
        with db.session.begin():
            db.session.add(new_movie)
        return "User was added", 201


@movie_ns.route("/<int:uid>")
class MovieView(Resource):
    def get(self, uid: int):
        try:
            movie = db.session.query(Movie).filter(Movie.id == uid).one()
            return movie_schema.dump(movie), 200
        except Exception:
            return "wrong id", 404

    def put(self, uid: int):
        movie = Movie.query.get(uid)
        req_json = request.json
        movie.title = req_json.get("title")
        movie.description = req_json.get("description")
        movie.trailer = req_json.get("trailer")
        movie.year = req_json.get("year")
        movie.rating = req_json.get("rating")
        movie.genre_id = req_json.get("genre_id")
        movie.director_id = req_json.get("director_id")
        db.session.add(movie)
        db.session.commit()
        return "User is updated", 204

    def delete(self, uid: int):
        movie = Movie.query.get(uid)
        db.session.delete(movie)
        db.session.commit()
        return "User is deleted", 204

