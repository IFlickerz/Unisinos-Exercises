solteiros = []
casados = []
divorciados = []
viuvos = []

for i in range(0, 20):
    nome = input("Digite o nome da pessoa: ")
    est_civil = input("Digite o estado civil da pessoa: ")

    est_civil = est_civil.lower()

    if est_civil == "solteiro" or est_civil == "solteira":
        solteiros.append(nome)
    elif est_civil == "casado" or est_civil == "casada":
        casados.append(nome)
    elif est_civil == "divorciado" or est_civil == "divorciada":
        divorciados.append(nome)
    else:
        viuvos.append(nome)

print("Solteiros:", solteiros, 
      "\nCasados:", casados,
      "\nDivorciados:", divorciados,
      "\nViúvos:", viuvos)