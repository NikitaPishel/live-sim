import math
import random as rnd

from configuration import config

# internal Cmd
def _getSum(amp):
    ampSum = 0

    for i in amp:
        ampSum += i

    return ampSum

def moveAgent(fieldTree, agent, displ):
    xPos = agent.pos[0] + displ[0]
    yPos = agent.pos[1] + displ[1]

    #print(f'moving from {agent.pos} to {[xPos, yPos]}')

    if xPos >= 0 and xPos < config.fieldSize[0]:
        if yPos >= 0 and yPos < config.fieldSize[1]:

            busy = posTaken(fieldTree.root, [xPos, yPos])
            
            if not busy:
                agent.pos = [xPos, yPos]


def posTaken(node, givenPos):
    if node != None:
        #print(f"checking if agent on {node.data.pos} is on {givenPos}...")
        if node.data.pos == givenPos:
            #print('position is busy')
            return True
        
        else:
            getLeft = posTaken(node.lChild, givenPos)
            getRight = posTaken(node.rChild, givenPos)

            if getLeft:
                busy = True
            
            elif getRight:
                busy = True
            
            else:
                busy = False

            return busy

    else:
        return False

# Input commands

def constantOn(fieldTree, agent) -> float:
    return 1.0

# Internal commadns

def tanhList(amp):
    ampSum = _getSum(amp)
    return math.tanh(ampSum)

def reLU(amp) -> float:
    ampSum = _getSum(amp)
    
    if ampSum > 0:
        return ampSum

    else:
        return 0

def invert(amp):
    return tanhList(amp) * 1

# Output commands

def outMoveSouth(fieldTree, agent, amp) -> bool:
    ampProc = math.tanh(_getSum(amp))
    
    if ampProc > 0:
        moveAgent(fieldTree, agent, [0, 1])

        return True

    else:
        return False

def outMoveNorth(fieldTree, agent, amp) -> bool:
    ampProc = math.tanh(_getSum(amp))
    
    if ampProc > 0:
        moveAgent(fieldTree, agent, [0, -1])

        return True

    else:
        return False

def outMoveEast(fieldTree, agent, amp) -> bool:
    ampProc = math.tanh(_getSum(amp))
    
    if ampProc > 0:
        moveAgent(fieldTree, agent, [1, 0])

        return True

    else:
        return False

def outMoveWest(fieldTree, agent, amp) -> bool:
    ampProc = math.tanh(_getSum(amp))
    
    if ampProc > 0:
        moveAgent(fieldTree, agent, [-1, 0])

        return True

    else:
        return False

def outMoveRnd(fieldTree, agent, amp) -> bool:
    ampProc = math.tanh(_getSum(amp))
    
    if ampProc > 0:
        xDispl = rnd.randint(-1, 1)
        yDispl = rnd.randint(-1, 1)
        moveAgent(fieldTree, agent, [xDispl, yDispl])

        return True

    else:
        return False

inputCmd = [
    constantOn
]

interCmd = [
    tanhList,
    reLU,
    invert
]

outputCmd = [
    outMoveSouth,
    outMoveNorth,
    outMoveEast,
    outMoveWest
]

allCmd = inputCmd + interCmd + outputCmd
