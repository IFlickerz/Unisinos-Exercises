ano = int(input("Insira o ano: "))
mes = int(input("Insira o mês: "))
dia = int(input("Insira o dia: "))

if ano >= 0 and ano <= 2022:
    if mes >= 1 and mes <= 12:
        if dia >= 1 and dia <= 31:
            if(mes == 2) and (dia <= 29) and (ano % 4 == 0):
                print("Data correta!")
            elif (mes == 2) and (dia > 28):
                print("Dia informado para Fevereiro deve ser entre 1 e 28 (ou 29 em anos bissextos)")
            else: 
                if (mes == 4) and (dia > 30):
                    print("Dia informado para Abril deve ser entre 1 e 30")
                else:
                    if (mes == 6) and (dia > 30):
                        print("Dia informado para Junho deve ser entre 1 e 30")
                    else:
                        if (mes == 9) and (dia > 30):
                            print("Dia informado para Setembro deve ser entre 1 e 30")
                        else:
                            if (mes == 11) and (dia > 30):
                                print("Dia informado para Novembro deve ser entre 1 e 30")            
                            else:
                                print("Data correta!")
        else:
            print("O dia informado deve ser entre 1 e 31")
    else:
        print("O mês informado deve ser entre 1 e 12")
else:
    print("O ano informado deve ser entre 0 e 2022")

