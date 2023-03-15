n1 = int(input("Digite o primeiro valor: "))
n2 = int(input("Digite o segundo valor: "))

if n1 >= 0 and n2 >= 0:
    if n1 >= n2:
        maior = n1
        menor = n2
        cont  = n2 
    else:
        maior = n2
        menor = n1
        cont  = n1

    while cont <= maior:
        if cont % 2 == 0:
            print(cont)
        cont += 1
    
       
