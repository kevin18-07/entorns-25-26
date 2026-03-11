# servidor/server.py
from flask import Flask, request, jsonify
from DaoServer import UserDAO, ChildDAO
from dadesServer import users

app = Flask(__name__)

user_dao = UserDAO()
child_dao = ChildDAO()

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    identifier = data.get('username')
    password = data.get('password')
    user = user_dao.login(identifier, password)
    if user:
        return jsonify({
            "coderesponse": "1",
            "data": user.__dict__,
            "msg": "Authenticated"
        }), 200
    else:
        return jsonify({
            "coderesponse": "0",
            "msg": "No validat"
        }), 400

@app.route('/login/token', methods=['POST'])
def login_token():
    token = request.headers.get("Authorization")
    user = next((u for u in users if u.token == token), None)
    if user:
        return jsonify({
            "id": user.id,
            "username": user.username,
            "email": user.email,
            "token": user.token,
            "idrole": user.idrole,
            "msg": "Usuari Ok",
            "coderesponse": "1"
        }), 200
    else:
        return jsonify({
            "coderesponse": "0",
            "msg": "No validat"
        }), 400

@app.route('/child', methods=['POST'])
def get_children():
    token = request.headers.get("Authorization")
    if not token:
        return jsonify({"msg": "Token missing", "coderesponse": "0"}), 401

    user = next((u for u in users if u.token == token), None)
    if not user:
        return jsonify({"msg": "No validat", "coderesponse": "0"}), 400

    children_list = child_dao.get_children(user)
    children_data = [c.__dict__ for c in children_list]

    msg_code = "1" if len(children_data) == 1 else str(len(children_data))
    return jsonify({
        "coderesponse": "1",
        "msg": msg_code,
        "data": children_data
    }), 200

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)