# client.py - Cliente para prototipo
import requests

class UserClient:
    def __init__(self, id, username, password, email, idrole, token):
        self.id = id
        self.username = username
        self.password = password
        self.email = email
        self.idrole = idrole
        self.token = token
    
    def __str__(self):
        return f"{self.username} ({self.email}) - Role: {self.idrole}"


class DaoUserClient:
    base_URL = "http://127.0.0.1:5000"

    def login(self, username, password):
        try:
            response = requests.post(
                f"{self.base_URL}/login",
                json={"username": username, "password": password}
            )
        except requests.exceptions.RequestException:
            return None

        if response.status_code == 200:
            resp_json = response.json()
            if resp_json["coderesponse"] == "1":
                user_data = resp_json["data"]
                return UserClient(
                    user_data["id"],
                    user_data["username"],
                    "",  # no almacenar password en cliente
                    user_data["email"],
                    user_data["idrole"],
                    user_data["token"]
                )
        return None


# implementar class ViewConsole: