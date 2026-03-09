import requests
from Prototip2 import User
from Prototip2 import View
from client import *
from flask import jsonify

class DaoUserClient:
    base_URL = "http://localhost:5000"

    def login(self, user):
        # user.username
        # user.password
        # TODO Validar
        # Agafo username y password del objeto user
        # Peticio HTTP al Webservice
        URL_peticio = self.base_URL + "/login"
        params_POST = {
            "username": user.username,
            "password": user.password
        }
        response = requests.post(URL_peticio, json=params_POST)
        if response.status_code == 200:
            user_data_raw = response.json()
            code_response=user_data_raw['coderesponse']
            if code_response == '1':
                user=User(user_data_raw['id'], user_data_raw['username'],
                           "" ,user_data_raw['email'], user_data_raw['idrole'], user_data_raw['token'])
                return user
            else:
                return None
        else:
            return None
#TEST        
daoClient=DaoUserClient()
user=User("", "mare", "12345", "", "", "")
resposta=daoClient.login(user)
print(resposta)