import pygame
import numpy as np
from const import *
from calc import *
from event import *

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))  # создание экрана
myfont = pygame.font.SysFont('Comic Sans MS', 30) #шрифты для надписи
titlefont = pygame.font.SysFont('meera', 70)
class DrawObj:
    def __init__(self, type, color, radius, x, y):
        self.type = type

        self.color = color
        self.r = abs(M*radius)
        if self.r<2:
            if self.type == 'star':
                self.r = 2
            elif self.type == 'planet':
                self.r = 1
            else:
                self.r = 0.5

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

    screen.blit(
        titlefont.render("UNIVERSAL SANDBOX", True, YELLOW), (80, 100)
    )
    for button in buttons['menu']:
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
    global M, A, B, dt
    M, A, B, dt = CheckButton(M, A, B, dt)
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
    screen.blit(
        myfont.render(buttons['panel'][0]['name'] + str(round(100/M * 1000)/1000) + " a.u./100px", False, COLORS_BUTTON[buttons['panel'][0]['color']]),
        (buttons['panel'][0]['x'], buttons['panel'][0]['y'])
    )
    screen.blit(
        myfont.render(buttons['panel'][1]['name'] + str(round(365*dt*FPS)) + " days/sec", False, COLORS_BUTTON[buttons['panel'][1]['color']]),
        (buttons['panel'][1]['x'], buttons['panel'][1]['y'])
    )


