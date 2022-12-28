from flask import request
from flask_restx import Resource, Namespace

from decorators import admin_required
from models import Auth

auth_ns = Namespace('auth')


@auth_ns.route('/')
class AuthView(Resource):
    @admin_required
    def post(self):
        req_json = request.json
        username = req_json.get("username")
        password = req_json.get("password")
        if None in [username, password]:
            return "", 401
        tokens = Auth.generate_tokens(username, password)
        return tokens, 201

    @admin_required
    def put(self):
        req_json = request.json
        token = req_json.get("refresh_token")
        tokens = Auth.approve_refresh_token(token)
        return tokens, 201
