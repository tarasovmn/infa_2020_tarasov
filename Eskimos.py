import pygame
from pygame.draw import *
import math

# Цвета:
white = (255, 255, 255)
grey = (199, 199, 199)
black = (0, 0, 0)

FPS = 30
# Создаём окно рисования
win_width = 600
win_length = 800
screen = pygame.display.set_mode((win_width, win_length))


def background():
    """ Функция рисует задний фон
    """
    rect(screen, grey, (0, 0, win_width, int(0.4 * win_length)))
    rect(screen, white, [0, int(0.4 * win_length), win_width, int(0.6 * win_length)])


def house(x, y, width, length):
    ''' Функция рисует домик ширины width и высоты length от опорной точки(x,y),
    которая находится в середине основания домика.
    :param x: Координата х середины основания домика
    :param y: Координата у середины основания домика
    :param width: Ширина домика
    :param length: Высота домика
    :return: None
    '''
    draw_house_walls(x, y, width, length)
    draw_house_lines(x, y, width, length)


def draw_house_walls(x, y, width, length):
    '''
    Функция рисует основную стену и основание домика
    :param x: Координата х середины основания домика
    :param y: Координата у середины основания домика
    :param width: Ширина домика
    :param length: Высота домика
    :return: None
    '''
    arc(screen, black, (x - int(0.5 * width), y - length, width, int(2 * length)), 0, math.pi, 3)
    line(screen, black, [x - int(0.5 * width), y], [x + int(0.5 * width), y], 2)


def draw_house_lines(x, y, width, length):
    ''' Функция рисует линии у дома
    '''
    # Горизонталғные линии
    line(screen, black, [x - int(7 * width / 15), y - int(2 * length / 7)],
         [x + int(7 * width / 15), y - int(2 * length / 7)])
    line(screen, black, [x - int(6 * width / 15), y - int(4 * length / 7)],
         [x + int(6 * width / 15), y - int(4 * length / 7)])
    line(screen, black, [x - int(4 * width / 15), y - int(6 * length / 7)],
         [x + int(4 * width / 15), y - int(6 * length / 7)])
    # Вертикальные линии
    line(screen, black, [x, y - length], [x - 10, y - int(6 * length / 7)])

    line(screen, black, [x - int(0.33 * width/2), y - int(6 * length / 7)],
         [x - int(0.40 * width/2), y - int(4 * length / 7)])
    line(screen, black, [x, y - int(6 * length / 7)], [x + int(0.02 * width/2), y - int(4 * length / 7)])
    line(screen, black, [x + int(0.33*width/2), y - int(6 * length / 7)], [x + int(0.45*width/2), y - int(4 * length / 7)])

    line(screen, black, [x - int(width / 4), y - int(4 * length / 7)],
         [x - int(1.11 * width / 4), y - int(2 * length / 7)])
    line(screen, black, [x - int(width / 12), y - int(4 * length / 7)],
         [x - int(1.06 * width / 12), y - int(2 * length / 7)])
    line(screen, black, [x + int(width / 12), y - int(4 * length / 7)],
         [x + int(1.10 * width / 12), y - int(2 * length / 7)])
    line(screen, black, [x + int(width / 4), y - int(4 * length / 7)],
         [x + int(1.20 * width / 4), y - int(2 * length / 7)])

    line(screen, black, [x - int(3*width/8), y - int(2 * length / 7)], [x - int(3.1*width/8), y])
    line(screen, black, [x - int(3*width/16), y - int(2 * length / 7)], [x - int(3.19*width/16) , y])
    line(screen, black, [x + int(3*width/16), y - int(2 * length / 7)], [x + int(3.12*width/16), y])
    line(screen, black, [x, y - int(2 * length / 7)], [x - int(0.01*width), y])
    line(screen, black, [x + int(3*width/8), y - int(2 * length / 7)], [x + int(3.15*width/8), y])



background()

house(400, 200, 300, 150)
house(200, 500, 150, 75)

# Конец
pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
