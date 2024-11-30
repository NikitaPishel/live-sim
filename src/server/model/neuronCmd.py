import math

def getSum(amp):
    ampSum = 0

    for i in amp:
        ampSum += i

    return ampSum

# Input commands

def getVisionNone(agent) -> float:
    pass

def getVisionCell(agent) -> float:
    pass

def getDir(agent) -> float:
    return agent.dir

# Internal commadns

def tanhList(amp):
    ampSum = getSum(amp)
    return math.tanh(ampSum)

def reLU(amp) -> float:
    ampSum = getSum(amp)
    
    if amp > 0:
        return ampSum

    else:
        return 0

def getProduct(amp):
    return 

# Output commands

def outRotate(agent, amp) -> bool:
    ampProc = math.tanh(getSum(amp))

def outMove(agent, amp) -> bool:
    ampProc = math.tanh(getSum(amp))
    
    moveCords = [0, 0]

    if ampProc > 0:
        if agent.dir > 0:
            moveCords[0] = 1
        
        if agent.dir >= -0.25 and agent.dir <= 0.25:
            moveCords[1] = 1

        return True

    else:
        return False

inputCmd = [
    getVisionNone,
    getVisionCell,
    getDir,
]

interCmd = [
    tanhList,
    reLU,
    getProduct


]

outputCmd = [
    outRotate
]

allCmd = inputCmd + interCmd + outputCmd
