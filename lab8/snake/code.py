import pygame
import random

pygame.init()


WIDTH, HEIGHT = 600, 600
CELL_SIZE = 20
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
FPS = 10

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")
clock = pygame.time.Clock()


class Snake:
    def __init__(self):
        self.body = [(WIDTH // 2, HEIGHT // 2)]
        self.direction = (CELL_SIZE, 0)
        self.grow = False

    def move(self):
        head = (self.body[0][0] + self.direction[0], self.body[0][1] + self.direction[1])
        
        if head[0] < 0 or head[0] >= WIDTH or head[1] < 0 or head[1] >= HEIGHT:
            return False
        
        if head in self.body:
            return False
        
        self.body.insert(0, head)
        if not self.grow:
            self.body.pop()
        else:
            self.grow = False
        return True

    def change_direction(self, new_direction):
        if (new_direction[0] != -self.direction[0] and 
            new_direction[1] != -self.direction[1]):
            self.direction = new_direction

    def grow_snake(self):
        self.grow = True

    def draw(self):
        for segment in self.body:
            pygame.draw.rect(screen, GREEN, (*segment, CELL_SIZE, CELL_SIZE))

def generate_food(snake_body):
    while True:
        food = (random.randint(0, (WIDTH // CELL_SIZE) - 1) * CELL_SIZE, 
                random.randint(0, (HEIGHT // CELL_SIZE) - 1) * CELL_SIZE)
        if food not in snake_body:
            return food

snake = Snake()
food = generate_food(snake.body)
score = 0
level = 1
running = True

while running:
    screen.fill(BLACK)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                snake.change_direction((0, -CELL_SIZE))
            elif event.key == pygame.K_DOWN:
                snake.change_direction((0, CELL_SIZE))
            elif event.key == pygame.K_LEFT:
                snake.change_direction((-CELL_SIZE, 0))
            elif event.key == pygame.K_RIGHT:
                snake.change_direction((CELL_SIZE, 0))
    
    if not snake.move():
        running = False 
    
    if snake.body[0] == food:
        snake.grow_snake()
        food = generate_food(snake.body)
        score += 1
        if score % 4 == 0:  
            level += 1
            FPS += 2
    
    pygame.draw.rect(screen, RED, (*food, CELL_SIZE, CELL_SIZE))
    
    font = pygame.font.Font(None, 36)
    score_text = font.render(f"Score: {score}  Level: {level}", True, WHITE)
    screen.blit(score_text, (10, 10))
    
    snake.draw()
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
