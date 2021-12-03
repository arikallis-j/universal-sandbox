import numpy as np

from const import *
from config import *
from event import *

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
    dt = CheckCalc(dt)
    for body in HEAVEN_OBJECTS:
        body.move_calc()


def UpDate():
    Force()
    Move()