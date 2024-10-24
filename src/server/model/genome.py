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
        if not (i in viewedGenome):
            fullGenome += getGenome(i, viewedGenome)

    return fullGenome


'''
TEMPORARY TEST CODE

GET GENOME TEST

myGenome = GeneRoot()

myGenome.joints.append(
    Signal()
)

signal1 = myGenome.joints[0]

signal1.joints.append(
    Processor()
)
signal1.joints.append(
    Processor()
)

signal1.joints[1].joints.append(
    signal1.joints[0]
)

signal1.joints[0].joints.append(
    Processor()
)

signal1.joints[0].joints[0].joints.append(
 signal1.joints[1]   
)

myGenomeArr = getGenome(myGenome)
print(myGenomeArr)

print(
    signal1.joints[0].joints[0].joints[0] == signal1.joints[1]
)'''