from Clase_Enemigo import Enemigo
import pygame
class Personaje:
    def __init__(self,raza,fuerza,velocidad,agilidad,sigilo,vida,x,y,nombre,sprite):
        super(Enemigo).__init__(raza,fuerza,velocidad,agilidad,sigilo,vida,x,y,nombre,sprite)
        self.objeto = None
    
    def equipar_espada(self, espada):
        self.espada = espada

    def movimiento(self):
        successes, failures = pygame.init()
        print("{0} successes and {1} failures".format(successes, failures))
        screen = pygame.display.set_mode((720, 480))
        clock = pygame.time.Clock()
        FPS = 60
        BLACK = (0, 0, 0)
        WHITE = (255, 255, 255)

        sprite = pygame.image()
        fondo = pygame.Surface((32, 32))
        fondo.fill(WHITE)
        while True:
            clock.tick(FPS)
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_w:
                        sprite.move_ip(0, -2)
                    elif event.key == pygame.K_s:
                        sprite.move_ip(0, 2)
                    elif event.key == pygame.K_a:
                        sprite.move_ip(-2, 0)
                    elif event.key == pygame.K_d:
                        sprite.move_ip(2, 0)
            screen.fill(BLACK)
            screen.blit(fondo, sprite)
            pygame.display.update() 


    def asignar_nombre(self):
        self.nombre = (input("ingrese el nombre de su espada: "))
        return self.nombre