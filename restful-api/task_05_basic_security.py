from flask import Flask
from flask import jsonify
from flask import request
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required
from flask_jwt_extended import JWTManager

app = Flask(__name__)
auth = HTTPBasicAuth()
app.config["JWT_SECRET_KEY"] = "super-secret"
jwt = JWTManager(app)

users = {
    "user1": {"username": "user1", "password": generate_password_hash("password"), "role": "user"},
    "admin1": {"username": "admin1", "password": generate_password_hash("password"), "role": "admin"}
}

@auth.verify_password
def verify_password(username, password):
    user = users.get(username)
    if user and check_password_hash(user["password"], password):
        return username

@app.route('/basic-protected', methods=['GET'])
@auth.login_required
def basic_protected():
    return f"Basic Auth: Access Granted"

@app.route('/login', methods=['POST'])
def login():
    if not request.is_json:
        return jsonify({"message": "Missing JSON in request"}), 400
    
    username = request.json.get("username")
    password = request.json.get("password")
    user = users.get(username)

    if not user or not check_password_hash(user["password"], password):
        return jsonify({"message": "Bad username or password"}), 401
    access_token = create_access_token(identity=username)
    return jsonify(access_token = access_token), 200

@app.route('/jwt-protected', methods=['GET'])
@jwt_required()
def jwtprotected():
    current_user = get_jwt_identity()
    return jsonify({"JWT Auth": "Access Granted"}), 200

@app.route('/admin-only', methods=['GET'])
@jwt_required()
def adminonly():
    current_user = get_jwt_identity()
    user = users.get(current_user)
    if user and user["role"] == 'admin':
        return jsonify({"Admin Access": "Granted"})
    else:
        return jsonify({"Error": "Admin only"})


if __name__ == '__main__':
    app.run(debug=True)
