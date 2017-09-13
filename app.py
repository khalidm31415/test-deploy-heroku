from flask import Flask, request
from flask_restful import Resource, Api, reqparse

app = Flask(__name__)
api = Api(app)

class Test(Resource):
    def get(self):
        return "<h1>Hello world!</h1>"

api.add_resource(Test, '/')

if __name__ == '__main__':
        app.run(port=8000, debug=True)
