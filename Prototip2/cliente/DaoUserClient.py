# cliente/DaoUserClient.py
import requests
from user import User

class DaoUserClient:
    base_URL = "http://localhost:5000"

    def login(self, username, password):
        URL_peticio = self.base_URL + "/login"
        params_POST = {"username": username, "password": password}

        try:
            response = requests.post(URL_peticio, json=params_POST)
        except requests.exceptions.RequestException as e:
            print("Error de conexión:", e)
            return None

        if response.status_code == 200:
            resp_json = response.json()
            if resp_json["coderesponse"] == "1":
                user_data = resp_json["data"]
                user = User(
                    user_data["id"],
                    user_data["username"],
                    "",  # no almacenar password en cliente
                    user_data["email"],
                    user_data["idrole"],
                    user_data["token"]
                )
                return user
        return None

# Test rápido
if __name__ == "__main__":
    daoClient = DaoUserClient()
    resposta = daoClient.login("mare", "12345")
    if resposta:
        print(f"Login OK: {resposta.username} - {resposta.email}")
    else:
        print("Login fallido")