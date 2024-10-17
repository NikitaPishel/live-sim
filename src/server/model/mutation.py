from genome import *
import neuronCmd
import random as rnd
from configuration import Configuration

config = Configuration()

def _searchNeurons(agentGenome):
    root = 0
    signals = 0
    processors = 0

    for i in agentGenome:
        if isinstance(i, Sensor):
            root += 1
        
        elif isinstance(i, Processor):
             processors += 1
    
        elif isinstance(i, Signal):
             signals += 1

    return {
        'sns': root,
        'prc': processors,
        'sgn': signals
            }

def _rndJointBase(agentGenome):
    while True:
        jointBase = rnd.choice(agentGenome)

        if isinstance(jointBase, Signal) == False:
            return jointBase

def _rndJointRef(agentGenome):
    while True:
        jointRef = rnd.choice(agentGenome)

        if isinstance(jointRef, Sensor) == False:
            return jointRef

def _addRndNeuron(agentGenome, root):
        jointBase = _rndJointBase(agentGenome)
        rndCmd = rnd.choice(neuronCmd.allCmd)

        if rndCmd in neuronCmd.inputCmd:
            mutation = Sensor()
            root.append(mutation)

        elif rndCmd in neuronCmd.interCmd:
            mutation = Processor()
            jointBase.append(mutation)
    
        else:
            mutation = Signal()
            jointBase.append(mutation)
        
        mutation.cmd = rndCmd

def _addRndJoint(agentGenome, root):
    if len(agentGenome) > 2:
        if rnd.random() > config.mutationChance:
            _addRndNeuron(agentGenome, root)

        else:
            jointBase = _rndJointBase(agentGenome)
    else:
        _addRndJoint(agentGenome, root)

def _delRndJoint(agentGenome, root, neuronTypes):
    while True:
        nrnJoints = _rndJointRef(agentGenome)
        randomJoint = rnd.choice(nrnJoints)

        if neuronTypes['sns'] > 1 and isinstance(randomJoint, Sensor):
            nrnJoints.remove(randomJoint)
            break

        elif neuronTypes['sgn'] > 1 and isinstance(randomJoint, Signal):
            nrnJoints.remove(randomJoint)
            break
        
        else:
            if neuronTypes['prc'] == 0:
                _addRndJoint(_addRndJoint)
                break

def mutate(agent):
    agentGenome = getGenome(agent)
    

    randomMutation = rnd.choice(['del', 'add'])

    if randomMutation == 'add':
        _addRndJoint(agentGenome, agent.joints)

    else:
        neuronTypes = _searchNeurons(agentGenome)
        
        _delRndJoint(agentGenome, agent.joints, neuronTypes)