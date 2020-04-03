from Constants.constants import *
from utils import Pose
from Player.player import Player
from Simulation.simulation import *
from Simulation.matrix_collision import drawBackgroundImage, matrixCollision
from Player.state_machine import FiniteStateMachine, MoveForwardState
from Simulation.keyboard import Keyboard
import numpy as np



pygame.init()

window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
icon = pygame.image.load("./Img/icon.png")
pygame.display.set_caption("Estratégias evolutivas")
clock = pygame.time.Clock()
pygame.display.set_icon(icon)

behavior = FiniteStateMachine(MoveForwardState())
pose = Pose(PIX2M * 932, PIX2M * 435, -pi/2)
player = np.array([Player(pose, 1.0, 2.0, behavior, 0)])
simulation = Simulation(player)

# cars
cars = []
for i in range(7):
    cars.append(pygame.image.load("./Img/carro"+str(i)+".png"))

# collision array
scale = 1
position = (0,0)
mapParameters = [scale, position]
carsParameters = []
drawBackgroundImage(simulation, window, mapParameters, cars, None, True)
collision_array = matrixCollision(window)

simulation.set_collisionArray(collision_array)


# user = input("Deseja jogar também?(y/n)")
# while user not in ['y', 'Y', 'n', 'N']:
#     user = input("Deseja jogar também?(y/n)")

# remove after
user = 'y'
run = True
key = None
while run:
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
        carsParameters = None
    draw(simulation, window, cars, mapParameters)
    simulation.update(carsParameters)


pygame.quit()
