"""
EJERCICIO 2: Cálculo de salario mensual
Un empleado desea conocer cuánto recibirá de salario este mes.
El programa debe:
1. Pedir el nombre del empleado.
2. Pedir el salario básico mensual.
3. Pedir la cantidad de horas extras trabajadas.
4. Cada hora extra vale $20.000.
5. Calcular el pago total por horas extras.
6. Calcular el total ganado.
7. Calcular el descuento de salud (4%).
8. Calcular el descuento de pensión (4%).
9. Calcular el salario final después de descuentos.
10. Mostrar todos los resultados en pantalla.
"""

print("===== CÁLCULO DE SALARIO =====")

nombre = input("Ingrese el nombre del empleado: ")
salario_base = float(input("Ingrese el salario base mensual: "))
horas_extras = int(input("Ingrese la cantidad de horas extras trabajadas: "))

valor_hora_extra = 20000

pago_horas_extras = horas_extras * valor_hora_extra
total_ganado = salario_base + pago_horas_extras

descuento_salud = total_ganado * 0.04
descuento_pension = total_ganado * 0.04

salario_final = total_ganado - descuento_salud - descuento_pension

print("\n===== DESPRENDIBLE DE PAGO =====")
print("Empleado:", nombre)
print("Pago por horas extras:", pago_horas_extras)
print("Total ganado:", total_ganado)
print("Descuento salud:", descuento_salud)
print("Descuento pensión:", descuento_pension)
print("Salario final:", salario_final)