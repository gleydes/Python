# Solicita ao usuário o número de termos da sequência de Fibonacci a serem impressos
n = int(input("Digite o número de termos da sequência de Fibonacci a serem impressos: "))

# Inicializa os primeiros dois termos da sequência de Fibonacci
termo1, termo2 = 0, 1

# Inicializa um contador para acompanhar quantos termos já foram impressos
contador = 0

# Loop para imprimir os primeiros "n" termos da sequência de Fibonacci
while contador < n:
    print(termo1, end=" ")
    termo_novo = termo1 + termo2
    termo1, termo2 = termo2, termo_novo
    contador += 1

print()  # Pula para a próxima linha após imprimir a sequência
