cont = 0

while cont <= 200:
    mult = 0
    for cont_primo in range (2,cont):
        if cont % cont_primo == 0:
            mult += 1
    if mult == 0:
        print(cont)
    cont += 1