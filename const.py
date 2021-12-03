from numpy import pi

WIDTH = 700 #длина экрана
HEIGHT = 700 #ширина экрана

FPS = 144
KEY = 'double-star'
RUN = {
    'menu': True,
    'game': False,
    'config': False
}

G = (2 * pi)**2 * 3 * 10**(-6) # a.e^3/(год^2*масса-земли)


dt, dt0 = 1/FPS , 0.00001
M, M0 = 10, 0.3
A, A0  = WIDTH/2, 1
B, B0 = HEIGHT/2, 1

SPACE = 0x002238
RED = 0xFF0000
BLUE = 0x0000FF
YELLOW = 0xFFC91F
GREEN = 0x00FF00
PINK = 0xFF7E93
BROWN = 0x964B00
OCHRE = 0xCC7722
MAGENTA = 0xFF03B8
CYAN = 0x00FFCC
BLACK = (0, 0, 0)
WHITE = 0xFFFFFF
GREY = 0x7D7D7D
COLORS_BUTTON = [WHITE]
COLORS_SUN_SYSTEM = [YELLOW, GREY, PINK, GREEN, RED, BROWN, OCHRE, CYAN, BLUE]
COLORS_DOUBLE_STAR = [YELLOW, BLUE]
COLORS = {
    'sun-system': COLORS_SUN_SYSTEM,
    'double-star': COLORS_DOUBLE_STAR
}

menu_buttons = [
    {
        'type': 'start',
        'name': 'Start game',
        'color': 0,
        'x': 260,
        'y': 300,
        'l': 200,
        'h': 30
    },
    {
        'type': 'config',
        'name': 'Configuration',
        'color': 0,
        'x': 270,
        'y': 370,
        'l': 100,
        'h': 30
    },
    {
        'type': 'exit',
        'name': 'Exit game',
        'color': 0,
        'x': 270,
        'y': 440,
        'l': 150,
        'h': 30
    },
]
config_buttons = [
    {
        'type': 'sun-system',
        'name': 'SUN SYSTEM',
        'color': 0,
        'x': 260,
        'y': 300,
        'l': 200,
        'h': 30
    },
    {
        'type': 'double-star',
        'name': 'DOUBLE STAR',
        'color': 0,
        'x': 270,
        'y': 370,
        'l': 100,
        'h': 30
    }
]

buttons = {
    'menu': menu_buttons,
    'config': config_buttons
}