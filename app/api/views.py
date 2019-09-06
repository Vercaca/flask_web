from flask import request
from flask import current_app

from flask_restful import Resource

from .user import User
from . import api


@api.route('/messages', methods=['POST'])
class Messages(Resource):
    def post(self):
        return self.message()

    @staticmethod
    def message():
        body = request.json
        current_app.logger.debug(body)


        return 'ok'


@api.route('/about', methods=['GET'])
class About(Resource):
    @staticmethod
    def get():
        return {"message": "HERE is about"}, 200


api.add_resource(About, "/about")
api.add_resource(User, "/user/<name>")
api.add_resource(Messages, '/messages')
