from snake import *
import math
import random
scl = 10
FPS = 10
width = 700
height = 500
fruit = [random.randint(0, math.floor((width-1)/scl))*scl, random.randint(0, math.floor((height-1)/scl))*scl]
pygame.init()
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")
clock = pygame.time.Clock()
snake = Snake(win)
running = True
STAT = pygame.font.SysFont("comicsans", 20)
text = STAT.render("Press Space Bar to toggle beteween AI and manual" , 1, (0, 0, 255))


while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    win.fill((255, 255, 255))
    text2 = STAT.render("AI mode : " + str(snake.ai), 1, (0, 0, 255))
    if snake.endGame():
        running = False
    if snake.x == fruit[0] and snake.y == fruit[1]:
        fruit = [random.randint(0, math.floor((width - 50) / scl)) * scl,
                 random.randint(0, math.floor((height - 50) / scl)) * scl]
        snake.eat()
    snake.update(fruit[0], fruit[1])
    snake.draw()
    pygame.draw.rect(win, (0, 0, 0), (fruit[0], fruit[1], 10, 10))
    win.blit(text, (width - 10 - text.get_width(), 10))
    win.blit(text2, (10 , 10))

    pygame.display.update()
pygame.quit()
