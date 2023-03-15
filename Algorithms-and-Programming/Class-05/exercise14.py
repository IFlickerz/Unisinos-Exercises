n = int(input("Digite um número: "))
mult = 0

for cont in range(2,n):
    if n % cont == 0:
        mult += 1

if mult == 0:
    print("O número é primo")
else:
    print("O número não é primo")