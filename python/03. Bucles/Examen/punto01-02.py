"""
Una empresa de tecnología tiene varias sucursales y desea calcular el valor total de la mercancía que tiene en cada una. El programa debe permitir procesar varias sucursales y, dentro de cada una, registrar diferentes tipos de productos con sus respectivos precios.

Requerimientos:
1. Registro de Sucursales: Solicitar al usuario cuántas sucursales desea auditar.
2. Registro de Productos: Por cada sucursal, preguntar cuántos productos distintos se van a registrar.
3. Cálculo de Valor: Solicitar el precio de cada producto y sumarlos para obtener el valor total de la sucursal.
4. Lógica de Clasificación (Condicionales): Según el valor total acumulado en la sucursal, el sistema debe imprimir una categoría de "Importancia de Inventario":
Básico: Menor a $1,000,000.
Intermedio: Entre $1,000,000 y $3,000,000.
Premium: Entre $3,000,001 y $5,000,000.
Crítico: Mayor a $5,000,000.
5. Salida Inmediata: Al terminar cada sucursal, se debe mostrar el nombre de la sucursal, el total de su inventario y su categoría antes de pasar a la siguiente.
6. Dentro del bucle de productos, si el usuario ingresa un precio negativo (menor a 0), el programa debe mostrar un mensaje de advertencia y solicitar de nuevo el precio de ese mismo producto. El contador de productos no debe aumentar hasta que el precio sea válido.
"""
# Sistema de Auditoría de Inventarios con Validación de Datos

print("--- AUDITORÍA DE INVENTARIO TECNO-STORE ---")

cant_sucursales = int(input("¿Cuántas sucursales va a auditar?: "))
i = 0

# Bucle Principal: Sucursales
while i < cant_sucursales:
    print(f"\n--- Datos de la Sucursal #{i + 1} ---")
    nombre_sucursal = input("Nombre de la sucursal: ")
    cant_productos = int(input(f"¿Cuántos productos registrará en {nombre_sucursal}?: "))
    
    total_inventario = 0
    j = 0
    
    # Bucle Anidado: Productos por sucursal
    while j < cant_productos:
        precio = float(input(f"  Ingrese el precio del producto {j + 1}: "))
        
        # ITEM AGREGADO: Validación de precio positivo
        if precio >= 0:
            total_inventario += precio
            j += 1 # Solo avanzamos al siguiente producto si el precio es válido
        else:
            print("  [ERROR]: El precio no puede ser negativo. Intente de nuevo.")
            # No aumentamos 'j', por lo que el bucle repetirá el mismo producto
    
    # Clasificación mediante condicionales
    if total_inventario < 1000000:
        categoria = "BÁSICO"
    elif 1000000 <= total_inventario <= 3000000:
        categoria = "INTERMEDIO"
    elif 3000001 <= total_inventario <= 5000000:
        categoria = "PREMIUM"
    else:
        categoria = "CRÍTICO"
    
    # Salida inmediata
    print(f"\n>>> REPORTE DE {nombre_sucursal.upper()} <<<")
    print(f"Total Inventario: ${total_inventario:,.2f}")
    print(f"Categoría de Importancia: {categoria}")
    print("-" * 30)
    
    i += 1

print("\nAuditoría finalizada.")