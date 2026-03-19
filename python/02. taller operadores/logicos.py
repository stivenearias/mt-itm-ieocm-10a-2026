"""
Define dos variables booleanas: tiene_entrada = True y tiene_dinero = False. Evalúa tres condiciones: 1. Si la persona puede entrar (necesita entrada y dinero). 2. Si puede entrar con un beneficio (necesita entrada o dinero). 3. El estado inverso de tener entrada usando el operador de negación.
"""

tiene_entrada = True
tiene_dinero = False

# Operador AND (Ambos deben ser True)
puede_entrar = tiene_entrada and tiene_dinero  # False

# Operador OR (Al menos uno debe ser True)
tiene_beneficio = tiene_entrada or tiene_dinero # True

# Operador NOT (Invierte el valor)
no_tiene_entrada = not tiene_entrada           # False

print(f"¿Puede entrar?: {puede_entrar}")
print(f"¿Tiene algún beneficio?: {tiene_beneficio}")
print(f"Inverso de entradamy6k: {no_tiene_entrada}")