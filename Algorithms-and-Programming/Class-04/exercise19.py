p1_name = input("Digite o nome do Jogador 1: ") 
p2_name = input("Digite o nome do Jogador 2: ")

p1_play = input("Digite a jogada do Jogador 1: ")
p2_play = input("Digite a jogada do Jogador 2: ")
p1_play = p1_play.lower()
p2_play = p2_play.lower()

if p1_play != "pedra" and p1_play != "papel" and p1_play != "tesoura" and p1_play != "lagarto" and p1_play != "spock":
    print("Jogador 1, insira uma jogada válida.")
elif p2_play != "pedra" and p2_play != "papel" and p2_play != "tesoura" and p2_play != "lagarto" and p2_play != "spock":
    print("Jogador 2, insira uma jogada válida.")
else:
    if p1_play == "pedra" and (p2_play == "lagarto" or p2_play == "tesoura"):
        print(p1_name + " é o vencedor!")
    elif p1_play == "papel" and (p2_play == "pedra" or p2_play == "spock"):
        print(p1_name + " é o vencedor!")
    elif p1_play == "tesoura" and (p2_play == "papel" or p2_play == "lagarto"):
        print(p1_name + " é o vencedor!")
    elif p1_play == "lagarto" and (p2_play == "papel" or p2_play == "spock"):
        print(p1_name + " é o vencedor!")
    elif p1_play == "spock" and (p2_play == "tesoura" or p2_play == "pedra"):
        print(p1_name + " é o vencedor!")
    else:
        print(p2_name + " é o vencedor!")
