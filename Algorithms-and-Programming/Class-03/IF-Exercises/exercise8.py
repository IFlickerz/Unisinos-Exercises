print("Digite 1 para somar dois valores")
print("Digite 2 para subtrair dois valores")
print("Digite 3 para multiplicar dois valores")
print("Digite 4 para dividir dois valores")
print("Digite 5 para realizar uma potência entre dois valores")
print("Digite 6 para realizar uma radiciação entre dois valores")
print("Digite qualquer outro número para sair")

opcao = int(input("Digite a opção desejada: "))

if opcao >= 1 and opcao <= 6:
    v1 = float(input("Digite o primeiro valor: "))
    v2 = float(input("Digite o segundo valor: "))

if opcao == 1:
    print(v1 + v2)
elif opcao == 2:
    print(v1 - v2)
elif opcao == 3:
    print(v1 * v2)
elif opcao == 4:
    print(v1 / v2)
elif opcao == 5:
    print(v1 ** v2)
elif opcao == 6:
    print(v1 ** (1/v2))
