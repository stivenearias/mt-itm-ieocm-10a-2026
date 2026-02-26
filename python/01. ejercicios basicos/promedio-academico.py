"""
EJERCICIO 3: Promedio académico ponderado
Un estudiante tiene las siguientes evaluaciones:
• Parcial 1 (30%)
• Parcial 2 (30%)
• Parcial 3 (30%)
• Proyecto final (10%)
El programa debe:
1. Solicitar el nombre del estudiante.
2. Pedir las 4 notas.
3. Calcular el promedio ponderado final.
4. Calcular cuántos puntos le faltan para obtener 5.0.
5. Calcular cuánto representa cada nota en el promedio final (en valor
numérico).
6. Mostrar todos los resultados en pantalla de forma organizada.
"""

print("===== CÁLCULO DE PROMEDIO =====")

nombre = input("Ingrese el nombre del estudiante: ")

nota1 = float(input("Ingrese nota del parcial 1: "))
nota2 = float(input("Ingrese nota del parcial 2: "))
nota3 = float(input("Ingrese nota del parcial 3: "))
nota_proyecto = float(input("Ingrese nota del proyecto final: "))

promedio = (nota1 * 0.3) + (nota2 * 0.3) + (nota3 * 0.3) + (nota_proyecto * 0.1)

faltante = 5.0 - promedio

print("\n===== RESULTADOS =====")
print("Estudiante:", nombre)
print("Promedio final:", promedio)
print("Puntos faltantes para 5.0:", faltante)