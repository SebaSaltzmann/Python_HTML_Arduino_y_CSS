import numpy as np


n = int(input("Ingrese el número de ciudades: "))

array = np.zeros(n)

for i in range(n):
    array[i] = float(input(f"Ingrese el valor para la ciudad {i+1}: "))
    
    print(f"Índice: {i}")
    print(f"Array actualizado: {array}")

print(f"Array final: {array}")
