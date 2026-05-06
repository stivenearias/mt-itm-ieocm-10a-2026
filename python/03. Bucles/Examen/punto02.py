"""
Un profesor necesita procesar las notas finales de sus alumnos. Escribe un programa que pida calificaciones una por una (en una escala de 0 a 10) y se detenga solo cuando el profesor ingrese un número negativo.

Al terminar el ingreso (cuando se ponga el número negativo), el programa debe mostrar:

La cantidad total de alumnos aprobados (nota mayor o igual a 3,5).

La cantidad total de alumnos reprobados (nota menor a 3,5).

Un mensaje especial si todos los alumnos registrados aprobaron (es decir, si la cuenta de reprobados es 0 y se ingresó al menos una nota).
"""

aprobados = 0
reprobados = 0
nota = 0

print("Ingrese las notas. Ingrese un número negativo para finalizar.")

while nota >= 0:
    nota = float(input("Ingrese la nota del alumno: "))
    
    if nota >= 0: # Para no contar el número negativo del final
        if nota >= 3.5:
            aprobados += 1
        else:
            reprobados += 1

print(f"\nResultados finales:")
print(f"Alumnos aprobados: {aprobados}")
print(f"Alumnos reprobados: {reprobados}")

if reprobados == 0 and aprobados > 0:
    print("¡Felicidades! Todo el grupo aprobó.")
