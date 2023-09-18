import random

# Gera um número aleatório entre 1 e 100
numero_secreto = random.randint(1, 100)

# Inicializa o contador de tentativas
tentativas = 0

print("Bem-vindo ao jogo de adivinhação! Tente adivinhar o número secreto entre 1 e 100.")

while True:
    # Solicita a tentativa do jogador
    tentativa = int(input("Digite sua tentativa: "))

    # Incrementa o contador de tentativas
    tentativas += 1

    # Verifica se a tentativa está correta
    if tentativa == numero_secreto:
        print(f"Parabéns! Você acertou o número secreto {numero_secreto} em {tentativas} tentativas.")
        break
    elif tentativa < numero_secreto:
        print("Tente um número maior.")
    else:
        print("Tente um número menor.")
