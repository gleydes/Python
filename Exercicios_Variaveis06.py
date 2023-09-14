# Solicita ao usuário a temperatura em Fahrenheit
fahrenheit = float(input("Digite a temperatura em graus Fahrenheit: "))

# Realiza a conversão para graus Celsius
celsius = (fahrenheit - 32) * 5/9

# Exibe o resultado da conversão
print(f"A temperatura em graus Celsius é: {celsius:.2f}°C")