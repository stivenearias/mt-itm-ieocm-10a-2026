"""
EJERCICIO 4: Presupuesto de construcción
Una persona quiere construir un piso rectangular.
El programa debe:
1. Pedir el largo del terreno en metros.
2. Pedir el ancho del terreno en metros.
3. Pedir el precio del metro cuadrado.
4. Calcular el área total del terreno.
5. Calcular el costo total de la construcción.
6. Calcular cuánto pagaría si lo divide en 12 cuotas iguales.
7. Calcular cuánto pagaría si recibe un descuento del 10% por pago de
contado.
8. Mostrar todos los resultados.
"""

print("===== CÁLCULO DE CONSTRUCCIÓN =====")

largo = float(input("Ingrese el largo del terreno (metros): "))
ancho = float(input("Ingrese el ancho del terreno (metros): "))
precio_metro = float(input("Ingrese el precio por metro cuadrado: "))

area = largo * ancho
costo_total = area * precio_metro

cuota = costo_total / 12
descuento = costo_total * 0.10
precio_descuento = costo_total - descuento

print("\n===== RESULTADOS =====")
print("Área total:", area)
print("Costo total:", costo_total)
print("Valor de cada cuota (12 meses):", cuota)
print("Precio pagando de contado (10% descuento):", precio_descuento)