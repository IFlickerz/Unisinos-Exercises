cont = 1
gremistas = 0

while cont <= 10:
    torcedor = input("Digite o time do " + str(cont) + "º torcedor: ")

    torcedor = torcedor.lower()

    if torcedor == "grêmio" or torcedor == "gremio":
        gremistas += 1

    cont += 1

print(gremistas, "torcedores são Gremistas")