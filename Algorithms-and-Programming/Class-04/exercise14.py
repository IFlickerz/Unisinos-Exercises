nome = input("Digite seu nome: ")
peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))

imc = peso / (altura**2)

if imc < 18.5:
    print("Abaixo do peso")
elif imc >= 18.5 and imc <= 24.9:
    print("Peso normal")
elif imc >= 25.0 and imc <= 29.9:
    print("Pré-obesidade")
elif imc >= 30.0 and imc <= 34.9:
    print("Obesidade Grau 1")
elif imc >= 35.0 and imc <= 39.9:
    print("Obesidade Grau 2")
else:
    print("Obesidade Grau 3")