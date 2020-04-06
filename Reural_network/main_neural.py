import numpy as np
from Constants.constants import * 
from Reural_network.neural_utils import *


class main_neural(object):

    def __init__(self, players):
        self.n_cars = len(players)
        self.players = players
        self.networks = self.initNetworks(self.n_cars)
        
        


    def initNetworks(self, n_cars):
        networks = []
        for i in range(n_cars):
            networks.append(Network(NEURAL_SIZE))
        
        return networks

    def resetNetworks(self, better_car):
        network = self.networks[better_car]
        print("melhor:",self.networks[better_car].biases[0])
        for i in range(self.n_cars):
            if i != better_car:
                self.networks[i].replace(network.biases, network.weights)
        print(self.networks[better_car].biases[0])

    def updatePlayers(self):
        for i in range(self.n_cars):
            if self.players[i].controllable == False:
                inputNeural = []
                for j in range(12):
                    sensor = self.players[i].sensors[j].distance()
                    inputNeural.append(sensor[1])
                inputNeural.append(self.players[i].linear_speed)
                inputNeural.append(self.players[i].angular_speed)

                output = self.networks[i].feedforward(inputNeural)
                self.players[i].networkController(output)



class Network(object):

    def __init__(self, sizes):
        self.num_layers = len(sizes)
        self.sizes = sizes
        self.biases = [np.random.randn(y, 1) for y in sizes[1:]]
        self.weights = [np.random.randn(y, x) for x, y in zip(sizes[:-1], sizes[1:])]

    def feedforward(self, inputNeural):
        for b,w in zip(self.biases, self.weights):
            inputNeural = sigmoid(np.dot(w, inputNeural) + b)
        return inputNeural

    def replace(self, biases, weights):

        # mutation
        for i in range(len(biases)):
            array = biases[i]
            for j in range(len(array)):
    
                array[j] = array[j] + np.random.randn()
            
            self.biases[i] = array

        for i in range(len(weights)):
            array = weights[i]
            for j in range(array.shape[0]):
                for k in range(array.shape[1]):
                    array[j,k] = array[j,k] + np.random.randn()
            
            self.weights[i] = array
        






    