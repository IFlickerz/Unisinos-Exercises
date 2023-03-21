cont = 0

while cont <= 3:
    if cont == 3:
        print("Número máximo de tentativas excedido")
    else:
        user = input("Digite seu usuário: ")
        passw = input("Digite sua senha: ")
        
        if user == "USER10" and passw == "PASSWORD1234":
            print("Login efetuado com sucesso!")
            break
        else:
            print("Falha no Login!\n")
    cont += 1