from flask_restful import Resource


class User (Resource):
    @staticmethod
    def get(name):
        return {
                'message': f'Hello {name}!'
               }, 200

    def post(self, name):
        pass

    def put(self, name):
        pass

    def delete(self, name):
        pass


