from flask_restx import Resource, Namespace
from easy.setup_db import db
from easy.models import Director, DirectorSchema

director_ns = Namespace('directors')
director_schema = DirectorSchema()
directors_schema = DirectorSchema(many=True)


@director_ns.route("/")
class DirectorView(Resource):
    def get(self):
        directors = db.session.query(Director).all()
        return directors_schema.dump(directors), 200


@director_ns.route("/<int:uid>")
class DirectorView(Resource):
    def get(self, uid: int):
        try:
            director = db.session.query(Director).filter(Director.id == uid).one()
            return director_schema.dump(director), 200
        except Exception:
            return "wrong id", 404