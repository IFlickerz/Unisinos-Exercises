while True:

    num = int(input("\nDigite um número: "))

    if num < 0:
        break

    soma = 1

    for i in range(2,num):
        if num % i == 0:
            soma += i

    if soma == num:
        print("\nO número digitado é um número perfeito.")
    else:
        print("\nO número digitado não é um número perfeito.")