class ViewConsole:
    def viewShowMenu(self):
        print("1. Login")
        print("2: Quit")
        while(True):
            option=input("Enter Option: ")
            if (option.isdigit):
                optionInt=int(option)
                if (optionInt < 2 and optionInt > 0):
                    return optionInt
                else:
                    print("Error, Input a correct option")
    
    def viewGeneral(self):
        option=1
        while (option != 2):
            option=self.viewShowMenu
            match option:
                case 1:
                    self.viewLogin()
                case 2:
                    print("Bye")

    def viewLogin(self):
        print("view Login")
        print("Input name or email and password")
        username = input("Username or email")
        password = input("Password")