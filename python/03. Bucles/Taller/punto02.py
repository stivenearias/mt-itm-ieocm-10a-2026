"""
Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo como el de más abajo, de altura el número introducido.

*****
****
***
**
*
"""

numero = int(input("Ingres eun numero:"))

while 1 <= numero:
  print(f"*"*numero)
  numero -= 1