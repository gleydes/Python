# Solicita o preço da mercadoria e converte para um número decimal
preco_mercadoria = float(input("Digite o preço da mercadoria: R$ "))

# Solicita o percentual de desconto e converte para um número decimal
percentual_desconto = float(input("Digite o percentual de desconto: "))

# Calcula o valor do desconto
valor_desconto = (percentual_desconto / 100) * preco_mercadoria

# Calcula o preço a pagar após o desconto
preco_a_pagar = preco_mercadoria - valor_desconto

# Exibe o valor do desconto e o preço a pagar
print(f"Valor do desconto: R$ {valor_desconto:.2f}")
print(f"Preço a pagar: R$ {preco_a_pagar:.2f}")
