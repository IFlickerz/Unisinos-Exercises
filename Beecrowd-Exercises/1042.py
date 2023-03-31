a, b, c = input().split()
a, b, c = int(a), int(b), int(c)

lista = [a, b, c]
lista.sort()

print(str(lista[0]) + "\n" +
      str(lista[1]) + "\n" +
      str(lista[2]) + "\n\n" +
      str(a) + "\n" + 
      str(b) + "\n" +
      str(c))