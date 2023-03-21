a = int(input("Digite o primeiro valor: "))
b = int(input("Digite o segundo valor: "))

if a <= b:
    for i in range(a+1, b):
        print(i)
else:
    for i in range(b+1, a):
        print(i)