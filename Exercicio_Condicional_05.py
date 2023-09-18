# Inicializa a variável de soma
soma = 0

while True:
    # Solicita ao usuário que insira um número inteiro
    numero = int(input("Digite um número inteiro (0 para sair): "))

    # Verifica se o número é zero para sair do loop
    if numero == 0:
        break

    # Adiciona o número à soma
    soma += numero

# Exibe a soma dos números digitados
print(f"A soma dos números é: {soma}")
