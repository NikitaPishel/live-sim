import math

# Input commands

def getVisionNone(agent) -> float:
    pass

def getVisionCell(agent) -> float:
    pass

def getDir(agent) -> float:
    pass

# Internal commadns

def Rectifier(amp) -> float:
    if amp > 0:
        return amp

    else:
        return 0

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
    Rectifier

]

outputCmd = [
    outRotate
]

allCmd = inputCmd + interCmd + outputCmd