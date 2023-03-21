opt = 0
cont = 0

while opt != 7:
    if cont == 5:

        print("\nParece que você não está entendendo o funcionamento do sistema. Até mais.\n")
        break

    else:    

        opt = int(input("\nOlá Fulano.\n\nDigite a opção desejada:\n\n1) Verificar triângulo\n\n2) Calcular equação do segundo grau\n\n3) Conferir data\n\n4) Verificar tamanho do texto\n\n5) Analisar CPF\n\n6) Contar caracteres\n\n7) Sair\n\n"))

        if opt == 1:

            a = int(input("\nDigite o valor para A: "))
            b = int(input("\nDigite o valor para B: "))
            c = int(input("\nDigite o valor para C: "))

            if ((abs(b - c)) < a < b + c) and ((abs(a - c)) < b < a + c) and ((abs(a - b)) < c < a + b):
                if a == b and a == c:
                    print("\nTriângulo Equilátero")
                elif a == b or a == c or b == c:
                    print("\nTriângulo Isóceles")
                else:
                    print("\nTriângulo Escaleno")
            else:
                print("\nNão forma um Triângulo")
        
        elif opt == 2:

            a = 0
            while a == 0:
                a = int(input("\nDigite o valor para 'a': "))
                if a == 0:
                    print("'a' não pode ser 0!")

            b = int(input("\nDigite o valor para 'b': "))
            c = int(input("\nDigite o valor para 'c': "))

            delta = (b**2 - 4 * a * c)

            if delta > 0:

                x1 = ((-1 * b) + delta**(1/2))/2*a
                x2 = ((-1 * b) - delta**(1/2))/2*a
                
                print("\nx¹ =", x1, "; x² =", x2)

            elif delta == 0:

                x = ((-1 * b)/2*a)

                print("\nx =", x)

            else:
                print("\nO Delta da equação é negativo, fazendo com que a equação não possua raízes reais, portanto não sendo calculada.") 

        elif opt == 3:
            
            error_ano = 1
            error_mes = 1
            error_dia = 1

            while error_ano == 1:

                ano = int(input("\nInsira o ano: "))

                if ano >= 0 and ano <= 2022:

                    error_ano = 0

                    while error_mes == 1:

                        mes = int(input("\nInsira o mês: "))
        
                        if mes >= 1 and mes <= 12:

                            error_mes = 0
                            
                            while error_dia == 1:

                                dia = int(input("\nInsira o dia: "))

                                if dia >= 1 and dia <= 31:
                                    if(mes == 2) and (dia <= 29) and (ano % 4 == 0):
                                        error_dia = 0
                                        print("\nData correta!\n")
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
                                                        error_dia = 0
                                                        print("\nData correta!")
                                else:
                                    print("\nO dia informado deve ser entre 1 e 31")
                        else:
                            print("\nO mês informado deve ser entre 1 e 12")
                else:
                    print("\nO ano informado deve ser entre 0 e 2022")

        elif opt == 4:

            error = 1

            while error == 1:

                texto = input("\nDigite um texto qualquer: ")

                if len(texto) < 5:
                    error = 0
                    print("\nO texto informado é muito pequeno")
                elif len(texto) >= 5 and len(texto) < 15:
                    error = 0
                    print("\nO texto informado é de tamanho médio")
                elif len(texto) >= 15 and len(texto) < 20:
                    error = 0
                    print("\nO texto informado é grande")
                else:
                    print("\nTexto inválido")

        elif opt == 5:

            cont = 0

            while cont <= 3:

                if cont == 3:
                    print("\nNúmero máximo de tentativas de CPF excedido")
                else:

                    cpf = input("\nDigite seu CPF: ")

                    if len(cpf) == 11 and cpf.isdigit() == True:
                        print("\nCPF válido")
                        break
                    else:
                        print("\nCPF inválido")
                cont += 1

        elif opt == 6:

            texto = input("\nDigite um texto qualquer: ")

            vogais  = texto.count("a")
            vogais += texto.count("e")
            vogais += texto.count("i")
            vogais += texto.count("o")
            vogais += texto.count("u")

            espacos = texto.count(" ")

            outros = len(texto) - vogais - espacos

            print("\nO seu texto possui:\n\n" + str(vogais) + " vogais\n\n" + str(espacos) + " espaços\n\n" + str(outros) + " outros caracteres")

        elif opt == 7:
            print("\nObrigado por utilizar nosso sistema.")
        else:
            print("\nERRO!\n\nDigite uma opção válida!")
            cont += 1