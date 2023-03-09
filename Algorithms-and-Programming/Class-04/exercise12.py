prod_nome = input("Digite o nome do produto: ")
prod_prec = float(input("Digite o preço do produto: "))

qntd_comp = int(input("Digite a quantidade que deseja comprar: "))

vlr_compr = prod_prec * qntd_comp

if qntd_comp >= 3 and qntd_comp <= 4:
    vlr_compr -= vlr_compr * 0.1
elif qntd_comp >= 5 and qntd_comp <= 10:
    vlr_compr -= vlr_compr * 0.15
elif qntd_comp > 10:
    vlr_compr -= vlr_compr * 0.2

print("Valor total da compra de", qntd_comp,"" + prod_nome + "(s): R$%.2f" % vlr_compr)