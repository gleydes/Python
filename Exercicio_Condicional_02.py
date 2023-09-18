# Solicita ao usuário um número inteiro positivo
numero = int(input("Digite um número inteiro positivo: "))

# Inicializa a variável de soma
soma = 0

# Verifica se o número é positivo
if numero <= 0:
    print("Por favor, insira um número inteiro positivo.")
else:
    # Loop para encontrar e somar os números pares
    i = 2  # Começamos em 2, o primeiro número par
    while i <= numero:
        soma += i
        i += 2  # Avançamos para o próximo número par

    # Exibe a soma dos números pares
    print(f"A soma dos números pares de 1 até {numero} é: {soma}")
