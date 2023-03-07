atvdp1 = float(input("Digite a nota da Primeira Atividade Prática: "))
atvdp2 = float(input("Digite a nota da Segunda Atividade Prática: "))

prova = float(input("Digite a nota da Prova em Laboratório: "))
teste = float(input("Digite a nota do Teste Teórico: "))
trabx = float(input("Digite a nota do Trabalho Extraclasse: "))

if atvdp1 < 0 or atvdp2 < 0 or prova < 0 or teste < 0 or trabx < 0:
    print("Erro!\nValor negativo informado")
else:
    grauA = float(atvdp1 * 0.45 + atvdp2 * 0.55)
    grauB = float(prova * 0.6 + teste * 0.2 + trabx * 0.2)

    nota = grauA * 0.33 + grauB * 0.67

    print(nota)

    if nota < 6:
        print("É necessário realizar o Grau C")
    else:
        print("Não é necessário realizar o Grau C")