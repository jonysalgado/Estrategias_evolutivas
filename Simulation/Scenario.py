import pygame
from pygame.rect import Rect
from pygame.gfxdraw import pie
from math import pi, sqrt
import numpy as np
from Constants.constants import *
# remove after
import matplotlib.pyplot as plt


class Scenario(object):
    def __init__(self, simulation, window, mapParameters, cars, initial):
        self.simulation = simulation
        self.window = window
        self.mapParameters = mapParameters
        self.cars = cars
        self.collision_array = None
        self.initial = initial
        self.cost_array = None
        self.n_players = simulation.number_players
        

    def  drawBackgroundImage(self):
        fundo = pygame.image.load('./Img/star.png')
        fundo = pygame.transform.scale(fundo, (SCREEN_WIDTH, SCREEN_HEIGHT))
        pista = pygame.image.load('./Img/pista.png')
        pista = pygame.transform.scale(pista, (SCREEN_WIDTH -200, SCREEN_HEIGHT))

        sensorPoint = pygame.image.load("./Img/luzAzul.png")
        sensorPoint = pygame.transform.scale(sensorPoint, (SENSOR_HEIGHT, SENSOR_HEIGHT))  
        
        
        if self.initial == False:
            self.window.blit(fundo, (0,0))
        self.window.blit(pista, (200,0))


        # cars
        for i in range(self.n_players):
            self.cars[i] = pygame.transform.scale(self.cars[i], (CARS_HEIGHT, CARS_WIDTH))
            car_rotate = pygame.transform.rotate(self.cars[i], round(-self.simulation.player[i].pose.rotation * RAD2DEGREE)%360)
            burntCar = pygame.image.load("./Img/carroQueimado.png")
            burntCar = pygame.transform.scale(burntCar, (CARS_HEIGHT, CARS_WIDTH))
            x = M2PIX * self.simulation.player[i].pose.position.x
            y = M2PIX * self.simulation.player[i].pose.position.y
            # print(x, y)
            if self.initial == False:
                collide = self.simulation.player[i].bumper_state
                if collide == False:
                    if i == 0:
                        self.drawSensors(self.simulation.player[i].sensors, (x,y), sensorPoint)
                    self.window.blit(car_rotate, (x-car_rotate.get_rect().center[0], y-car_rotate.get_rect().center[1]))
                else:
                    # explosion = []
                    # if self.simulation.player[i].animationFrame != 45:
                    #     for j in range(1, 45):
                    #         explosion.append(pygame.image.load("./Img/explosion/exp (" + str(j) + ").png"))
                    #         explosion[j-1] = pygame.transform.scale(explosion[j-1], (200, 200))
                    burntCar = pygame.transform.rotate(burntCar, round(-self.simulation.player[i].pose.rotation * RAD2DEGREE)%360)
                    self.window.blit(burntCar, (x-burntCar.get_rect().center[0], y-burntCar.get_rect().center[1]))
                    # if self.simulation.player[i].animationFrame < 45:
                    #     # self.window.blit(explosion[self.simulation.player[i].animationFrame - 1], (x-100, y-100))
                    #     self.simulation.player[i].animationFrame += 1

        self.drawScore()
        windowScale = pygame.transform.scale(pygame.display.get_surface(), (SCREEN_WIDTH * self.mapParameters[0], SCREEN_HEIGHT * self.mapParameters[0]))
        self.window.fill((0,0,0))
        self.window.blit(windowScale, self.mapParameters[1])


    def drawSensors(self, sensors, centerPos, sensorPoint):
        if self.simulation.player[0].controllable != False:
            for i in range(N_SENSORS):
                pygame.draw.line(self.window, COLOR_SENSOR, sensors[i].distance()[0], centerPos, 1)
                center = sensors[i].distance()[0]
                self.window.blit(sensorPoint, (center[0] - SENSOR_HEIGHT/2, center[1] - SENSOR_HEIGHT/2))

        
    def drawScore(self):
        
        font = pygame.font.SysFont('Comic Sans MS', 30)
        generation = "Geração: " + str(self.simulation.generation)
        textsurface = font.render(generation, False, (255, 255, 255))
        self.window.blit(textsurface, (20,200))
        distance = "Melhor distância: "
        textsurface = font.render(distance, False, (255, 255, 255))
        self.window.blit(textsurface, (15,240))
        distance = str(self.simulation.better_distance * M2PIX) + " pix"
        textsurface = font.render(distance, False, (255, 255, 255))
        self.window.blit(textsurface, (100,265))

        if self.simulation.better_distance >= (INITIAL_DISTANCE - 2) * PIX2M:
            conclusion = "Eu aprendi a dirigir, Jony!"
            textsurface = font.render(conclusion, False, (255, 255, 255))
            self.window.blit(textsurface, (15,300))

    def matrixCollision(self):
        pxarray = pygame.PixelArray(self.window)
        array = np.array(pxarray, dtype="int32")
        for i in range(SCREEN_WIDTH):
            for j in range(SCREEN_HEIGHT):
                if array[i,j] < self.window.map_rgb((110,110,110)):
                    array[i, j] = 0
                elif  array[i,j] >= self.window.map_rgb((118,118,118)):
                    array[i, j] = 0
                else:
                    array[i,j] = 1
        # plt.matshow(array)
        # plt.show()
        self.collision_array = array
        self.cost_function()
        self.initial = False
        return array

    
    def cost_function(self):
        array = np.copy(self.collision_array)
        nodeArray = np.empty((SCREEN_WIDTH, SCREEN_HEIGHT), dtype=Node)

        # preparing array
        for i in range(SCREEN_WIDTH):
            for j in range(SCREEN_HEIGHT):
                if array[i,j] == 0:
                    nodeArray[i, j] = Node(i,j,-1)
                else:
                    nodeArray[i, j] = Node(i,j,-2)

        # queue of pixels
        queue = []
        # set zero for finish line
        initialPoint = FINISH_LINE[0]
        finishPoint = FINISH_LINE[1]
        for i in range(initialPoint[0], finishPoint[0] + 1):
            nodeArray[i, initialPoint[1]].setCost(0)
            queue.append(nodeArray[i, initialPoint[1]])


        while len(queue) != 0:
            node = queue.pop(0)
            # print(type(node.neighbor))
            for nodes in node.neighbor:
                if nodeArray[nodes].cost == -2:
                    queue.append(nodeArray[nodes])
                    nodeArray[nodes].setCost(node.cost + 1)

        
        for i in range(SCREEN_WIDTH):
            for j in range(SCREEN_HEIGHT):
                array[i, j] = nodeArray[i,j].cost

        self.cost_array = array
        # plt.matshow(array)
        # plt.show()
        self.simulation.resetTime()



class Node(object):

    def __init__(self, i, j, cost):
        
        self.i = i
        self.j = j
        self.cost = cost
        self.neighbor = self.getNeighbor()

    def setCost(self, cost):
        
        self.cost = cost

    def getNeighbor(self):
        neighbor = []
        for di in range(-1,2):
            for dj in range(-1,2):
                if self.is_index_valid(self.i+di, self.j+dj) and (di != 0 or dj != 0):
                    neighbor.append((self.i+di, self.j+dj))
            
        return neighbor

    def is_index_valid(self, i, j):
        return 0 <= i < SCREEN_WIDTH and 0 <= j < SCREEN_HEIGHT

    