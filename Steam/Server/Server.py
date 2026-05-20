from flask import Flask, request, jsonify
from flask_cors import CORS
from dataclasses import dataclass, asdict
from DaoServer import SteamDAO

# ---------------- RESPONSE ----------------

@dataclass
class ApiResponse:
    msg: str
    coderesponse: str
    data: object


# ---------------- INIT ----------------

app = Flask(__name__)
CORS(app)  # 🔥 IMPORTANTE
dao = SteamDAO()


# ---------------- LOGIN ----------------

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()

    user = dao.login(
        data.get('username'),
        data.get('password')
    )

    if user:
        return jsonify(asdict(ApiResponse(
            msg="Authenticated",
            coderesponse="1",
            data=user
        ))), 200

    return jsonify(asdict(ApiResponse(
        msg="Not authenticated",
        coderesponse="0",
        data=None
    ))), 400


# ---------------- REGISTER ----------------

@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()

    result = dao.create_user(
        data.get("username"),
        data.get("password")
    )

    # 🔥 NORMALIZAR RESPUESTA (IMPORTANTE PARA FRONTEND)
    return jsonify(asdict(ApiResponse(
        msg=result.get("msg", "User created"),
        coderesponse=result.get("coderesponse", "1"),
        data=result.get("data", None)
    ))), 200


# ---------------- GAMES ----------------

@app.route('/games', methods=['GET'])
def get_games():
    return jsonify(asdict(ApiResponse(
        msg="Game list",
        coderesponse="1",
        data=dao.get_games()
    ))), 200


@app.route('/games', methods=['POST'])
def add_game():
    data = request.get_json()

    result = dao.add_game(
        data.get("id"),
        data.get("title"),
        data.get("description"),
        data.get("price")
    )

    return jsonify(asdict(ApiResponse(
        msg=result.get("msg", "Game added"),
        coderesponse=result.get("coderesponse", "1"),
        data=result.get("data", None)
    ))), 200


# ---------------- LIBRARY ----------------

@app.route('/library/<int:user_id>', methods=['GET'])
def library(user_id):
    return jsonify(asdict(ApiResponse(
        msg="User library",
        coderesponse="1",
        data=dao.get_library(user_id)
    ))), 200


@app.route('/library', methods=['POST'])
def add_library():
    data = request.get_json()

    result = dao.add_to_library(
        data.get("user_id"),
        data.get("game_id")
    )

    return jsonify(asdict(ApiResponse(
        msg=result.get("msg", "Added to library"),
        coderesponse=result.get("coderesponse", "1"),
        data=result.get("data", None)
    ))), 200


# ---------------- RUN ----------------

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10030, debug=True)