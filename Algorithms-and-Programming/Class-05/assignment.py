p = int(input("Digite de quantos patinhos será a música: "))

if p >= 2:
    for cont in range(p,0,-1):

        minus = cont - 1

        if minus == 0:
            print("1 patinho\nFoi passear\nAlém das montanhas\nPara brincar\nA mamãe gritou\nQuack quack quack quack\nMas nenhum patinho\nVoltou de lá\n\nA mamãe patinha\nFoi procurar\nAlém das montanhas\nNa beira do mar\nA mamãe gritou\nQuack quack quack quack\nE os", p, "patinhos\nVoltaram de lá")
        elif minus == 1:
            print(cont, "patinhos\nForam passear\nAlém das montanhas\nPara brincar\nA mamãe gritou\nQuack quack quack quack\nMas só 1 patinho\nVoltou de lá\n")
        else:
            print(cont, "patinhos\nForam passear\nAlém das montanhas\nPara brincar\nA mamãe gritou\nQuack quack quack quack\nMas só", minus, "patinhos\nVoltaram de lá\n")

else:
    print("Para fazer a música, é necessário ao menos 2 patinhos")