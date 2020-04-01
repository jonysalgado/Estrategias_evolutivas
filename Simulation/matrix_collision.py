# from simulation import *
import pygame
from pygame.rect import Rect
from pygame.gfxdraw import pie
from math import pi
import numpy as np
from Constants.constants import *
from PIL import Image

def  drawBackgroundImage(window):
    fundo = pygame.image.load('./Img/star.png')
    fundo = pygame.transform.scale(fundo, (SCREEN_WIDTH, SCREEN_HEIGHT))
    pista = pygame.image.load('./Img/pista.png')
    pista = pygame.transform.scale(pista, (SCREEN_WIDTH -200, SCREEN_HEIGHT))   

    window.blit(fundo, (0,0))
    window.blit(pista, (200,0))
    
    return matrixCollision(window)

def matrixCollision(window):
    pxarray = pygame.PixelArray(window)
    
    array = np.array(pxarray)
    for i in range(SCREEN_WIDTH):
        for j in range(SCREEN_HEIGHT):
            if array[i,j] == COLOR_TRACK:
                array[i,j] = 1
            else:
                array[i,j] = 0
    
    return array