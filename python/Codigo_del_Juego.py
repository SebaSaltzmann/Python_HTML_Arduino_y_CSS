from Clase_Personaje import Personaje
from Clase_Espada import Espada
from Clase_Dragon import Dragon
import random
import tkinter as tk

# Crear objetos
Elfo = Personaje("Elfo", 150, 200, 800, 400, 800, 0, 0, "nombre")
Dragon1 = Dragon("Dragon", 300, 200, 100, 100, 1000, 5, 5, "Smaug")
Excalibur = Espada(500, "nombre", 0, 1)

# Comienzo
if Elfo.x == Elfo.x and Elfo.y == Elfo.y:
    print(f"###Actualmente estas en la cordenada x{Elfo.x}-y{Elfo.y}###")
    print("**En la coordenada x0-y1 esta excalibur** **en la coordenada x1-y0 hay una trampa**")
    
    Elfo.movimiento()
    print(f"Actualmente estas en la coordenada x{Elfo.x}-y{Elfo.y}")

# Verificar colisión entre el personaje y la espada
if Elfo.x == Excalibur.x and Elfo.y == Excalibur.y:
    print("¡Colisión! El personaje ha recogido la espada.")
    Elfo.equipar_espada(Excalibur)
    Excalibur.asignar_nombre()

# Ataque de Elfo
def ataque_personaje():
    if Excalibur is not None:
        danio_total = Elfo.fuerza + Excalibur.daño
        Dragon1.vida -= danio_total
        print(f"{Elfo.raza} atacó a {Dragon1.raza} con un daño de {danio_total}")
    else:
        print("No tienes una espada equipada.")


# Realizar un ataque del personaje al dragón
if Elfo.espada is not None:
    ataque_personaje()
    print(f"El Dragon {Dragon1.nombre} tiene {Dragon1.vida} puntos de vida restantes.")

# trampa
if Elfo.x == 1 and Elfo.y == 0:
    Elfo.vida = 0

if Elfo.vida == 0:
    print("Has caido en una trama, tu personaje esta **muerto**(x_x)")

