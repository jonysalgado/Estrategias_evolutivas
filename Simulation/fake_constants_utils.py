# constants
SCREEN_WIDTH = 900
SCREEN_HEIGHT = 700
PIX2M = 0.01  # factor to convert from pixels to meters
M2PIX = 100.0  # factor to convert from meters to pixels
RADIUS_PLAYER = 0.15
TRACK_WIDTH = 7 * RADIUS_PLAYER * M2PIX
# colors
COLOR_WHITE = (255,255,255)
COLOR_GRAY = (70, 66, 47)
COLOR_BLACK = (0, 0, 0)
COLOR_TRACK = (71, 74, 81)

class Point(object):

    def __init__(self, x, y):
        
        self.x = x
        self.y = y

    def displacement(self, x, y):
        return Point(self.x + x, self.y + y)

    def ToTuple(self):
        return (self.x, self.y)