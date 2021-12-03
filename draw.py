import pygame
import numpy as np
from const import *
from calc import *
from event import *

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))  # создание экрана
myfont = pygame.font.SysFont('Comic Sans MS', 30) #шрифты для надписи

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

def DrawMenu():
    screen.fill(SPACE)
    for button in buttons['menu']:
        myfont.render(button['name'], False, COLORS_BUTTON[button['color']])
        screen.blit(
                    myfont.render(button['name'], False, COLORS_BUTTON[button['color']]),
                    (button['x'], button['y'])
                    )
def DrawConfig():
    screen.fill(SPACE)
    for button in buttons['config']:
        myfont.render(button['name'], False, COLORS_BUTTON[button['color']])
        screen.blit(
                    myfont.render(button['name'], False, COLORS_BUTTON[button['color']]),
                    (button['x'], button['y'])
                    )


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


