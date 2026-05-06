"""
Recibir 2 numeros. Crear una tabla de multiplicar donde el numero 1 indica el numero de la tabla y el numero 2 indica hasta que numero se hace la multiplicacion
"""

num1 = int(input("Ingrese el numero d ela tabla de multiplicar que desea:"))
num2 = int(input("Ingrese hasta que numero desea la tabal de:"))
cont = 1

while num2 >= cont:
  print(f"{num1} x {cont} = {num1*cont}")
  cont += 1