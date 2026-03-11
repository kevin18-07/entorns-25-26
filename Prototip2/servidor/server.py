from flask import Flask, request, jsonify
from DaoServer import UserDAO, ChildDAO, TapDAO
from dataclasses import dataclass, asdict

@dataclass
class ApiResponse():
    msg: str
    coderesponse: str
    data: list

userDao = UserDAO()
childDao = ChildDAO()
tapDao = TapDAO()

app = Flask(__name__)

@app.route('/getusers', methods=['GET'])
def getusers():
    response = ApiResponse(
        msg="All Users",
        coderesponse="1",
        data=userDao.getAllUsers()
    )
    return jsonify(asdict(response)), 200


@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()

    identifier = data.get('username')
    password = data.get('password')

    user = userDao.login(identifier, password)

    response = ApiResponse(
        msg="login",
        coderesponse="-1",
        data=user
    )

    if user:
        response = ApiResponse(
            msg="Authenticated",
            coderesponse="1",
            data=user.__dict__
        )
    else:
        response = ApiResponse(
            msg="Not authenticated",
            coderesponse="0",
            data=""
        )

    return jsonify(asdict(response)), 200


@app.route('/child', methods=['POST'])
def get_children():
    data = request.get_json()
    username = data.get("username")

    user = userDao.get_user_by_username(username)

    if not user:
        response = ApiResponse(
            msg="User not found",
            coderesponse="0",
            data=[]
        )
        return jsonify(asdict(response)), 200

    children = childDao.get_children(user)

    response = ApiResponse(
        msg="Children list",
        coderesponse="1",
        data=[c.__dict__ for c in children]
    )

    return jsonify(asdict(response)), 200



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)