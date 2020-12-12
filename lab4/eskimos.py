# imports
import pygame
import math
from pygame.draw import *

pygame.init()
FPS = 30

# colors in RGB
sky_blue = (204, 229, 255)
snow_white = (255, 250, 250)
ice_blue = (204, 255, 255)
black = (0, 0, 0)
brown = (148, 49, 38)
dark_brown = (120, 40, 31)
light_fur = (250, 229, 211)
dark_fur = (147, 81, 22)
face = (253, 242, 233)
white = (255, 255, 255)
cat_grey = (166, 172, 175)

# create screen and background
screen = pygame.display.set_mode((600, 1200))
polygon(screen, sky_blue, ((0, 0), (0, 600), (600, 600), (600, 0)))
polygon(screen, snow_white, ((0, 600), (600, 600), (1200, 1200), (0, 1200)))


def draw_snowhouse(x, y, width, height):
    """
    :param x: x coord of house bottom center
    :param y: y coord of house bottom center
    :param width: house width
    :param height: house height
    """
    # outer lines
    arc(screen, black, [x - int(0.5 * width), y - height, width, int(2 * height)], 0, math.pi, 3)
    line(screen, black, [x - int(0.5 * width), y], [x + int(0.5 * width), y], 2)

    # inner lines
    # horizontal
    line(screen, black, [x - int(7 * width / 15), y - int(2 * height / 7)],
         [x + int(7 * width / 15), y - int(2 * height / 7)])
    line(screen, black, [x - int(6 * width / 15), y - int(4 * height / 7)],
         [x + int(6 * width / 15), y - int(4 * height / 7)])
    line(screen, black, [x - int(4 * width / 15), y - int(6 * height / 7)],
         [x + int(4 * width / 15), y - int(6 * height / 7)])
    # vertical
    line(screen, black, [x, y - height], [x - 10, y - int(6 * height / 7)])
    line(screen, black, [x - int(0.33 * width / 2), y - int(6 * height / 7)],
         [x - int(0.40 * width / 2), y - int(4 * height / 7)])
    line(screen, black, [x, y - int(6 * height / 7)], [x + int(0.02 * width / 2), y - int(4 * height / 7)])
    line(screen, black, [x + int(0.33 * width / 2), y - int(6 * height / 7)],
         [x + int(0.45 * width / 2), y - int(4 * height / 7)])
    line(screen, black, [x - int(width / 4), y - int(4 * height / 7)],
         [x - int(1.11 * width / 4), y - int(2 * height / 7)])
    line(screen, black, [x - int(width / 12), y - int(4 * height / 7)],
         [x - int(1.06 * width / 12), y - int(2 * height / 7)])
    line(screen, black, [x + int(width / 12), y - int(4 * height / 7)],
         [x + int(1.10 * width / 12), y - int(2 * height / 7)])
    line(screen, black, [x + int(width / 4), y - int(4 * height / 7)],
         [x + int(1.20 * width / 4), y - int(2 * height / 7)])
    line(screen, black, [x - int(3 * width / 8), y - int(2 * height / 7)], [x - int(3.1 * width / 8), y])
    line(screen, black, [x - int(3 * width / 16), y - int(2 * height / 7)], [x - int(3.19 * width / 16), y])
    line(screen, black, [x + int(3 * width / 16), y - int(2 * height / 7)], [x + int(3.12 * width / 16), y])
    line(screen, black, [x, y - int(2 * height / 7)], [x - int(0.01 * width), y])
    line(screen, black, [x + int(3 * width / 8), y - int(2 * height / 7)], [x + int(3.15 * width / 8), y])


def draw_eskimos(x, y, width, height):
    """
    :param x: x coord of eskimos bottom center
    :param y: y coord of eskimos bottom center
    :param width: eskimos width
    :param height: eskimos height
    """
    # hands
    ellipse(screen, brown,
            (x - int(width / 2.3), y - height + int(0.35 * width), int(5.5 * width / 17), int(1.1 * width / 11)))
    line(screen, black, [x - int(width / 2.2), y - height], [x - int(width / 3), y - int(width / 8)], 2)
    surface = pygame.Surface((int(5.5 * width / 17), int(1.1 * width / 11)))
    surface.fill(snow_white)
    surface.set_alpha(255)
    ellipse(surface, brown, (0, 0, int(5.5 * width / 17), int(1.1 * width / 11)))
    surface = pygame.transform.rotate(surface, - 40)
    screen.blit(surface, [x + int(width / 9), y - height + int(0.31 * width)])

    # body
    ellipse(screen, brown,
            (x - int(width / 3.6), y - height + int(width / 5), int(width / 1.8), int(3.75 * height / 4)), 0)
    rect(screen, snow_white, (x - int(width / 3.6), y - int(height / 4), int(width / 1.8), int(3.75 * height / 4)))
    rect(screen, dark_brown,
         (x - int(width / 12), y - height + int(0.3 * width), int(3 * width / 20), int(1.85 * height / 4)))

    # head
    ellipse(screen, light_fur, (x - int(width / 4), y - height, int(width / 2), int(height / 3)))
    ellipse(screen, dark_fur,
            (x - int(width / 5), y - height + int(width / 25), int(3.7 * width / 9), int(3.4 * height / 14)))
    ellipse(screen, face,
            (x - int(width / 6.2), y - height + int(width / 12), int(3 * width / 9), int(2.5 * height / 14)))
    line(screen, black, [x - int(width / 8.5), y - height + int(width / 7.2)],
         [x - int(width / 23), y - height + int(width / 6.2)])
    line(screen, black, [x + int(width / 20), y - height + int(width / 6.3)],
         [x + int(width / 7.7), y - height + int(width / 7.2)])
    arc(screen, black, (x - int(width / 17), y - height + int(width / 5), int(3 * width / 17), int(height / 10)),
        math.pi / 12, 11 * math.pi / 12)

    # legs
    ellipse(screen, brown,
            (x - int(width / 5), y - height + int(0.71 * width), int(2.7 * width / 20), int(1.85 * height / 8)), 0)
    ellipse(screen, brown,
            (x + int(width / 20), y - height + int(0.71 * width), int(2.7 * width / 20), int(1.85 * height / 8)), 0)
    ellipse(screen, black,
            (x - int(width / 3.55), y - height + int(0.87 * width), int(1.5 * height / 8), int(1 * width / 11)), 0)
    ellipse(screen, black,
            (x + int(width / 13), y - height + int(0.87 * width), int(1.5 * height / 8), int(1 * width / 11)), 0)
    rect(screen, dark_brown,
         (x - int(width / 3.65), y - height + int(0.76 * width), int(9.3 * width / 17), int(width / 15)))


def draw_cat(x, y, length, height):
    """

    :param x: x coord of cat body center
    :param y: y coord of cat body center
    :param length: cat body length
    :param height: cat body height
    """

    leg = pygame.Surface((int(length * 0.6), int(height * 0.3)))
    leg.fill((255, 255, 255, 10))
    ellipse(leg, cat_grey, (0, 0, int(length * 0.6), int(height * 0.3)))
    leg1 = pygame.transform.rotate(leg, -40)
    screen.blit(leg1, [x + int(length * 0.4), y + int(height * 0.4)])
    leg2 = pygame.transform.rotate(leg, -30)
    screen.blit(leg2, [x + int(length * 0.6), y + int(height * 0.3)])

    ellipse(screen, cat_grey, (x, y, length, height))


'''
    ellipse(screen, brown,
            (x - int(width / 2.3), y - height + int(0.35 * width), int(5.5 * width / 17), int(1.1 * width / 11)))
    line(screen, black, [x - int(width / 2.2), y - height], [x - int(width / 3), y - int(width / 8)], 2)
    surface = pygame.Surface((int(5.5 * width / 17), int(1.1 * width / 11)))
    surface.fill((255, 255, 255, 10))
    surface.set_alpha(255)
    ellipse(surface, brown, (0, 0, int(5.5 * width / 17), int(1.1 * width / 11)))
    surface = pygame.transform.rotate(surface, - 40)
    screen.blit(surface, [x + int(width / 9), y - height + int(0.31 * width)])
'''

draw_snowhouse(100, 320, 200, 150)
draw_eskimos(400, 800, 200, 210)
draw_cat(200, 800, 150, 50)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
