from flask import Blueprint, request, jsonify
from services import UserService

user_bp = Blueprint("users", __name__)

service = UserService()

@user_bp.route("/users", methods=["POST"])
def create_user():

    data = request.get_json()

    user = service.create_user(
        data["name"]
    )

    return jsonify({
        "id": user.id,
        "name": user.name
    })

@user_bp.route("/users")
def list_users():

    users = service.list_users()

    return jsonify([
        {
            "id": u.id,
            "name": u.name
        }
        for u in users
    ])
