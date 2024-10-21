from genome import *
import neuronCmd
import random as rnd
from configuration import config

def _searchNeurons(agentGenome):
    sensors = 0
    signals = 0
    processors = 0

    for i in agentGenome:
        if isinstance(i, Sensor):
            sensors += 1
        
        elif isinstance(i, Processor):
             processors += 1
    
        elif isinstance(i, Signal):
             signals += 1

    return {
        'sns': sensors,
        'prc': processors,
        'sgn': signals
            }

def _getDelblJoints(agentGenome, neuronTypes):
    joints = []
    for nrnBase in agentGenome:

        for nrnRef in nrnBase.joints:

            if isinstance(nrnRef, Sensor):
                if neuronTypes['sns'] > 1:
                    delPos = {
                        'base': nrnBase, 
                        'ref': nrnRef
                        }
                    joints.append(delPos)
            
            else:
                delPos = {
                    'base': nrnBase, 
                    'ref': nrnRef
                    }
                joints.append(delPos)

    return joints

def _delRndJoint(agentGenome, root, neuronTypes, noRootGenome):
    rndDelJoint = rnd.choice(_getDelblJoints(agentGenome))

    if len(rndDelJoint) > 0:
        rndJoint = rnd.choice(rndDelJoint)
        rndJoint['base'].pop('ref')
        return True

    else:
        return False

def _getAddblJoints(noRootGenome):
    joints = []

    for nrnBase in noRootGenome:
        for nrnRef in noRootGenome:
            if not isinstance(nrnRef, Sensor):
                if not (nrnRef in nrnBase.joints):
                    addPos = {
                        'base': nrnBase,
                        'ref': nrnRef
                    }
                    joints.append(addPos)

def _getJointBases(noRootGenome):
    joints = []

    for i in noRootGenome:
        if not isinstance(i, Signal):
            joints.append(i)
    
    return joints

def _addRndNeuron(noRootGenome, root):
        jointBase = rnd.choice(_getJointBases(noRootGenome))
        rndCmd = rnd.choice(neuronCmd.allCmd)

        if rndCmd in neuronCmd.inputCmd:
            mutation = Sensor(rndCmd)
            root.joints.append(mutation)

        elif rndCmd in neuronCmd.interCmd:
            mutation = Processor(rndCmd)
            jointBase.append(mutation)
    
        elif rndCmd in neuronCmd.outputCmd:
            mutation = Signal(rndCmd)
            jointBase.append(mutation)
        
        else:
            raise Exception(
                f'Unknown command \'{rndCmd}\' in function \'{_addRndNeuron}\''
                )

def _addRndJoint(noRootGenome, root):
    rndJoint = _getAddblJoints()

    if len(rndJoint) > 0:
        rndJoint['base'].append(rndJoint['ref'])

    else:
        _addRndNeuron(noRootGenome, root)

def mutate(agent):
    agentGenome = getGenome(agent.gene)
    
    noRootGenome = agentGenome.copy()
    noRootGenome.pop(0)                 # root always has an index of 0

    randomMutation = rnd.choice(['del', 'add'])

    if randomMutation == 'add':
        _addRndJoint(noRootGenome, agent.gene)

    else:
        neuronTypes = _searchNeurons(noRootGenome)
        jointDelted = _delRndJoint(agentGenome, agent.gene, neuronTypes, noRootGenome)

        if not jointDelted:
            _addRndJoint(noRootGenome, agent.gene)