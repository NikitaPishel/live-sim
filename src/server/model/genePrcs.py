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
            print(f"inserting input: {nrnInp}")

        else:
            nrnInp = []
            print('no input found, returing empty list')

        queueCall = {'nrn': child, 'input': nrnInp}
        
        print(f'enqueueing nrn call: {queueCall}')
        runQueue.enqueue(queueCall)

def _saveInput(nrnOut, nrnData, neuron):
    for child in neuron.joints:
        if child not in nrnData.keys():
            print(f'creating data record for {child}...')
            nrnData[child] =  {}

        print(f'writing {nrnOut} into {child}')
        nrnData[child][neuron] = nrnOut
#        print(f'nrnData: {nrnData}')

def runGene(agent):
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
        print(f'timer: {timer}')
        
        if timer >= config.geneTime:
            active = False

        if actions >= config.maxActions:
            active = False

        currentCall = runQueue.peek()
        
        if currentCall == None:
            active = False
        
        else:
            neuron = currentCall['nrn']
            print(f'recieving nrnInput: {currentCall['input']}')
            
            if isinstance(neuron, gnm.Sensor):
                nrnOut = neuron.recall(agent)
                _saveInput(nrnOut, nrnData, neuron)
                print(f'sns output: {nrnOut}')
            
            elif isinstance(neuron, gnm.Processor):
                nrnInp = currentCall['input']
                nrnOut = neuron.recall(nrnInp)
                _saveInput(nrnOut, nrnData, neuron)
                print(f'prcs output: {nrnOut}')

            elif isinstance(neuron, gnm.Signal):
                nrnInp = currentCall['input']
                nrnRun = neuron.recall(agent, nrnInp)
                
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
    print(nrnData)

# TEST СODE
# should be rebuilt into a unit test

def snsInp(agent):
    print('sns input: 0.45')
    return 0.45

def sgnOut(agent, amp):
    print(f'{amp} -> {agent}')

tRoot = gnm.GeneRoot()

tRoot.joints.append(gnm.Sensor())
tRoot.joints[0].cmd = snsInp

tRoot.joints[0].joints.append(gnm.Processor())
tRoot.joints[0].joints[0].cmd = cmds.tanhList

tRoot.joints[0].joints.append(gnm.Processor())
tRoot.joints[0].joints[1].cmd = cmds.tanhList

tRoot.joints[0].joints[0].joints.append(
    tRoot.joints[0].joints[1]
    )

tRoot.joints[0].joints[1].joints.append(
    gnm.Signal()
    )

tRoot.joints[0].joints[1].joints[0].cmd = sgnOut

tAgent = agent.Agent()
tAgent.gene = tRoot

runGene(tAgent)
