import math 

a = int(input("Digite o valor para A: "))
b = int(input("Digite o valor para B: "))
c = int(input("Digite o valor para C: "))

if ((math.fabs(b - c)) < a < b + c) and ((math.fabs(a - c)) < b < a + c) and ((math.fabs(a - b)) < c < a + b):
    if a == b and a == c:
        print("Triângulo Equilátero")
    if a == b or a == c or b == c:
        print("Triângulo Isóceles")
    else:
        print("Triângulo Escaleno")
else:
    print("Não forma um Triângulo")
