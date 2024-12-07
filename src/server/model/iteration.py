import random as rnd
import math
from time import time

import data_structures as dts
from agent import Agent
import genome as gnm
from mutation import mutate
from configuration import config

def addRndAgent(field, maxPos):
    rndID = rnd.randint(0, maxPos)
    newID = findFree(field, maxPos, rndID)
    
    yPos = math.floor(newID/config.fieldSize[1])
    xPos = newID % config.fieldSize[1]      # remainder of a division above = x pos of an agent

    rndAgent = Agent()
    rndAgent.pos = [xPos, yPos]
    rndAgent.dir = rnd.randint(0, 7)
    
    for i in range(config.startMutation):
        mutate(rndAgent)

    field.insert(newID, rndAgent)

# Finding free postion on a map
def findFree(field, maxPos, currentID):
    print(f'\ncurrentID: {currentID}')

    occupied = field.exists(currentID)

    if not occupied:
        print(f'ID found: {currentID}')
        print(f'=============================')
        return currentID

    else:
        print('cell occupied')
        newID = currentID + 1

        if newID > maxPos:
            newID = 0

        freePos = findFree(field, maxPos, newID)

        return freePos

# Single iteration process
def runItr():
    pass

# Simulation execution code
def run():
    maxPos = config.fieldSize[0] * config.fieldSize[1]
    fieldTree = dts.AvlTree()

    for i in range(config.maxAgents):
        print(f'creating agent №{i}')
        addRndAgent(fieldTree, maxPos)

    runSim = True
    timer = 0
    while runSim:
        itrData = runItr()
        timer += 1
        print('Simulation Launched!')

        if timer > 10:
            runSim = False

start = time()
run()
end = time()

print(f'time taken: {end - start}')