import random as rnd
import math
from time import time

import data_structures as dts
from agent import Agent
import genome as gnm
from mutation import mutate
from configuration import config

def addRndAgent(field, agentQueue, maxPos):
    rndID = rnd.randint(0, maxPos)
    newID = findFree(field, maxPos, rndID)
    
    yPos = math.floor(newID/config.fieldSize[1])
    xPos = newID % config.fieldSize[1]      # remainder of a division above = x pos of an agent
    print(f'agent position: ({xPos}, {yPos})')
    print(f'=============================')

    rndAgent = Agent()
    rndAgent.pos = [xPos, yPos]
    rndAgent.dir = rnd.randint(0, 7)
    
    for i in range(config.startMutation):
        mutate(rndAgent)

    field.insert(newID, rndAgent)
    agentQueue.enqueue(rndAgent)

# Finding free postion on a map
def findFree(field, maxPos, currentID):
    print(f'\ncurrentID: {currentID}')

    occupied = field.exists(currentID)

    if not occupied:
        print(f'ID found: {currentID}')
        return currentID

    else:
        print('cell occupied')
        newID = currentID + 1

        if newID > maxPos:
            newID = 0

        freePos = findFree(field, maxPos, newID)

        return freePos

# Single iteration process
def runItr(maxPos, fieldTree, agentQueue):

    agentsAmount = agentQueue.getLength()

    if config.trigger == 'timer':
        timer = 0

    iterate = True
    while iterate:
        if config.trigger == 'timer':
            if timer >= config.timeLim:
                break
            
            else:
                timer += 1
                runAgents(maxPos, fieldTree, agentQueue, agentsAmount)
        
        elif config.trigger == 'minAgents':
            if agentsAmount <= config.agentsLim:
                break
        
        print(f'current time: {timer}')

def runAgents(maxPos, fieldTree, agentQueue, agentsAmount):
    pass

# Simulation execution code
def run():
    maxPos = config.fieldSize[0] * config.fieldSize[1]
    fieldTree = dts.AvlTree()
    agentQueue = dts.Queue()

    for i in range(config.maxAgents):
        print(f'creating agent №{i}')
        addRndAgent(fieldTree, agentQueue, maxPos)

    runSim = True
    while runSim:
        itrData = runItr(maxPos, fieldTree, agentQueue)
        itrData = runItr(maxPos, fieldTree, agentQueue)
        itrData = runItr(maxPos, fieldTree, agentQueue)
        runSim = False  

start = time()
run()
end = time()

print(f'time taken: {end - start}')