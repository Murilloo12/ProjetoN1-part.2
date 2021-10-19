import src.repositories.user_repository as repository

from src.views.user_view import displayUsers
from src.views.user_view import displayMenu

def insertUser():
    user = {
        "name": input("Digite o nome do usuário: "),
        "surname": input("Digite o sobrenome do usuário: "),
        "email": input("Digite o e-mail do usuário: ")
    }

    repository.insertUser(user)

def listUser():
    userList = repository.getUsers()
    displayUsers(userList)

def setup():
    while(True):
        displayMenu()
        menuAnswer = int(input("Qual ação você deseja realizar? (Digite apenas o número)\n"))

        if(menuAnswer == 1):
            insertUser()
        elif(menuAnswer == 2):
            listUser()
        else:
            break

