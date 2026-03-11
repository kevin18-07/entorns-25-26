
from DaoUserClient import DaoUserClient
from user import User

class ViewConsole:
    def __init__(self):
        self.dao = DaoUserClient()
        self.user = None

    def viewShowMenu(self):
        print("\n=== MENU ===")
        print("1. Login")
        print("2. Quit")
        while True:
            option = input("Enter Option: ")
            if option.isdigit():
                optionInt = int(option)
                if optionInt in [1, 2]:
                    return optionInt
            print("Error, input a correct option (1 or 2)")

    def viewGeneral(self):
        option = 1
        while option != 2:
            option = self.viewShowMenu()
            if option == 1:
                self.viewLogin()
            elif option == 2:
                print("Bye")

    def viewLogin(self):
        print("\n=== LOGIN ===")
        username = input("Username or email: ")
        password = input("Password: ")
        user = self.dao.login(username, password)
        if user:
            self.user = user
            self.viewUser(user)
        else:
            self.viewUserNotAuthenticated()

    def viewUser(self, user):
        print("\nUsuario autenticado:")
        print(user)

    def viewUserNotAuthenticated(self):
        print("\nUsuario NO autenticado")

# Ejecutar la consola
if __name__ == "__main__":
    viewConsole = ViewConsole()
    viewConsole.viewGeneral()