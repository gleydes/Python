# Distância em metros
distancia_metros = 5

# Converter a distância para quilômetros
distancia_quilometros = distancia_metros / 1000  # 1 metro = 0,001 quilômetros

# Velocidade em quilômetros por hora
velocidade_kmph = 10

# Calcular o tempo em horas
tempo_horas = distancia_quilometros / velocidade_kmph

# Exibir a resposta ao usuário
print(f"Para percorrer uma distância de {distancia_metros} metros a uma velocidade de {velocidade_kmph} km/h, levará {tempo_horas:.2f} horas.")
