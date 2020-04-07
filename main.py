from Constants.constants import *
from Utils.utils import Pose
from Player.player import Player
from Simulation.simulation import *
from Simulation.Scenario import Scenario
from Simulation.keyboard import Keyboard
import numpy as np
# pegartempo
import time



pygame.init()
window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
icon = pygame.image.load("./Img/icon.png")
pygame.display.set_caption("Carros autonâmos")
clock = pygame.time.Clock()
pygame.display.set_icon(icon)


# init players
players = []
for i in range(N_PLAYERS):
    pose = Pose(PIX2M * round(907 + i*65/N_PLAYERS), PIX2M * 435, -pi/2)
    players.append(Player(pose, 3 * FORWARD_SPEED, 3 * ANGULAR_SPEED, i))

player = np.array(players)

simulation = Simulation(player)
# cars
cars = []
for i in range(N_PLAYERS):
    cars.append(pygame.image.load("./Img/carro"+str(i%7)+".png"))

# collision array
scale = 1
position = (0,0)
mapParameters = [scale, position]
carsParameters = []
simulation.initScenario(window, mapParameters, cars)

user = input("Deseja jogar também?(y/n)")
while user not in ['y', 'Y', 'n', 'N']:
    user = input("Deseja jogar também?(y/n)")

# remove after
# user = 'y'
run = True
key = None
while run:
    # pegartempo
    init = time.time()
    clock.tick(FREQUENCY)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.KEYDOWN:
            mapParameters, carsParameters = Keyboard(event.key, mapParameters, carsParameters)
        else:
            key = None
    if key == None:
        mapParameters, carsParameters = Keyboard(key, mapParameters, carsParameters)
    if user in ['n', 'N']:
        carsParameters = []
    draw(simulation)
    simulation.update(carsParameters)
    # fim = time.time()
    # pegartempo
    # print(init - fim)


pygame.quit()
