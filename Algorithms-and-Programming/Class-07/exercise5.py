quant = int(input("Digite quantos produtos serão adicionados na lista: "))

compras = []

for i in range(0, quant):
    compras.append(input("Digite o produto para adicionar na lista: "))

print(compras)