from app import db


class Profile(db.Model):
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), primary_key=True)
    profile_image_url = db.Column(db.String(255))
    bio = db.Column(db.Text)
