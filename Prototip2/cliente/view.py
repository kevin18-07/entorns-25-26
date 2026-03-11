# cliente/view.py
from DaoUserClient import DaoUserClient

class ViewConsole:
    def __init__(self):
        self.dao = DaoUserClient()
        self.user = None

    def viewShowMenu(self):
        print("\n=== MENU ===")
        print("1. Login")
        print("2. Ver hijos")
        print("3. Quit")
        while True:
            option = input("Enter Option: ")
            if option.isdigit():
                optionInt = int(option)
                if optionInt in [1, 2, 3]:
                    return optionInt
            print("Error, input a correct option (1, 2 or 3)")

    def viewGeneral(self):
        option = 1
        while option != 3:
            option = self.viewShowMenu()
            if option == 1:
                self.viewLogin()
            elif option == 2:
                self.viewShowChildren()
            elif option == 3:
                print("Bye")

    def viewLogin(self):
        print("\n=== LOGIN ===")
        username = input("Username or email: ")
        password = input("Password: ")
        user = self.dao.login(username, password)
        if user:
            self.user = user
            print(f"\nUsuario autenticado: {user}")
        else:
            print("\nUsuario NO autenticado")

    def viewShowChildren(self):
        if not self.user:
            print("\nDebes estar logueado primero")
            return

        children = self.dao.get_children(self.user.username)
        if not children:
            print("\nNo se encontraron hijos")
            return

        print("\n=== Lista de hijos ===")
        for child in children:
            print(f"{child.child_name} | Sleep Avg: {child.sleep_average} | Treatment ID: {child.treatment_id} | Time: {child.time}")


# Ejecutar consola
if __name__ == "__main__":
    viewConsole = ViewConsole()
    viewConsole.viewGeneral()