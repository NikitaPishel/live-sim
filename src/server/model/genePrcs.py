# This file will contains code that will run agent's gene
# breadth-first search
import genome as gnm
import data_structures as dts
from configuration import config

def _enqueueJoints(nrnData, runQueue, neuron):
    for child in neuron.joints:
        nrnInp = list(nrnData[child].values())

        queueCall = {'nrn': child, 'input': nrnInp}
        runQueue.enqueue(queueCall)

def _saveInput(nrnOut, nrnData, neuron):
    for child in neuon.joints:
        nrnData[child][neuron] =  nrnOut

def runGene(root):
    runQueue = dts.Queue()
    # nrnData - {<child nrn>: {<parent nrn>: 0.452}}
    nrnData  = {}
    
    _enqueueJoints(nrnData, runQueue, root)
    
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
        neuron = cuurentCall['nrn']
        nrnInp = currentCall['input']

        if isinstance(neuron, gnm.Sensor):
            nrnOut = neuron.recall()
            _saveInput(nrnOut, nrnData, neuron)
        
        if isinstance(neuron, gnm.Processor):
            nrnInp = currentCall['input']
            nrnOut = neuron.recall(nrnInp)
            _saveInput(nrnOut, nrnData, neuron)

        if isinstance(neuron, gnm.Sensor):
            nnrnInp = currentCall['input']
            euron.recall(nrnInp)
            actions += 1

            if actions >= config.maxActions:
                active = False

        _enqueueJoints(currentCall, runQueue)
        
        runQueue.dequeue()



# TEST СODE

# should be rebuilt into a unit test

def snsInp():
    return 0.45

def sgnOut(amp):
    print(amp)

tRoot = gnm.GeneRoot()

tRoot.joints.append(gnm.Sensor)
tRoot.joints[0].cmd = snsInput

tRoot.joints[0].joints.append(gnm.Processor())
tRoot.joints[0].joints.append(gnm.Processor())

tRoot.joints[0].joints[0].joints.append(
tRoot.joints[0].joints[1]
)

tRoot.joints[0].joints[0].joints[0].joints.append(gnm.Signal)

tRoot.joints[0].joints[0].joints[0].joints[0].cmd = sgnOut
