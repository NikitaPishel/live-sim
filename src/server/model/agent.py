import random as rnd

import genome as gnm
from configuration import config
import neuronCmd as nrnCmd

class Agent:
    def __init__(self, x=0, y=0):
        self.pos = [x, y]
        self.dir = 0 # 8 directions 0 to 7 from down clockwise (south=0, south-east=1, east=2, etc.)

        self.gene = gnm.GeneRoot() # decision map of an agent
        
        rndSensor = gnm.Sensor()
        rndCmd = rnd.choice(nrnCmd.inputCmd)
        rndSensor.cmd = rndCmd
        self.gene.joints.append(rndSensor)
    
    def clone(self):
        agentClone = Agent()

        agentClone.pos = self.pos
        agentClone.dir = self.dir
        agentClone.gene = self.gene

        return agentClone
