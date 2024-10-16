from random import randint
import genome as gnm
import data_structures as dts

class Agent:
    def __init__(self, x=0, y=0):
        self.position = [x, y]
        self.direction = 0 # 0-7 from top clockwise

        self.sensors = [] # decision map of an agent
        self.id = 0
        self.active = True

        gnm.genMutation(self.sensors)

    def getVision(self):
        pass

    def getSensors(self):
        pass