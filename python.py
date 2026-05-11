usuario = input("Digite o nome de usuário: ")

if usuario == "admin":
    senha = input("Digite a senha: ")

    if senha == "1234":
        print("Acesso concedido")
    else:
        print("Acesso negado")
else:
    print("Acesso negado")