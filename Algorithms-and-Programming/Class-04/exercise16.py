p1_nome = input("Digite o nome do jogador 1: ")
p2_nome = input("Digite o nome do jogador 2: ")

p1_opcao = input("Digite a opção do jogador 1: ")

p1_opcao = p1_opcao.lower()

if p1_opcao == "par" or p1_opcao == "impar" or p1_opcao == "ímpar":
    p1_numero = int(input("Digite o número do jogador 1: "))
    p2_numero = int(input("Digite o número do jogador 2: "))

    if p1_opcao == "par" and ((p1_numero + p2_numero) % 2) == 0:
        print(p1_nome + " ganhou!")
    elif p1_opcao == "impar" and ((p1_numero + p2_numero) % 2) != 0:
        print(p1_nome + " ganhou!")
    else:
        print(p2_nome + " ganhou!")

else:
    print("Digite 'par' ou 'ímpar' para opção do jogador 1.")
