from Prototip1.ClientD import User
from Prototip2 import *
from dataclasses import dataclass, asdict
from flask import jsonify
from Prototip2 import user




class UserDAO:
    def __init__(self):
        self.users = user

    def getAllUsers(self):
        return [user.__dict__ for user in self.users]

    def getUserByUsername(self, username):
        for user in self.users:
            if user.username == username:
                return user.__dict__
        return None
    
    def login(self, identifier, password):
        for user in self.users:
            if (user.username == identifier or user.email == identifier) and user.password == password:
                return user
        return None
    
    def getUserRole(self,user_id):
        return [relation['rol_id'] for relation in relation_user_child if relation['user_id'] == user_id]


class ChildDAO:
    def __init__(self):
        self.childs = children
        self.relation_user_child = relation_user_child
    
    def getChilds(self, user):
        child_ids =  {r['child_id'] for r in self.relation_user_child if r['user_id'] == user.id}
        return [c for c in self.childs if c.id in child_ids]

cDao = ChildDAO()
u=User(id=1, username="", password="", email="", idrole=1 ,token="")
listChilds=cDao.getChilds(u)
print(listChilds)

userDao = UserDAO()
listAllUsers=userDao.getAllUsers()
print(type(listAllUsers))
print(" ".join([str(x) for x in userDao.getAllUsers()]))


@dataclass
class ApiResponse():
    msg: str
    coderesponse: str
    data: list

response = ApiResponse(
    msg="All Users",
    coderesponse="1",
    data=userDao.getAllUsers()
)
print(response)
print(asdict(response))

class TapDao:

    def getTapsByChild(self, child_id):
        return [t.__dict__ for t in taps if t.child_id == child_id]