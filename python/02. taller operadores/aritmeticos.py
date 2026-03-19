"""
Crea un script que tome dos variables, a = 15 y b = 4, y calcule todas las operaciones básicas: suma, resta, multiplicación, división real, división entera (sin decimales), el residuo de la división (módulo) y la potencia de a elevado a b.
"""

# Variables iniciales
a = 15
b = 4

# Operaciones
suma = a + b              # 19
resta = a - b             # 11
multiplicacion = a * b    # 60
division = a / b          # 3.75
division_entera = a // b  # 3
modulo = a % b            # 3
potencia = a ** b         # 50625

print(f"Suma: {suma}, Resta: {resta}, Multi: {multiplicacion}, División: {division}, Entera: {division_entera}, Módulo: {modulo}, Potencia: {potencia}")