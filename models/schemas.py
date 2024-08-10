from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from models import User, Profile, Recipe, db


class UserSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = User
        sqla_session = db.session
        load_instance = True


class ProfileSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Profile
        sqla_session = db.session
        load_instance = True


class RecipeSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Recipe
        sqla_session = db.session
        load_instance = True
