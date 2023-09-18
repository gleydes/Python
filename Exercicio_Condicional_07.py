# Inicializa variáveis
soma_notas = 0
contador_notas = 0

while True:
    # Solicita ao usuário que insira uma nota ou -1 para sair
    nota = float(input("Digite uma nota (-1 para sair): "))

    # Verifica se o usuário deseja sair
    if nota == -1:
        break

    # Verifica se a nota é válida (entre 0 e 10)
    if 0 <= nota <= 10:
        soma_notas += nota
        contador_notas += 1
    else:
        print("Nota inválida. Por favor, insira uma nota entre 0 e 10.")

# Calcula a média das notas
if contador_notas > 0:
    media = soma_notas / contador_notas
    print(f"A média das {contador_notas} notas é: {media:.2f}")
else:
    print("Nenhuma nota válida foi inserida.")
