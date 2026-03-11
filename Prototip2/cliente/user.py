# cliente/user.py
class User:
    def __init__(self, id, username, password, email, idrole, token=""):
        self.id = id
        self.username = username
        self.password = password
        self.email = email
        self.idrole = id
        self.token = token

    def __str__(self):
        return f"User(ID={self.id}, name={self.username}, email={self.email}, password={self.password}, token={self.token}, IDROLE={self.idrole})"

    def to_dict(self):
        return {
            "id": self.id,
            "username": self.username,
            "password": self.password,
            "email": self.email,
            "idrole": self.idrole,
            "token": self.token
        }