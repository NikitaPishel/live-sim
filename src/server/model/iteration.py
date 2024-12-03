import random as rnd

import data_structures as dts
from agent import Agent
import genome as gnm
from configuration import config

# iteration process

def runItr():
    pass

# Simulation execution code
def run():

    agents - dts.avlTree()
    for i in range(config.maxAgents):
        newAgent = Agent()

        newAgent.pos = rndFreePos()
        newAgent.dir = rnd.randint(0, 7)

    runSim = True
    while runSim:
        itrData = runItr()
