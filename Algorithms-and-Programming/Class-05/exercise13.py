numero = int(input("Digite um número natural positivo: "))

cont = numero

if numero >= 0:
    while cont > 1:
        cont -= 1
        numero *= cont

    print(numero)