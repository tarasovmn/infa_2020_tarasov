import pygame
from pygame.draw import *
from random import randint

pygame.init()

FPS = 1
balls_number = 0
plus_number = 0
score = 0
screen_height = 600
screen_width = 1000
pygame.display.set_caption("Catch the ball")
screen = pygame.display.set_mode((screen_width, screen_height))

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]


pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished :
    r1 = randint(10,100)
    x1 = randint(r1, screen_width - r1)
    y1 = randint(r1, screen_height - r1)
    color = COLORS[randint(0,5)]
    ball1 = circle(screen, color, (x1, y1), r1)
    balls_number = balls_number + 1

    r2 = randint(10, 100)
    x2 = randint(r2, screen_width - r2)
    y2 = randint(r2, screen_height - r2)
    color = COLORS[randint(0, 5)]
    ball2 = circle(screen, color, (x2, y2), r2)
    balls_number = balls_number + 1

    a = randint(50,100)
    x = randint(a, screen_width - a)
    y = randint(a, screen_height - a)
    plus = polygon(screen, color, ((x - a/2, y + a/20), (x - a/20, y + a/20), (x - a/20, y + a/2), (x + a/20, y + a/2),
                                  (x + a/20, y + a/20), (x + a/2, y + a/20), (x + a/2, y - a/20), (x + a/20, y - a/20),
                                  (x + a/20, y - a/2), (x - a/20, y - a/2), (x - a/20, y - a/20), (x - a/2, y - a/20)))
    plus_number = plus_number + 1

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            cursor_x, cursor_y = event.pos
            if (abs(x - cursor_x)) ** 2 + (abs(y - cursor_y)) ** 2 <= r ** 2:
                score += 1
                print("score = ", score)
                break

pygame.quit()
