from utils import Pose, function_linear
from math import pi, fabs, sqrt, cos
from Constants.constants import SCREEN_WIDTH, SCREEN_HEIGHT, M2PIX
import matplotlib.pyplot as plt


class Sensors(object):

    def __init__(self, collide_array, center_player, number):
        """
        angle: angle in radian
        """
        self.collide_array = collide_array
        self.centerPose = center_player
        self.number = number
        self.angle = 2*pi*number/12


    def totalAngle(self):
        return self.angle + self.centerPose.rotation

    def normalAngle(self, angle):
        """
        Return a angle between 0 and 2*pi
        """

        while angle >= 2*pi:
            angle -= 2*pi
        
        while angle < 0:
            angle += 2*pi
        
        return angle

    def distance(self):
        centerY = self.centerPose.position.y * M2PIX
        centerX = self.centerPose.position.x * M2PIX
        totalAngle = self.totalAngle()
        if fabs(self.normalAngle(totalAngle) - pi/2) < 1.0e-3:
            point = self.getFinalPosition(1)
            if point != None:
                distance = sqrt((point[0]-centerX)**2 + (point[1]-centerY)**2)
            else:
                distance = 0
                point = (centerX,centerY)
            return point, distance
        
        elif fabs(self.normalAngle(totalAngle) - 3*pi/2) < 1.0e-3:
            point = self.getFinalPosition(2)
            if point != None:
                distance = sqrt((point[0]-centerX)**2 + (point[1]-centerY)**2)
            else:
                distance = 0
                point = (centerX,centerY)
            return point, distance

        elif cos(self.normalAngle(totalAngle)) > 0:
            point = self.getFinalPosition(3)
            if point != None:
                distance = sqrt((point[0]-centerX)**2 + (point[1]-centerY)**2)
            else:
                distance = 0
                point = (centerX,centerY)
            return point, distance
        
        elif cos(self.normalAngle(totalAngle)) < 0:
            point = self.getFinalPosition(4)
            if point != None:
                distance = sqrt((point[0]-centerX)**2 + (point[1]-centerY)**2)
            else:
                distance = 0
                point = (centerX,centerY)
            return point, distance


    def getFinalPosition(self, case):
        centerY = self.centerPose.position.y * M2PIX
        centerX = self.centerPose.position.x * M2PIX
        # angle is 90 degrees
        if case == 1:
            for i in range(round(centerY), SCREEN_HEIGHT):
                if self.is_index_valid(round(centerX), i):
                    if self.collide_array[round(centerX), i] == 0:
                        point = (centerX, i)
                        return point

        # angle is 270 degrees
        elif case == 2:
            for i in range(round(centerY), 0, -1):
                if self.is_index_valid(round(centerX), i):
                    if self.collide_array[round(centerX), i] == 0:
                        point = (centerX, i)
                        return point
            
        # angle is between 3*pi/2 and pi/2
        elif case == 3:
            function = function_linear(self.normalAngle(self.totalAngle()), self.centerPose)
            for i in range(round(centerX), SCREEN_WIDTH):
                j = function.y(i)
                if self.is_index_valid(i, round(j)):
                    if self.collide_array[i, round(j)] == 0:
                        point = (i, j)
                        return point

        # angle is between pi/2 and 3*pi/2
        elif case == 4:
            function = function_linear(self.normalAngle(self.totalAngle()), self.centerPose)
            for i in range(round(centerX), 0, -1):
                j = function.y(i)
                if self.is_index_valid(i, round(j)):
                    if self.collide_array[i, round(j)] == 0:
                        point = (i, j)
                        return point

    def is_index_valid(self, i, j):
        return 0 <= i < SCREEN_WIDTH and 0 <= j < SCREEN_HEIGHT

    def update(self, center_player):

        self.centerPose = center_player

        




    
