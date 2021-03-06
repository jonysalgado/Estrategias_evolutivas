import math
from Constants.constants import M2PIX

def clamp(value, min, max):
    """
    Clamps a value to keep it within the interval [min, max].

    :param value: value to be clamped.
    :param min: minimum value.
    :param max: maximum value.
    :return: clamped value.
    """
    if value > max:
        return max
    elif value < min:
        return min
    return value


class Vector2(object):
    """
    Represents a bidimensional geometric vector.
    """
    def __init__(self, x, y):
        """
        Creates a bidimensional geometric vector.

        :param x: x coordinate.
        :type x: float
        :param y: y coordinate.
        :type y: float
        """
        self.x = x
        self.y = y
    
    def normalize(self):
        m = self.magnitude()
        if m == 0:
            self.x = 1
            m = 1
        self.x /= m
        self.y /= m

    def dot(self, v):
        return self.x * v.x + self.y * v.y

    def magnitude(self):
        return math.sqrt((self.x)**2 + (self.y)**2)

    # padronization: angle in degrees
    def rotation(self, angle):
        return Vector2(self.x*math.cos(angle), self.y*math.sin(angle))

class Pose(object):
    """
    Represents a pose on the plane, i.e. a (x, y) position plus a rotation.
    """
    def __init__(self, x, y, rotation):
        """
        Creates a pose on the plane.

        :param x: x coordinate.
        :type x: float
        :param y: y coordinate.
        :type y: float
        :param rotation: rotation around z axis.
        :type rotation: float
        """
        self.position = Vector2(x, y)
        self.rotation = rotation

class TransformCartesian(object):

    def __init__(self, linear_speed, rotation):
        self.x = linear_speed * math.cos(rotation)
        self.y = linear_speed * math.sin(rotation)

class TransformPolar(object):
    
    def __init__(self, x, y):
        self.linear_speed = math.sqrt(x**2 + y**2)
        if x > 1.0e-03:
            self.rotation = math.atan(y/x)
        elif y > 0:
            self.rotation = math.pi
        else:
            self.rotation = -1*math.pi
        if x < 0:
            self.rotation += math.pi


class function_linear(object):

    def __init__(self, total_angle, centerPos):
        self.total_angle = total_angle
        self.centerPos = centerPos
        self.a, self.b = self.calcAB()
        # print("a,b, total:",self.a,self.b, self.total_angle)

    def calcAB(self):
        y0 = round(self.centerPos.position.y  * M2PIX)
        x0 = round(self.centerPos.position.x  * M2PIX)
        a = math.tan(self.total_angle)
        b = y0 - a*x0
        return a, b
    
    def y(self, x):
        return self.a*x + self.b

    def x(self, y):
        return (y - self.b)/self.a

        
