from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from models import Recipe, db

bp = Blueprint("recipes", __name__, url_prefix="/recipes")


@bp.route("", methods=["GET"])
def get_recipes():
    recipes = Recipe.query.all()
    return jsonify([recipe.to_dict() for recipe in recipes])


@bp.route("", methods=["POST"])
@jwt_required()
def create_recipe():
    data = request.get_json()
    current_user = get_jwt_identity()
    new_recipe = Recipe(
        user_id=current_user,
        title=data["title"],
        description=data.get("description"),
        country=data.get("country"),
        number_of_people_served=data.get("number_of_people_served"),
    )
    db.session.add(new_recipe)
    db.session.commit()
    return jsonify(new_recipe.to_dict()), 201


@bp.route("/<int:recipe_id>", methods=["GET"])
def get_recipe(recipe_id):
    recipe = Recipe.query.get_or_404(recipe_id)
    return jsonify(recipe.to_dict())


@bp.route("/<int:recipe_id>", methods=["PUT"])
@jwt_required()
def update_recipe(recipe_id):
    data = request.get_json()
    current_user = get_jwt_identity()
    recipe = Recipe.query.get_or_404(recipe_id)

    if recipe.user_id != current_user:
        return jsonify({"msg": "Unauthorized"}), 403

    recipe.title = data.get("title", recipe.title)
    recipe.description = data.get("description", recipe.description)
    recipe.country = data.get("country", recipe.country)
    recipe.number_of_people_served = data.get(
        "number_of_people_served", recipe.number_of_people_served
    )
    db.session.commit()
    return jsonify(recipe.to_dict())


@bp.route("/<int:recipe_id>", methods=["DELETE"])
@jwt_required()
def delete_recipe(recipe_id):
    current_user = get_jwt_identity()
    recipe = Recipe.query.get_or_404(recipe_id)

    if recipe.user_id != current_user:
        return jsonify({"msg": "Unauthorized"}), 403

    db.session.delete(recipe)
    db.session.commit()
    return jsonify({"msg": "Recipe deleted"}), 200
