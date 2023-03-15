quant = int(input("Digite quantos números irá digitar: "))

cont = 1

while cont <= quant:
    numero = int(input("Digite um número: "))

    if numero == 0:
        print("O número digitado é 0")
    elif numero > 0:
        print("O número digitado é positivo")
    else:
        print("O número digitado é negativo")

    cont += 1
        