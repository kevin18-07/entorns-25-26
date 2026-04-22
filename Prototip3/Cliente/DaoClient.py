import requests

class DAOClient:

    def __init__(self):
        self.base_url = "http://127.0.0.1:5000"

    def login(self, identifier, password):
        url = f"{self.base_url}/login"

        payload = {
            "identifier": identifier,
            "password": password
        }

        response = requests.post(url, json=payload)

        if response.status_code == 200:
            return response.json()
        else:
            return response.json()


# Ejemplo de uso
client = DAOClient()
res = client.login("mare", "mare")
print(res)