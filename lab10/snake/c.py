import pygame as pg
import random
import time
import psycopg2

# --- Подключение к PostgreSQL ---
conn = psycopg2.connect(
    dbname="snake",
    user="postgres",
    password="asyl",
    host="localhost",
    port="5432"
)
cursor = conn.cursor()

# --- Получение имени пользователя и регистрация (если новый) ---
username = input("Enter your username: ")

cursor.execute("SELECT username FROM users WHERE username = %s", (username,))
user = cursor.fetchone()

if not user:
    cursor.execute("INSERT INTO users (username) VALUES (%s)", (username,))
    conn.commit()
    print(f"Welcome, {username}!")
else:
    print(f"Welcome back, {username}!")

# --- Получаем максимальный уровень игрока (если есть) ---
cursor.execute("SELECT MAX(level) FROM user_score WHERE username = %s", (username,))
last_level = cursor.fetchone()[0]
level = last_level if last_level else 1
print(f"Starting from level {level}")

# --- Настройки Pygame ---
pg.init()

width, height = 600, 400
cellsize = 20
white, green, red, blue, black = (255, 255, 255), (0, 255, 0), (255, 0, 0), (0, 0, 255), (0, 0, 0)
fps = 10
speed = fps + (level - 1) * 2

screen = pg.display.set_mode((width, height))
pg.display.set_caption("Snake Game")

font = pg.font.Font(None, 30)

snake = [(100, 100), (90, 100), (80, 100)]
snake_dir = (cellsize, 0)
score = 0

food = None
food_value = 0
food_timer = 0

def generate_food():
    global food_value, food_timer
    while True:
        x = random.randint(0, (width // cellsize) - 1) * cellsize
        y = random.randint(0, (height // cellsize) - 1) * cellsize
        if (x, y) not in snake:
            food_value = random.choice([10, 20, 30])
            food_timer = time.time()
            return (x, y)

food = generate_food()

def wait_for_key():
    waiting = True
    screen.fill(black)
    text = font.render("Press any key to start...", True, white)
    screen.blit(text, (width // 2 - 100, height // 2))
    pg.display.flip()
    while waiting:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                cursor.close()
                conn.close()
                exit()
            elif event.type == pg.KEYDOWN:
                waiting = False

wait_for_key()


running = True
clock = pg.time.Clock()

while running:
    screen.fill(black)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_UP and snake_dir != (0, cellsize):
                snake_dir = (0, -cellsize)
            elif event.key == pg.K_DOWN and snake_dir != (0, -cellsize):
                snake_dir = (0, cellsize)
            elif event.key == pg.K_LEFT and snake_dir != (cellsize, 0):
                snake_dir = (-cellsize, 0)
            elif event.key == pg.K_RIGHT and snake_dir != (-cellsize, 0):
                snake_dir = (cellsize, 0)
            elif event.key == pg.K_s:
                cursor.execute(
                    "INSERT INTO user_score (username, score, level) VALUES (%s, %s, %s)",
                    (username, score, level)
                )
                conn.commit()
                print(f"Game saved! Score: {score}, Level: {level}")

    new_head = (snake[0][0] + snake_dir[0], snake[0][1] + snake_dir[1])

    if new_head[0] < 0 or new_head[0] >= width or new_head[1] < 0 or new_head[1] >= height:
        running = False

    if new_head in snake:
        running = False

    snake.insert(0, new_head)

    if new_head == food:
        score += food_value
        if score % 30 == 0:
            level += 1
            speed += 2
        food = generate_food()
    else:
        snake.pop()

    if time.time() - food_timer > 5:
        food = generate_food()

    for segment in snake:
        pg.draw.rect(screen, green, (segment[0], segment[1], cellsize, cellsize))

    pg.draw.rect(screen, red, (food[0], food[1], cellsize, cellsize))

    score_text = font.render(f"Score: {score}  Level: {level}", True, white)
    screen.blit(score_text, (10, 10))

    pg.display.flip()
    clock.tick(speed)

pg.quit()
cursor.close()
conn.close()
