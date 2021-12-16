import numpy as np

from const import *
from config import *
from event import *
from math import *

def dist(self,other):
    d = np.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)
    return d


class HeavObj:
    def __init__(self, x, y, vx, vy, mass, radius, color, type):
        self.type = type

        self.color = color
        self.r = radius

        self.x = x
        self.y = y

        self.vx = vx
        self.vy = vy

        self.ax = 0
        self.ay = 0

        self.m = mass


    def force_calc(self, other):
        d = dist(self, other)
        self.ax += - G * other.m * (self.x - other.x) / (d ** 3)
        self.ay += - G * other.m * (self.y - other.y) / (d ** 3)
    def move_calc(self):
        self.vx += self.ax * dt
        self.vy += self.ay * dt
        self.x += self.vx * dt
        self.y += self.vy * dt
        self.ax, self.ay = 0, 0


HEAVEN_OBJECTS = []
def Start(key):
    HEAVEN_OBJECTS.clear()
    for k in range(len(objects[key])):
        HEAVEN_OBJECTS.append(
            HeavObj(
                objects[key][k]['x'],
                objects[key][k]['y'],
                objects[key][k]['vx'],
                objects[key][k]['vy'],
                objects[key][k]['m'],
                objects[key][k]['r'],
                COLORS[key][objects[key][k]['c']],
                objects[key][k]['t']
            ))

def Force():
    for body_this in HEAVEN_OBJECTS:
        for body_other in HEAVEN_OBJECTS:
            if body_other == body_this:
                pass
            else:
                body_this.force_calc(body_other)

def Move():
    global dt
    dt = CheckButton(M,A,B,dt)[3]
    for body in HEAVEN_OBJECTS:
        body.move_calc()


def UpDate():
    Force()
    Move()

def collision(i, j):
    m1 = HEAVEN_OBJECTS[i].m
    vx1 = HEAVEN_OBJECTS[i].vx
    vy1 = HEAVEN_OBJECTS[i].vy
    x1 = HEAVEN_OBJECTS[i].x
    y1 = HEAVEN_OBJECTS[i].y

    m2 = HEAVEN_OBJECTS[j].m
    vx2 = HEAVEN_OBJECTS[j].vx
    vy2 = HEAVEN_OBJECTS[j].vy
    x2 = HEAVEN_OBJECTS[j].x
    y2 = HEAVEN_OBJECTS[j].y
    
    l = sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
    vX1  = ((x2 - x1) * vx1 + (y2 - y1) * vy1) / l
    vX2  = ((x1 - x2) * vx2 + (y1 - y2) * vy2) / l
    alpha1 = acos((x2 - x1) / sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2))
    alpha2 = acos((x1 - x2) / sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2))
    vX1x = vX1 * cos(alpha1)
    vX1y = vX1 * sin(alpha1)
    vX2x = vX2 * cos(alpha2)
    vX2y = vX2 * sin(alpha2)
    vx1c = vx1 - vX1x
    vy1c = vy1 - vX1y
    vx2c = vx2 - vX2x
    vy2c = vy2 - vX2y
    vX1 = ((m1 - m2) * vx1 + 2 * m2 * vx2) / (m1 + m2)
    vX2 = (2 * m1 * vx1 + (m2 - m1) * vx2) / (m1 + m2)
    vX1x = vX1 * cos(alpha1)
    vX1y = vX1 * sin(alpha1)
    vX2x = vX2 * cos(alpha2)
    vX2y = vX2 * sin(alpha2)
    vx1 = vx1c + vX1x
    vx2 = vx2c + vX2x
    vy1 = vy1c + vX1y
    vy2 = vy2c + vX2y

def check_collision(HEAVEN_OBJECTS):
    for i in range (len(HEAVEN_OBJECTS) - 1):
        for j in range (i + 1, len(HEAVEN_OBJECTS)):
            x1 = HEAVEN_OBJECTS[i].x
            y1 = HEAVEN_OBJECTS[i].y
            x2 = HEAVEN_OBJECTS[j].x
            y2 = HEAVEN_OBJECTS[j].y
            dr = HEAVEN_OBJECTS[i].r + HEAVEN_OBJECTS[j].r
            if (x1 - x2) ** 2 + (y1 - y2) ** 2 <= dr ** 2:
                collision(i, j)
