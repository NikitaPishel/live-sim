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
class _AvlNode:
    def __init__(self):
        self.key = None
        self.data = None
        self.lChild = None
        self.rChild = None
        self.height = 1
        self.balance = 0
```

#### AvlTree
```python
class AvlTree:
    def __init__(self):
        self.root = None
```

#### QueueNode
```python
class _QueueNode:

    def __init__(self, data=None, child=None):
        self.data = data
        self.child = child
```

#### Queue
```python
class Queue:
    def __init__(self):
        self.rear = None
```

#### StackNode
```python
class _StackNode:
    def __init__(self):
        self.data = None
        self.child = None
```

#### Stack
```python
class Stack:
    def __init__(self):
        self.front = None
```

### Functions

#### searchNode (AvlNode)
```python
    def _searchNode(self, key):
        if key > self.key:
            if self.rChild != None:
                return self.rChild._searchNode(key)

            else:
                raise Exception(f'Trying to search for unexisting tree key \'{key}\'')    

        elif key < self.key:
            if self.lChild != None:
                return self.lChild._searchNode(key)
            
            else:
                raise Exception(f'Trying to search for unexisting tree key \'{key}\'')
        
        elif self.key == key:
            return self
```

#### inTree (AvlNode)
```python
    def inTree(self, key):
        if key > self.key:
            if self.rChild != None:
                return self.rChild.inTree(key)

            else:
                return False    

        elif key < self.key:
            if self.lChild != None:
                return self.lChild.inTree(key)
            
            else:
                return False

        elif self.key == key:
            return True
```

#### insertNode (AvlNode)
```python
    def insertNode(self, key, data):
        if key < self.key:
            if self.lChild != None:
                self.lChild.insertNode(key, data)
            
            else:
                self.lChild = _AvlNode()
                self.lChild.key = key
                self.lChild.data = data
        
        elif key > self.key:
            if self.rChild != None:
                self.rChild.insertNode(key, data)

            else:
                self.rChild = _AvlNode()
                self.rChild.key = key
                self.rChild.data = data

        elif self.key == key:
            raise Exception(f'Current tree key \'{key}\' already exists')
        
        else:
            raise Exception(f'Unexpected tree key \'{key}\' was used')
```

#### deleteNode (AvlNode)
```python
    def deleteNode(self):
        if self.lChild != None and self.rChild != None:
            newNode = self.rChild.lowest()

            newSubtree = deleteTree(self.rChild, newNode.key)
            self.rChild = newSubtree

            newNode.lChild = self.lChild
            newNode.rChild = self.rChild

        elif self.lChild != None:
            newNode = self.lChild

        elif self.rChild != None:
            newNode = self.rChild
        
        else:
            return None
        
        return newNode
```

#### findSuccessorParent (AvlNode)
```python
    def findSuccessorParent(self, tree):
        if tree.lChild.key == self.key:
            return tree.rChild
```

#### updateHeight (AvlNode)
```python
    def updateHeight(self):
        if self.lChild != None:
            lHeight = self.lChild.updateHeight()
            self.rChild = _balanceTree(self.rChild)
        
        else:
            lHeight = 0

        if self.rChild != None:
            rHeight = self.rChild.updateHeight()
            self. rChild = _balanceTree(self.rChild)

        else:
            rHeight = 0
        
        self.height = max(lHeight, rHeight) + 1

        return self.height
```

#### lowest (AvlNode)
```python
    def lowest(self):
        if self.lChild != None:
            scrNode = self.lChild.lowest()
            
            return scrNode
            
        else:
            return self
```

#### deleteTree (AvlNode)
```python
def deleteTree(node, key):
    if node != None:
        if key < node.key:
            newSub = deleteTree(node.lChild, key)
            node.lChild = newSub
            
            return node
        
        elif key > node.key:
            newSub = deleteTree(node.rChild, key)
            node.rChild = newSub
            
            return node

        elif node.key == key:
            newRoot = node.deleteNode()

            return newRoot
        
    else:
        raise Exception('Trying to delete unexisting tree key \'{key}\'')
```

#### getBalance (AvlNode)
```python
def getBalance(node):
    if node == None:
        return 0

    else:
        if node != None:
            if node.lChild != None:
                lHeight = node.lChild.height

            else:
                lHeight = 0

            if node.rChild != None:
                rHeight = node.rChild.height
            
            else:
                rHeight = 0
        
        return lHeight - rHeight  
```

#### balanceTree (AvlNode)
```python
def _balanceTree(node):

        balance = getBalance(node)
        
        if balance < -1:
            rBalance = getBalance(node.rChild)

            if rBalance == 1:
                newTree = _lrTurn(node)
                return newTree
            
            else:
                newTree = _lTurn(node)
                return newTree

        elif balance > 1:
            lBalance = getBalance(node.lChild)

            if lBalance == -1:
                newTree = _rlTurn(node)
                return newTree
            
            else:
                newTree = _rTurn(node)
                return newTree


        else:
            return node
```

#### lTurn (AvlNode)
```python
def _lTurn(node):
    newRoot = node.rChild
    midTree = newRoot.lChild
    
    newRoot.lChild = node
    node.rChild = midTree

    return newRoot
```

#### rTurn (AvlNode)
```python
def _rTurn(node):
    newRoot = node.lChild
    midTree = newRoot.rChild

    node.lChild = midTree
    newRoot.rChild = node

    return newRoot
```

#### lrTurn (AvlNode)
```python
def _lrTurn(node):
    node.rChild = _rTurn(node.rChild)
    newTree = _lTurn(node)

    return newTree
```

#### rlTurn (AvlNode)
```python
def _rlTurn(node):
    node.lChild = _lTurn(node.lChild)
    newTree = _rTurn(node)
    return newTree
```

#### get (AvlTree)
```python
    def get(self, key):
        if self.root != None:
            return self.root._searchNode(key)

        else:
            raise Exception(f'Trying to search for unexisting tree key \'{key}\'')
```

#### setData (AvlTree)
```python
    def setData(self, key, data):
        if self.root != None:
            node = self.root._searchNode(key)

            node.data = data

        else:
            raise Exception(f'Trying to search for unexisting tree key \'{key}\'')
```

#### insert (AvlTree)
```python
    def insert(self, key, data=None):
        if self.root != None:
            self.root.insertNode(key, data)
            self.root.updateHeight()
            self.root = _balanceTree(self.root)
        
        else:
            self.root = _AvlNode()
            self.root.key = key
            self.root.data = data
```

#### delete (AvlTree)
```python
    def delete(self, key):
        if self.root != None:
            self.root = deleteTree(self.root, key)

            if self.root != None:
                self.root.updateHeight()
                self.root = _balanceTree(self.root)

        else:
            raise Exception("Deleting a node from an empty tree")
```

#### exists (AvlTree)
```python
    def exists(self, key):
        if self.root != None:
            keyExists = self.root.inTree(key)
            return keyExists

        else:
            return False
```

#### searchData (QueueNode)
```python
    def searchData(self, data) -> bool:
        if self == data:
            return True
        
        elif self.child == None:
                return None
```

#### itrLength (QueueNode)
```python
    def itrLength(self, qLength) -> int:
        qLength += 1

        if self.child != None:
            return self.child.itrLength(qLength)
        
        elif self.child == None:
            return qLength
```

#### enqueue (Queue)
```python
    def enqueue(self, data):
        newNode = _QueueNode(data)

        if self.rear == None:
            self.front = newNode
            self.rear = newNode
        
        else:
            self.rear.child = newNode
            self.rear = newNode
```

#### dequeue (Queue)
```python
    def dequeue(self):
        if self.front == self.rear:
            self.front = None
            self.rear = None

        elif self.front != None:
            self.front = self.front.child

        else:
            raise Exception('Calling \'deque\' command in an empty Queue')
```

#### peek (Queue)
```python
    def peek(self):
        if self.front == None:
            return None
        
        else:
            return self.front.data
```

#### getLength (Queue)
```python
    def getLength(self):
        if self.front != None:
            return self.front.itrLength(0)
        
        else:
            return 0
```

#### itrLength (StackNode)
```python
    def itrLength(self, currLength):
        if self.child != None:
            return self.child.itrLength(currLength + 1)
        
        else:
            return currLength + 1
```

#### itrFind (StackNode)
```python
    def itrFind(self, data):

        if self.data == data:
            return True
        
        elif self.child != None:
            return self.child.itrFind(data)
        
        else:
            return False
```

#### isOccupied (Stack)
```python
    def isOccupied(self):
        if self.front == None:
            return False
        
        else:
            return True
```

#### peek (Stack)
```python
    def peek(self):
        if self.isOccupied():
            return self.front.data
        
        else:
            return None
```

#### insert (Stack)
```python
    def insert(self, data):
        oldFront = self.front
        newFront = _StackNode()

        newFront.data = data
        newFront.child = self.front
        self.front = newFront
```

#### getLength (Stack)
```python
    def getLength(self):
        if self.isOccupied():
            return self.front.itrLength(0)
```

#### find (Stack)
```python
    def find(self, data):
        if self.isOccupied():
            return self.front.itrFind(data)
```

#### delete (Stack)
```python
    def delete(self):
        if self.isOccupied():
            self.front = self.front.child
        
        else:
            raise Exception ('deleting an element from an empty stack')
```

---

## Configuration

### Classes
#### Configuration
```python
class Configuration:
    _instance = None

    def __init__(self):
        Configuration._instance = self

        # Changing recursion limit
        sys.setrecursionlimit(2500)

        # Load standard settings
        self.loadConfig(f'./data/presets/standard.json')
```

### Functions
#### getInstance
```python
    @classmethod
    def getInstance(cls):
        if Configuration._instance == None:
            Configuration()
        return cls._instance
```

#### loadConfig
```python
    # This method loads different parameters from the configurational JSON file.
    @classmethod
    def loadConfig(self, filename):
        with open(filename, 'r') as file:
            settings = json.load(file)

        if settings['fieldSize'] != None:
            self.fieldSize = settings['fieldSize']

        if settings['maxAmountOfAgents'] != None:
            self.maxAgents = settings['maxAmountOfAgents']
        
        if settings['maxGenomeLength'] != None:
            self.maxGenomeLen = settings['maxGenomeLength']

        if settings['mutationChance'] != None:
            self.mutationChance = settings['mutationChance']

        if settings['newNeuronChance'] != None:
            self.newNeuronChance = settings['newNeuronChance']
        
        if settings['leveledMutation'] != None:
            self.lvldMutation = settings['leveledMutation']

        # Amount of mutations that are created on the start of a simulation
        if settings['startMutation'] != None:
            self.startMutation = settings['startMutation']

        if settings['maxActions'] != None:
            self.maxActions = settings['maxActions']

        geneRuntime = settings['geneRuntime']

        if geneRuntime != None:
            if geneRuntime['multiplier'] != None:
                self._multiplier = geneRuntime['multiplier']
            
            if geneRuntime['dependency'] != None:
                self.dependency = geneRuntime['dependency']

            if self.dependency == 'fixed':

                if geneRuntime['fixedValue'] != None:
                    self._fixedGeneValue = geneRuntime['fixedValue']

                self.geneTime = self._multiplier * self._fixedGeneValue

            elif self.dependency == 'geneLength':
                self.geneTime = self._multiplier * self.maxGenomeLen
                math.floor(self.geneTime)
            
            else:
                raise Exception('unknow dependency in \'geneRuntime\' variable')
        
        trigParams = settings['triggerConditions']

        if settings['newGenTrigger'] == 'timer':
            self.trigger = 'timer'
            
            if trigParams['timeLimit'] != None:
                self.timeLim = trigParams['timeLimit']
        
        elif settings['newGenTrigger'] == 'minAgents':
            self.trigger = 'minAgents'

            if self.agentsLim != None:
                self.agentsLim = trigParams['minAmountOfAgents']
        
        if settings['numberOfIterations'] != None:
            self.itrNum = settings['numberOfIterations']
        
        if settings['savingLevels'] != None:

            svLvls = settings['savingLevels']

            if svLvls['passedNumber'] != None:
                self.savePassedNumber = svLvls['passedNumber']
            
            if svLvls['passedGenomes'] != None:
                self.savePassedGenomes = svLvls['passedGenomes']
            
            if svLvls['iteration'] != None:
                self.saveIteration = svLvls['iteration']
        
        if settings['outputPath'] != None:
            self.outputPath = settings['outputPath']

        # exceptions
        if self.maxActions < 1:
            raise Exception('configErr, maxActions below 1')
        
        if self.geneTime < 1:
            raise Exception('configErr, maxActions below 1')
```

### JSON files
#### Standart.json
```json
{
    "fieldSize": [32, 32],
    "maxAmountOfAgents": 10,
	"startMutation": 5,

    "maxGenomeLength": 10,
    "mutationChance": 0.1,
    "newNeuronChance": 0.3,
    "leveledMutation": true,

    "maxActions": 1,
    "geneRuntime": {
        "multiplier": 1,
        "dependency": "fixed",

        "fixedValue": 50
    },

    "newGenTrigger": "timer",
    "triggerConditions": {
        "timeLimit": 100
    },

    "numberOfIterations": 10,

    "savingLevels": {
        "passedNumber": 1,
        "passedGenomes": 100,
        "iteration": 100
    },

    "outputPath": "./data/logs"
}
```

#### example.json
```json
{
    "fieldSize": [64, 64],
    "maxAmountOfAgents": 128,
	"startMutation": 20,

    "maxGenomeLength": 20,
    "mutationChance": 0.5,
    "newNeuronChance": 0.5,
    "leveledMutation": null,

    "maxActions": 1,
    "geneRuntime": null,

    "newGenTrigger": "timer",
    "triggerConditions": {
        "timeLimit": 100
    },

    "numberOfIterations": 10,

    "savingLevels": {
        "passedNumber": 1,
        "passedGenomes": 10,
        "iteration": 1
    },

    "outputPath": null
}
```
---

## Agents

### Classes

#### Agent
```python
class Agent:
    def __init__(self, x=0, y=0):
        self.pos = [x, y]

        # Creating root of the genome
        self.gene = gnm.GeneRoot() # decision map of an agent
        
        # Adding one random input to the genome as an agent is created, as genome functions work only with non-empty genes.
        rndSensor = gnm.Sensor()
        rndCmd = rnd.choice(nrnCmd.inputCmd)
        rndSensor.cmd = rndCmd
        self.gene.joints.append(rndSensor)
```


### Functions

#### clone (Agent)
```python
    # Creates in memory exact clone of the agent
    def clone(self):
        agentClone = Agent()

        agentClone.pos = self.pos
        agentClone.gene = gnm.cloneGene(self.gene)

        return agentClone
```

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

#### enqueueJoints
```python
def _enqueueJoints(nrnData, runQueue, neuron):
    for child in neuron.joints:
        if child in nrnData.keys():
            nrnInp = list(nrnData[child].values())

        else:
            nrnInp = []

        queueCall = {'nrn': child, 'input': nrnInp}
        
        runQueue.enqueue(queueCall)
```

#### saveInput
```python
def _saveInput(nrnOut, nrnData, neuron):
    for child in neuron.joints:
        if child not in nrnData.keys():
            nrnData[child] =  {}

        nrnData[child][neuron] = nrnOut
```

#### runGene
```python
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
```

---

## Neuron Commands

### Functions

#### getSum
```python
def _getSum(amp):
    ampSum = 0

    for i in amp:
        ampSum += i

    return ampSum
```

#### tanhList
```python
def tanhList(amp):
    ampSum = _getSum(amp)
    return math.tanh(ampSum)
```

#### reLU
```python
def reLU(amp) -> float:
    ampSum = _getSum(amp)
    
    if ampSum > 0:
        return ampSum

    else:
        return 0
```

#### invert
```python
def invert(amp):
    return tanhList(amp) * 1
```

---

## Data Output

### Functions

#### makeGeneReadable
```python
def makeGeneReadable(gene):
    readableGene = []

    cmdNameTable = {
        nrnCmd.constantOn: "ConstantOn",
        nrnCmd.tanhList: "tanhList",
        nrnCmd.reLU: "reLU",
        nrnCmd.invert: "invert",
        nrnCmd.outMoveNorth: "moveNorth",
        nrnCmd.outMoveSouth: "moveSouth",
        nrnCmd.outMoveEast: "moveEast",
        nrnCmd.outMoveWest: "moveWest"
        }

    for i in range(len(gene)):
        nrnjoints = []
        for ref in gene[i].joints:
            nrnjoints.append(gene.index(ref))

        nrnData = {}
        nrnData["id"] = i
        nrnData["command"] = cmdNameTable[gene[i].cmd]
        nrnData["joints"] = nrnjoints

        readableGene.append(nrnData)

    return readableGene
```

#### saveGenome
```python
def saveGenome(dataOut, itrNum, itrData):
    if itrNum % config.savePassedGenomes == 0:
        dataOut[itrNum]['succGenomes'] = []

        for agentIndex in range(len(itrData)):
            slctGene = gnm.getGenome(itrData[agentIndex].gene, [])
            slctGene.pop(0)

            rdblGene = makeGeneReadable(slctGene)

            dataOut[itrNum]['succGenomes'].append(rdblGene)
```

#### savePassedNum
```python
def savePassedNum(dataOut, itrNum, itrData):
    if itrNum % config.savePassedNumber == 0:

        slctAmount = len(itrData)
        srv = math.floor((slctAmount / config.maxAgents) * 1000) / 10

        dataOut[itrNum]['passedAmount'] = slctAmount
        dataOut[itrNum]['survivability'] = f'{srv}%'
```

#### saveRunData
```python
def saveRunData(data, filename):
    with open(f'{config.outputPath}/{filename}', 'w') as path:
        json.dump(data, path)
```

---

## Model

### function run
```python
def run():
    dataOut = {}

    for i in range(config.itrNum):
        print(f'running iteration {i+1}/{config.itrNum}')

        dataOut[i+1] = {}
```