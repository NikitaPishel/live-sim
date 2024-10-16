import neuronsCmd

import random as rnd

class Neuron:
    def __init__(self):
        self.cmd = None
        self.joints = []
        self.id = 0

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

def _genomeSearch(neuron):
    fullGenome = [neuron]
    for i in neuron.joints:
        fullGenome += _genomeSearch(i)
    # Need to add loop detection
    return fullGenome

def getGenome(sensors):
    fullGenome = []
    for i in sensors:
        fullGenome += _genomeSearch(i)

    return fullGenome

def _randomNeuron(nType):
    if nType == 'any':
        rndCmd = rnd.choice(neuronsCmd.allCmd)

        if rndCmd in neuronsCmd.inputCmd:
            newNeuron = Sensor()
        
        elif rndCmd in neuronsCmd.outputCmd:
            newNeuron = Sensor()
        
        elif rndCmd in neuronsCmd.interCmd:
            newNeuron = Processor()
    
    elif nType == 'snr':
        rndCmd = rnd.choice(neuronsCmd.inputCmd)
        newNeuron = Sensor()

    newNeuron.cmd = rndCmd

    return newNeuron

def genMutation(senors):
    agentGenome = getGenome(senors)

    if len(senors) <= 1:
        mutation = _randomNeuron('snr')
        
        if len(mutation.joints) > 0:
            mutation.joints.append(rnd.choice(agentGenome))

        senors.append(mutation)
    
    else:
        mutation = _randomNeuron('any')

        if isinstance(mutation, Sensor):
            mutation.joints.append(rnd.choice(agentGenome))
            senors.append(mutation)

        elif isinstance(mutation, Processor):
            mutation.joints.append(rnd.choice(agentGenome))
            rnd.choice(agentGenome).joints.append(mutation)

        elif isinstance(mutation, Signal):
            rnd.choice(agentGenome).joints.append(mutation)