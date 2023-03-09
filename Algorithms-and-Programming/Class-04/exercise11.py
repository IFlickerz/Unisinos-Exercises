prod_nome = input("Digite o nome do produto: ")
prod_prec = float(input("Digite o preço do produto: "))

qntd_comp = int(input("Digite a quantidade que deseja comprar: "))

print("Valor total da compra de", qntd_comp,"" + prod_nome + "(s): R$%.2f" % (prod_prec * qntd_comp))