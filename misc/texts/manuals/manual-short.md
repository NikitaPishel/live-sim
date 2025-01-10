# Quickstart

## Contents
[Intro](#Getting-Started)
[Environment](#Simple-Environment)
[Configuration](#Configuration)
[Model](#Creating-Model)

## Getting Started
This manual gives you a good intro to the topic. Before using this manual, don't forget to [install it](../README.md)!

## Simple Environment
First of all, we need an environment. For explanation I will use the built-in example. This model trains cells (in computing called agents) that can only move in any 4 directions: south, west, north and east. They can only move on a zone set by a user, so if they try to walk out of the map they will just hit the wall. Let's look at our agent's code:

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
*src/server/model/agent.py*

As we can see, our cell has got 2 parameters: position and genome. Position allows our cell to move around the map, and gene - is our main tool, as it is neural nwtwork itself, in other words "brain" of a cell. Now let's look at functions that neurons can complete:


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
*src/server/model/neuronCmd.py*

Usually our internal functions stay the same as they are mathematical functions used in almost every AI. But our inputs and outputs are depend from the environment. In our situation, our only input is a function that always returns 1, and our outputs are 4 movement directions.

## Configuration


## Creating simple Model
Now let's create a simple model for our environment. This is the simplest part, as we just implement our environment. First, we need to create a run function, in which all out code will be executed. Also we need to import our configuration class:

```python
# Example of a working model
from time import time
from envExample import *

# Simulation execution code
def run(outFile):
    pass

# Run training
start = time()
run(dataFile)
end = time()

print(f'time taken: {(end - start)/60} min')
```
*src/server/model/modelExample.py*