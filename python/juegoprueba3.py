import random
import tkinter as tk
#random.randint()
class Espada:
    def __init__(self, daño, nombre, x, y):
        self.daño = daño
        self.x = x
        self.y = y
        self.nombre = (input("ingrese el nombre de su personaje"))

    def mover_arriba(self):
        self.y += 1

    def mover_abajo(self):
        self.y -= 1

    def mover_izquierda(self):
        self.x -= 1

    def mover_derecha(self):
        self.x += 1

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

    def atacar(self, objetivo):
        if self.espada is not None:
            danio_total = self.fuerza + self.espada.daño
            objetivo.vida -= danio_total
            print(f"{self.raza} atacó a {objetivo.raza} con un daño de {danio_total}")
        else:
            print("No tienes una espada equipada.")

    
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
    
    def movimiento(self, direccion):
        if direccion == "arriba":
            self.y += self.velocidad
        elif direccion == "abajo":
            self.y -= self.velocidad
        elif direccion == "izquierda":
            self.x -= self.velocidad
        elif direccion == "derecha":
            self.x += self.velocidad

    def atacar(self, objetivo):
        danio_total = self.fuerza
        objetivo.vida -= danio_total
        print(f"{self.raza} atacó a {objetivo.raza} con un daño de {danio_total}")

# Crear objetos
Elfo = Personaje("Elfo", 150, 200, 800, 400, 800, 0, 0)
obj2 = Dragon("Dragon", 300, 200, 100, 100, 1000, 5, 5)
Espada1 = Espada(500, 2, 2)



# Verificar colisión entre el personaje y la espada
if Elfo.x == Espada1.x and Elfo.y == Espada1.y:
    print("¡Colisión! El personaje ha recogido la espada.")
    Elfo.equipar_espada(Espada1)
    

# Realizar un ataque del personaje al dragón
if Elfo.espada is not None:
    Elfo.atacar(obj2)
    print(f"{obj2.raza} tiene {obj2.vida} puntos de vida restantes.")
