senha = input("Digite uma senha: ")

tem_maiuscula = False

tem_minuscula = False

tem_numero = False

tem_especial = False

if len(senha) >= 8:

    for caractere in senha:

        if caractere.isupper():

            tem_maiuscula = True

        elif caractere.islower():

            tem_minuscula = True

        elif caractere.isdigit():

            tem_numero = True

        elif caractere in "!@#$%^&*":

            tem_especial = True

if tem_maiuscula and tem_minuscula and tem_numero and tem_especial:

    print("Senha válida!")

else:

    print("Senha inválida!")