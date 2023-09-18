import random

# Gera um número aleatório entre 1 e 100
numero_secreto = random.randint(1, 100)

# Define o número máximo de tentativas
tentativas_maximas = 10
tentativas = 0

print("Bem-vindo ao jogo de adivinhação! Você tem 10 tentativas para adivinhar o número secreto entre 1 e 100.")

while tentativas < tentativas_maximas:
    # Solicita a tentativa do jogador
    tentativa = int(input("Digite sua tentativa: "))

    # Incrementa o número de tentativas
    tentativas += 1

    # Verifica se a tentativa está correta
    if tentativa == numero_secreto:
        print(f"Parabéns! Você acertou o número secreto {numero_secreto} em {tentativas} tentativas.")
        break
    elif tentativa < numero_secreto:
        print("Tente um número maior.")
    else:
        print("Tente um número menor.")
else:
    print(f"Fim das tentativas. O número secreto era {numero_secreto}.")
