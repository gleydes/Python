# Solicita ao usuário o valor em metros
valor_metro = float(input("Digite o valor em metros (m): "))

# Calcula os múltiplos e submúltiplos
centimetros = valor_metro * 100  # 1 metro = 100 centímetros
milimetros = valor_metro * 1000  # 1 metro = 1000 milímetros

# Exibe os resultados
print(f"{valor_metro} metros é igual a:")
print(f"{centimetros:.2f} centímetros")
print(f"{milimetros:.2f} milímetros")
