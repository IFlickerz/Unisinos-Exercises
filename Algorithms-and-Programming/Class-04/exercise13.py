nome = input("Digite o seu nome: ")
senha = input("Digite sua senha: ")

if senha.startswith(nome) and senha.endswith("9876"):
    print("Login realizado.")
else:
    print("Usuário ou Senha incorreta.")