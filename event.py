import pygame
from const import *
pygame.init()
def CheckDraw(M, A, B):
    keys = pygame.key.get_pressed()

    if keys[pygame.K_ESCAPE]:
        exit()


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
