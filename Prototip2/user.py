class user:
    def __init__ (self, id, username, email, password, token, idrole):
        self.id = id
        self.username = username
        self.email = email
        self.password = password
        self.token = token
        self.idrole = idrole
        def __str__(self):
            return f"User(ID={self.id}, name={self.username}, email={self.email}, password={self.password}, token={self.token}, IDROLE={self.idrole})"