from flask import request
from flask_restx import Resource, Namespace

from decorators import auth_required, admin_required
from models import User, UserSchema
from setup_db import db

user_ns = Namespace('users')


@user_ns.route('/')
class UsersView(Resource):
    @auth_required
    def get(self):
        rs = db.session.query(User).all()
        res = UserSchema(many=True).dump(rs)
        return res, 200

    def post(self):
        req_json = request.json
        ent = User(**req_json)

        db.session.add(ent)
        db.session.commit()
        return "", 201, {"location": f"/users/{ent.id}"}


@user_ns.route('/<int:rid>')
class UserView(Resource):
    @auth_required
    def get(self, rid):
        r = db.session.query(User).get(rid)
        sm_d = UserSchema().dump(r)
        return sm_d, 200

    @admin_required
    def put(self, bid):
        user = db.session.query(User).get(bid)
        req_json = request.json
        user.username = req_json.get("username")
        user.password = req_json.get("password")
        user.role = req_json.get("role")
        db.session.add(user)
        db.session.commit()
        return "", 204

    @admin_required
    def delete(self, bid):
        movie = db.session.query(User).get(bid)
        db.session.delete(movie)
        db.session.commit()
        return "", 204
