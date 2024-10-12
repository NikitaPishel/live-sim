class Neuron:
    def __init__(self):
        self.joints = []

class Sensor(Neuron):
    def __init__(self, agent, cmd):
        self.cmd = cmd
        self.agent = agent
    
    def recall(self):
        self.cmd(self.agent)


def getVisionNone(agent):
    pass

def getVisionCell(agent):
    pass

def getCompass(agent):
    pass

def rotateLeft(agent):
    pass

def rotateRight(agent):
    pass