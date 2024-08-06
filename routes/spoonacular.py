from flask import Blueprint, request, jsonify
import requests
import os

bp = Blueprint("spoonacular", __name__, url_prefix="/spoonacular")


@bp.route("/recipes/findByIngredients", methods=["GET"])
def find_recipes_by_ingredients():
    ingredients = request.args.get("ingredients")
    api_key = os.environ.get("SPOONACULAR_API_KEY")
    response = requests.get(
        f"https://api.spoonacular.com/recipes/findByIngredients?ingredients={ingredients}&apiKey={api_key}"
    )
    return jsonify(response.json())
