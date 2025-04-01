import pygame
import random

pygame.init()

WIDTH, HEIGHT = 600, 800
WHITE = (255, 255, 255)
ROAD_COLOR = (50, 50, 50)
FPS = 60

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Racer Game")
clock = pygame.time.Clock()

car_image = pygame.image.load("car.png")
car_image = pygame.transform.scale(car_image, (50, 100))
coin_image = pygame.image.load("coin.png")
coin_image = pygame.transform.scale(coin_image, (30, 30))

class Car:
    def __init__(self):
        self.x = WIDTH // 2 - 25
        self.y = HEIGHT - 120
        self.speed = 5

    def move(self, dx):
        self.x += dx
        self.x = max(100, min(self.x, WIDTH - 150))  

    def draw(self):
        screen.blit(car_image, (self.x, self.y))

class Coin:
    def __init__(self):
        self.x = random.randint(100, WIDTH - 150)
        self.y = random.randint(-300, -50)
        self.speed = 5

    def move(self):
        self.y += self.speed
        if self.y > HEIGHT:
            self.reset()

    def reset(self):
        self.x = random.randint(100, WIDTH - 150)
        self.y = random.randint(-300, -50)

    def draw(self):
        screen.blit(coin_image, (self.x, self.y))

car = Car()
coins = [Coin() for _ in range(5)]
score = 0
font = pygame.font.Font(None, 36)
running = True
while running:
    screen.fill(ROAD_COLOR)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        car.move(-car.speed)
    if keys[pygame.K_RIGHT]:
        car.move(car.speed)
    
    for coin in coins:
        coin.move()
        if car.x < coin.x < car.x + 50 and car.y < coin.y < car.y + 100:
            score += 1
            coin.reset()
        coin.draw()
    
    text = font.render(f"Coins: {score}", True, WHITE)
    screen.blit(text, (WIDTH - 120, 20))
    
    car.draw()
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
