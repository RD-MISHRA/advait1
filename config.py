import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'advaitfoundation')
    JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY', 'advaitfoundationachryaprashant')
    MONGO_URI = os.environ.get('MONGO_URI', 'mongodb+srv://rdmishrax:rdmishrax@acharya.ugyxnws.mongodb.net/?retryWrites=true&w=majority&appName=acharya')