import pygame
from pygame.rect import Rect
from pygame.gfxdraw import pie
from math import sin, cos, sqrt
from Constants.constants import *
from utils import *
from Simulation.matrix_collision import drawBackgroundImage


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

    def set_collisionArray(self, collision_array):

        self.collision_array = collision_array
        self.player[0].set_collision_array(collision_array)

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


    def update(self, carsParameters):
        """
        Updates the simulation.
        """
        self.player[0].update(carsParameters)
        # Adding roomba's current position to the movement history
        # self.point_list.append((round(M2PIX * self.player[NUM_1].pose.position.x), round(M2PIX * self.player[NUM_1].pose.position.y)))
        # if len(self.point_list) > 2000:
        #     self.point_list.pop(0)
        # Verifying collision
        
        

    def draw(self, window, cars, mapParameters):
        """
        Draws the roomba and its movement history.

        :param window: pygame's window where the drawing will occur.
        """
        
        
        # draw map
        scale = 1
        position = (0,0)
        drawBackgroundImage(self, window, mapParameters, cars, self.collision_array)
        

    

def draw(simulation, window, cars, mapParameters):
    """
    Redraws the pygame's window.

    :param simulation: the simulation object.
    :param window: pygame's window where the drawing will occur.
    """
    
    # print(simulation.player[0].pose.rotation)
    simulation.draw(window, cars, mapParameters)
    pygame.display.update()



