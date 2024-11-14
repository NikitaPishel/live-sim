# This file will contain code that will run agent's gene

# breadth-first search

import genome as gnm
import data_structures as dts
from configuration import config

def _enqueueJoints(neuron, runQueue):
    for i in neuron.joints:
        runQueue.enqueue(i)

def _saveInput(neuron):
    pass

def runGene(root):
    runQueue = dts.Queue()

    _enqueueJoints(neuron, runQueue)
    
    active = True
    timer = 0
    actions = 0
    
    while active:
        timer += 1
        
        if timer >= config.mutationTimeLimit:
            active = False

            if actions >= config.maxActions:
                active = False

        neuron = runQueue.peek()

        neuron.recall()

        if isinstance(neuron, gnm.Sensor):
            nrnOutput = neuron.recall()
            _saveInput(neuron)
        
        if isinstance(neuron, gnm.Processor):
            nrnOutput = neuron.recall()
            _saveInput(neuron)
        
        if isinstance(neuron, gnm.Sensor):
            neuron.recall()
            actions += 1

        _enqueueJoints(neuron, runQueue)
        
        runQueue.dequeue()