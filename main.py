import sys
sys.path.insert(0, '/Player')
sys.path.insert(1, '/Simulation')

from Constants.constants import *
from utils import Pose
from Player.player import Player
from Simulation.simulation import *
from Simulation.matrix_collision import drawBackgroundImage
from Player.state_machine import FiniteStateMachine, MoveForwardState
import numpy as np


pygame.init()

window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
icon = pygame.image.load("./Img/icon.png")
pygame.display.set_caption("Estratégias evolutivas")
clock = pygame.time.Clock()
pygame.display.set_icon(icon)

behavior = FiniteStateMachine(MoveForwardState())
pose = Pose(PIX2M * SCREEN_WIDTH/3, PIX2M * SCREEN_HEIGHT/2, 0)
player = np.array([Player(pose, 1.0, 2.0, behavior, 0)])
simulation = Simulation(player)

# collision array
collision_array = drawBackgroundImage(window)

# cars
cars = []
for i in range(7):
    cars.append(pygame.image.load("./Img/carro"+str(i)+".png"))


run = True
while run:
    clock.tick(FREQUENCY)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    draw(simulation, window, collision_array, cars)
    # simulation.update()


pygame.quit()
