from genome import *
import neuronCmd as nrnCmd
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
                        'base': nrnBase.joints, 
                        'ref': nrnRef
                        }
                    joints.append(delPos)
            
            else:
                delPos = {
                    'base': nrnBase.joints, 
                    'ref': nrnRef
                    }
                joints.append(delPos)

    return joints

def _delRndJoint(agentGenome, neuronTypes):
    delJoints = _getDelblJoints(agentGenome, neuronTypes)

    if len(delJoints) > 0:
        rndJoint = rnd.choice(delJoints)
        rndJoint['base'].remove(rndJoint['ref'])
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
                        'base': nrnBase.joints,
                        'ref': nrnRef
                    }
                    joints.append(addPos)
    
    return joints

def _getJointBases(noRootGenome):
    joints = []

    for i in noRootGenome:
        if not isinstance(i, Signal):
            joints.append(i)
    
    return joints

def _addRndNeuron(noRootGenome, root):
        rndCmd = rnd.choice(nrnCmd.allCmd)

        if rndCmd in nrnCmd.inputCmd:
            mutation = Sensor()
            root.joints.append(mutation)

        elif rndCmd in nrnCmd.interCmd:
            jointBase = rnd.choice(_getJointBases(noRootGenome))
            mutation = Processor()
            jointBase.joints.append(mutation)
    
        elif rndCmd in nrnCmd.outputCmd:
            jointBase = rnd.choice(_getJointBases(noRootGenome))
            mutation = Signal()
            jointBase.joints.append(mutation)
        
        else:
            raise Exception(
                f'Unknown command \'{rndCmd}\' in function \'{_addRndNeuron}\''
                )
        
        mutation.cmd = rndCmd

def _addRndJoint(noRootGenome, root):
    addblJoints = _getAddblJoints(noRootGenome)
    if len(noRootGenome) <= config.maxGenomeLen:
        if config.newNeuronChance >= rnd.random():
            _addRndNeuron(noRootGenome, root)

        elif len(addblJoints) > 0:
            rndJoint = rnd.choice(addblJoints)
            rndJoint['base'].append(rndJoint['ref'])

        else:
            _addRndNeuron(noRootGenome, root)

def mutate(agent):
    agentGenome = getGenome(agent.gene)
    
    #print(agentGenome)

    noRootGenome = agentGenome.copy()
    noRootGenome.pop(0)                 # root always has an index of 0

    randomMutation = rnd.choice(['del', 'add'])
    
    if randomMutation == 'add':
        _addRndJoint(noRootGenome, agent.gene)

    else:
        neuronTypes = _searchNeurons(noRootGenome)
        jointDelted = _delRndJoint(agentGenome, neuronTypes)

        if not jointDelted:
            _addRndJoint(noRootGenome, agent.gene)