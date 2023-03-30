#Exercise 1:

def imprimeValor(a):
    print(a)

#Exercise 2:

def somaValores(a, b):
    print(a + b)

#Exercise 3:

def isDivisivel(val1, val2):
    if val1 % val2 == 0:
        return True
    return False

#Exercise 4:

def maiorValor(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c
    
#Exercise 5:

def somaEntre(a):
    if a < 0: return -1
    soma = 0
    for i in range(a+1):
        soma += i
    return soma

#Exercise 6:

def charQuant(texto):
    return len(texto)

#Exercise 7:

def printList(lista):
    for i in lista:
        print(i)

#Exercise 8:

def maiorList(lista):
    menor = lista[0]
    for i in lista:
        if len(i) < len(menor):
            menor = i
    return menor

#Exercise 9:

def imprimeVezes(n, s):
    for i in range(n+1):
        print(s)