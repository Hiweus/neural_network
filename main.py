#!/usr/bin/env python3
from random import random
class Neuron:
    weigth = []
    length = 0
    
    def __init__(self, numberOfInputs):

        #inicializa os pesos
        for i in range(numberOfInputs):
            self.weigth+=[random()]

        #salva o numero de entradas
        self.length = numberOfInputs

    def ajust(self, value):

        #soma o valor de correcao no neuroio
        for i in range(self.length):
            self.weigth[i] += value

    def compute(self, inputs):

        #processa a informacao
        output = 0
        for i in range(self.length):
            output += (inputs[i]*self.weigth[i])
        return output


class Layer:
    neurons = []
    length = 0
    numberOfInputs = 0
    def __init__(self, numberOfNeurons, numberOfInputs):
        self.length = numberOfNeurons
        self.numberOfInputs = numberOfInputs
        for i in range(numberOfNeurons):
            self.neurons += [Neuron(numberOfInputs)]

    def compute(self, inputs):
        out = []
        for i in self.neurons:
            out += [i.compute(inputs)]
        return out

    def ajust(self, value):
        for i in self.neurons:
            i.ajust(value)


class Network:
    layers = []
    length = 0
    numberOfInputs = 0
    end = None

    def __init__(self, numberOfInputs, numberOfLayers, NeuronsInMiddle):
        self.length = numberOfLayers
        self.end = Neuron(numberOfInputs)

        for i in range(numberOfLayers):
            self.layers += [Layer(NeuronsInMiddle, numberOfInputs)]
        
    def compute(self, inputs):
        out = inputs
        for i in self.layers:
            out = i.compute(out)
        
        out = self.end.compute(out)
        return out

    def ajust(self,value):
        for i in self.layers:
            i.ajust(value)
        self.end.ajust(value)


###################################################

def end(value):
    return 1 if value > 0.5 else 0


q = [[0,0],[0,1],[1,0],[1,1]]
r = [0,1,1,1]

n = Network(2,1,5)

for i in range(len(q)):
    out = n.compute(q[i])
    erro = r[i] - end(out)
    n.ajust(erro)



for i in q:
    rr = end(n.compute(i))
    print(str(i)+" > "+str(rr))
