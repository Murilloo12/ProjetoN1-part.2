import src.repositories.user_repository as repository

from src.views.user_view import displayUsers
from src.views.user_view import displayMenu

from src.utils.console_utils import clearConsole

def insertUser():
    clearConsole()

    user = {
        "name": input("Digite o nome do usuário: "),
        "surname": input("Digite o sobrenome do usuário: "),
        "email": input("Digite o e-mail do usuário: ")
    }

    repository.insertUser(user)

    print("\nUsuário Inserido com Sucesso!\n")

def listUser():
    clearConsole()

    userList = repository.getUsers()
    displayUsers(userList)

def listUserSorted():
    clearConsole()

    userList = repository.getUsersSorted()
    displayUsers(userList)

def findUserByName():
    clearConsole()

    name = input("Digite o nome do usuário: ")
    userList = repository.findUserByName(name)

    clearConsole()

    if(len(userList) > 0):
        print("Usuário encontrado!\n")
        displayUsers(userList)
    else:
        print("Usuário não encontrado!\n")

def setup():
    clearConsole()
    while(True):
        displayMenu()

        try:
            menuAnswer = int(input("Qual ação você deseja realizar? (Digite apenas o número)\n"))
            if(menuAnswer == 1):
                insertUser()
            elif(menuAnswer == 2):
                listUser()
            elif(menuAnswer == 3):
                listUserSorted()
            elif(menuAnswer == 4):
                findUserByName()
            else:
                break
        except ValueError as erro:
            clearConsole()
            print("Digite somente números e inteiros!\n")

