userList = []

def insertUser(user):
    userList.append(user)

def getUsers():
    return userList

def getUsersSorted():
    userList.sort()
    return userList

def checkUserExists(user):
    return user in userList
