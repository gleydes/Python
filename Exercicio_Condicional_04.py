# Solicita ao usuário um número inteiro positivo
numero = int(input("Digite um número inteiro positivo: "))

# Verifica se o número é positivo
if numero < 0:
    print("Por favor, insira um número inteiro positivo.")
else:
    # Inicializa o fatorial como 1
    fatorial = 1

    # Calcula o fatorial usando um loop while
    i = 1
    while i <= numero:
        fatorial *= i
        i += 1

    # Exibe o resultado
    print(f"O fatorial de {numero} é {fatorial}")
