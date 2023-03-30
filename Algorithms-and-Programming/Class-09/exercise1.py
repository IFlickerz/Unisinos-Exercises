while True:

    meses = int(input("\nDigite quantos meses serão avaliados: "))
    crescente = True
    aud_media, audiencia = 0, 0

    for i in range(1, meses+1):

        aud_ant   = audiencia
        audiencia = float(input("\nDigite a audiência do " + str(i) + "º mês: "))

        if audiencia <= aud_ant:
            crescente = False

        aud_media += audiencia

    if crescente == True:
        print("\nAudiência sempre crescente.")
    else:
        print("\nAudiência nem sempre crescente.")

    print("\nMédia de audiência: %.1f" % (aud_media / meses))

    continuar = input("\nDeseja continuar?\n")
    continuar = continuar.lower()

    if continuar == "n" or continuar == "nao" or continuar == "não":
        break
