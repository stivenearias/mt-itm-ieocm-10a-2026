"""
Una pequeña librería local desea digitalizar su proceso de ventas. Debes escribir un programa que ayude a registrar las ventas del día. El programa debe funcionar de la siguiente manera:

Primero, solicitar al usuario la cantidad inicial de libros disponibles en el inventario.

Luego, mediante un bucle, el programa debe preguntar cuántos libros desea comprar el cliente.

Condiciones:

Si la cantidad solicitada es menor o igual a la disponible, se realiza la venta y se resta del inventario.

Si la cantidad solicitada es mayor a la disponible, el programa debe mostrar un mensaje de error indicando que no hay suficiente stock.

El proceso debe repetirse hasta que el inventario llegue a 0.

Al finalizar, mostrar un mensaje informando que el inventario se ha agotado.
"""

stock = int(input("Ingrese la cantidad inicial de libros en inventario: "))

while stock > 0:
    pedido = int(input(f"Inventario actual: {stock}. ¿Cuántos libros desea comprar?: "))
    
    if pedido <= stock:
        stock -= pedido
        print(f"Venta exitosa. Libros restantes: {stock}")
    else:
        print(f"Error: No hay suficiente stock. Solo quedan {stock} unidades.")

print("El inventario se ha agotado. Fin de la jornada.")