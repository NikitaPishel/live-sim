import math

def getSum(amp):
    ampSum = 0

    for i in range(amp):
        ampSum += amp

    return ampSum

# Input commands

def getVisionNone(agent) -> float:
    pass

def getVisionCell(agent) -> float:
    pass

def getDir(agent) -> float:
    return agent.dir

# Internal commadns

def reLU(amp) -> float:
    ampSum = getSum(amp)
    
    if amp > 0:
        return amp

    else:
        return 0

def getProduct(amp):
    return 

# Output commands

def outRotate(agent, amp) -> None:
    ampProc = math.tanh(getSum(amp))

def outMove(agent, amp) -> None:
    ampProc = math.tanh(getSum(amp))
    
    moveCords = [0, 0]

    if agent.dir > 0:
        moveCords[0] = 1
    
    if agent.dir >= -0.25 and agent.dir <= 0.25:
        moveCords[1] = 1

inputCmd = [
    getVisionNone,
    getVisionCell,
    getDir,
]

interCmd = [
    math.tanh,
    reLU,
    getProduct


]

outputCmd = [
    outRotate
]

allCmd = inputCmd + interCmd + outputCmd