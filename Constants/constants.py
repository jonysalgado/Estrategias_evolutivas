from math import pi
# Simulation Parameters
# big screen
# SCREEN_WIDTH = 1600 
# SCREEN_HEIGHT = 920 
# Small screen
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 650
PIX2M = 0.01  # factor to convert from pixels to meters
M2PIX = 100.0  # factor to convert from meters to pixels
RAD2DEGREE = 180/pi

# Sample Time Parameters
FREQUENCY = 60.0  # simulation frequency
SAMPLE_TIME = 1.0 / FREQUENCY  # simulation sample time

# colors
COLOR_WHITE = (255,255,255)
COLOR_GRAY = (70, 66, 47)
COLOR_BLACK = (0, 0, 0)
COLOR_TRACK = (110, 110, 110)
COLOR_SENSOR = (0, 132, 180)
COLOR_RED = (248, 1, 3)
COLOR_YELLOW = (255, 255, 0)


# cars dimensions
CARS_WIDTH = 18
CARS_HEIGHT = 35

# sensor dimension
SENSOR_HEIGHT = CARS_HEIGHT - 10

# Move Parameters
FORWARD_SPEED = 3.0
BACKWARD_SPEED = -1.0
ANGULAR_SPEED = 2.0

# Finish line
FINISH_LINE = ((906,506), (976, 506))

# cost start
COST_START = 2750
INITIAL_DISTANCE = 2627

# Pressing array
KEY_A = 97
KEY_D = 100
KEY_S = 115
KEY_W = 119
KEY_UP = 273
KEY_DOWN = 274
KEY_LEFT = 276
KEY_RIGHT = 275
