import pygame
from pygame.draw import *
import math

# Цвета:
white = (255, 255, 255)
grey = (199, 199, 199)
black = (0, 0, 0)
grey_cat = (163, 163, 163)

FPS = 30
# Создаём окно рисования:
win_width = 600  # Ширина окна
win_length = 600  # Высота окна
screen = pygame.display.set_mode((win_width, win_length))


def draw_background() -> object:
    """ Функция рисует задний фон
    """
    rect(screen, grey, (0, 0, win_width, int(0.4 * win_length)))
    rect(screen, white, [0, int(0.4 * win_length), win_width, int(0.6 * win_length)])


def draw_house_walls(x, y, width, length):
    """
    Функция рисует основную стену и основание домика
    :param x: Координата х середины основания домика
    :param y: Координата у середины основания домика
    :param width: Ширина домика
    :param length: Высота домика
    :return: None
    """
    arc(screen, black, (x - int(0.5 * width), y - length, width, int(2 * length)), 0, math.pi, 3)
    line(screen, black, [x - int(0.5 * width), y], [x + int(0.5 * width), y], 2)


def draw_house_lines(x, y, width, length):
    """ Функция рисует линии у дома
    :param x: Координата х середины основания домика
    :param y: Координата у середины основания домика
    :param width: Ширина домика
    :param length: Высота домика
    :return: None
    """
    # Горизонталғные линии
    line(screen, black, [x - int(7 * width / 15), y - int(2 * length / 7)],
         [x + int(7 * width / 15), y - int(2 * length / 7)])
    line(screen, black, [x - int(6 * width / 15), y - int(4 * length / 7)],
         [x + int(6 * width / 15), y - int(4 * length / 7)])
    line(screen, black, [x - int(4 * width / 15), y - int(6 * length / 7)],
         [x + int(4 * width / 15), y - int(6 * length / 7)])
    # Вертикальные линии
    line(screen, black, [x, y - length], [x - 10, y - int(6 * length / 7)])

    line(screen, black, [x - int(0.33 * width / 2), y - int(6 * length / 7)],
         [x - int(0.40 * width / 2), y - int(4 * length / 7)])
    line(screen, black, [x, y - int(6 * length / 7)], [x + int(0.02 * width / 2), y - int(4 * length / 7)])
    line(screen, black, [x + int(0.33 * width / 2), y - int(6 * length / 7)],
         [x + int(0.45 * width / 2), y - int(4 * length / 7)])

    line(screen, black, [x - int(width / 4), y - int(4 * length / 7)],
         [x - int(1.11 * width / 4), y - int(2 * length / 7)])
    line(screen, black, [x - int(width / 12), y - int(4 * length / 7)],
         [x - int(1.06 * width / 12), y - int(2 * length / 7)])
    line(screen, black, [x + int(width / 12), y - int(4 * length / 7)],
         [x + int(1.10 * width / 12), y - int(2 * length / 7)])
    line(screen, black, [x + int(width / 4), y - int(4 * length / 7)],
         [x + int(1.20 * width / 4), y - int(2 * length / 7)])

    line(screen, black, [x - int(3 * width / 8), y - int(2 * length / 7)], [x - int(3.1 * width / 8), y])
    line(screen, black, [x - int(3 * width / 16), y - int(2 * length / 7)], [x - int(3.19 * width / 16), y])
    line(screen, black, [x + int(3 * width / 16), y - int(2 * length / 7)], [x + int(3.12 * width / 16), y])
    line(screen, black, [x, y - int(2 * length / 7)], [x - int(0.01 * width), y])
    line(screen, black, [x + int(3 * width / 8), y - int(2 * length / 7)], [x + int(3.15 * width / 8), y])


def draw_house(x, y, width, length):
    """ Функция рисует домик ширины width и высоты length от опорной точки(x,y),
    которая находится в середине основания домика.
    :param x: Координата х середины основания домика
    :param y: Координата у середины основания домика
    :param width: Ширина домика
    :param length: Высота домика
    :return: None
    """
    draw_house_walls(x, y, width, length)
    draw_house_lines(x, y, width, length)


# def draw_cat(x, y, cat_width, cat_length):
#     """
#     Функция рисует кота с рыбой
#     :param x: координата x середины тела кота
#     :param y: координата y середины тела кота
#     :param cat_width: Ширина центрального эллипса у тела кота
#     :param cat_length: Высота центрального эллипса у  тела кота
#     :return: None
#     """
#     draw_cat_body(x, y, cat_width, cat_length)
#     draw_cat_legs()
#     draw_cat_tail(x, y, cat_width, cat_length)
#     draw_cat_head()
#     draw_fish()
#     pass
#
#
# def draw_cat_body(x, y, cat_width, cat_length):
#     """
#     Функция рисует тело кота
#     :param x: координата x середины тела кота
#     :param y: координата y середины тела кота
#     :param cat_width: Ширина тела кота
#     :param cat_length: Высота тела кота
#     :return: x_tail, y_tail, tail_width, tail_length
#     """
#     pass
#
#
# def draw_cat_tail(x, y, cat_width, cat_length):
#     """
#     Функция рисует хвост кота
#     :param x: координата x середины тела кота
#     :param y: координата y середины тела кота
#     :param cat_width: Ширина центрального эллипса y тела кота
#     :param cat_length: Высота центрального эллипса y  тела кота
#     :return: None
#     """
#     pass
#
#
# def draw_cat_legs(x, y, cat_width, cat_length):
#     pass
#
#
# def draw_cat_head(x, y, cat_width, cat_length):
#     pass
#
#
# def draw_fish(x, y, cat_width, cat_length):
#     pass

def draw_men(x, y, men_height, men_width):
    """
    Функция рисует человека
    :param x: Координата x середины нижней части прямоугольника, описанного вокруг человека
    :param y: Координата y середины нижней части прямоугольника, описанного вокруг человека
    :param men_height: Высота человека(высота прямоугольникаБ описывающего человека)
    :param men_width: Ширина человека(ширина прямоугольникаБ описывающего человека)
    :return: None
    """
    draw_men_head(x, y, men_height, men_width)
    draw_men_body(x, y, men_height, men_width)
    draw_men_hands(x, y, men_height, men_width)
    draw_men_legs(x, y, men_height, men_width)


def draw_men_head(x, y, men_width, men_height):
    """
    Функция рисует голову человека
    :param x: Координата x середины нижней части прямоугольника, описанного вокруг человека
    :param y: Координата y середины нижней части прямоугольника, описанного вокруг человека
    :param men_height: Высота человека(высота прямоугольникаБ описывающего человека)
    :param men_width: Ширина человека(ширина прямоугольникаБ описывающего человека)
    :return: None
    """
    ellipse(screen, (244, 247, 225), (x - int(men_width / 4), y - men_height, int(men_width / 2), int(men_height / 3)))
    ellipse(screen, (199, 162, 90), (
        x - int(men_width / 5), y - men_height + int(men_width / 25), int(3.7 * men_width / 9),
        int(3.4 * men_height / 14)))
    ellipse(screen, (173, 169, 161), (
        x - int(men_width / 6.2), y - men_height + int(men_width / 12), int(3 * men_width / 9),
        int(2.5 * men_height / 14)))
    line(screen, black, [x - int(men_width / 8.5), y - men_height + int(men_width / 7.2)],
         [x - int(men_width / 23), y - men_height + int(men_width / 6.2)])
    line(screen, black, [x + int(men_width / 20), y - men_height + int(men_width / 6.3)],
         [x + int(men_width / 7.7), y - men_height + int(men_width / 7.2)])
    arc(screen, black,
        (x - int(men_width / 17), y - men_height + int(men_width / 5), int(3 * men_width / 17), int(men_height / 10)),
        math.pi / 12, 11 * math.pi / 12)


def draw_men_body(x, y, men_width, men_height):
    """
    Функция рисует тело человека
    :param x: Координата x середины нижней части прямоугольника, описанного вокруг человека
    :param y: Координата y середины нижней части прямоугольника, описанного вокруг человека
    :param men_height: Высота человека(высота прямоугольникаБ описывающего человека)
    :param men_width: Ширина человека(ширина прямоугольникаБ описывающего человека)
    :return: None
    """
    ellipse(screen, (102, 80, 37),
            (x - int(men_width / 3.6), y - men_height + int(men_width / 5), int(men_width / 1.8),
             int(3.75 * men_height / 4)), 0)
    rect(screen, white, (x - int(men_width / 3.6), y - int(men_height / 4), int(men_width / 1.8),
                         int(3.75 * men_height / 4)))
    rect(screen, (71, 53, 16), (x - int(men_width / 12), y - men_height + int(0.3 * men_width), int(3 * men_width / 20),
                                int(1.85 * men_height / 4)))


def draw_men_legs(x, y, men_width, men_height):
    """
    Функция рисует ноги человека
    :param x: Координата x середины нижней части прямоугольника, описанного вокруг человека
    :param y: Координата y середины нижней части прямоугольника, описанного вокруг человека
    :param men_height: Высота человека(высота прямоугольникаБ описывающего человека)
    :param men_width: Ширина человека(ширина прямоугольникаБ описывающего человека)
    :return: None
    """
    ellipse(screen, (102, 80, 37),
            (x - int(men_width / 5), y - men_height + int(0.71 * men_width), int(2.7 * men_width / 20),
             int(1.85 * men_height / 8)), 0)
    ellipse(screen, (102, 80, 37),
            (x + int(men_width / 20), y - men_height + int(0.71 * men_width), int(2.7 * men_width / 20),
             int(1.85 * men_height / 8)), 0)
    ellipse(screen, black,
            (x - int(men_width / 3.55), y - men_height + int(0.87 * men_width), int(1.5 * men_height / 8),
             int(1 * men_width / 11)), 0)
    ellipse(screen, black,
            (x + int(men_width / 13), y - men_height + int(0.87 * men_width), int(1.5 * men_height / 8),
             int(1 * men_width / 11)), 0)
    rect(screen, (71, 53, 16), (
        x - int(men_width / 3.65), y - men_height + int(0.76 * men_width), int(9.3 * men_width / 17),
        int(men_width / 15)))


def draw_men_hands(x, y, men_width, men_height):
    """
    Функция рисует ркуи человек
    :param x: Координата x середины нижней части прямоугольника, описанного вокруг человека
    :param y: Координата y середины нижней части прямоугольника, описанного вокруг человека
    :param men_height: Высота человека(высота прямоугольникаБ описывающего человека)
    :param men_width: Ширина человека(ширина прямоугольникаБ описывающего человека)
    :return: None
    """
    ellipse(screen, (102, 80, 37), (
    x - int(men_width / 2.3), y - men_height + int(0.35 * men_width), int(5.5 * men_width / 17), int(1.1 * men_width / 11)))
    line(screen, black, [x - int(men_width / 2.2), y - men_height], [x - int(men_width / 3), y - int(men_width / 8)], 2)


# Вызываем все функции
draw_background()
draw_men_body(320, 520, 400, 420)
draw_men_head(320, 520, 400, 420)
draw_men_legs(320, 520, 400, 420)
draw_men_hands(320, 520, 400, 420)

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
