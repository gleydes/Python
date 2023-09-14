import cmath

# Solicita os coeficientes da equação
a = float(input("Digite o coeficiente a: "))
b = float(input("Digite o coeficiente b: "))
c = float(input("Digite o coeficiente c: "))

# Calcula o discriminante
d = (b**2) - (4*a*c)

# Calcula as duas soluções
sol1 = (-b-cmath.sqrt(d))/(2*a)
sol2 = (-b+cmath.sqrt(d))/(2*a)

# Apresenta as soluções
print("As soluções da equação são: ", sol1, " e ", sol2)
