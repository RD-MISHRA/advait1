import os
from dotenv import load_dotenv
from flask import Flask
from flask_jwt_extended import JWTManager
from pymongo import MongoClient
from config import Config

load_dotenv()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    mongo_client = MongoClient(app.config['MONGO_URI'])
    database = mongo_client.get_database("acharya")
    collection = database.get_collection("prashant")

    jwt = JWTManager(app)


    from routes.auth import auth_bp
    app.register_blueprint(auth_bp, url_prefix='/auth')

 
    app.config['COLLECTION'] = collection

    @app.route('/')
    def home():
        return "Home Page"

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)