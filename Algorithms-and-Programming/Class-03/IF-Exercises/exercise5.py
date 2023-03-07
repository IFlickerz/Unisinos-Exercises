preco = float(input("Digite o preço do produto: "))

if preco <= 0:
    print("Preço inválido")
elif preco > 0 and preco <= 30:
    print("Preço baixo")
elif preco > 30 and preco <= 50:
    print("Preço médio")
else:
    print("Preço alto")