from flask import Flask, request, jsonify
from dao.user_dao import UserDAO

app = Flask(__name__)
dao = UserDAO()


# =========================
# LOGIN (credencials o token)
# =========================
@app.route("/login", methods=["POST"])
def login():

    token = request.headers.get("Authorization")

    # =========================
    # 🔐 LOGIN PER TOKEN
    # =========================
    if token:
        user = dao.get_user_by_token(token)

        if user:
            return jsonify({
                "coderesponse": "1",
                "id": user["id"],
                "username": user["username"],
                "email": user["email"],
                "token": user["token"],
                "idrole": str(user["idrole"]),
                "msg": "Usuari Ok"
            }), 200

        return jsonify({
            "coderesponse": "0",
            "msg": "No validat"
        }), 400

    # =========================
    # 🔐 LOGIN PER USER/PASS
    # =========================
    data = request.get_json()

    username = data.get("username")
    password = data.get("password")

    user = dao.get_user_by_username_or_email(username)

    if user and dao.validate_password(user, password):

        return jsonify({
            "coderesponse": "1",
            "data": {
                "email": user["email"],
                "id": user["id"],
                "idrole": user["idrole"],
                "password": user["password"],
                "token": user["token"],
                "username": user["username"]
            },
            "msg": "Authenticated"
        }), 200

    return jsonify({
        "coderesponse": "0",
        "msg": "No validat"
    }), 400


if __name__ == "__main__":
    app.run(debug=True)