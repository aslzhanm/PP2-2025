import pygame

# Инициализация Pygame
pygame.init()

# Константы
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Создание окна
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Paint Program")
screen.fill(WHITE)

# Переменные для рисования
drawing = False
last_pos = None
color = BLACK
mode = "pen"  # Режим рисования: pen, rect, circle, eraser

# Основной цикл
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            drawing = True
            last_pos = event.pos
            if mode == "rect":
                pygame.draw.rect(screen, color, (event.pos[0], event.pos[1], 50, 50))
            elif mode == "circle":
                pygame.draw.circle(screen, color, event.pos, 25)
        elif event.type == pygame.MOUSEBUTTONUP:
            drawing = False
        elif event.type == pygame.MOUSEMOTION and drawing:
            if mode == "pen":
                pygame.draw.line(screen, color, last_pos, event.pos, 3)
                last_pos = event.pos
            elif mode == "eraser":
                pygame.draw.line(screen, WHITE, last_pos, event.pos, 10)
                last_pos = event.pos
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                mode = "rect"
            elif event.key == pygame.K_c:
                mode = "circle"
            elif event.key == pygame.K_p:
                mode = "pen"
            elif event.key == pygame.K_e:
                mode = "eraser"
            elif event.key == pygame.K_1:
                color = BLACK
            elif event.key == pygame.K_2:
                color = RED
            elif event.key == pygame.K_3:
                color = GREEN
            elif event.key == pygame.K_4:
                color = BLUE
            elif event.key == pygame.K_SPACE:
                screen.fill(WHITE)  
    
    pygame.display.flip()

pygame.quit()
