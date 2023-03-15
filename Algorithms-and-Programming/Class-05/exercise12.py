print("Digite números positivos: ")

cont = 0
media = 0

while True:
    numero = float(input())

    if numero < 0:
        if cont != 0:
            print(media / cont)
        break
    else:
        media += numero
        cont += 1