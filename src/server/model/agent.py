import mutation as mtn
import genome as gnm
import data_structures as dts
import random as rnd

class Agent:
    def __init__(self, x=0, y=0):
        self.pos = [x, y]
        self.dir = 0 # 8 directions 0-7 from top clockwise (nort, north-east, east, etc.)

        self.gene = gnm.GeneRoot() # decision map of an agent
        self.id = 0
        self.active = True

# Temporary test files

myAgent = Agent()

myAgent.gene.joints.append(mtn.Sensor())
myAgent.gene.joints[0].cmd = rnd.choice(mtn.nrnCmd.inputCmd)

mtn.mutate(myAgent)