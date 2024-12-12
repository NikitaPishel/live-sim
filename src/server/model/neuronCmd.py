import math

from configuration import config

# internal Cmd
def _getSum(amp):
    ampSum = 0

    for i in amp:
        ampSum += i

    return ampSum

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

def getVisionAny(fieldTree, agent) -> float:
    return 1

def getVisionCell(fieldTree, agent) -> float:
    return 1

def getDir(fieldTree, agent) -> float:
    return (agent.dir / 7)

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

def outRotate(fieldTree, agent, amp) -> bool:
    ampProc = math.tanh(_getSum(amp))

    if ampProc > 0:
        
        # left turn
        if ampProc < 5:
            agent.dir -= 1

            if agent.dir == -1:
                agent.dir = 7

        # right turn
        else:
            agent.dir += 1

            if agent.dir == 8:
                agent.dir = 0

        return True

    else:
        return False

def outMove(fieldTree, agent, amp) -> bool:
    ampProc = math.tanh(_getSum(amp))
    
    moveCords = [0, 0]

    if ampProc > 0:
        if agent.dir >= 1 and agent.dir <= 3:
            moveCords[0] = 1
        
        elif agent.dir >= 5:
            moveCords[0] = -1
        
        else:
            moveCords[0] = 0
        
        if agent.dir == 7 or agent.dir <= 1:
            moveCords[1] = 1
        
        elif agent.dir <= 5 and agent.dir >= 3:
            moveCords[1] = -1
    
        else:
            moveCords[1] = 0

        xPos = agent.pos[0] + moveCords[0]
        yPos = agent.pos[1] + moveCords[1]
        newPos = [xPos, yPos]

        if xPos >= 0 and xPos < config.fieldSize[0]:
            if yPos >= 0 and yPos < config.fieldSize[1]:

                busy = posTaken(fieldTree.root, newPos)
                
                if not busy:
                    agent.pos = newPos

        return True

    else:
        return False

inputCmd = [
    getVisionAny,
    getVisionCell,
    getDir,
]

interCmd = [
    tanhList,
    reLU,
    invert


]

outputCmd = [
    outRotate,
    outMove
]

allCmd = inputCmd + interCmd + outputCmd
