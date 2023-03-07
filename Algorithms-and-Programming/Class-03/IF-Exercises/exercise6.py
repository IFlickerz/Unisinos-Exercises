preco = float(input("Digite o preço: "))

if preco < 100:
    preco += preco * 0.1
elif preco >= 100 and preco < 300:
    preco += preco * 0.2
elif preco >= 300 and preco < 1000:
    preco += preco * 0.5

if preco < 0:
    print("Valor inválido")
else:
    print(preco)
