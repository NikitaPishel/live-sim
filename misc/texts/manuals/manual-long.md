# Full Manual

## Contents
[Intro](#Getting-Started)
[Data Strustures](#Data-Structures)
[Configuration](#Configuration)
[Agents](#Agents)
[Genome](#Genome)
[Mutations](#Mutations)
[Model](#Model)

## Getting Started
This manual gives a full explanation of the whole code, each function, class, etc. General structure of this manual will include every function in a separate code block with some comment bellow it. Also there will be some comments for each section of code (e. g. mutation section is needed to <...>).

---

## Data Structures

### Classes

#### AvlNode
```python
```

#### AvlTree
```python
```

#### QueueNode
```python
```

#### Queue
```python
```

#### StackNode
```python
```

#### Stack
```python
```

### Functions

#### searchNode (AvlNode)
```python
```

#### inTree (AvlNode)
```python
```

#### insertNode (AvlNode)
```python
```

#### deleteNode (AvlNode)
```python
```

#### findSuccessorParent (AvlNode)
```python
```

#### updateHeight (AvlNode)
```python
```

#### lowest (AvlNode)
```python
```

#### getBalance (AvlNode)
```python
```

#### balanceTree (AvlNode)
```python
```

#### lTurn (AvlNode)
```python
```

#### rTurn (AvlNode)
```python
```

#### lrTurn (AvlNode)
```python
```

#### rlTurn (AvlNode)
```python
```

#### rlTurn (AvlNode)
```python
```

#### get (AvlTree)
```python
```

#### setData (AvlTree)
```python
```

#### insert (AvlTree)
```python
```

#### delete (AvlTree)
```python
```

#### exists (AvlTree)
```python
```

#### searchData (QueueNode)
```python
```

#### itrLength (QueueNode)
```python
```

#### enqueue (Queue)
```python
```

#### dequeue (Queue)
```python
```

#### peek (Queue)
```python
```

#### getLength (Queue)
```python
```

#### itrLength (StackNode)
```python
```

#### itrFind (StackNode)
```python
```

#### isOccupied (Stack)
```python
```

#### peek (Stack)
```python
```

#### insert (Stack)
```python
```

#### getLength (Stack)
```python
```

#### find (Stack)
```python
```

#### delete (Stack)
```python
```

---

## Configuration

### Classes
#### Configuration

### Functions
#### getInstance
```python
```

#### loadConfig
```python
```

### JSON files

---

## Agents

### Classes


### Functions

---

## Genome

### Classes

#### Neuron super class
```python
class Neuron:
    def __init__(self, cmd=None):
        self.cmd = cmd      # neuron's command
        self.joints = []
```

#### Sensor class
```python
class Sensor(Neuron):
    def __init__(self):
        super().__init__()
    
    def recall(self, fieldTree, agent) -> float:
        cmdOut = self.cmd(fieldTree, agent)
        return cmdOut
```

#### Processor class
```python
class Processor(Neuron):
    def __init__(self):
        super().__init__()
    
    def recall(self, amp) -> float:
        cmdOut  = self.cmd(amp)
        return cmdOut
```

#### Signal class
```python
class Signal(Neuron):
    def __init__(self):
        super().__init__()
        self.refs = 0   # stores amount of joints that are referenced to this neuron, used to check if can delete a signal
    
    def recall(self, fieldTree,  agent, amp) -> bool:
        cmdOut = self.cmd(fieldTree, agent, amp)
        return cmdOut
```
#### GeneRoot class
```python
class GeneRoot:
    def __init__(self):
        self.joints = []
```

### Functions
```python
```

#### Find genome
```python
# DFS search. Returns a list of all neurons in a genome, capable of loop detection
def getGenome(root, viewedGenome=[]):
    viewedGenome.append(root)

    for i in root.joints:
        if i not in viewedGenome:

            viewedGenome = getGenome(i, viewedGenome)

    return viewedGenome
```

#### CloneNrn
```python
# Create in memory an exact copy of a specific neuron
def cloneNrn(nrn, cloneDict):
    # print(nrn)
    nrnClone = type(nrn)()
    cloneDict[nrn] = nrnClone
   
    if not isinstance(nrn, GeneRoot):
        nrnClone.cmd = nrn.cmd

    for i in nrn.joints:
        childClone = cloneDict.get(i)

        if childClone == None:
            childClone = cloneNrn(i, cloneDict)

        nrnClone.joints.append(childClone)

    return nrnClone
```

#### CloneGene
```python
# Create in memory a clone of a genome
def cloneGene(oldRoot):
    gene = getGenome(oldRoot, [])
    
    cloneDict = {}

    newRoot = cloneNrn(oldRoot, {})
    
    return newRoot
```

## Mutations

### Functions
#### searchNeurons
```python
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
```

#### getDelblJoints
```python
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
```

#### delRndJoint
```python
def _delRndJoint(agentGenome, neuronTypes):
    delJoints = _getDelblJoints(agentGenome, neuronTypes)

    if len(delJoints) > 0:
        rndJoint = rnd.choice(delJoints)
        rndJoint['base'].remove(rndJoint['ref'])
        return True

    else:
        return False
```

#### getAddblJoints
```python
def _getAddblJoints(noRootGenome):
    addblJoints = []
    
    for nrnBase in noRootGenome:
        if not isinstance(nrnBase, Signal):

            for nrnRef in noRootGenome:
                if not isinstance(nrnRef, Sensor):
                    if nrnRef not in nrnBase.joints:
                        addPos = {
                            'base': nrnBase.joints,
                            'ref': nrnRef
                        }
                        addblJoints.append(addPos)
    
    return addblJoints
```

#### 
```python
def _getJointBases(noRootGenome):
    joints = []

    for i in noRootGenome:
        if not isinstance(i, Signal):
            joints.append(i)
    
    return joints
```

#### addRndNeuron
```python
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
                f'Unknown command \'{rndCmd}\' in function \'_addRndNeuron\''
                )
        
        mutation.cmd = rndCmd
```

#### genRndJoint
```python
def genRndJoint(addblJoints):
    rndJoint = rnd.choice(addblJoints)
    rndJoint['base'].append(rndJoint['ref'])
```

#### addRndJoint
```python
def _addRndJoint(noRootGenome, root):
    addblJoints = _getAddblJoints(noRootGenome)
    genType = rnd.random()

    if len(noRootGenome) < config.maxGenomeLen:
        if config.newNeuronChance >= genType:
            _addRndNeuron(noRootGenome, root)
            return True
        
        elif len(addblJoints) > 0:
            genRndJoint(addblJoints)
            return True
        
        else:
            _addRndNeuron(noRootGenome, root)
            return True

    else:
        if len(addblJoints) > 0:
            genRndJoint(addblJoints)
            return True
        
        else:
            return False
```

#### mutate
```python
def mutate(agent):
    agentGenome = getGenome(agent.gene, [])

    noRootGenome = agentGenome.copy()
    noRootGenome.pop(0)     # root always has an index of 0

    randomMutation = rnd.choice(['del', 'add'])
    
    if randomMutation == 'add':
        jointAdded = _addRndJoint(noRootGenome, agent.gene)

        if not jointAdded:
            neuronTypes = _searchNeurons(noRootGenome)
            _delRndJoint(agentGenome, neuronTypes)\

    else:
        neuronTypes = _searchNeurons(noRootGenome)
        jointDelted = _delRndJoint(agentGenome, neuronTypes)

        if not jointDelted:
            _addRndJoint(noRootGenome, agent.gene)
```

#### rndMutate
```python
def rndMutate(agent):
    dropChance = rnd.random()
    
    if dropChance <= config.mutationChance:
        mutate(agent)

        if config.lvldMutation:
            rndMutate(agent)
```

---

## GenePrcs

### Functions

---

## Neuron Commands

### Functions

---

## Data Output

### Functions

---

## Model

### Functions