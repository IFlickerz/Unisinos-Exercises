for i in range(0,6):
    
    senha = input("Digite sua senha: ")
    
    if senha.isdigit() == False or len(senha) < 5 or len(senha) > 10:
        print("\nErro ao definir a sua senha\n")
        if i == 5:
            print("Número máximo de tentativas excedido")
    else:
        print("\nSenha definida com sucesso!")
        break
