from flask import Blueprint, request, jsonify
import requests
import os

bp = Blueprint("spoonacular", __name__, url_prefix="/spoonacular")


# Helper function to make Spoonacular API requests
def spoonacular_api_request(endpoint, params=None):
    api_key = os.environ.get("SPOONACULAR_API_KEY")
    base_url = f"https://api.spoonacular.com/{endpoint}"
    headers = {"Content-Type": "application/json"}
    params = params or {}
    params["apiKey"] = api_key
    response = requests.get(base_url, headers=headers, params=params)
    return response.json()


# Route to find recipes by ingredients
@bp.route("/recipes/findByIngredients", methods=["GET"])
def find_recipes_by_ingredients():
    ingredients = request.args.get("ingredients")
    if not ingredients:
        return jsonify({"error": "Ingredients parameter is required"}), 400
    data = spoonacular_api_request(
        "recipes/findByIngredients", {"ingredients": ingredients}
    )
    return jsonify(data)


# Route to get a recipe by ID
@bp.route("/recipes/<int:recipe_id>", methods=["GET"])
def get_recipe_by_id(recipe_id):
    data = spoonacular_api_request(f"recipes/{recipe_id}/information")
    return jsonify(data)


# Route to get a list of recipes by instructions
@bp.route("/recipes/searchByInstructions", methods=["GET"])
def find_recipes_by_instructions():
    instructions = request.args.get("instructions")
    if not instructions:
        return jsonify({"error": "Instructions parameter is required"}), 400
    params = {"instructionsRequired": True, "query": instructions}
    data = spoonacular_api_request("recipes/complexSearch", params)
    return jsonify(data)


# Route to perform a complex search for recipes
@bp.route("/recipes/complexSearch", methods=["GET"])
def complex_search_recipes():
    params = request.args.to_dict()
    data = spoonacular_api_request("recipes/complexSearch", params)
    return jsonify(data)


# Route to get detailed information about a recipe
@bp.route("/recipes/<int:recipe_id>/information", methods=["GET"])
def get_recipe_information(recipe_id):
    data = spoonacular_api_request(f"recipes/{recipe_id}/information")
    return jsonify(data)


# Additional routes can be added here as needed
