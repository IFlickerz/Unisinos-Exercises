a = int(input("Digite o valor para 'a': "))
b = int(input("Digite o valor para 'b': "))
c = int(input("Digite o valor para 'c': "))

x1 = ((-1 * b) + (b**2 - 4 * a * c)**(1/2))/2*a
x2 = ((-1 * b) - (b**2 - 4 * a * c)**(1/2))/2*a

print("x¹ =", x1, "; x² =", x2)