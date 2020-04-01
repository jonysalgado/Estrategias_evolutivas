from math import pi
# Simulation Parameters
# soccer field (105,68) x 6
SCREEN_WIDTH = 1000 # 636
SCREEN_HEIGHT = 650 # 414
PIX2M = 0.01  # factor to convert from pixels to meters
M2PIX = 100.0  # factor to convert from meters to pixels

# Sample Time Parameters
FREQUENCY = 60.0  # simulation frequency
SAMPLE_TIME = 1.0 / FREQUENCY  # simulation sample time

# colors
COLOR_WHITE = (255,255,255)
COLOR_GRAY = (70, 66, 47)
COLOR_BLACK = (0, 0, 0)
COLOR_TRACK = 16777215

# cars dimensions
CARS_WIDTH = 25
CARS_HEIGHT = 45