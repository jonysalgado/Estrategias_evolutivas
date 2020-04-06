from main_neural import *

rede = Network([14,1,4])
input = [300,300,300,300,300,300,300,300,300,300,300,300,300,300]

output = rede.feedforward(input)
for i in range(len(output)):
    if output[i] >= 0.5:
        output[i] = True
    else:
        output[i] = False
print(output)