import pygame
from pygame.draw import*

pygame.init()
FPS = 30

screen = pygame.display.set_mode((400, 800))
polygon(screen, (255,240,240), ((0,0), (0,400), (400,0), (400,400)))
polygon(screen, (255,250,250), ((0,400), (400,400), (0,800), (400,800)))

ellipse(screen,(0,0,0), (200,500, 200, 150),)


pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
