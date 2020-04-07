import numpy as np
from Constants.constants import * 
from Reural_network.neural_utils import *


class main_neural(object): # essa classe armazena a rede de cada carrinho

    def __init__(self, players): # players é um array de players
        self.n_cars = len(players)
        self.players = players
        self.networks = self.initNetworks(self.n_cars)
        
        


    def initNetworks(self, n_cars):
        networks = []
        for i in range(n_cars):
            networks.append(Network(NEURAL_SIZE))    
        
        return networks

    def resetNetworks(self, distance):
        # clonning
        elitism = round(ELITISM_RATE * self.n_cars)
        for i in range(elitism):
            j = elitism + i
            while j < self.n_cars:
                network = self.networks[i]
                self.networks[j].replace(network.biases, network.weights)
                j += elitism

        for i in range(elitism, self.n_cars):
            self.networks[i].back_propagation()
        

            

    def updatePlayers(self):
        for i in range(self.n_cars):
            if self.players[i].controllable == False:
                inputNeural = []
                for j in range(N_SENSORS):
                    sensor = self.players[i].sensors[j].distance()
                    inputNeural.append(sensor[1])
                inputNeural.append(self.players[i].linear_speed)
                inputNeural.append(self.players[i].angular_speed)
                inputNeural = np.array(inputNeural)

                output = self.networks[i].feedforward(inputNeural)
                self.players[i].networkController(output)
        





class Network(object):

    def __init__(self, sizes):
        self.num_layers = len(sizes)
        self.sizes = sizes
        self.biases = [np.random.randn(y) for y in sizes[1:]]
        self.weights = [np.random.randn(y, x) for x, y in zip(sizes[:-1], sizes[1:])]

    def feedforward(self, inputNeural):
        for b,w in zip(self.biases, self.weights):
            inputNeural = sigmoid(np.dot(w, inputNeural) + b)

        return inputNeural

    def replace(self, biases, weights):

        # reproduction
        self.biases = biases
        self.weights = weights
        
    def back_propagation(self):

        # mutation
        tipo = np.random.randint(0, 1000)%3
        if tipo == 0:
            self.biases = [np.random.randn(y) for y in self.sizes[1:]]
            self.weights = [np.random.randn(y, x) for x, y in zip(self.sizes[:-1], self.sizes[1:])]
            
        elif tipo == 1:
            biases = self.biases
            self.biases = []
            for element in biases:
                rand = element + 2 * np.random.randn(element.shape[0])
                self.biases.append(rand)

            weights = self.weights
            self.weights = []
            for element in weights:
                rand = element + 2 * np.random.randn(element.shape[0], element.shape[1])
                self.weights.append(rand)
        
        else:
            biases = self.biases
            self.biases = []
            for element in biases:
                rand = element * np.random.randn(element.shape[0])
                self.biases.append(rand)

            weights = self.weights
            self.weights = []
            for element in weights:
                rand = element * np.random.randn(element.shape[0], element.shape[1])
                self.weights.append(rand)






    