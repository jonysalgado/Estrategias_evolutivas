import pygame
from pygame.rect import Rect
from pygame.gfxdraw import pie
from math import sin, cos, sqrt
from Constants.constants import *
from utils import *
from Simulation.Scenario import Scenario
import datetime


class Simulation(object):
    """
    Represents the simulation.
    """
    def __init__(self, player):
        """
        Creates the simulation.

        :param roomba: the roomba robot used in this simulation.
        :type roomba: Roomba
        """
        self.point_list = []
        self.player = player
        self.number_players = len(player)
        self.collision_array = None
        self.scenario = None
        self.simulationTime = datetime.datetime.now()
        self.generation = 1
        self.better_distance = 0
        


    def resetTime(self):
        
        self.simulationTime = datetime.datetime.now()


    def initScenario(self, window, mapParameters, cars):
        
        self.scenario = Scenario(self, window, mapParameters, cars, True)
        self.scenario.drawBackgroundImage()
        collision_array = self.scenario.matrixCollision()
        self.set_collisionArray(collision_array)

    
    def set_collisionArray(self, collision_array):

        self.collision_array = collision_array
        for i in range(self.number_players):
            self.player[i].set_collision_array(collision_array)

    def checkcollision(self):
        """
        Checks collision between the robot and the walls.

        :return: the bumper state (if a collision has been detected).
        :rtype: bool
        """
        for i in range(self.number_players):
            x0 = M2PIX * self.player[i].pose.position.x
            y0 = M2PIX * self.player[i].pose.position.y
            for di in range(-1, 2):
                for dj in range(-1, 2):
                    if self.is_index_valid(round(x0) + di, round(y0) + dj):
                        if self.collision_array[round(x0) + di, round(y0) + dj] == 0:
                            self.player[i].set_bumper_state(True)
            
            if 26.27 >= PIX2M * (INITIAL_DISTANCE -  self.scenario.cost_array[round(x0), round(y0)]) > self.better_distance:
                self.better_distance =  PIX2M * (INITIAL_DISTANCE -  self.scenario.cost_array[round(x0), round(y0)])

    
    def burntCarTime(self):
        self.scenario.cost_array
        now = datetime.datetime.now()
 
        if (now - self.simulationTime).seconds%2 == 0:
            for i in range(self.number_players):
                x0 = M2PIX * self.player[i].pose.position.x
                y0 = M2PIX * self.player[i].pose.position.y
                cost = self.scenario.cost_array[round(x0), round(y0)]
                cost_limit = COST_START - 17 * (now - self.simulationTime).seconds

                if cost_limit <= cost:
                    self.player[i].set_bumper_state(True)


        

    def restart_game(self):
        """
        Put a player on initial position.
        """
        restart = True
        for i in range(self.number_players):
            if self.player[i].bumper_state == False:
                restart = False
        
        if restart == True:
            for i in range(7):
                self.player[i].pose = Pose(PIX2M * round(907 + i*65/7), PIX2M * 435, -pi/2)
                self.player[i].set_bumper_state(False)
                
                for j in range(12):
                    self.player[i].sensors[j].update(self.player[i].pose)

            self.generation += 1
            self.resetTime()


    def is_index_valid(self, i, j):
        return 0 <= i < SCREEN_WIDTH and 0 <= j < SCREEN_HEIGHT

    def update(self, carsParameters):
        """
        Updates the simulation.
        """
        for i in range(self.number_players):
            self.player[i].update(carsParameters)
        self.checkcollision()
        # laser
        self.burntCarTime()
        # restart game
        self.restart_game()
        
        

    def draw(self):
        """
        Draws the roomba and its movement history.

        :param window: pygame's window where the drawing will occur.
        """
        
        self.scenario.drawBackgroundImage()
        

    

def draw(simulation):
    """
    Redraws the pygame's window.

    :param simulation: the simulation object.
    :param window: pygame's window where the drawing will occur.
    """
    
    # print(simulation.player[0].pose.rotation)
    simulation.draw()
    pygame.display.update()



