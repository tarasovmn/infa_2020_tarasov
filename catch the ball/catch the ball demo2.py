import pygame
from pygame.draw import *
from random import randint

pygame.init()

#  Цвета:
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN, WHITE]

# Задаём последовательность праметров для шара.
X = 0
Y = 1
R = 2
COLOR = 3
VX = 4
VY = 5

# Экран:
WIDTH = 1200
HEIGHT = 500
FPS = 30
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Начальные условия
score = 0
number = 7  # Колличесво шаров
balls = [0] * number


def text(score):
    """ Функция выводит счёт на экран
    score - счёт, который будет отображаться на экране
    """
    f1 = pygame.font.SysFont('arial', 55)
    text = f1.render(score, 1, WHITE)
    screen.blit(text, (60, 20))


def draw(ball) -> object:
    """ Функция рисует шарик """
    circle(screen, ball[COLOR], (ball[X], ball[Y]), ball[R])


def new_ball():
    """ Функция рисует новый шарик """
    x = randint(10, WIDTH - 80)  # Рандомная координата шара по x
    y = randint(10, HEIGHT - 80)  # Рандомная координата шара по y
    vx = randint(-6, 6)  # Рандомная скорость шара vx
    vy = randint(-6, 6)  # Рандомная скорость vy
    r = randint(30, 80)  # Рандомный радиус шара r
    color = COLORS[randint(0, 6)]  # Рандомный цвет для шара
    circle(screen, color, (x, y), r)
    ball = [0] * 6
    ball[X] = x
    ball[Y] = y
    ball[VX] = vx
    ball[VY] = vy
    ball[R] = r
    ball[COLOR] = color
    return ball


def move_ball(ball):
    """ Функция производит движение и отскоки шарика """
    r = ball[R]
    x = ball[X]
    y = ball[Y]
    vx = ball[VX]
    vy = ball[VY]
    x += vx
    y += vy
    if x + r > WIDTH or x - r < 0:  # Отскок по вертикали
        vx = -vx
        x += vx
        y += vy
    if y + r > HEIGHT or y - r < 0:  # Отскок по горизонтали
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
            print("Всего очков:", score)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            for i, ball in enumerate(balls):
                x1, y1 = event.pos
                x = ball[X]
                y = ball[Y]
                r = ball[R]
                if (x - x1) ** 2 + (y - y1) ** 2 <= r ** 2:
                    balls[i] = new_ball()
                    score += 100 - r
                    text(str(score))

    for ball in balls:
        ball = move_ball(ball)
        draw(ball)

    pygame.display.update()
    screen.fill(BLACK)

pygame.quit()