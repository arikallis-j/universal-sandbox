import pygame

from const import *
from calc import *

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))  # создание экрана


class DrawObj:
    def __init__(self, type, color, radius, x, y):
        self.type = type

        self.color = color
        self.r = radius

        self.x = x*M + A
        self.y = y*M + B

    def draw(self):
        if type==0:
            pygame.draw.circle(screen, self.color, (self.x, self.y), self.r)
        else:
            pass

DRAW_OBJECTS = []
for body in HEAVEN_OBJECTS:
    DRAW_OBJECTS.append(
        DrawObj(
            body.type,
            body.color,
            body.r,
            body.x,
            body.y
        ))
def Draw():
    for body in DRAW_OBJECTS:
        body.draw()