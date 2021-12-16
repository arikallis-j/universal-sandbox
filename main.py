import sys

import numpy as np
import pygame

from draw import *
from calc import *
from event import *


pygame.init()

clock = pygame.time.Clock() #таймер

run = RUN
key = KEY
pygame.display.update()
while True:
    while run['menu']:
        clock.tick(FPS)
        DrawMenu()
        run = CheckMenu(run)
        pygame.display.update()

    while run['config']:
        clock.tick(FPS)
        DrawConfig()
        run, key = CheckConfig(run, key)
        pygame.display.update()
    if run['game']:
        Start(key)
    while run['game']:
        clock.tick(FPS)
        Draw()
        UpDate()
        run = Check(run)
        pygame.display.update()
pygame.quit()
