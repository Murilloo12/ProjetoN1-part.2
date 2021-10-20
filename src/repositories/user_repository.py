import os
import json

DIRNAME = os.path.dirname(os.path.realpath(__file__))

DATA_FILENAME = "users_data.json"
DATA_DIR_PATH = DIRNAME.replace("repositories", "data")
DATA_FILE_PATH = os.path.join(DATA_DIR_PATH, DATA_FILENAME)

def updateUserFile(userList):
    try:
        fileData = open(DATA_FILE_PATH, "w")
        fileData.write(json.dumps(userList))
        fileData.close()
    except Exception as error:
        print("Ocorreu um erro ao atualizar o arquivo dos usuários")
        print(error)
        print("\n")

def getUsers():
    try:
        fileData = open(DATA_FILE_PATH, "r")

        usersData = fileData.read()
        usersData = "[]" if usersData is None or usersData == "" else usersData

        return json.loads(usersData)
    except Exception as error:
        print("Ocorreu um erro ao obter os usuários")
        print(error)
        print("\n")

def insertUser(user):
    try:
        userList = getUsers()
        userList.append(user)

        updateUserFile(userList)
    except Exception as error:
        print("Ocorreu um erro ao inserir um usuário")
        print(error)
        print("\n")

def getUsersSorted():
    try:
        userList = getUsers()
        userListSorted = sorted(userList, key=lambda user: user['name'])

        return userListSorted
    except Exception as error:
        print("Ocorreu um erro ao obter os usuários na ordem alfabética")
        print(error)
        print("\n")

def findUserByName(name):
    try:
        userList = getUsers()
        userListFiltered = list(filter(lambda user: user['name'] == name, userList))

        return userListFiltered
    except Exception as error:
        print("Ocorreu um erro ao obter o usuário pelo nome")
        print(error)
        print("\n")

def removeUserByEmail(email):
    try:
        userList = getUsers()
        for user in range(len(userList)):
            if userList[user]['email'] == email:
                del userList[user]
                break

        updateUserFile(userList)
    except Exception as error:
        print("Ocorreu um erro ao remover um usuário")
        print(error)
        print("\n")

def checkUserByEmail(email):
    try:
        userList = getUsers()
        userExists = False
        for user in range(len(userList)):
            if userList[user]['email'] == email:
                userExists = True
                break

        return userExists
    except Exception as error:
        print("Ocorreu um erro ao checar se usuário existe")
        print(error)
        print("\n")

def changeNameByEmail(userUpdated):
    try:
        userList = getUsers()
        for user in range(len(userList)):
            if userList[user]['email'] == userUpdated["email"]:
                userList[user] = userUpdated
                updateUserFile(userList)
                break
    except Exception as error:
        print("Ocorreu um erro ao alterar um usuário")
        print(error)
        print("\n")