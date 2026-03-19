"""
Determina si un número x = 10 cumple con las siguientes condiciones comparándolo contra un número y = 20. Debes comprobar si: son iguales, son diferentes, si x es mayor que y, si es menor, si es mayor o igual, y si es menor o igual. El resultado debe ser un valor Booleano (True o False).
"""

x = 10
y = 20

# Comparaciones
es_igual = (x == y)          # False
es_diferente = (x != y)      # True
mayor_que = (x > y)          # False
menor_que = (x < y)          # True
mayor_o_igual = (x >= y)     # False
menor_o_igual = (x <= y)     # True

print(f"Iguales?: {es_igual}, ¿Diferentes?: {es_diferente}")
print(f"Mayor?: {mayor_que}, Menor? {menor_que}")
print(f"Mayor o igual? {mayor_o_igual}, Menor o igual? {menor_o_igual}")