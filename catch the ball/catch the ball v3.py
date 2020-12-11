# imports
import pygame
from pygame.draw import *
from random import randint

# initialise game engine
pygame.init()

# screen
screen_width = 1000
screen_height = 600
FPS = 30
pygame.display.set_caption("Catch the ball")
screen = pygame.display.set_mode((screen_width, screen_height))

#  colors in RGB
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

# enter ball params
X = 0
Y = 1
R = 2
COLOR = 3
VX = 4
VY = 5

# at the beginning
score = 0
ball_number = 3
balls = [0] * ball_number

# show current score on the screen
def text(score):
    f1 = pygame.font.SysFont('arial', 40)
    text = f1.render(score, 1, WHITE)
    screen.blit(text, (60, 20))


def draw(ball):
    circle(screen, ball[COLOR], (ball[X], ball[Y]), ball[R])


def new_ball():
    x = randint(100, screen_width - 100)
    y = randint(100, screen_height - 100)
    vx = randint(-10, 10)
    vy = randint(-6, 6)
    r = randint(20, 100)
    color = COLORS[randint(0, 5)]
    circle(screen, color, (x, y), r)
    ball = [0] * 6
    ball[X] = x
    ball[Y] = y
    ball[VX] = vx
    ball[VY] = vy
    ball[R] = r
    ball[COLOR] = color
    return ball


def ball_movement(ball):
    r = ball[R]
    x = ball[X]
    y = ball[Y]
    vx = ball[VX]
    vy = ball[VY]
    x += vx
    y += vy
    if x + r > screen_width or x - r < 0:
        vx = -vx
        x += vx
        y += vy
    if y + r > screen_height or y - r < 0:
        vy = -vy
        x += vx
        y += vy
    else:
        x += vx
        y += vy

    ball[X] = x
    ball[Y] = y
    ball[VX] = vx
    ball[VY] = vy
    return ball


for i, ball in enumerate(balls):
    balls[i] = new_ball()

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
            print("Score = ", score)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            for i, ball in enumerate(balls):
                cursor_x, cursor_y = event.pos
                x = ball[X]
                y = ball[Y]
                r = ball[R]
                if (x - cursor_x) ** 2 + (y - cursor_y) ** 2 <= r ** 2:
                    balls[i] = new_ball()
                    score += 10 - r%10
                    text(str(score))

    for ball in balls:
        ball = ball_movement(ball)
        draw(ball)

    pygame.display.update()
    screen.fill(BLACK)Pychar

pygame.quit()