# cliente/user.py
class User:
    def __init__(self, id, username, password, email, idrole, token=""):
        self.id = id
        self.username = username
        self.password = password
        self.email = email
        self.idrole = idrole
        self.token = token  # No lo usamos, pero lo dejamos por compatibilidad

    def __str__(self):
        return f"User(ID={self.id}, name={self.username}, email={self.email}, IDROLE={self.idrole})"

    def to_dict(self):
        return {
            "id": self.id,
            "username": self.username,
            "password": self.password,
            "email": self.email,
            "idrole": self.idrole,
            "token": self.token
        }

# Clase Child para el cliente
class Child:
    def __init__(self, id, child_name, sleep_average, treatment_id, time):
        self.id = id
        self.child_name = child_name
        self.sleep_average = sleep_average
        self.treatment_id = treatment_id
        self.time = time

    def __str__(self):
        return f"Child(ID={self.id}, Name={self.child_name}, Sleep Avg={self.sleep_average}, Treatment={self.treatment_id})"