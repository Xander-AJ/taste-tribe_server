from flask import Blueprint, request, jsonify
from flask_jwt_extended import (
    create_access_token,
    create_refresh_token,
    jwt_required,
    get_jwt_identity,
)
from models import User, db
from werkzeug.security import generate_password_hash

bp = Blueprint("auth", __name__, url_prefix="/auth")


@bp.route("/register", methods=["POST"])
def register():
    data = request.get_json()

    if User.query.filter_by(username=data["username"]).first():
        return jsonify({"msg": "Username already exists"}), 400

    if User.query.filter_by(email=data["email"]).first():
        return jsonify({"msg": "Email already exists"}), 400

    new_user = User(
        username=data["username"],
        email=data["email"],
        password_hash=generate_password_hash(data["password"]),
    )

    db.session.add(new_user)
    db.session.commit()

    access_token = create_access_token(identity=new_user.id)
    refresh_token = create_refresh_token(identity=new_user.id)

    return jsonify(access_token=access_token, refresh_token=refresh_token), 201


@bp.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    user = User.query.filter_by(username=data["username"]).first()

    if user and user.check_password(data["password"]):
        access_token = create_access_token(identity=user.id)
        refresh_token = create_refresh_token(identity=user.id)

        return jsonify(access_token=access_token, refresh_token=refresh_token), 200

    return jsonify({"msg": "Invalid username or password"}), 401


@bp.route("/refresh", methods=["POST"])
@jwt_required(refresh=True)
def refresh():
    current_user = get_jwt_identity()
    new_access_token = create_access_token(identity=current_user)
    return jsonify(access_token=new_access_token), 200


@bp.route("/protected", methods=["GET"])
@jwt_required()
def protected():
    current_user = get_jwt_identity()
    return jsonify(logged_in_as=current_user), 200
