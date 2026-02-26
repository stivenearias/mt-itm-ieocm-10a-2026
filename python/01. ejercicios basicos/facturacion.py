"""
EJERCICIO 1: Sistema de facturación
Una tienda vende tres productos diferentes.
El programa debe:
1. Solicitar el nombre del cliente.
2. Pedir el precio y la cantidad comprada de cada uno de los 3 productos.
3. Calcular el subtotal de cada producto.
4. Calcular el total sin IVA.
5. Calcular el IVA del 19%.
6. Calcular el total final a pagar.
7. Mostrar todos los resultados organizados en pantalla.
El programa debe mostrar:
• Nombre del cliente
• Subtotal de cada producto
• Total sin IVA
• Valor del IVA
• Total final
"""

# Titulo del ejercicio
print("========= SISTEMA DE FACTURACION ==========")

# Solicitar informacion al clinete
nombre = input("Ingrese nombre del cliente: ")

producto1 = input("Ingrese el nombre del primer producto:")
precio1   = float(input("Ingrese el precio del primer producto: "))
cantidad1 = int(input("Ingrese la cantidad del primer producto: "))

producto2 = input("Ingrese el nombre del segundo producto:")
precio2   = float(input("Ingrese el precio del segundo producto: "))
cantidad2 = int(input("Ingrese la cantidad del segundo producto: "))

producto3 = input("Ingrese el nombre del tercer producto:")
precio3   = float(input("Ingrese el precio del tercer producto: "))
cantidad3 = int(input("Ingrese la cantidad del tercer producto: "))

# Calcular el subtotal de cada producto
subtotal1 = precio1 * cantidad1
subtotal2 = precio2 * cantidad2
subtotal3 = precio3 * cantidad3

# Calcular el total sin IVA
total_sin_iva = subtotal1 + subtotal2 + subtotal3

# Calcular el IVA del 19%
iva = total_sin_iva * 0.19

# Calcular el total final a pagar
total_final = total_sin_iva + iva

# Mostrar resultados organizados en pantalla
print("\n========= FACTURA ==========")
print(f"Nombre del cliente {nombre}")
print(f"Subtotal del producto {producto1}: {subtotal1}")
print(f"Subtotal del producto {producto2}: {subtotal2}")
print(f"Subtotal del producto {producto3}: {subtotal3}")
print(f"Total sin IVA: {total_sin_iva}")
print(f"Valor del IVA: {iva}")
print(f"Total final: {total_final}")