from flask import Flask, jsonify

app = Flask(__name__)

users = [
    {"id": 1, "name": "John Doe", "email": "John.Doe@mail.com"},
    {"id": 2, "name": "Jane Smith", "email": "Jane.Smith@mail.com"},
    {"id": 3, "name": "Webster Joe", "email": "Webster.Joe@mail.com"},
]

# base route
@app.route("/")
def greet():
    return ("Flask Crash Course")

# get all users data
@app.route("/users", methods=["GET"])
def get_all_users():
    return jsonify({
        "users": users,
        "Success": True
    })

# get single user data using the id param
@app.route("/users/<int:user_id>", methods=["GET"])
def get_user_by_id(user_id):
    return jsonify({
        "user": users[user_id],
        "Success": True
    })

@app.route("/users", methods=["POST"])
def create_user():
    user = {"id": 4, "name": "Shuma Gorath", "email": "Shuma@mail.com"}
    users.append(user)
    return jsonify({
        "createdUser": user,
        "success": True
    })


if __name__ == "__main__":
    app.run(debug = True)