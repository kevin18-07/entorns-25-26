# DaoServer.py - DAOs para servidor
from dadesServer import User, users, children, taps, relation_user_child

class UserDAO:
    def __init__(self):
        self.users = users

    def get_all_users(self):
        return [user.__dict__ for user in self.users]

    def get_user_by_username(self, username):
        for user in self.users:
            if user.username == username:
                return user.__dict__
        return None
    
    def login(self, identifier, password):
        for user in self.users:
            if (user.username == identifier or user.email == identifier) and user.password == password:
                return user
        return None
    
    def get_user_roles(self, user_id):
        return [relation['rol_id'] for relation in relation_user_child if relation['user_id'] == user_id]


class ChildDAO:
    def __init__(self):
        self.children = children
        self.relation_user_child = relation_user_child
    
    def get_children(self, user):
        child_ids = {r['child_id'] for r in self.relation_user_child if r['user_id'] == user.id}
        return [c for c in self.children if c.id in child_ids]


class TapDAO:
    def get_taps_by_child(self, child_id):
        return [t.__dict__ for t in taps if t.child_id == child_id]