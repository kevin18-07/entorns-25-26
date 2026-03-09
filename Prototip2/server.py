# server.py - WebService Flask
from flask import Flask, request, jsonify
from dataclasses import dataclass, asdict
from DaoServer import UserDAO, ChildDAO

@dataclass
class ApiResponse:
    msg: str
    coderesponse: str
    data: list

app = Flask(__name__)

user_dao = UserDAO()
child_dao = ChildDAO()

@app.route('/getusers', methods=['GET'])
def get_users():
    response = ApiResponse(
        msg="All Users",
        coderesponse="1",
        data=[asdict(u) for u in user_dao.get_all_users()]
    )
    return jsonify(asdict(response)), 200

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    identifier = data.get('username')
    password = data.get('password')
    user = user_dao.login(identifier, password)
    if user:
        response = ApiResponse(
            msg="Authenticated",
            coderesponse="1",
            data=[asdict(user)]
        )
    else:
        response = ApiResponse(
            msg="Not authenticated",
            coderesponse="0",
            data=[]
        )
    return jsonify(asdict(response)), 200

@app.route('/child', methods=['POST'])
def get_children():
    token = request.headers.get("Authorization")
    if not token:
        return jsonify({"msg": "Token missing", "coderesponse": "0"}), 401
    # Para prototipo, asumimos user_id=1 si token existe
    user_id = 1
    # Buscar usuario ficticio
    from dadesServer import users
    user = next((u for u in users if u.id == user_id), None)
    children_list = child_dao.get_children(user)
    response = ApiResponse(
        msg="Children fetched",
        coderesponse="1",
        data=[c.__dict__ for c in children_list]
    )
    return jsonify(asdict(response)), 200

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)