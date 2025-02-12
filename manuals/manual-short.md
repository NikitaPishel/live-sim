# Quickstart

## Contents
[Intro](#Getting-Started)
[Genome](#About-Genome)
[Mutation](#Mutations-and-Genetic-Algorithm)
[Configuration](#Configuration)
[Environment](#Simple-Environment)
[Model](#Creating-Model)

## Getting Started
This manual gives you a good intro to the topic. Before using this manual, don't forget to [install it!](../README.md)

## About Genome
First of all, let's talk about the most essential part of all the project, genome. It has a specific structure, and it defines the whole way how our Neural Network works. This is very important because all these different factors will affect the speed and efficiency of a model, its capabilities, efficiency, speed of training, etc.

#### Structure
My NN structure is called oriented graph with loops. In Neural Networks, It doesn't meet as often. There's some reasons for this, but now we will look at how it looks like.

```python
class Neuron:
    def __init__(self, cmd=None):
        self.cmd = cmd      # neuron's command
        self.joints = []
```
*src/server/model/genome.py*

We've got a super class *Neuron*, which defines 2 parameters that are same for all neurons, not depending on whether they are internal, inputs, or outputs. other child classes define only function inputs.

```python
class Sensor(Neuron):
    def __init__(self):
        super().__init__()
    
    def recall(self, fieldTree, agent) -> float:
        cmdOut = self.cmd(fieldTree, agent)
        return cmdOut

class Processor(Neuron):
    def __init__(self):
        super().__init__()
    
    def recall(self, amp) -> float:
        cmdOut  = self.cmd(amp)
        return cmdOut

class Signal(Neuron):
    def __init__(self):
        super().__init__()
        self.refs = 0   # stores amount of joints that are referenced to this neuron, used to check if can delete a signal
    
    def recall(self, fieldTree,  agent, amp) -> bool:
        cmdOut = self.cmd(fieldTree, agent, amp)
        return cmdOut
```
*[src/server/model/genome.py](../src/server/model/genome.py)*

As I said earlier, there's 3 types of neurons, inputs internal and outputs. In code they are called *Sensors, Processors and Signals*. Their function *recall* runs their command stored in parameter *cmd* with a special set for arguments. *Signals* and *Processors* return values from -1 to 1, while *Signals* return boolean value, *true* if output is successful and *false* if output has failed.

There's also *GeneRoot* class present in the code
```python
class GeneRoot:
    def __init__(self):
        self.joints = []
```

It serves as a starter point for a genome. Its joints are only *Sensor* class Neuron, and *Sensor* class object can only be a child of *GeneRoot*. *Signal* objects can't have any joints, as they are "end points" of a genome, and they output their signal externally.
*[src/server/model/genome.py](../src/server/model/genome.py)*

#### Commands
Commands in the project are stored in 4 lists, one for each neuron type and a combined one with a full list of functions.
```python
inputCmd = [
    constantOn
]

interCmd = [
    tanhList,
    reLU,
    invert
]

outputCmd = [
    outMoveSouth,
    outMoveNorth,
    outMoveEast,
    outMoveWest
]

allCmd = inputCmd + interCmd + outputCmd
```
*[src/server/model/neuronCmd.py](../src/server/model/neuronCmd.py)*

Commands can be any function with specific inputs and outputs which depend from either it's input command, internal or output. Commands is the main way how you train a model with the usage of an environment. The way NN behaves is dictated by the commands. Internal neurons are the main brain which creates dependency graph, while inputs and outputs are used to work with external factors. In this example we've got constant 1 as an input, and 4 movement directions as outputs. If you want to add any new command, you give to it any specific parameters and add them to the list. Parameters for internal neurons always stay the same as they don't directly communicate with external factors.

## Mutations and Genetic Algorithm
The model that is used to train a NN is called *Genetic Algorithm*. As said earlier, it has some sort of an environment, and NN tries to meet the condition by random mutations. It meets the requirement using mutations with a mechanism which picks agents who met the requirement, and these successful agents create a new population with some mutations, which can randomly produce more successful genome (Neural Network). 

[flowchart](../images/evolution-chart-2.png)

Notice, that mutations don't create random neuron, they create random connections between them. During the connection addition, there's a chance set by user that mutation will create a connection from random neuron to the new one, meaning it creates a new neuron. Also, when the only connection to the neuron is deleted, there's no more reference to the neuron, so it gets deleted.

There's also an additional function called *leveled mutation*:
```python
def rndMutate(agent):
    dropChance = rnd.random()
    
    if dropChance <= config.mutationChance:
        mutate(agent)

        if config.lvldMutation:
            rndMutate(agent)
```
*[src/server/model/mutation.py](../src/server/model/mutation.py)*

It's a main mutation function. As we can see in the *lvldMutation* part if mutation is created, it will try to mutate once more, until it fails to.

## Configuration
Our simulation can be configured with specified for these files. They've got a set of settings, which can configure either environment or Neural Network (genome) itself. Let's look at our standard settings:
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
*[data/presets/standard.json](../data/presets/standard.json)*

each setting corresponds for some value in the code. Also, configuration supports multiple layers. In other words, configuration will keep some settings from the first layer, then it will take some more from the second one, etc. Let's look at our 2nd-level json example file:
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
*[data/presets/example.json](../data/presets/example.json)*

As we can see, there's some settings that are set to value *null*. This means that they are not covered by the 2nd layer, and they keep values from a previous, standard configuration. You can add any amount of layers, but in example there's only 2 present.

**Full list of settings**:
- fieldSize: list \[x, y\] which states the map size, e. g. [32, 64] will create a field with 32 tiles wide and 64 tiles tall
- maxAmountOfAgents: amount of agents that are created in each simulation
- startMutation: amount of mutations created on the start of training or when none of agents survived

- maxGenomeLength: maximum size of neurons in a neural network
- mutationChance: chance with which a genome of a new cell will mutate at the start of a new iteration
- newNeuronChance: chance of creation of a new neuron instead of a new joint
- leveledMutation: if *true*, and mutation appeared, it will "drop a dice" for a new mutation. it will repeat until mutation doesn't happen

- maxActions: maximal amount of actions (outputs) that an agent can do during one move
- geneRuntime: stores information about for how long can a genome run
    - multiplier: multiplies value of a current runtime
    - dependency: states from what factors runtime will depend. Environment support 2 types below
        - fixed: it will be a constant number
        - geneLength: it will correspond to maximal genome length, and can be combined with multiplier to reach more specific values
    - fixedValue: if dependency is *fixed*, it will use this parameter to get the fixed runtime value. Notice, that it is still multiplied by the parameter *multiplier*

- newGenTrigger: states trigger needed to start a new iteration. In example supports only *timer*
- triggerConditions: a set of parameters to control iteration trigger
    - timeLimit: time limit of simulation, used in *timer* trigger

- numberOfIterations: amount of iterations present in a full training cycle

- savingLevels: a set of parameters used to find out which data should be stored in a log
    - passedNumber: states one of how many iterations it will store the amount of passed agent and survivability, e. g. if 10 it will store every 10th iteration's passed amount, if 20 every 20th, etc.
    - passedGenomes: states one of how many iterations it will store all the genomes of all passed agents
    - iteration: states one of how many iterations it will store every position of cells in every move of an iteration

- outputPath: path of output log folder

Notice that many values from this configuration are needed only for built-in environment, but some (like mutation chance) are needed for Neural Network.

## Simple Environment
Now we need an environment. Same as earlier, for explanation I will use the built-in example.

#### Adding environment parameters to Agent class
This model trains cells that can only move in any 4 directions: south, west, north and east. They can only move on a zone set by a user, so if they try to walk out of the map they will just hit the wall. They will learn to move left. Let's look at our agent's code:

```python
import random

import genome
from configuration import config
import neuronCmd

class Agent:
    def __init__(self, x=0, y=0):
        self.pos = [x, y]

        # Creating root of the genome
        self.gene = genome.GeneRoot() # decision map of an agent
        
        # Adding one random input to the genome as an agent is created, as genome functions work only with non-empty genes.
        rndSensor = genome.Sensor()
        rndCmd = random.choice(neuronCmd.inputCmd)
        rndSensor.cmd = rndCmd
        self.gene.joints.append(rndSensor)
```
*[src/server/model/agent.py](../src/server/model/agent.py)*

As we can see, our cell has got 2 parameters: position and genome. Position allows our cell to move around the map, and gene - is our main tool, as it is neural network itself, in other words "brain" of a cell.

#### Writing custom functions
Now let's look at functions that neurons can perform:

```python
inputCmd = [
    constantOn
]

interCmd = [
    tanhList,
    reLU,
    invert
]

outputCmd = [
    outMoveSouth,
    outMoveNorth,
    outMoveEast,
    outMoveWest
]

allCmd = inputCmd + interCmd + outputCmd
```
*[src/server/model/neuronCmd.py](../src/server/model/neuronCmd.py)*

Usually our internal functions stay the same as they are mathematical functions used in almost every AI ever created. But our inputs and outputs depend on the environment. In our situation, the only input is a function that always returns 1, and our outputs are 4 movement directions.

#### Generating Environment
New environment with new agents should be generated each time as we run a new iteration. As an input it has successful agents from the previous iteration, which will be needed to generate new iteration with some mutations. Let's look at the function *genEnv*:

```python
def genEnv(slctList, maxPos):
    fieldTree = dts.AvlTree()
    agentQueue = dts.Queue()

    slctAmount = len(slctList)

    srv = math.floor((slctAmount / config.maxAgents) * 1000) / 10
    print(f'agents passed: {slctAmount}')
    print(f'survivability: {srv}%')

    if slctAmount == 0:
        for i in range(config.maxAgents):
            addRndAgent(fieldTree, agentQueue, maxPos)
    
    else:
        fixedClones = math.floor(config.maxAgents / slctAmount)
        rndClones = config.maxAgents % slctAmount

        for i in range(fixedClones):
            for slctAgent in slctList:
                clonedAgent = slctAgent.clone()

                newID = genId(fieldTree, maxPos)
                clonedAgent.pos = getPos(newID)

                rndMutate(clonedAgent)

                fieldTree.insert(newID, clonedAgent)
                agentQueue.enqueue(clonedAgent)
        
        for i in range(rndClones):
            rndIndex = rnd.randint(0, slctAmount-1)

            slctAgent = slctList[rndIndex]
            clonedAgent = slctAgent.clone()

            newID = genId(fieldTree, maxPos)
            clonedAgent.pos = getPos(newID)

            rndMutate(clonedAgent)

            fieldTree.insert(newID, clonedAgent)
            agentQueue.enqueue(clonedAgent)
    
    return {'field': fieldTree, 'queue': agentQueue}
```
*[src/server/model/envExample.py](../src/server/model/envExample.py)*

As we can see it create a new field and new run queue of agents. After this it will use list of succesful agents from the previous iteration to create copies of them until we reach the needed amount of agents. Then it creates random mutations among their Neural Networks and places new agents in random places around the map. Finally it returns ready environment so it can be used in our model.

## Creating Model
Now let's create a simple model for the environment. This is the simplest part, as we just need to connect framework with an environment. First, we need to create a run function, in which all our code will be executed. Also we need to import our configuration class. Also, all our data will be stored in a dictionary, so it can be later formatted into JSON and displayed on a web client:

```python
# Preset for custom models
# =====
from time import time
from configuration import config

# Simulation execution code
def run():
    dataOut = {}

    for i in range(config.itrNum):
        print(f'running iteration {i+1}/{config.itrNum}')

        dataOut[i+1] = {}

# Simple config input
dataFile = input('Enter name of your output file: ')
dataFile += '.json'

# Run execution code
start = time()
run(dataFile)
end = time()

print(f'time taken: {(end - start)/60} min')
```
*[src/server/model/modelPreset.py](../src/server/model/modelPreset.py)*

After we've got our basic skeleton, we can implement our environment. We need to create an environment configuration before the *iteration loop*, then we need to write our iteration cycle inside of *iteration loop*. After the training process, we need to output information after the loop.

```python
from configuration import config
import dataOutput as dtOut
from envExample import *

# Simulation execution code
def run(outFile):

    # Data for info output
    dataOut = {}

    # Env setup
    maxPos = config.fieldSize[0] * config.fieldSize[1]
    itrData = []

    # Training process
    for i in range(config.itrNum):
        print(f'running iteration {i+1}/{config.itrNum}')
        # Creating new iteration record
        dataOut[i+1] = {}

        # Loading new iteration
        currEnv = genEnv(itrData, maxPos)
        fieldTree = currEnv['field']
        agentQueue = currEnv['queue']

        # Running an iteration
        itrData = runItr(maxPos, fieldTree, agentQueue)

        # Saving data into current iteration record
        dtOut.saveGenome(dataOut, i+1, itrData)
        dtOut.savePassedNum(dataOut, i+1, itrData)

    # After sim end saving final result
    dataOut[config.itrNum] = {}
    dtOut.saveGenome(dataOut, config.itrNum, itrData)
    dtOut.saveRunData(dataOut, outFile)

# User input
dataFile = input('Enter name of your output file: ')
dataFile += '.json'

# Run training
start = time()
run(dataFile)
end = time()

print(f'time taken: {(end - start)/60} min')
```
*[src/server/model/modelExample.py](../src/server/model/modelExample.py)*

As we can see in an example of a model, we create *maxPos* and itrData list to configure our environment before the first launch. Then, in a loop, we create a dictionary addressed as *i+1* so we can store iteration result. After this we create a new environment, based on information given. Notice, that *itrData* is an empty list that is created before the loop, and later, when we've got some output from the previous iteration, we use it to train our future iteration. In our case this information is a list of successful agents. Finally, we run a simulation, store output in *itrData* list and add formatted data into the output dictionary. After the training process we store the output data in a file.