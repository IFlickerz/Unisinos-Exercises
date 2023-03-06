atvdp1 = float(input("Digite a nota da Primeira Atividade Prática: "))
atvdp2 = float(input("Digite a nota da Segunda Atividade Prática: "))

grauA = float(atvdp1 * 0.45 + atvdp2 * 0.55)

prova = float(input("Digite a nota da Prova em Laboratório: "))
teste = float(input("Digite a nota do Teste Teórico: "))
trabx = float(input("Digite a nota do Trabalho Extraclasse: "))

grauB = float(prova * 0.6 + teste * 0.2 + trabx * 0.2)

print(grauA * 0.33 + grauB * 0.67)