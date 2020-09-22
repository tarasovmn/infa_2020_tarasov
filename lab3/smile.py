import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 400))
circle(screen, (255,255,0), (200,200), 150)
circle(screen, (255, 0, 0), (150,150), 30)
circle(screen, (0, 0, 0), (150,150), 15)
circle(screen, (255, 0, 0), (250,150), 30)
circle(screen, (0, 0, 0), (250,150), 15)

line(screen, (0, 0, 0), (170, 140), (50, 100), 5)
line(screen, (0, 0, 0), (230, 140), (350, 100), 5)
line(screen, (0, 0, 0), (150, 320), (250, 320), 10)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()