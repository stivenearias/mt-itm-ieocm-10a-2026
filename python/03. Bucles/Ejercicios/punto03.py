"""
Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla todos los números impares desde 1 hasta ese número.
"""

numero = int(input("Ingrese un numero: "))
contador = 0

while contador < numero:
  contador += 1
  if contador % 2 == 0:
    continue
  print(contador)
