class Neuron:
    def __init__(self, cmd=None):
        self.cmd = cmd
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
    
    def recall(self, agent, amp):
        self.cmd(agent, amp)

class GeneRoot:
    def __init__(self):
        self.joints = []

# Need to add loop detection
def getGenome(root, viewedGenome=[]):
    viewedGenome.append(root)
    for i in root.joints:
        if (i in viewedGenome) == False:
            viewedGenome += getGenome(i, viewedGenome)

    return viewedGenome