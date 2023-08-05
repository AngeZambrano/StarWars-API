"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
from flask import Flask, request, jsonify, url_for, Blueprint
from api.models import db, User, Characters, Planets, Favorites
from api.utils import generate_sitemap, APIException

api = Blueprint('api', __name__)


@api.route('/hello', methods=['POST', 'GET'])
def handle_hello():

    response_body = {
        "message": "Hello! I'm a message that came from the backend, check the network tab on the google inspector and you will see the GET request"
    }

    return jsonify(response_body), 200


# ENDPOINTS GET ALL USERS

@api.route('/users', methods=['GET'])
def get_all_users():

    users_query = User.query.all()
    results = list(map(lambda item: item.serialize(), users_query))
    # print(users_query)
    # print(results)

    response_body = {
        "message": "ok",
        "results": results

    }

    return jsonify(response_body), 200

# ENDPOINTS ONE USER

@api.route('/users/<int:user_id>', methods=['GET'])
def get_one_users(user_id):

    user_query = User.query.filter_by(id=user_id).first()

    response_body = {
        "message": "ok",
        "result": user_query.serialize()

    }

    return jsonify(response_body), 200

# ENDPOINT CREATE ONE USER

@api.route('/users', methods=['POST'])
def create_one_users():

    request_body = request.get_json(force=True)
    print(request_body)
    user = User(name=request_body["name"], email=request_body["email"], password=request_body["password"])
    db.session.add(user)
    db.session.commit()

    # user_query = User.query.filter_by(id=user_id).first()

    response_body = {
        "message": "User created",
        # "result": user_query.serialize()

    }

    return jsonify(response_body), 200
