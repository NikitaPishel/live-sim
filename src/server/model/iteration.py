import random as rnd
import math
from time import time

import data_structures as dts
from agent import Agent
import genome as gnm
from mutation import mutate, rndMutate
from configuration import config
from genePrcs import runGene

def genId(field, maxPos):
    rndID = rnd.randint(0, maxPos)
    newID = findFree(field, maxPos, rndID)

    return newID

def getPos(newID):
    yPos = math.floor(newID/config.fieldSize[1])
    xPos = newID % config.fieldSize[1]      # remainder of a division above = x pos of an agent

    return [xPos, yPos]

def addRndAgent(field, agentQueue, maxPos):
    newID = genId(field, maxPos)
    #print(f'agent position: ({xPos}, {yPos})')
    print(f'=============================')

    newAgent = Agent()
    newAgent.pos = getPos(newID)
    newAgent.dir = rnd.randint(0, 7)
    
    for i in range(config.startMutation):
        #print(f'Mutating {i}...')
        mutate(newAgent)

    field.insert(newID, newAgent)
    agentQueue.enqueue(newAgent)

# Finding free postion on a map
def findFree(field, maxPos, currentID):
    #print(f'\ncurrentID: {currentID}')

    occupied = field.exists(currentID)

    if not occupied:
        #print(f'ID found: {currentID}')
        return currentID

    else:
        #print('cell occupied')
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
                iterate = False
            
            else:
                timer += 1
                print(f'=====\ntimer: {timer}\n')
                runAgents(maxPos, fieldTree, agentQueue, agentsAmount)
        
        elif config.trigger == 'minAgents':
            if agentsAmount <= config.agentsLim:
                iterate = False
            
            else:
                runAgents(maxPos, fieldTree, agentQueue, agentsAmount)
    
    print('selecting agents...')
    
    return selectAgents(agentQueue)

def runAgents(maxPos, fieldTree, agentQueue, agentsAmount):
    for i in range(agentsAmount):
        currAgent = agentQueue.peek()

        runGene(currAgent, fieldTree)

        #print(f'\nagent: {currAgent}\nposition: {currAgent.pos}')
        #print(f'agent position: {currAgent.pos}')

        agentQueue.dequeue()
        agentQueue.enqueue(currAgent)

def selectAgents(agentQueue):
    slctList = []
    selecting = True
    while selecting:
        currAgent = agentQueue.peek()

        if currAgent == None:
            selecting = False
        
        else:
            # If an agent is in first for rows (0 to 3) it gets selected
            if currAgent.pos[0] <= 3:
                slctList.append(currAgent)
                print('agent selected')
            agentQueue.dequeue()

    print(f"selected agents: {slctList}")
    return slctList

def genEnv(slctList, maxPos):
    fieldTree = dts.AvlTree()
    agentQueue = dts.Queue()
    slctAmount = len(slctList)
    print(f'agents passed: {slctAmount}')

    if slctAmount == 0:
        for i in range(config.maxAgents):
            print(f'creating agent №{i}')
            addRndAgent(fieldTree, agentQueue, maxPos)
    
    else:
        fixedClones = math.floor(config.maxAgents / slctAmount)
        rndClones = config.maxAgents % slctAmount

        for i in range(fixedClones):
            for slctAgent in slctList:
                print(f'cloning agent {slctAgent}')
                clonedAgent = slctAgent.clone()

                newID = genId(fieldTree, maxPos)
                clonedAgent.pos = getPos(newID)

                rndMutate(clonedAgent)

                fieldTree.insert(newID, clonedAgent)
                agentQueue.enqueue(clonedAgent)
        
        for i in range(rndClones):
            rndIndex = rnd.randint(0, slctAmount-1)
            print(f'adding random agent {rndIndex}')

            slctAgent = slctList[rndIndex]
            clonedAgent = slctAgent.clone()
            print(f'cloning agent {slctAgent}')

            newID = genId(fieldTree, maxPos)
            clonedAgent.pos = getPos(newID)

            rndMutate(clonedAgent)

            fieldTree.insert(newID, clonedAgent)
            agentQueue.enqueue(clonedAgent)
    
    return {'field': fieldTree, 'queue': agentQueue}

# Simulation execution code
def run():
    maxPos = config.fieldSize[0] * config.fieldSize[1]

    currEnv = genEnv([], maxPos)

    fieldTree = currEnv['field']
    agentQueue = currEnv['queue']

    runSim = True
    for i in range(50):
        itrData = runItr(maxPos, fieldTree, agentQueue)
        currEnv = genEnv(itrData, maxPos)
        fieldTree = currEnv['field']
        agentQueue = currEnv['queue']

start = time()
run()
end = time()

print(f'time taken: {end - start}')