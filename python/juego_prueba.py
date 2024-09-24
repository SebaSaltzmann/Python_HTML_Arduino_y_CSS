import pygame
import random

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Juego de Aventura")

# Colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
CYAN = (0, 255, 255)
YELLOW = (255, 255, 0)

# Clase personaje
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        self.health = 100
        self.mana = 100
        self.attack_power = 10
        self.defense_power = 5
        self.magic_power = 20
        self.defending = False
        self.attacking = False
        self.attack_timer = 0

    def update(self, enemies, projectiles):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= 5
        if keys[pygame.K_RIGHT]:
            self.rect.x += 5
        if keys[pygame.K_UP]:
            self.rect.y -= 5
        if keys[pygame.K_DOWN]:
            self.rect.y += 5

        #colisiones
        collided_enemies = pygame.sprite.spritecollide(self, enemies, False)
        for enemy in collided_enemies:
            if self.defending:
                self.health -= 0.5  # Reduce la salud del jugador menos cuando está defendiendo
            else:
                self.health -= 1  # Reduce la salud del jugador por cada colisión
            if self.health <= 0:
                print("Game Over")
                pygame.quit()
                quit()

        if self.attacking:
            self.attack_timer -= 1
            if self.attack_timer <= 0:
                self.attacking = False

    def attack(self):
        if not self.attacking:
            self.attacking = True
            self.attack_timer = 10  # Duración del ataque en cuadros
            print("Ataque físico!")

    def defend(self):
        self.defending = True

    def magic_attack(self, projectiles):
        if self.mana >= 10:  # Verifica si el jugador tiene suficiente maná
            print("Ataque mágico!")
            projectile = Projectile(self.rect.centerx, self.rect.top)
            projectiles.add(projectile)
            self.mana -= 10  # Reduce el maná

    def stop_defending(self):
        self.defending = False

    def draw_health_bar(self, surface):
        pygame.draw.rect(surface, RED, (10, 10, self.health * 2, 20))

    def draw_mana_bar(self, surface):
        pygame.draw.rect(surface, CYAN, (10, 40, self.mana * 2, 20))  # Dibuja la barra de maná

    def draw_attack(self, surface):
        if self.attacking:
            attack_rect = pygame.Rect(self.rect.right, self.rect.centery - 10, 20, 20)  # Posición y tamaño del "puño"
            pygame.draw.rect(surface, YELLOW, attack_rect)
            return attack_rect
        return None

# Clase para los proyectiles mágicos
class Projectile(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((10, 20))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.top = y
        self.speed = -10

    def update(self):
        self.rect.y += self.speed
        if self.rect.bottom < 0:
            self.kill()

# Clase para los enemigos
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, SCREEN_WIDTH - 50)
        self.rect.y = random.randint(0, SCREEN_HEIGHT - 50)
        self.speed = random.randint(1, 3)
        self.health = 5

    def update(self):
        # Movimiento simple de los enemigos (puede mejorarse)
        self.rect.x += self.speed
        if self.rect.right > SCREEN_WIDTH or self.rect.left < 0:
            self.speed = -self.speed

        # Verifica si el enemigo fue alcanzado por un proyectil
        if self.health <= 0:
            self.kill()

# Función principal del juego
def main():
    clock = pygame.time.Clock()
    player = Player()
    all_sprites = pygame.sprite.Group()
    all_sprites.add(player)

    enemies = pygame.sprite.Group()
    for _ in range(5):  # Crear 5 enemigos
        enemy = Enemy()
        all_sprites.add(enemy)
        enemies.add(enemy)

    projectiles = pygame.sprite.Group()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    player.attack()
                elif event.key == pygame.K_d:
                    player.defend()
                elif event.key == pygame.K_m:
                    player.magic_attack(projectiles)
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_d:
                    player.stop_defending()

        # Actualizar proyectiles y enemigos
        projectiles.update()
        enemies.update()
        # Actualizar jugador con colisiones
        player.update(enemies, projectiles)

        # Detectar colisiones entre proyectiles y enemigos
        for projectile in projectiles:
            collided_enemies = pygame.sprite.spritecollide(projectile, enemies, False)
            for enemy in collided_enemies:
                enemy.health -= player.magic_power
                projectile.kill()

        # Detectar colisiones entre el ataque físico (puño) y enemigos
        attack_rect = player.draw_attack(screen)
        if attack_rect:
            collided_enemies = [enemy for enemy in enemies if attack_rect.colliderect(enemy.rect)]
            for enemy in collided_enemies:
                enemy.health -= player.attack_power

        screen.fill(BLACK)
        all_sprites.draw(screen)
        projectiles.draw(screen)
        player.draw_health_bar(screen)
        player.draw_mana_bar(screen)  # Dibuja la barra de maná
        player.draw_attack(screen)  # Dibuja el ataque físico (puño)
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
