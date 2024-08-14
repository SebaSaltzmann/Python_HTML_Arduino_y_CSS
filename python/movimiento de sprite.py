import pygame
from pygame.locals import *

class Personaje:
    def __init__(self, raza, fuerza, velocidad, agilidad, sigilo, vida, x, y, nombre, sprite):
        self.raza = raza
        self.fuerza = fuerza
        self.velocidad = velocidad
        self.agilidad = agilidad
        self.sigilo = sigilo
        self.vida = vida
        self.x = x
        self.y = y
        self.espada = None
        self.nombre = nombre
        self.sprite = sprite
    
    def equipar_espada(self, espada):
        self.espada = espada

    def movimiento(self):
        menu = """ingrese a que direccion quiere ir:
            opciones :
            ####-arriba ######
            ####-abajo #######
            ####-izquierda ###
            ####-derecha ##### """
        print(menu)
        
        direccion = (input("--> "))
        
        if direccion == "arriba":
            self.y += 1
        elif direccion == "abajo":
            self.y -= 1
        elif direccion == "izquierda":
            self.x -= 1
        elif direccion == "derecha":
            self.x += 1

    def asignar_nombre(self):
        self.nombre = (input("ingrese el nombre de su espada: "))
        return self.nombre

# Función para cargar sprites
def cargar_sprites():
    sprite_personaje = pygame.image.load("sprite_0.png")  
    return sprite_personaje

# Función para dibujar personajes en la pantalla
def dibujar_personaje(personaje, pantalla):
    pantalla.blit(personaje.sprite, (personaje.x, personaje.y))

# Función principal del juego
def main():
    pygame.init()
    pantalla = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Mi Juego")

    # Cargar sprites
    sprite_personaje = cargar_sprites()

    # Crear instancia de Personaje
    jugador = Personaje("Humano", 10, 5, 7, 8, 100, 100, 100, "Jugador 1", sprite_personaje)

    # Bucle principal del juego
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                return
        
        # Dibujar personajes en la pantalla
        pantalla.fill((255, 255, 255))
        dibujar_personaje(jugador, pantalla)
        pygame.display.flip()

if __name__ == "__main__":
    main()