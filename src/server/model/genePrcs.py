# This file will contains code that will run agent's gene
# breadth-first search
import genome as gnm
import data_structures as dts
from configuration import config

def _enqueueJoints(nrnCalls, runQueue):
    for i in neuron.joints:
        queueCall = {'nrn': i, 'inp': nrnCalls[i]}}
        runQueue.enqueue(queueCall)

def _saveInput(neuron):
    pass

def runGene(root):
    runQueue = dts.Queue()
    nrnCalls  = {} 

    # neuron call - {nrn: {nrnOut:0.456}, ...}
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

        currentCall = runQueue.peek()

        if isinstance(neuron, gnm.Sensor):
            nrnOutput = neuron.recall()
            _saveInput(neuron)
        
        if isinstance(neuron, gnm.Processor):
            nrnOutput = neuron.recall()
            _saveInput(neuron)
        
        if isinstance(neuron, gnm.Sensor):
            neuron.recall()
            actions += 1

        _enqueueJoints(currentCall, runQueue)
        
        runQueue.dequeue()
