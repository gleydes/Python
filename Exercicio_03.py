numero = int(input("Digite um número: "))

if numero % 3 == 0 and numero % 5 == 0:
    print("O número é múltiplo de 3 e de 5.")
elif numero % 3 == 0:
    print("O número é múltiplo de 3, mas não de 5.")
elif numero % 5 == 0:
    print("O número é múltiplo de 5, mas não de 3.")
else:
    print("O número não é múltiplo de 3 nem de 5.")