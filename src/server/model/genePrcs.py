# This file will contains code that will run agent's gene
# breadth-first search
import agent
import genome as gnm
import data_structures as dts
import neuronCmd as cmds
from configuration import config

def _enqueueJoints(nrnData, runQueue, neuron):
    for child in neuron.joints:
        if isinstance(neuron, gnm.Sensor):
            queueCall = {'nrn': child, 'input': []}

        else:
            nrnInp = list(nrnData[child].values())
            queueCall = {'nrn': child, 'input': nrnInp}

        runQueue.enqueue(queueCall)

def _saveInput(nrnOut, nrnData, neuron):
    for child in neuron.joints:
        if child not in nrnData:
            nrnData[child] =  {}

        nrnData[child][neuron] = nrnOut

def runGene(agent):
    root = agent.gene
    runQueue = dts.Queue()
    nrnData  = {}
    # nrnData - {<child nrn>: {<parent nrn>: 0.452}}

    _saveInput(None, nrnData, root)
    _enqueueJoints(nrnData, runQueue, root)
    
    active = True
    timer = 0
    actions = 0

    while active:
        timer += 1
        
        if timer >= config.geneTime:
            active = False

        if actions >= config.maxActions:
            active = False

        currentCall = runQueue.peek()
        neuron = currentCall['nrn']
        nrnInp = currentCall['input']

        if isinstance(neuron, gnm.Sensor):
            nrnOut = neuron.recall(agent)
            _saveInput(nrnOut, nrnData, neuron)
        
        elif isinstance(neuron, gnm.Processor):
            nrnInp = currentCall['input']
            nrnOut = neuron.recall(nrnInp)
            _saveInput(nrnOut, nrnData, neuron)

        elif isinstance(neuron, gnm.Sensor):
            nnrnInp = currentCall['input']
            neuron.recall(nrnInp)
            actions += 1

            if actions >= config.maxActions:
                active = False
        
        else:
            raise Exception(
                f'Non-classified neuron type \'{neuron}\''
                )

        _enqueueJoints(nrnData, runQueue, neuron)
        
        runQueue.dequeue()

# TEST СODE
# should be rebuilt into a unit test

def snsInp(agent):
    return 0.45

def sgnOut(amp):
    print(amp)

tRoot = gnm.GeneRoot()

tRoot.joints.append(gnm.Sensor())
tRoot.joints[0].cmd = snsInp

tRoot.joints[0].joints.append(gnm.Processor())
tRoot.joints[0].joints.append(gnm.Processor())

tRoot.joints[0].joints[0].joints.append(
    tRoot.joints[0].joints[1]
    )

tRoot.joints[0].joints[0].joints[0].joints.append(
    gnm.Signal
    )

tRoot.joints[0].joints[0].joints[0].joints[0].cmd = sgnOut

tAgent = agent.Agent()
tAgent.gene = tRoot

runGene(tAgent)