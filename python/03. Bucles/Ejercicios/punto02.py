"""
Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los años que ha cumplido (desde 1 hasta su edad).
"""

contador = 1
edad = int(input("Ingrese la edad:"))

while contador <= edad:
  print(contador)
  contador += 1
