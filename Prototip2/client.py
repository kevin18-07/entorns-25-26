import requests

class User:
    def __init__(self, id, username, password ,email, idrole, token):
        self.id = id
        self.username = username
        self.password = password
        self.email = email
        self.idrole = idrole
        self.token = token
    
    def __str__(self):
        return f"{self.username} ({self.email}) - Role: {self.idrole}"


class daoUserClient:

    def login(self, username, password):

        response = requests.post(
            'http://127.0.0.1:5000/login',
            json={
                "username": username,
                "password": password
            }
        )

        if response.status_code == 200:

            data = response.json()

            if data["coderesponse"] == "1":
                return User(
                    data["id"],
                    data["username"],
                    data["password"],
                    data["email"],
                    data["idrole"],
                    data["token"]
                )

        return None


# implementar class ViewConsole: