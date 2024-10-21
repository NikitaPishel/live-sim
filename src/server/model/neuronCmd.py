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
    pass

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
    pass

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