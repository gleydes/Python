# Define as constantes
PI = 3.14159

# Calcula a área do círculo
raio_circulo = 6.8
area_circulo = PI * raio_circulo**2

# Calcula a área do quadrado
lado_quadrado = 89
area_quadrado = lado_quadrado**2

# Calcula a área do triângulo
base_triangulo = 58
altura_triangulo = 34
area_triangulo = (base_triangulo * altura_triangulo) / 2

# Calcula a área do cilindro
raio_cilindro = 4.2
altura_cilindro = 17
area_cilindro = 2 * PI * raio_cilindro * (raio_cilindro + altura_cilindro)

# Calcula a área da esfera
raio_esfera = 12.35
area_esfera = 4 * PI * raio_esfera**2

# Apresenta os resultados
print("A área do círculo é: {:.2f}".format(area_circulo))
print("A área do quadrado é: {:.2f}".format(area_quadrado))
print("A área do triângulo é: {:.2f}".format(area_triangulo))
print("A área do cilindro é: {:.2f}".format(area_cilindro))
print("A área da esfera é: {:.2f}".format(area_esfera))