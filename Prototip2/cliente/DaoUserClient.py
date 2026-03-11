import requests
from user import User, Child

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
                    "",  # No guardamos contraseña
                    user_data["email"],
                    user_data["idrole"]
                )
                return user
        return None

    def get_children(self, username):
        URL_peticio = self.base_URL + "/child"
        params_POST = {"username": username}

        try:
            response = requests.post(URL_peticio, json=params_POST)
        except requests.exceptions.RequestException as e:
            print("Error de conexión:", e)
            return []

        if response.status_code == 200:
            resp_json = response.json()
            children_list = []
            if resp_json["coderesponse"] == "1":
                for c in resp_json.get("data", []):
                    child = Child(
                        id=c["id"],
                        child_name=c["child_name"],
                        sleep_average=c["sleep_average"],
                        treatment_id=c["treatment_id"],
                        time=c["time"]
                    )
                    children_list.append(child)
            return children_list
        return []