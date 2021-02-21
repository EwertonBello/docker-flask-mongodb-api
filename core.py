import os

from flask import Flask, jsonify
from flask_restful import reqparse, abort, Api, Resource

from pymongo import MongoClient, TEXT
from pymongo.errors import DuplicateKeyError

from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)
api = Api(app)

db_uri = os.getenv("MONGODB_URI")

client = MongoClient(db_uri)
db = client.get_database()
users = db['users']
users.create_index([('username', TEXT)], unique=True)

def abort_if_user_doesnt_exist(username):
    user = users.find_one({"username": username})
    if not user:
        abort(404, message="User {} doesn't exist".format(username))
    return user

parser = reqparse.RequestParser()
parser.add_argument('name')
parser.add_argument('username')


class User(Resource):
    def get(self, username):
        user = abort_if_user_doesnt_exist(username)
        response_user = {
            'username': user['username'],
            'name': user['name'],
        }
        return jsonify(response_user)

    def delete(self, username):
        abort_if_user_doesnt_exist(username)
        users.delete_one({"username": username})

        return "User deleted successfully!", 204

    def put(self, username):
        abort_if_user_doesnt_exist(username)
        args = parser.parse_args()
        users.update_one(
            {'username': username},
            {'$set': {'name': args['name']}}
        )

        return "User updated successfully!", 201


class UserList(Resource):
    def get(self):
        response_users = list()
        for user in users.find():
            response_users.append({
                'username': user['username'],
                'name': user['name'],
            })

        return jsonify(response_users)

    def post(self):
        args = parser.parse_args()
        try:            
            user = {
                'username': args['username'],
                'name': args['name'],
            }
            users.insert_one(user)
            return "User created successfully!", 201
        except DuplicateKeyError as e:
            return "User already exists!", 400

        return "Unsuccessful request!", 500

api.add_resource(UserList, '/users/')
api.add_resource(User, '/users/<username>')


if __name__ == '__main__':
    app.run(debug=True)
