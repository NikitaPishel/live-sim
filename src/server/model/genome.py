class Neuron:
    def __init__(self, cmd=None):
        self.cmd = cmd      # neuron's command
        self.joints = []

class Sensor(Neuron):
    def __init__(self):
        super().__init__()
    
    def recall(self, agent):
        self.cmd(self.agent)

class Processor(Neuron):
    def __init__(self):
        super().__init__()
    
    def recall(self, amp):
        self.cmd(amp)

class Signal(Neuron):
    def __init__(self):
        super().__init__()
        self.refs = 0   # stores amount of joints that are referenced to this neuron, used to check if can delete a signal
    
    def recall(self, agent, amp):
        self.cmd(agent, amp)

class GeneRoot:
    def __init__(self):
        self.joints = []

# Need to add loop detection
def getGenome(root, viewedGenome=[]):
    fullGenome = []
    fullGenome.append(root)
    viewedGenome.append(root)
    for i in root.joints:
        if (i in viewedGenome) == False:
            fullGenome = getGenome(i, viewedGenome)

    return fullGenome