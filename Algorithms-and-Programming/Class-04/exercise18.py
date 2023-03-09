saldo = float(input("Digite o saldo da conta: "))

print("\n1. Realizar um Saque\n2. Realizar um Depósito\n")

op = int(input("Digite o número da operação desejada: "))

if op == 1 or op == 2:
    valor = float(input("Digite o valor da operação: "))

    if op == 1 and valor > saldo:
        print("Insucesso!\nValor de Saque não pode ser maior que o Saldo da conta")
    elif op == 2 and valor > 300:
        print("Insucesso!\nNão é possível depositar mais do que R$300,00")
    elif op == 1:
        print("Sucesso!\nSaldo atual da conta: R$%.2f" % (saldo - valor))
    else:
        print("Sucesso!\nSaldo atual da conta: R$%.2f" % (saldo + valor))

else:
    print("Selecione entre a operação 1 ou 2")