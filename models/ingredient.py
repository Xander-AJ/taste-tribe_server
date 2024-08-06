from app import db


class Ingredient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    recipe_id = db.Column(db.Integer, db.ForeignKey("recipe.id"), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    quantity = db.Column(db.String(50))
