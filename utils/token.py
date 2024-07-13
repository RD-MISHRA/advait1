from flask_jwt_extended import create_access_token, create_refresh_token, decode_token
from datetime import timedelta

def generate_tokens(identity):
    access_token = create_access_token(identity=identity, expires_delta=timedelta(minutes=15))
    refresh_token = create_refresh_token(identity=identity, expires_delta=timedelta(days=30))
    return access_token

def decode_jwt(token):
    return decode_token(token)