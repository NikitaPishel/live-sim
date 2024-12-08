# This file will contains code that will run agent's gene
# breadth-first search
import agent
import genome as gnm
import data_structures as dts
import neuronCmd as cmds
from configuration import config

def _enqueueJoints(nrnData, runQueue, neuron):
    for child in neuron.joints:
        if child in nrnData.keys():
            nrnInp = list(nrnData[child].values())

        else:
            nrnInp = []

        queueCall = {'nrn': child, 'input': nrnInp}
        
        runQueue.enqueue(queueCall)

def _saveInput(nrnOut, nrnData, neuron):
    for child in neuron.joints:
        if child not in nrnData.keys():
            nrnData[child] =  {}

        nrnData[child][neuron] = nrnOut

def runGene(agent, fieldTree):
    root = agent.gene
    runQueue = dts.Queue()
    nrnData  = {}
    # nrnData - {<child nrn>: {<parent nrn>: 0.452}}

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
        
        if currentCall == None:
            active = False
        
        else:
            neuron = currentCall['nrn']
            
            if isinstance(neuron, gnm.Sensor):
                nrnOut = neuron.recall(fieldTree, agent)
                _saveInput(nrnOut, nrnData, neuron)
            
            elif isinstance(neuron, gnm.Processor):
                nrnInp = currentCall['input']
                nrnOut = neuron.recall(nrnInp)
                _saveInput(nrnOut, nrnData, neuron)

            elif isinstance(neuron, gnm.Signal):
                nrnInp = currentCall['input']
                nrnRun = neuron.recall(fieldTree, agent, nrnInp)
                
                if nrnRun:
                    actions += 1

                    if actions >= config.maxActions:
                        active = False

            else:
                raise Exception(
                    f'Non-classified neuron type \'{neuron}\''
                    )

            _enqueueJoints(nrnData, runQueue, neuron)
            
            runQueue.dequeue()