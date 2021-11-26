import numpy as np

from const import *
from config import *

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
        self.ax = - G * other.m * (self.x - other.x) / (d ** 3)
        self.ay = - G * other.m * (self.y - other.y) / (d ** 3)

    def move_calc(self):
        self.vy += self.ax * dt
        self.vx += self.ay * dt
        self.x += self.vx * dt
        self.y += self.vy * dt

HEAVEN_OBJECTS = []

for k in range(N_objects):
    HEAVEN_OBJECTS.append(
        HeavObj(
            objects[k]['x'],
            objects[k]['y'],
            objects[k]['vx'],
            objects[k]['vy'],
            objects[k]['m'],
            objects[k]['r'],
            COLORS[objects[k]['c']],
            objects[k]['t']
        ))

def Force():
    for body_this in HEAVEN_OBJECTS:
        for body_other in HEAVEN_OBJECTS:
            body_this.force_calc(body_other)

def Move():
    for body in HEAVEN_OBJECTS:
        body.move_calc()


def UpDate():
    Force()
    Move()