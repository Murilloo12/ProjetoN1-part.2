import os
import json

DIRNAME = os.path.dirname(os.path.realpath(__file__))

DATA_FILENAME = "users_data.json"
DATA_DIR_PATH = DIRNAME.replace("repositories", "data")
DATA_FILE_PATH = os.path.join(DATA_DIR_PATH, DATA_FILENAME)

def getUsers():
    fileData = open(DATA_FILE_PATH, "r")

    usersData = fileData.read()
    usersData = "[]" if usersData is None or usersData == "" else usersData

    return json.loads(usersData)

def insertUser(user):
    userList = getUsers()
    userList.append(user)

    fileData = open(DATA_FILE_PATH, "w")
    fileData.write(json.dumps(userList))
    fileData.close()

def getUsersSorted():
    userList.sort()
    return userList

def checkUserExists(user):
    return user in userList
