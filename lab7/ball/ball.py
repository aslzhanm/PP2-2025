import pygame
import os

pygame.init()

WIDTH, HEIGHT = 400, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Red Ball Game")

WHITE = (255, 255, 255)
RED = (255, 0, 0)

ball_radius = 25
ball_x, ball_y = WIDTH // 2, HEIGHT // 2
ball_speed = 20

running = True
while running:
    screen.fill(WHITE)  
    pygame.draw.circle(screen, RED, (ball_x, ball_y), ball_radius)  
    pygame.display.flip()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and ball_y - ball_radius - ball_speed >= 0:
                ball_y -= ball_speed
            elif event.key == pygame.K_DOWN and ball_y + ball_radius + ball_speed <= HEIGHT:
                ball_y += ball_speed
            elif event.key == pygame.K_LEFT and ball_x - ball_radius - ball_speed >= 0:
                ball_x -= ball_speed
            elif event.key == pygame.K_RIGHT and ball_x + ball_radius + ball_speed <= WIDTH:
                ball_x += ball_speed

pygame.quit()
