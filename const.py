from numpy import pi

WIDTH = 700 #длина экрана
HEIGHT = 700 #ширина экрана

FPS = 120
KEY = 'double-star'
RUN = {
    'menu': True,
    'game': False,
    'config': False
}

G = (2 * pi)**2 * 3 * 10**(-6) # a.e^3/(год^2*масса-земли)


dt, dt0 = 0.001 , 1.001
M, M0 = 100, 1.001
A, A0  = WIDTH/2, 1
B, B0 = HEIGHT/2, 1

SPACE = 0x001119 #0x002238
TITLE = (127,255,0)
RED = 0xFF0000
BLUE = 0x0000FF
YELLOW = (255,255,0)
GREEN = 0x00FF00
PINK = 0xFF7E93
BROWN = 0x964B00
OCHRE = 0xCC7722
MAGENTA = 0xFF03B8
CYAN = 0x00FFCC
BLACK = 0x000000
WHITE = 0xFFFFFF
GREY = 0x7D7D7D
COLORS_BUTTON = [WHITE,YELLOW]
COLORS_SUN_SYSTEM = [YELLOW, GREY, PINK, GREEN, RED, BROWN, OCHRE, CYAN, BLUE]
COLORS_DOUBLE_STAR = [YELLOW, BLUE]
COLORS_COLLISION = [GREEN]
COLORS = {
    'sun-system': COLORS_SUN_SYSTEM,
    'double-star': COLORS_DOUBLE_STAR,
    'collision': COLORS_COLLISION
}

menu_buttons = [
    {
        'type': 'start',
        'name': 'Start game',
        'color': 0,
        'x': 270,
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
        'name': 'Sun system',
        'color': 0,
        'x': 270,
        'y': 300,
        'l': 200,
        'h': 30
    },
    {
        'type': 'double-star',
        'name': 'Double star',
        'color': 0,
        'x': 270,
        'y': 370,
        'l': 100,
        'h': 30
    },
    {
        'type': 'collision',
        'name': 'Collision',
        'color': 0,
        'x': 270,
        'y': 440,
        'l': 100,
        'h': 30
    }
]

panel = [
    {
        'type': 'scale',
        'name': 'Scale: ',
        'color': 0,
        'x': 0,
        'y': 0,
        'l': 100,
        'h': 30
    },
    {
        'type': 'time',
        'name': 'Time: ',
        'color': 0,
        'x': 0,
        'y': 20,
        'l': 100,
        'h': 30
    }

]

buttons = {
    'menu': menu_buttons,
    'config': config_buttons,
    'panel': panel
}
