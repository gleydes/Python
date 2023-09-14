# Definindo os salários base, descontos e acréscimos para cada cargo
salario_base_ADW = 4500.00
descontos_ADW = 7
acrescimo_ADW = 5

salario_base_AS = 3200.00
descontos_AS = 7
acrescimo_AS = 4

salario_base_GTI = 12299.00
descontos_GTI = 7
acrescimo_GTI = 10

# Calculando o salário líquido para cada cargo
salario_liquido_ADW = (salario_base_ADW + (salario_base_ADW * acrescimo_ADW / 100)) - (salario_base_ADW * descontos_ADW / 100)
salario_liquido_AS = (salario_base_AS + (salario_base_AS * acrescimo_AS / 100)) - (salario_base_AS * descontos_AS / 100)
salario_liquido_GTI = (salario_base_GTI + (salario_base_GTI * acrescimo_GTI / 100)) - (salario_base_GTI * descontos_GTI / 100)

# Imprimindo o salário líquido para cada cargo
print("O salário líquido do Analista Desenvolvedor Web é R$ %.2f" % salario_liquido_ADW)
print("O salário líquido do Analista de Suporte é R$ %.2f" % salario_liquido_AS)
print("O salário líquido do Gerente de TI é R$ %.2f" % salario_liquido_GTI)