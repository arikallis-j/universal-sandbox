import numpy as np
import pygame

from draw import *
from calc import *
from event import *


pygame.init()

clock = pygame.time.Clock() #таймер
screen.fill(SPACE)
pygame.display.update()

run = True
while run:
    clock.tick(FPS)
    Draw()
    UpDate()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()


pygame.quit()