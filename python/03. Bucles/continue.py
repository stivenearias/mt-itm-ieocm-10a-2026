contador = 0

while contador < 10:
  contador += 1
  if contador % 2 == 0:
    continue  # Salta las iteraciones donde contador es par
  print(f"Contador impar: {contador}")