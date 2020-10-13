# import libraries
import pygame
from pygame.draw import *
from random import randint

# initialise game engine
pygame.init()

score = 0
FPS = 1
pygame.display.set_caption("Catch the ball")
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
    global x, y, r, speed_x, speed_y
    x = randint(100, 900)
    y = randint(100, 500)
    r = randint(10, 100)
    color = COLORS[randint(0, 5)]
    circle(screen, color, (x, y), r)


def click(event):
    print(x, y)


# pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
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
            pygame.display.update()
    new_ball()
    pygame.display.update()

pygame.quit()