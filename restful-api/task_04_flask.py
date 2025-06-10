from flask import Flask, jsonify, request
import json

app = Flask(__name__)

users = {
    #"jane": {"name": "Jane", "age": 28, "city": "Los Angeles"}
    }

@app.route('/')
def home():
    return "Welcome to the Flask API!"

@app.route('/data', methods=['GET'])
def list_usernames():
    usernames = list(users.keys())
    return jsonify(usernames), 200

@app.route('/status', methods=['GET'])
def get_status():
    return "OK", 200

@app.route('/users/<username>')
def get_user(username):
    user = users.get(username)
    if user is None:
        return jsonify({"error": "User not found"}), 404
    return jsonify(user), 200

@app.route('/add_user', methods=['POST'])
def add_user():
    data = request.get_json()
    if not data:
        return jsonify({"error":"Username is required"}), 400
    if 'username' not in data:
        return jsonify({"error": "User not found"}), 201

    username = data['username']
    if username is users:
        return jsonify({"error": "User already exists"}), 409

    users[username] = {
        "username": username,
        "name": data.get("name", ""),
        "age": data.get("age", 0),
        "city": data.get("city", "")
    }
    return jsonify({"msg": "User added", "user": users[username]}), 201

if __name__ == '__main__':
    app.run()


