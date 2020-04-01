import pygame
from pygame.rect import Rect
from pygame.gfxdraw import pie
from math import sin, cos, sqrt
from Constants.constants import *
from utils import *


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

    # def check_collision(self):
    #     """
    #     Checks collision between the robot and the walls.

    #     :return: the bumper state (if a collision has been detected).
    #     :rtype: bool
    #     """

    
    # def check_goal(self):
    #     """
    #     Check how far is a player.
    #     """
        

    # def restard_game(self):
    #     """
    #     Put a player on initial position.
    #     """


    # def update(self):
    #     """
    #     Updates the simulation.
    #     """
    #     # Adding roomba's current position to the movement history
    #     # self.point_list.append((round(M2PIX * self.player[NUM_1].pose.position.x), round(M2PIX * self.player[NUM_1].pose.position.y)))
    #     # if len(self.point_list) > 2000:
    #     #     self.point_list.pop(0)
    #     # Verifying collision
        
        

    def draw(self, window, cars):
        """
        Draws the roomba and its movement history.

        :param window: pygame's window where the drawing will occur.
        """
        cars[0] = pygame.transform.scale(cars[0], (CARS_HEIGHT, CARS_WIDTH))
        # cars[0] = pygame.transform.rotate(cars[0], 90)  
        window.blit(cars[0], (0,0))
        

    

def draw(simulation, window, collision_array, cars):
    """
    Redraws the pygame's window.

    :param simulation: the simulation object.
    :param window: pygame's window where the drawing will occur.
    """
    

    simulation.draw(window, cars)
    pygame.display.update()



