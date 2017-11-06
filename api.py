from flask import Flask
from flask_restful import Resource, Api, reqparse

from lib.validator import calculate

app = Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser()
parser.add_argument('name')

class Index(Resource):
    def get(self):
        args = parser.parse_args()
        return {'hello': args['name']}

api.add_resource(Index, '/')

if __name__ == '__main__':
    app.run(debug=True)