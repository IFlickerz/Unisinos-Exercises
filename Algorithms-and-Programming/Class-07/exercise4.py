texto = input("Digite um texto: ")

cont = 0

for i in range(0, len(texto)):
    if texto[i] == "a" or texto[i] == "e" or texto[i] == "o" or texto[i] == "i" or texto[i] == "u":
        cont += 1

print(cont, "vogais presentes no texto")