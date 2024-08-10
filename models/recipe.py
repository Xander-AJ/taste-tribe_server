from app import db
from datetime import datetime
from sqlalchemy.dialects.sqlite import JSON

class Recipe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    country = db.Column(db.String(50))
    number_of_people_served = db.Column(db.Integer)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(
        db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow
    )

    ingredients = db.Column(JSON, nullable=False)  # Store ingredients as a JSON object

    comments = db.relationship(
        "Comment", backref="recipe", lazy="dynamic", cascade="all, delete-orphan"
    )
    ratings = db.relationship(
        "Rating", backref="recipe", lazy="dynamic", cascade="all, delete-orphan"
    )
    bookmarks = db.relationship(
        "Bookmark", backref="recipe", lazy="dynamic", cascade="all, delete-orphan"
    )
