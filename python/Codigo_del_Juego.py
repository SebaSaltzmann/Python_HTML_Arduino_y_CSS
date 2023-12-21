import random
import tkinter as tk
#random.randint()
class Espada:
    def __init__(self, daño, nombre, x, y):
        self.daño = daño
        self.x = x
        self.y = y
        self.nombre = nombre

    def mover_arriba(self):
        self.y += 1

    def mover_abajo(self):
        self.y -= 1

    def mover_izquierda(self):
        self.x -= 1

    def mover_derecha(self):
        self.x += 1

    def asignar_nombre(self):
        self.nombre = (input("ingrese el nombre de su espada: "))
        return self.nombre

class Personaje:
    def __init__(self, raza, fuerza, velocidad, agilidad, sigilo, vida, x, y):
        self.raza = raza
        self.fuerza = fuerza
        self.velocidad = velocidad
        self.agilidad = agilidad
        self.sigilo = sigilo
        self.vida = vida
        self.x = x
        self.y = y
        self.espada = None
    
    def equipar_espada(self, espada):
        self.espada = espada

    def movimiento(self, direccion):
        direccion = (input("ingrese a que direccion quiere ir: "))
        print(""" opciones :
        -arriba
        -abajo
        -izquierda
        -derecha """)

        if direccion == "arriba":
            self.y += self.velocidad
        elif direccion == "abajo":
            self.y -= self.velocidad
        elif direccion == "izquierda":
            self.x -= self.velocidad
        elif direccion == "derecha":
            self.x += self.velocidad
    

"""ventana = tk.Tk()

ventana.title("Ejemplo de botón")

boton = tk.Button(ventana, text="Presionar el botón", command=)
boton.pack()

ventana.mainloop()"""


class Dragon:
    def __init__(self, raza, fuerza, velocidad, agilidad, sigilo, vida, x, y):
        self.raza = raza
        self.fuerza = fuerza
        self.velocidad = velocidad
        self.agilidad = agilidad
        self.sigilo = sigilo
        self.vida = vida
        self.x = x
        self.y = y
    
    def mover_arriba(self):
        self.y += 1

    def mover_abajo(self):
        self.y -= 1

    def mover_izquierda(self):
        self.x -= 1

    def mover_derecha(self):
        self.x += 1

    def atacar(self, objetivo):
        danio_total = self.fuerza
        objetivo.vida -= danio_total
        print(f"{self.raza} atacó a {objetivo.raza} con un daño de {danio_total}")


# Crear objetos
Elfo = Personaje("Elfo", 150, 200, 800, 400, 800, 2, 2)
Dragon1 = Dragon("Dragon", 300, 200, 100, 100, 1000, 5, 5)
Excalibur = Espada(500, "nombre", 2, 2)



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
    print(f"{Dragon1.raza} tiene {Dragon1.vida} puntos de vida restantes.")
