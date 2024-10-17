class Neuron:
    def __init__(self):
        self.cmd = None
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

def getGenome(neuron, viewedGenome=[]):
    viewedGenome.append(neuron)
    
    for i in neuron.joints:
        if (i in viewedGenome) == False:
            viewedGenome += getGenome(i, viewedGenome)
    # Need to add loop detection
    return viewedGenome