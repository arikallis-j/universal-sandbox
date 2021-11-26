from numpy import pi

WIDTH = 700 #длина экрана
HEIGHT = 700 #ширина экрана

FPS = 30

SPACE = 0x002238
RED = 0xFF0000
BLUE = 0x0000FF
YELLOW = 0xFFC91F
GREEN = 0x00FF00
MAGENTA = 0xFF03B8
CYAN = 0x00FFCC
BLACK = (0, 0, 0)
WHITE = 0xFFFFFF
GREY = 0x7D7D7D
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

N_objects = 1

G = (2 * pi)**2 * 3 * 10**(-6) # a.e^3/(год^2*масса-земли)
dt = 1
M = 1
A = 0
B = -HEIGHT