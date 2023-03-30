a, b, c = input().split()
a, b, c = float(a), float(b), float(c)

delta = (b**2 - 4 * a * c)

if delta >= 0 and a != 0:

    r1 = ((-1 * b) + delta**(1/2))/(2*a)
    r2 = ((-1 * b) - delta**(1/2))/(2*a)
                
    print("R1 = %.5f" % r1)
    print("R2 = %.5f" % r2)

else:
    print("Impossivel calcular")