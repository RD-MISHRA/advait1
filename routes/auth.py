

# from flask import Blueprint, request, jsonify, current_app
# from flask_jwt_extended import (
#     JWTManager, jwt_required, get_jwt_identity, create_access_token, create_refresh_token, get_jwt
# )
# from werkzeug.security import generate_password_hash, check_password_hash

# auth_bp = Blueprint('auth', __name__)


# blacklist = set()

# def create_user(email, password, collection):
#     hashed_password = generate_password_hash(password)
#     user = {'email': email, 'password': hashed_password}
#     collection.insert_one(user)

# def find_user_by_email(email, collection):
#     return collection.find_one({'email': email})

# def verify_password(stored_password, provided_password):
#     return check_password_hash(stored_password, provided_password)
# # i have written post api to signup
# @auth_bp.route('/signup', methods=['POST'])
# def signup():
#     data = request.get_json()
#     email = data.get('email')
#     password = data.get('password')
#     collection = current_app.config['COLLECTION']
#     if find_user_by_email(email, collection):
#         return jsonify({"msg": "User already exists"}), 400
#     create_user(email, password, collection)
#     return jsonify({"msg": "User created successfully"}), 201
# #here user will use their credentials and will get a accesstoken
# @auth_bp.route('/signin', methods=['POST'])
# def signin():
#     data = request.get_json()
#     email = data.get('email')
#     password = data.get('password')
#     collection = current_app.config['COLLECTION']
#     user = find_user_by_email(email, collection)
#     if user and verify_password(user['password'], password):
#         access_token = create_access_token(identity=email)
       
#         return jsonify(access_token=access_token), 200
#     return jsonify({"msg": "Invalid credentials"}), 401



# #user can user their access token here and they will get a new token 
# @auth_bp.route('/refresh', methods=['POST'])
# @jwt_required()
# def refresh():
#     try:
#         identity = get_jwt_identity()
#         access_token = create_access_token(identity=identity)
#         return jsonify(access_token=access_token), 200
#     except Exception as e:
#         return jsonify({"msg": "Token refresh failed", "error": str(e)}), 401




# #this api will invalidate the existing token and user can not use the token again 
# @auth_bp.route('/revoke', methods=['POST'])
# @jwt_required()
# def revoke():
#     jti = get_jwt()["jti"]
#     blacklist.add(jti)
#     return jsonify({"msg": "Token revoked"}), 200




# #if the token is valid then user will able to get resource else they will get error
# @auth_bp.route('/protected', methods=['GET'])
# @jwt_required()
# def protected():
#     return jsonify({"message": "You accessed the protected resource!"}), 200

# @auth_bp.errorhandler(401)
# def custom_401(error):
#     return jsonify({"msg": "Missing or invalid token"}), 401

# @auth_bp.errorhandler(422)
# def custom_422(error):
#     return jsonify({"msg": "Unprocessable Entity"}), 422

# def is_token_revoked(jwt_payload):
#     jti = jwt_payload["jti"]
#     return jti in blacklist


from flask import Blueprint, request, jsonify, current_app
from flask_jwt_extended import (
    JWTManager, jwt_required, get_jwt_identity, create_access_token, get_jwt
)
from werkzeug.security import generate_password_hash, check_password_hash

auth_bp = Blueprint('auth', __name__)
blacklist = set()

# Functions for user management and authentication

def create_user(email, password, collection):
    hashed_password = generate_password_hash(password)
    user = {'email': email, 'password': hashed_password}
    collection.insert_one(user)

def find_user_by_email(email, collection):
    return collection.find_one({'email': email})

def verify_password(stored_password, provided_password):
    return check_password_hash(stored_password, provided_password)

# Routes for authentication

@auth_bp.route('/signup', methods=['POST'])
def signup():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')
    collection = current_app.config['COLLECTION']
    if find_user_by_email(email, collection):
        return jsonify({"msg": "User already exists"}), 400
    create_user(email, password, collection)
    return jsonify({"msg": "User created successfully"}), 201

@auth_bp.route('/signin', methods=['POST'])
def signin():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')
    collection = current_app.config['COLLECTION']
    user = find_user_by_email(email, collection)
    if user and verify_password(user['password'], password):
        access_token = create_access_token(identity=email)
        return jsonify(access_token=access_token), 200
    return jsonify({"msg": "Invalid credentials"}), 401

@auth_bp.route('/refresh', methods=['POST'])
@jwt_required()
def refresh():
    try:
        identity = get_jwt_identity()
        access_token = create_access_token(identity=identity)
        return jsonify(access_token=access_token), 200
    except Exception as e:
        return jsonify({"msg": "Token refresh failed", "error": str(e)}), 401

@auth_bp.route('/revoke', methods=['POST'])
@jwt_required()
def revoke():
    jti = get_jwt()["jti"]
    blacklist.add(jti)
    return jsonify({"msg": "Token revoked"}), 200

@auth_bp.route('/protected', methods=['GET'])
@jwt_required()
def protected():
    jti = get_jwt()["jti"]
    if jti in blacklist:
        return jsonify({"msg": "Token has been revoked"}), 401
    else:
        return jsonify({"message": "You accessed the protected resource!"}), 200

@auth_bp.errorhandler(401)
def custom_401(error):
    return jsonify({"msg": "Missing or invalid token"}), 401

@auth_bp.errorhandler(422)
def custom_422(error):
    return jsonify({"msg": "Unprocessable Entity"}), 422