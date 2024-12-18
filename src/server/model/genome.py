import neuronCmd as nrnCmd

class Neuron:
    def __init__(self, cmd=None):
        self.cmd = cmd      # neuron's command
        self.joints = []

class Sensor(Neuron):
    def __init__(self):
        super().__init__()
    
    def recall(self, fieldTree, agent) -> float:
        cmdOut = self.cmd(fieldTree, agent)
        return cmdOut

class Processor(Neuron):
    def __init__(self):
        super().__init__()
    
    def recall(self, amp) -> float:
        cmdOut  = self.cmd(amp)
        return cmdOut

class Signal(Neuron):
    def __init__(self):
        super().__init__()
        self.refs = 0   # stores amount of joints that are referenced to this neuron, used to check if can delete a signal
    
    def recall(self, fieldTree,  agent, amp) -> None:
        cmdOut = self.cmd(fieldTree, agent, amp)
        return cmdOut

class GeneRoot:
    def __init__(self):
        self.joints = []

# DFS search
def getGenome(root, viewedGenome=[]):
    viewedGenome.append(root)

    for i in root.joints:
        if i not in viewedGenome:

            viewedGenome = getGenome(i, viewedGenome)

    return viewedGenome

# Clone specific neuron
def cloneNrn(nrn):
    print(nrn)
    nrnClone = nrn.__class__
    nrnClone.joints = nrn.joints.copy()
    
    if not isinstance(nrn, GeneRoot):
        nrnClone.cmd = nrn.cmd

    return nrnClone

tRoot = GeneRoot()

tRoot.joints.append(Sensor())
tRoot.joints[0].cmd = 'test'

tClone = cloneNrn(tRoot.joints[0])
tClone.cmd = 'abc'
print(tRoot.joints[0].cmd)