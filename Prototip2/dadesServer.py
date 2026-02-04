from flask import Flask, request, jsonify
from datetime import datetime
import uuid

# --- Clases ---
class User:
    def __init__(self, id, username, password, email, idrole):
        self.id = id
        self.username = username
        self.password = password
        self.email = email
        self.idrole = idrole  # corregido

    def __str__(self):
        return f"{self.username}:{self.password}:{self.email}"

    def to_dict(self):
        return {
            "id": self.id,
            "username": self.username,
            "password": self.password,
            "email": self.email,
            "idrole": self.idrole
        }

class Child:
    def __init__(self, id, child_name, sleep_average, treatment_id, time):
        self.id = id
        self.child_name = child_name
        self.sleep_average = sleep_average
        self.treatment_id = treatment_id
        self.time = time

    def to_dict(self):
        return {
            "id": self.id,
            "child_name": self.child_name,
            "sleep_average": self.sleep_average,
            "treatment_id": self.treatment_id,
            "time": self.time
        }

class Tap:
    def __init__(self, id, child_id, status_id, user_id, init, end=None):
        self.id = id
        self.child_id = child_id
        self.status_id = status_id
        self.user_id = user_id
        self.init = init
        self.end = end

    def to_dict(self):
        return {
            "id": self.id,
            "child_id": self.child_id,
            "status_id": self.status_id,
            "user_id": self.user_id,
            "init": self.init,
            "end": self.end
        }

class Status:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def to_dict(self):
        return {"id": self.id, "name": self.name}

class Role:
    def __init__(self, id, type_rol):
        self.id = id
        self.type_rol = type_rol

    def to_dict(self):
        return {"id": self.id, "type_rol": self.type_rol}

class Treatment:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def to_dict(self):
        return {"id": self.id, "name": self.name}

# --- Datos ---
users = [
    User(id=1, username="mare", password="12345", email="pepe@gmail.com", idrole=1),
    User(id=2, username="pare", password="123", email="prova2@gmail.com", idrole=1)
]

children = [
    Child(id=1, child_name="Carol Child", sleep_average=8, treatment_id=1, time=6),
    Child(id=2, child_name="Jaco Child", sleep_average=10, treatment_id=2, time=6)
]

taps = [
    Tap(id=1, child_id=1, status_id=1, user_id=1, init="2024-12-18T19:42:43"),
    Tap(id=2, child_id=2, status_id=2, user_id=2, init="2024-12-18T21:42:43")
]

relation_user_child = [
    {"user_id": 1, "child_id": 1, "rol_id": 1},
    {"user_id": 1, "child_id": 2, "rol_id": 1},
    {"user_id": 1, "child_id": 1, "rol_id": 2},
    {"user_id": 2, "child_id": 2, "rol_id": 1},
    {"user_id": 2, "child_id": 2, "rol_id": 2}
]

roles = [
    Role(id=1, type_rol='Admin'),
    Role(id=2, type_rol='Tutor Mare Pare'),
    Role(id=3, type_rol='Cuidador'),
    Role(id=4, type_rol='Seguiment')
]

statuses = [
    Status(id=1, name="sleep"),
    Status(id=2, name="awake yes_eyepatch"),
    Status(id=3, name="awake no_eyepatch")
]

treatments = [
    Treatment(id=1, name='Hour'),
    Treatment(id=2, name='percentage')
]

# --- DAO ---
class DAOUser:
    def __init__(self, users, children, taps, relation_user_child):
        self.users = users
        self.children = children
        self.taps = taps
        self.relation_user_child = relation_user_child

    def listar(self):
        return [u.to_dict() for u in self.users]

    def add_user(self, data):
        if any(u.email == data["email"] for u in self.users):
            return None
        max_id = max([u.id for u in self.users], default=0)
        user = User(id=max_id+1, **data)
        self.users.append(user)
        return user.to_dict()

    def update_user(self, id, data):
        for u in self.users:
            if u.id == id:
                u.username = data.get("username", u.username)
                u.password = data.get("password", u.password)
                u.email = data.get("email", u.email)
                u.idrole = data.get("idrole", u.idrole)
                return u.to_dict()
        return None

    def delete_user(self, id):
        for u in self.users:
            if u.id == id:
                self.users.remove(u)
                return True
        return False

    def search_by_email(self, email):
        for u in self.users:
            if u.email == email:
                return u.to_dict()
        return None

    def login(self, username, password):
        for u in self.users:
            if u.username == username and u.password == password:
                return u.to_dict()
        return None

    def login_token(self, username, password):
        user = self.login(username, password)
        if user:
            token = str(uuid.uuid4())
            return {"user": user, "token": token, "issued_at": datetime.now().isoformat()}
        return None

    def get_children_by_user(self, user_id):
        child_ids = [r["child_id"] for r in self.relation_user_child if r["user_id"] == user_id]
        return [c.to_dict() for c in self.children if c.id in child_ids]

    def get_taps_by_user(self, user_id):
        return [t.to_dict() for t in self.taps if t.user_id == user_id]

# --- Instancia DAO ---
dao = DAOUser(users, children, taps, relation_user_child)

# --- Flask ---
app = Flask(__name__)

@app.route("/users", methods=["GET"])
def listar_users():
    return jsonify(dao.listar())

@app.route("/users", methods=["POST"])
def add_user_route():
    data = request.json
    result = dao.add_user(data)
    if result:
        return jsonify(result), 201
    return jsonify({"error": "Email ya existe"}), 400

@app.route("/users/<int:id>", methods=["PUT"])
def update_user_route(id):
    data = request.json
    result = dao.update_user(id, data)
    if result:
        return jsonify(result)
    return jsonify({"error": "Usuario no encontrado"}), 404

@app.route("/users/<int:id>", methods=["DELETE"])
def delete_user_route(id):
    if dao.delete_user(id):
        return jsonify({"status": "Eliminado"})
    return jsonify({"error": "Usuario no encontrado"}), 404

@app.route("/users/email/<email>", methods=["GET"])
def search_user_email(email):
    result = dao.search_by_email(email)
    if result:
        return jsonify(result)
    return jsonify({"error": "Usuario no encontrado"}), 404

@app.route("/login", methods=["POST"])
def login_route():
    data = request.json
    result = dao.login(data["username"], data["password"])
    if result:
        return jsonify(result)
    return jsonify({"error": "Credenciales incorrectas"}), 401

@app.route("/login/token", methods=["POST"])
def login_token_route():
    data = request.json
    result = dao.login_token(data["username"], data["password"])
    if result:
        return jsonify(result)
    return jsonify({"error": "Credenciales incorrectas"}), 401

@app.route("/users/<int:id>/children", methods=["GET"])
def get_children(id):
    return jsonify(dao.get_children_by_user(id))

@app.route("/users/<int:id>/taps", methods=["GET"])
def get_taps(id):
    return jsonify(dao.get_taps_by_user(id))

# --- Ejecutar server ---
if __name__ == "__main__":
    app.run(debug=True)