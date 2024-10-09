from random import randint
from genome import randomGenome

class agent:
    def __init__(self, x=0, y=0):
        self.position = [x, y]
        self.direction = 0 # 0-7 from top clockwise
        self.genome = [] # decision tree
        self.active = True

    def getVision(self):
        pass

def createRandomAgent():
    randAgent = agent(0, 0)

    randAgent.active = True
    randAgent.direction = randint(0, 7)
    randAgent.genome = genome.randomGenome()