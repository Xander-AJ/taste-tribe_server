from .auth import bp as auth_bp
from .recipes import bp as recipes_bp
from .users import bp as users_bp
from .spoonacular import bp as spoonacular_bp


def register_blueprints(app):
    app.register_blueprint(auth_bp)
    app.register_blueprint(recipes_bp)
    app.register_blueprint(users_bp)
    app.register_blueprint(spoonacular_bp)
