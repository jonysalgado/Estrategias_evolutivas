# from simulation import *
import pygame
from pygame.rect import Rect
from pygame.gfxdraw import pie
from math import pi, sqrt
import numpy as np
from Constants.constants import *
import matplotlib.pyplot as plt

def  drawBackgroundImage(simulation, window, mapParameters, cars, collision_array=None, initial = False):
    fundo = pygame.image.load('./Img/star.png')
    fundo = pygame.transform.scale(fundo, (SCREEN_WIDTH, SCREEN_HEIGHT))
    pista = pygame.image.load('./Img/pista.png')
    pista = pygame.transform.scale(pista, (SCREEN_WIDTH -200, SCREEN_HEIGHT))
    sensorPoint = []
    for i in range(12):
        sensorPoint.append(pygame.image.load('./Img/luzAzul.png'))
        sensorPoint[i] = pygame.transform.scale(sensorPoint[i], (CARS_HEIGHT - 10, CARS_HEIGHT - 10))  
    
    
    if initial == False:
        window.blit(fundo, (0,0))
    window.blit(pista, (200,0))


    # cars
    cars[0] = pygame.transform.scale(cars[0], (CARS_HEIGHT, CARS_WIDTH))
    a = pygame.transform.rotate(cars[0], round(-simulation.player[0].pose.rotation * RAD2DEGREE)%360)
    x = M2PIX * simulation.player[0].pose.position.x
    y = M2PIX * simulation.player[0].pose.position.y 
    if initial == False:
        testSensors(simulation.player[0].sensors, window, (x,y), sensorPoint)
        window.blit(a, (x-a.get_rect().center[0], y-a.get_rect().center[1]))
        testMatrixCollision((round(x), round(y)), collision_array)




    windowScale = pygame.transform.scale(pygame.display.get_surface(), (SCREEN_WIDTH * mapParameters[0], SCREEN_HEIGHT * mapParameters[0]))
    window.fill((0,0,0))
    window.blit(windowScale, mapParameters[1])


def testSensors(sensors, window, centerPos, sensorPoint):

    for i in range(12):
        pygame.draw.line(window, COLOR_SENSOR, sensors[i].distance()[0], centerPos, 1)
        center = sensors[i].distance()[0]
        window.blit(sensorPoint[i], (center[0] - CARS_HEIGHT/2 + 5, center[1] - CARS_HEIGHT/2 + 5))


def testMatrixCollision(center, array):
    collide = False
    if array[center[0], center[1]] == 0:
        collide = True
    

    
    

def matrixCollision(window):
    pxarray = pygame.PixelArray(window)

    array = np.array(pxarray)
    for i in range(SCREEN_WIDTH):
        for j in range(SCREEN_HEIGHT):
            if array[i,j] != 0:    
                array[i,j] = 1
    # plt.matshow(array)
    # plt.show()
    
    return array
