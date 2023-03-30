cod, quant = input().split()
cod, quant = int(cod), int(quant)

if cod == 1:
    print("Total: R$ %.2f" % (4 * quant))
elif cod == 2:
    print("Total: R$ %.2f" % (4.5 * quant))
elif cod == 3:
    print("Total: R$ %.2f" % (5 * quant))
elif cod == 4:
    print("Total: R$ %.2f" % (2 * quant))
elif cod == 5:
    print("Total: R$ %.2f" % (1.5 * quant))