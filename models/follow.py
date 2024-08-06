from app import db
from datetime import datetime


class Follow(db.Model):
    follower_id = db.Column(db.Integer, db.ForeignKey("user.id"), primary_key=True)
    followed_id = db.Column(db.Integer, db.ForeignKey("user.id"), primary_key=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
