#mi código
import random

rangoF = 10
rango1 = 1
rango2 = 100
i = 0



numeroAleatorio = random.randint(rango1, rango2)

texto = """ En este programa tendras que adiviniar un numero
 del 1 al 100 con pistas de mayor o menor valor, tienes 10 intentos.

 """
print(texto)

for i in range(rangoF):

    print(f"intento {i+1}")   
    adivinador = int(input("ingresa un número: ")) 

    if adivinador < numeroAleatorio:
        print("Mas alto, intenta de nuevo.")
    elif adivinador > numeroAleatorio:
        print("Muy alto, intenta de nuevo.")
    else:
        print("¡Correcto! ¡Felicidades, has adivinado el número!")
        break
else:
    print(f"Lo siento, no adivinaste el número. Era {numeroAleatorio}.")

#Mejoras de ChatGPT
"""
import random

# Parámetros del juego
rango_intentos = 10
rango_min = 1
rango_max = 100

# Generar número aleatorio
numero_aleatorio = random.randint(rango_min, rango_max)

# Instrucciones
print(f"
¡Bienvenido al juego "Adivina el Número"!
He pensado un número entre {rango_min} y {rango_max}.
Tienes {rango_intentos} intentos para adivinarlo.
¡Buena suerte!")

# Bucle principal
for intento in range(rango_intentos):
    print(f"Intento {intento + 1} de {rango_intentos}")
    
    # Validación de entrada
    try:
        adivinador = int(input("Ingresa un número: "))
        if adivinador < rango_min or adivinador > rango_max:
            print(f"Por favor, ingresa un número entre {rango_min} y {rango_max}.")
            continue
    except ValueError:
        print("Entrada inválida. Ingresa un número válido.")
        continue

    # Comprobar el número
    if adivinador < numero_aleatorio:
        print("Más alto, intenta de nuevo.")
    elif adivinador > numero_aleatorio:
        print("Muy alto, intenta de nuevo.")
    else:
        print("¡Correcto! ¡Felicidades, has adivinado el número!")
        break
else:
    print(f"Lo siento, no adivinaste el número. Era {numero_aleatorio}.")

"""