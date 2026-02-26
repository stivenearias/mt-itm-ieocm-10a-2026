"""
EJERCICIO 5: Cálculo de consumo de gasolina
Un conductor quiere calcular cuánto gastará en gasolina en un viaje.
El programa debe:
1. Pedir la distancia del viaje en kilómetros.
2. Pedir el rendimiento del vehículo (kilómetros por litro).
3. Pedir el precio del litro de gasolina.
4. Calcular cuántos litros necesita para el viaje.
5. Calcular el costo total del viaje solo de ida.
6. Calcular el costo de ida y vuelta.
7. Calcular cuánto pagaría cada persona si el costo se divide entre 4
personas.
8. Mostrar todos los resultados en pantalla.
"""

print("===== CÁLCULO DE VIAJE =====")

distancia = float(input("Ingrese la distancia del viaje (km): "))
rendimiento = float(input("Ingrese el rendimiento del vehículo (km por litro): "))
precio_litro = float(input("Ingrese el precio del litro de gasolina: "))

litros_necesarios = distancia / rendimiento
costo_ida = litros_necesarios * precio_litro

costo_ida_vuelta = costo_ida * 2
costo_por_persona = costo_ida_vuelta / 4

print("\n===== RESULTADOS =====")
print("Litros necesarios:", litros_necesarios)
print("Costo solo ida:", costo_ida)
print("Costo ida y vuelta:", costo_ida_vuelta)
print("Costo por persona (4 personas):", costo_por_persona)