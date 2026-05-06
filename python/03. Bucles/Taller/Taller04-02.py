print("--- SISTEMA DE CALIFICACIONES FINAL ---")

cantidad_materias = int(input("¿Cuántas materias desea registrar? "))
contador_materias = 0

# Creamos una lista vacía para guardar los resultados de cada materia
reporte_final = []

while contador_materias < cantidad_materias:
    print(f"\n--- Datos de la Materia {contador_materias + 1} ---")
    nombre_materia = input("Nombre de la materia: ")
    num_notas = int(input(f"¿Cuántas notas ingresará para {nombre_materia}? "))
    
    suma_notas = 0
    contador_notas = 0
    
    while contador_notas < num_notas:
        nota = float(input(f"  Ingrese la nota {contador_notas + 1}: "))
        suma_notas += nota
        contador_notas += 1
    
    promedio = suma_notas / num_notas
    
    # Determinamos el desempeño
    if promedio < 3.5:
        desempeno = "BAJO"
    elif 3.6 <= promedio <= 4.0:
        desempeno = "MEDIO"
    elif 4.1 <= promedio <= 4.5:
        desempeno = "ALTO"
    else:
        desempeno = "SUPERIOR"
    
    # En lugar de hacer print() aquí, guardamos el texto en nuestra lista
    resultado = f"Materia: {nombre_materia:15} | Promedio: {promedio:.2f} | Desempeño: {desempeno}"
    reporte_final.append(resultado)
    
    contador_materias += 1

# --- SALIDA FINAL FUERA DE LOS BUCLES ---
print("\n" + "="*50)
print("             BOLETÍN DE CALIFICACIONES")
print("="*50)

# Recorremos la lista para mostrar todos los resultados guardados
for linea in reporte_final:
    print(linea)

print("="*50)