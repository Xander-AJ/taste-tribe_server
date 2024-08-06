import os
from flask.json import JSONEncoder as FlaskJSONEncoder

from datetime import timedelta
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


class Config:
    SECRET_KEY = os.getenv("SECRET_KEY") or "you-will-never-guess"
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY") or "jwt-secret-string"
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(hours=1)
    JWT_REFRESH_TOKEN_EXPIRES = timedelta(days=30)
    SPOONACULAR_API_KEY = os.getenv("SPOONACULAR_API_KEY")
