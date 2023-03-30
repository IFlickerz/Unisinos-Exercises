def isPrimo(a):
    if a < 0: return False
    for i in range(2,a**(1/2)+1):
        if a % i == 0:
            return False
    return True

print(isPrimo(int(input("Digite um número: "))))