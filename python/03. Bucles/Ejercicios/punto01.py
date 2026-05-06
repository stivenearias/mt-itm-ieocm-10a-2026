"""
Escribir un programa que pida al usuario una palabra y la muestre por pantalla 10 veces.
"""

cont = 0
palabra = input("Ingrese una palabra:")

while cont < 10:
  cont += 1
  print(f"{cont}: {palabra}")