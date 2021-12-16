import numpy as np

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

    def collision_calc(self, other):
        m1 = self.m
        vx1 = self.vx
        vy1 = self.vy
        x1 = self.x
        y1 = self.y

        m2 = other.m
        vx2 = other.vx
        vy2 = other.vy
        x2 = other.x
        y2 = other.y

        d = dist(self,other)
        R = self.r + other.r
        if d <= R and self.type=='planet' and other.type=='planet':
            vX1 = ((x2 - x1) * vx1 + (y2 - y1) * vy1) / d
            vX2 = ((x1 - x2) * vx2 + (y1 - y2) * vy2) / d
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

            self.vx = vx1c + vX1x
            self.vy = vy1c + vX1y
            other.vx = vx2c + vX2x
            other.vy = vy2c + vX2y


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

def Collisions():
    for body_this in HEAVEN_OBJECTS:
        for body_other in HEAVEN_OBJECTS:
            if body_other == body_this:
                pass
            else:
                body_this.collision_calc(body_other)

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
    Collisions()
    Force()
    Move()



