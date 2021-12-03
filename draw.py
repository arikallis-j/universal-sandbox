import pygame
import numpy as np
from const import *
from calc import *
from event import *

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))  # создание экрана


class DrawObj:
    def __init__(self, type, color, radius, x, y):
        self.type = type

        self.color = color
        self.r = abs(M)/100* radius
        if self.r<1:
            self.r = 1

        self.x = x*M + A
        self.y = y*M + B

    def draw(self):
        if self.type == 'star':
            pygame.draw.circle(screen, self.color, (self.x, self.y), self.r)
        elif self.type == 'planet':
            pygame.draw.circle(screen, self.color, (self.x, self.y), self.r)
        else:
            pass

def Draw():
    global M, A, B
    M, A, B = CheckDraw(M, A, B)
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
    screen.fill(SPACE)
    for body in DRAW_OBJECTS:
        body.draw()
