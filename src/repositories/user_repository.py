import os
import json

dirPath = os.path.dirname(os.path.realpath(__file__))

def insertUser(user):
    user = open
    userList.append(user)

def getUsers():
    return userList

def getUsersSorted():
    userList.sort()
    return userList

def checkUserExists(user):
    return user in userList
