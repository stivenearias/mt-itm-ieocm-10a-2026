"""
Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de años, y muestre por pantalla el capital obtenido en la inversión cada año que dura la inversión.
"""

# Solicitar datos al usuario
inversion = float(input("¿Cantidad a invertir?: "))
interes_anual = float(input("¿Interés porcentual anual?: "))
años = int(input("¿Número de años?: "))

# Inicializamos el contador de años
año_actual = 1

print("\n--- Proyección de Capital ---")

# El ciclo se ejecutará hasta llegar al número de años indicado
while año_actual <= años:
    # Calculamos el capital del año actual
    # Fórmula: inversion = inversion * (1 + (interes / 100))
    inversion *= (1 + interes_anual / 100)
    
    # Mostramos el resultado formateado a 2 decimales
    print(f"Año {año_actual}: {inversion:.2f}")
    
    # Incrementamos el contador para evitar un bucle infinito
    año_actual += 1