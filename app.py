from flask import Flask, request
from flask_restful import Resource, Api, reqparse

app = Flask(__name__)
api = Api(app)

class Test(Resource):
    def get(self):
        return {"message":"Hello world!"}

api.add_resource(Test, '/')

if __name__ == '__main__':
        app.run(port=8000, debug=True)
