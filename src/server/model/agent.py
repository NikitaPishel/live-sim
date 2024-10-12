from random import randint
import genome as gnm
import data_structures as dts

class Agent:
    def __init__(self, x=0, y=0):
        self.position = [x, y]
        self.direction = 0 # 0-7 from top clockwise
        self.gen = gnm.Genome() # decision map of an agent
        self.active = True

    def getVision(self):
        pass

    def getSensors(self):
        pass

def createRandomAgent():
    randAgent = Agent(0, 0)

    randAgent.active = True
    randAgent.direction = randint(0, 7)
    randAgent.genome = gnm.randomGenome()