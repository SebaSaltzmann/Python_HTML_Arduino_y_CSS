import random

llaves = {
    "llave_1": True, 
    "llave_2": True,  
    "llave_3": False  
}


print("Bienvenido al puzzle del cofre con las 3 llaves.")
print("Tienes tres llaves: llave_1, llave_2 y llave_3.")
print("Dos de las llaves son correctas, pero una siempre miente.")
print("Para abrir el cofre, necesitas usar las dos llaves correctas.")
print("¡Buena suerte!\n")

def intentar_abrir(llave_a, llave_b):
    if llaves[llave_a] and llaves[llave_b]:
        print(f"¡Correcto! Has abierto el cofre con {llave_a} y {llave_b}.")
        return True
    else:
        print(f"Lo siento, la combinación {llave_a} y {llave_b} no funciona.")
        return False

cofre_abierto = False
intentos = 0
while not cofre_abierto:
    intentos += 1
    llave_a = input("Elige la primera llave (llave_1, llave_2, llave_3): ")
    llave_b = input("Elige la segunda llave (llave_1, llave_2, llave_3): ")
    
    if llave_a == llave_b:
        print("No puedes elegir la misma llave dos veces. Intenta de nuevo.")
        continue

    cofre_abierto = intentar_abrir(llave_a, llave_b)

print(f"¡Has abierto el cofre en {intentos} intentos!")
