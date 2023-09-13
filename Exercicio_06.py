data = input("Digite uma data no formato dd/mm/aaaa: ")

dia, mes, ano = data.split("/")

valida = True

if int(ano) < 1:

    valida = False

elif int(mes) < 1 or int(mes) > 12:

    valida = False

elif int(dia) < 1 or int(dia) > 31:

    valida = False

elif (int(mes) == 4 or int(mes) == 6 or int(mes) == 9 or int(mes) == 11) and int(dia) > 30:

    valida = False

elif int(mes) == 2:

    if (int(ano) % 4 == 0 and int(ano) % 100 != 0) or (int(ano) % 400 == 0):

        if int(dia) > 29:
            valida = False

    elif int(dia) > 28:

        valida = False

if valida:

    print("A data é válida!")

else:

    print("A data é inválida!")

