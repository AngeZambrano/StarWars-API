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

# ENDPOINT GET ALL CHARACTERS

@api.route('/characters', methods=['GET'])
def get_all_characters():

    characters_query = Characters.query.all()
    results = list(map(lambda item: item.serialize(), characters_query))
    # print(characters_query)
    # print(results)

    response_body = {
        "message": "ok",
        "results": results

    }

    return jsonify(response_body), 200

# ENDPOINT ONE CHARACTER

@api.route('/characters/<int:character_id>', methods=['GET'])
def get_one_character(character_id):

    character_query = Characters.query.filter_by(id=character_id).first()
    # print(character_query)

    response_body = {
        "message": "ok",
        "result": character_query.serialize()

    }

    return jsonify(response_body), 200

# ENDPOINT GET ALL PlANETS

@api.route('/planets', methods=['GET'])
def get_all_planets():

    planets_query = Planets.query.all()
    results = list(map(lambda item: item.serialize(), planets_query))
    # print(planets_query)
    print(results)

    response_body = {
        "message": "ok",
        "results": results

    }

    return jsonify(response_body), 200

# ENDPOINT ONE PLANET

@api.route('/planets/<int:planet_id>', methods=['GET'])
def get_one_planet(planet_id):

    planet_query = Planets.query.filter_by(id=planet_id).first()
    # print(planet_query)

    response_body = {
        "message": "ok",
        "result": planet_query.serialize()

    }

    return jsonify(response_body), 200

# CREATE ONE FAVORITE PLANET_ID

@api.route('/favorite/planet/<int:planet_id>', methods=['POST'])
def create_one_planet(planet_id):

    request_body = request.get_json(force=True)

    # print(request_body)
    favorite = Favorites(user_id=request_body["user_id"], planets_id=planet_id)
    db.session.add(favorite)
    db.session.commit()

    response_body = {
        "message": "Planet created",
        "result": favorite.serialize()

    }

    return jsonify(response_body), 200

# CREATE ONE FAVORITE CHARACTER_ID

@api.route('/favorite/characters/<int:character_id>', methods=['POST'])
def create_one_character(character_id):

    request_body = request.get_json(force=True)

    # print(request_body)
    new_favorite = Favorites(user_id=request_body["user_id"], characters_id=character_id)
    db.session.add(new_favorite)
    db.session.commit()

    response_body = {
        "message": "Character created",
        "result": new_favorite.serialize()

    }

    return jsonify(response_body), 200

# DELETE ONE FAVORITE PLANET_ID

@api.route('/favorite/planet/<int:planet_id>', methods=['DELETE'])
def delete_one_planet(planet_id):

    request_body = request.get_json(force=True)

    delete_favorite= Favorites.query.filter_by(planets_id=planet_id).filter_by(user_id=request_body["user_id"]).first()
    
    db.session.delete(delete_favorite)
    db.session.commit()

    response_body = {
        "message": "favorite deleted"

    }

    return jsonify(response_body), 200

# DELETE ONE FAVORITE CHARACTER_ID

@api.route('/favorite/characters/<int:character_id>', methods=['DELETE'])
def delete_one_character(character_id):

    request_body = request.get_json(force=True)

    delete_favorite_character= Favorites.query.filter_by(characters_id=character_id).filter_by(user_id=request_body["user_id"]).first()
    
    db.session.delete(delete_favorite_character)
    db.session.commit()

    response_body = {
        "message": "favorite deleted"

    }

    return jsonify(response_body), 200





