a, b, c = input().split()
a, b, c = float(a), float(b), float(c)

lista = [a, b, c]
lista.sort(reverse = True)

a = lista[0]
b = lista[1]
c = lista[2]

if a >= (b + c):
    print("NAO FORMA TRIANGULO")
elif (a**2) == (b**2 + c**2):
    print("TRIANGULO RETANGULO")
elif (a**2) > (b**2 + c**2):
    print("TRIANGULO OBTUSANGULO")
else:
    print("TRIANGULO ACUTANGULO")

if a == b and a == c:
    print("TRIANGULO EQUILATERO")
elif a == b and a != c:
    print("TRIANGULO ISOSCELES")
elif b == c and b != a:
    print("TRIANGULO ISOSCELES")