from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from models import User, Profile, db

bp = Blueprint("users", __name__, url_prefix="/users")


@bp.route("", methods=["GET"])
def get_users():
    users = User.query.all()
    return jsonify([user.to_dict() for user in users])


@bp.route("/<int:user_id>", methods=["GET"])
def get_user(user_id):
    user = User.query.get_or_404(user_id)
    return jsonify(user.to_dict())


@bp.route("/<int:user_id>/profile", methods=["PUT"])
@jwt_required()
def update_profile(user_id):
    current_user = get_jwt_identity()
    if current_user != user_id:
        return jsonify({"msg": "Unauthorized"}), 403

    data = request.get_json()
    profile = Profile.query.filter_by(user_id=user_id).first()
    if not profile:
        profile = Profile(user_id=user_id)
        db.session.add(profile)

    profile.profile_image_url = data.get("profile_image_url", profile.profile_image_url)
    profile.bio = data.get("bio", profile.bio)
    db.session.commit()
    return jsonify(profile.to_dict())
