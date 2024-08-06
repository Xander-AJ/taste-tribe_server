from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from config import Config

db = SQLAlchemy()
migrate = Migrate()
jwt = JWTManager()


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)
    CORS(app)

    from routes import register_blueprints

    register_blueprints(app)

    @app.route("/")
    def home():
        return "Welcome to the Flask API! The Backend Works!", 200

    @app.route("/health")
    def health_check():
        return "OK", 200

    return app
