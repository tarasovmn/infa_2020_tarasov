# import libraries
import pygame
from pygame.draw import *
from random import randint

# initialise game engine
pygame.init()

c
screen = pygame.display.set_mode((1000, 600))

# colors in RGB
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]


# this function draws new ball of random size and color in random place on the screen
def new_ball():
    global x, y, r, speed_x, speed_y, color
    r = randint(10, 100)
    ball = randint(r, 1000-r)
    y = randint(r, 600-r)
    speed_x = randint(-10, 10)
    speed_y = randint(-6, 6)
    color = COLORS[randint(0, 5)]
    circle(screen, color, (x, y), r)

def plus():
    a = randint(50, 100)
    polygon(screen, color, (()))


# pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    new_ball()
    for i in range(10):
        circle(screen, (0, 0, 0), (x, y), r)
        if 0<= x + speed_x <= 1000:
            x = x + speed_x
        else:
            x = x - speed_x
        if 0 <= y + speed_y <= 600:
            y = y + speed_y
        else:
            y = y - speed_y
        circle(screen, color, (x, y), r)
        pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            cursor_x, cursor_y = event.pos
            if (abs(x - cursor_x)) ** 2 + (abs(y - cursor_y)) ** 2 <= r ** 2:
                print('Click!')
                score += 1
                print("score = ", score)
                circle(screen, (0, 0, 0), (x, y), r)
                break
            else:
                screen.fill(BLACK)
                break
    # new_ball()
    pygame.display.update()

pygame.quit()
