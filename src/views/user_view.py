def displayUsers(listUsers):
    for user in listUsers:
        print("\nNome: {} {}".format(user.get("name"), user.get("name")))
        print("E-mail: ", user.get("email"))

def displayMenu():
    print("1 - Inserir novo usuário")
    print("2 - Listar usuários por ordem de cadastro")
    print("3 - Listar usuários por ordem alfabética")
    print("4 - Checar se o usuário está inscrito")
    print("5 - Remover usuário através do e-mail")
    print("6 - Alterar usuário através do e-mail")
    print("0 - Sair do sistema")