from flask import Blueprint, jsonify, request

main_bp = Blueprint('main', __name__)

# Temporary in-memory database
data = {
    "users": []
}

@main_bp.route('/', methods=['GET'])
def home():
    return jsonify({"message": "Welcome to the Flask App!"})

@main_bp.route('/healthcheck', methods=['GET'])
def healthcheck():
    return jsonify({"status": "healthy"})

@main_bp.route('/users', methods=['GET'])
def get_users():
    return jsonify(data["users"])

@main_bp.route('/users', methods=['POST'])
def create_user():
    user_data = request.json
    user_id = len(data["users"]) + 1
    new_user = {"id": user_id, "name": user_data["name"]}
    data["users"].append(new_user)
    return jsonify(new_user), 201

@main_bp.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = next((u for u in data["users"] if u["id"] == user_id), None)
    if not user:
        return jsonify({"error": "User not found"}), 404
    data["users"].remove(user)
    return jsonify({"message": "User deleted"}), 200