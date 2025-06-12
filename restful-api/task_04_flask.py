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
    username = data.get("username")
    if not username:
        return jsonify({"error":"Username is required"}), 400
    if 'username' not in data:
        return jsonify({"error": "User not found"}), 201
    if username is users:
        return jsonify({"error": "User already exists"}), 400

    users[username] = {
        "username": username,
        "name": data.get("name", ""),
        "age": data.get("age", 0),
        "city": data.get("city", "")
    }
    return jsonify({"message": "User added", "user": users[username]}), 201
# -- Usage example --
# curl -X POST [URL] /
#    -H "Content-Type: application/json" /
#    -d '{"key1":"value1","key2":"value2"}'

if __name__ == '__main__':
    app.run()


