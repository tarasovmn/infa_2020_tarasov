import pygame
from pygame.draw import *

pygame.init()
FPS = 60

# Цвета
white = (255, 255, 255)
grey = (220, 220, 220)
black = (0, 0, 0)

# Создаём экран
screen = pygame.display.set_mode((600, 800))
screen.fill(white)

polygon(screen, grey, ((0, 0), (0, 400), (400, 400), (400, 0)))
polygon(screen, white, ((0, 400), (400, 400), (800, 800), (0, 800)))

# Происходит рисование хаты
ellipse(screen, black, (50, 350, 200, 150), 2)
polygon(screen, (255, 250, 250), ((0, 450), (400, 450), (800, 800), (0, 800)))
lines(screen, black, False, ((55, 450), (60, 455), (250, 443)))
line(screen, black, (50, 425), (245, 425))
line(screen, black, (58, 400), (242, 400))
line(screen, black, (75, 375), (225, 375))
line(screen, black, (100, 360), (103, 375))
line(screen, black, (135, 355), (134, 375))
line(screen, black, (173, 355), (174, 375))
line(screen, black, (80, 375), (81, 400))
line(screen, black, (120, 375), (119, 400))
line(screen, black, (160, 375), (161, 400))
line(screen, black, (190, 375), (188, 400))
line(screen, black, (75, 400), (72, 425))
line(screen, black, (125, 400), (130, 425))
line(screen, black, (155, 400), (156, 425))
line(screen, black, (195, 400), (196, 425))
line(screen, black, (65, 425), (66, 455))
line(screen, black, (100, 425), (101, 454))
line(screen, black, (145, 425), (146, 450))
line(screen, black, (190, 425), (189, 447))
line(screen, black, (220, 425), (221, 444))

ellipse(screen, (240, 240, 240), (290, 420, 60, 45))
ellipse(screen, (160, 80, 50), (275, 440, 90, 180))
polygon(screen, (255, 250, 250), ((0, 530), (400, 530), (800, 800), (0, 800)))
ellipse(screen, (170, 100, 60), (295, 425, 50, 35))
ellipse(screen, (240, 230, 140), (300, 430, 40, 30))
ellipse(screen, (160, 80, 50), (290, 515, 20, 40))
ellipse(screen, (160, 80, 50), (330, 515, 20, 40))
ellipse(screen, (160, 80, 50), (330, 540, 35, 15))
ellipse(screen, (160, 80, 50), (270, 540, 35, 15))
ellipse(screen, (0, 0, 0), (270, 548, 35, 8))
ellipse(screen, (0, 0, 0), (330, 548, 35, 8))
ellipse(screen, (160, 80, 50), (260, 467, 40, 15))
polygon(screen, (140, 70, 20), ((310, 460), (330, 460), (330, 525), (310, 525)))
polygon(screen, (140, 70, 20), ((275, 520), (360, 520), (360, 535), (280, 535)))
circle(screen, (0, 0, 0), (320, 485), 4)
circle(screen, (0, 0, 0), (320, 500), 4)
circle(screen, (0, 0, 0), (320, 515), 4)
line(screen, (0, 0, 0), (265, 450), (270, 530), 2)
line(screen, (0, 0, 0), (315, 440), (315, 442), 2)
line(screen, (0, 0, 0), (327, 440), (327, 442), 2)
line(screen, (0, 0, 0), (317, 450), (325, 452), 2)
line(screen, (0, 0, 0), (325, 457), (326, 470), 2)
line(screen, (0, 0, 0), (323, 457), (324, 470), 2)
line(screen, (0, 0, 0), (324, 456), (324, 471), 2)
line(screen, (0, 0, 0), (328, 457), (329, 468), 2)
line(screen, (0, 0, 0), (317, 458), (317, 471), 2)
line(screen, (0, 0, 0), (320, 457), (319, 470), 2)
line(screen, (0, 0, 0), (315, 457), (314, 470), 2)

ellipse(screen, (192, 192, 192), (100, 600, 80, 30))
ellipse(screen, (192, 192, 192), (90, 585, 30, 20))
ellipse(screen, (192, 192, 192), (100, 590, 18, 20))
ellipse(screen, (255, 255, 255), (95, 587, 5, 3))
ellipse(screen, (255, 255, 255), (100, 587, 5, 3))
ellipse(screen, (0, 0, 0), (96, 588, 3, 2))
ellipse(screen, (0, 0, 0), (101, 588, 3, 2))
polygon(screen, (192, 192, 192), ((95, 586), (98, 582), (101, 586)))
polygon(screen, (192, 192, 192), ((105, 586), (108, 580), (111, 586)))

circle(screen, (255, 250, 250), (300, 700), 20)
circle(screen, (255, 250, 250), (320, 700), 20)
circle(screen, (255, 250, 250), (310, 690), 20)

# The end
pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
