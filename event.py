import pygame
import sys
from const import *
pygame.init()

def CheckMenu(RUN):
    run = RUN
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            for button in buttons['menu']:
                get_clicked = event.button == 1
                get_pos_right = event.pos[0] < (button['x'] + button['l'])
                get_pos_left = event.pos[0] > (button['x'])
                get_pos_down = event.pos[1] < (button['y'] + button['h'])
                get_pos_up = event.pos[1] > (button['y'])
                get_pos = get_pos_right&get_pos_left&get_pos_up&get_pos_down
                if get_clicked and get_pos:
                    run['menu'] = False
                    if button['type']=='exit':
                        run['exit'] = True
                        sys.exit()
                    if button['type']=='start':
                        run['game'] = True
                    if button['type']=='config':
                        run['config']= True

    return run

def CheckConfig(RUN, KEY):
    key = KEY
    run = RUN
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            for button in buttons['config']:
                get_clicked = event.button == 1
                get_pos_right = event.pos[0] < (button['x'] + button['l'])
                get_pos_left = event.pos[0] > (button['x'])
                get_pos_down = event.pos[1] < (button['y'] + button['h'])
                get_pos_up = event.pos[1] > (button['y'])
                get_pos = get_pos_right&get_pos_left&get_pos_up&get_pos_down
                if get_clicked and get_pos:
                    run['config'] = False
                    if button['type']=='sun-system':
                        run['menu'] = True
                        key = button['type']
                    if button['type']=='double-star':
                        run['menu'] = True
                        key = button['type']

    return run, key

def Check(RUN):
    run = RUN
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    keys = pygame.key.get_pressed()

    if keys[pygame.K_ESCAPE]:
        run['game'] = False
        run['menu'] = True

    return run

def CheckDraw(M, A, B):
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        A -= A0

    if keys[pygame.K_RIGHT]:
        A += A0


    if keys[pygame.K_UP]:
        B -= B0

    if keys[pygame.K_DOWN]:
        B += B0


    if keys[pygame.K_w]:
        M += M0

    if keys[pygame.K_s]:
        M -= M0

    return M, A, B
def CheckCalc(dt):
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        dt -= dt0

    if keys[pygame.K_d]:
        dt += dt0

    if keys[pygame.K_0]:
        dt = 0 #остановка объектов

    return dt
