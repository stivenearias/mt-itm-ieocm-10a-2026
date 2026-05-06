"""
Crear un programa que permita a un docente registrar las calificaciones de varias materias para un estudiante. El programa debe ser flexible, permitiendo ingresar cualquier cantidad de materias y, para cada materia, cualquier cantidad de notas.

Requerimientos:

1. Entrada de Materias: Solicitar al usuario cuántas materias desea registrar.
2. Entrada de Notas: Por cada materia, preguntar cuántas notas se van a promediar.
3. Cálculo: Utilizar un bucle while para solicitar cada nota, validando que se sumen correctamente.
4. Lógica de Desempeño: Una vez obtenido el promedio de la materia, el sistema debe determinar el nivel de desempeño según la siguiente escala:
Bajo: Menor a 3.5
Medio: Entre 3.6 y 4.0
Alto: Entre 4.1 y 4.5
Superior: Entre 4.6 y 5.0
5. Salida: Mostrar el nombre de la materia, su promedio final y el desempeño obtenido.
"""


# Sistema de Gestión de Notas Académicas
print("--- BIENVENIDO AL SISTEMA DE CALIFICACIONES ---")

# 1. Entrada de datos inicial
cantidad_materias = int(input("¿Cuántas materias desea registrar? "))
contador_materias = 0

# Bucle principal para las materias
while contador_materias < cantidad_materias:
    print(f"\n--- Configuración de la Materia {contador_materias + 1} ---")
    nombre_materia = input("Nombre de la materia: ")
    num_notas = int(input(f"¿Cuántas notas ingresará para {nombre_materia}? "))
    
    # Variables de control para las notas
    suma_notas = 0
    contador_notas = 0
    
    # 2. Bucle anidado para las notas de la materia actual
    while contador_notas < num_notas:
        nota = float(input(f"  Ingrese la nota {contador_notas + 1}: "))
        suma_notas += nota
        contador_notas += 1
    
    # 3. Cálculo del promedio
    promedio = suma_notas / num_notas
    
    # 4. Estructura condicional para determinar el desempeño
    if promedio < 3.5:
        desempeno = "BAJO"
    elif 3.6 <= promedio <= 4.0:
        desempeno = "MEDIO"
    elif 4.1 <= promedio <= 4.5:
        desempeno = "ALTO"
    else: # De 4.6 a 5.0
        desempeno = "SUPERIOR"
    
    # 5. Salida de resultados por materia
    print(f"\nRESULTADO PARA {nombre_materia.upper()}:")
    print(f"Promedio final: {promedio:.2f}")
    print(f"Nivel de desempeño: {desempeno}")
    
    contador_materias += 1

print("\n--- Proceso finalizado con éxito ---")
