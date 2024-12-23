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
def cloneNrn(nrn, cloneDict):
    # print(nrn)
    nrnClone = type(nrn)()
    cloneDict[nrn] = nrnClone
   
    if not isinstance(nrn, GeneRoot):
        nrnClone.cmd = nrn.cmd

    for i in nrn.joints:
        childClone = cloneDict.get(i)

        if childClone == None:
            childClone = cloneNrn(i, cloneDict)

        nrnClone.joints.append(childClone)

    return nrnClone

def cloneGene(oldRoot):
    gene = getGenome(oldRoot, [])
    
    cloneDict = {}

    newRoot = cloneNrn(oldRoot, {})
    
    return newRoot