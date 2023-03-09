nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))

if idade >= 18:
    pergunta1 = input("1 - Ao prestar socorro à vítima de um acidente, NÃO se deve:\n\na) acionar imediatamente o Corpo de Bombeiros\nb) dar água, comida ou qualquer substância para a vítima cheirar\nc) conversar com a vítima para saber de suas condições gerais\nd) deixar a vítima confortável até a chegada do socorro especializado\n\nResposta: ")
    pergunta2 = input("2 - Ao se deparar com uma sinaleira na cor vermelha, você deve:\n\na) rir dela\nb) passar mais rápido, pois é perigoso parar\nc) dobrar a direita, pois vermelho indica direita\nd) parar\n\nResposta: ")
    pergunta3 = input("3 - Segundo a direção defensiva, quando você está em uma via e um pedestre vai atrevessar, você...\n\na) buzina muito forte para que o pedestre se assuste\nb) atropela o pedestre, pois lugar de pedestre é na calçada\nc) para e dá uma carona para o pedestre, pois é uma lei de trânsito\nd) para e aguarda ele atravessar\n\nResposta: ")

    pergunta1 = pergunta1.lower()
    pergunta2 = pergunta2.lower()
    pergunta3 = pergunta3.lower()

    acertos = 0

    if pergunta1 == "b":
        acertos += 1
    if pergunta2 == "d":
        acertos += 1
    if pergunta3 == "d":
        acertos += 1
        
    if acertos >= 2:
        print("Você está apto para retirar a Carteira de Motorista!")
    else:
        print("Você não está apto para retirar a Carteira de Motorista.")

else:
    print("Para retirar a Carteira de Motorista é necessário ser maior de idade.")