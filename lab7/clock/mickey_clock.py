import pygame
import time
import math

pygame.init()

WIDTH, HEIGHT = 600, 450
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mickey Clock")

background = pygame.image.load("mickey.png")  
background = pygame.transform.scale(background, (WIDTH, HEIGHT))

minute_hand = pygame.image.load("right_hand.png") 
second_hand = pygame.image.load("left_hand.png")  

def draw_hand(image, angle, x, y):
    rotated_image = pygame.transform.rotate(image, -angle)
    new_rect = rotated_image.get_rect(center=(x, y))
    screen.blit(rotated_image, new_rect.topleft)


running = True
while running:
    screen.fill((255, 255, 255))
    screen.blit(background, (0, 0))

   
    current_time = time.localtime()
    seconds = current_time.tm_sec
    minutes = current_time.tm_min

    second_angle = (seconds % 60) * 6 
    minute_angle = (minutes % 60) * 6  

    draw_hand(second_hand, second_angle, WIDTH // 2, HEIGHT // 2)
    draw_hand(minute_hand, minute_angle, WIDTH // 2, HEIGHT // 2)

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
