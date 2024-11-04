import mutation as mtn
import genome as gnm
import data_structures as dts
import random as rnd
from configuration import config

class Agent:
    def __init__(self, x=0, y=0):
        self.pos = [x, y]
        self.dir = 0 # 8 directions -1 to 1 from down clockwise (south=-1, south-west=-0.75, west=-0.5, etc.)

        self.gene = gnm.GeneRoot() # decision map of an agent
        self.id = 0

# Temporary test files
from time import time
'''
agents = []

startTime = time()

for i in range(5000):
    print('creating agent...')
    agents.append(Agent())

    agents[i].gene.joints.append(mtn.Sensor())
    agents[i].gene.joints[0].cmd = rnd.choice(mtn.nrnCmd.inputCmd)
    
    mtn.mutate(agents[i])

    print(mtn.getGenome(agents[i].gene))
    print(f'agent {i} created!')

endTime = time()
'''

'''
startTime = time()

agentsList = []

for sus in range(1):
    myAgent = Agent()
    myAgent.gene.joints.append(gnm.Sensor())

    for i in range(2):
        print(f'mutation {i}')
        mtn.mutate(myAgent)
        #print(f'mutation {i} created!')

        myGenome = gnm.getGenome(myAgent.gene)
        print(myGenome)

        agentGenomeLen = len(myGenome)-1
        print(agentGenomeLen)


        
        if agentGenomeLen > config.maxGenomeLen:
            print(agentGenomeLen, config.maxGenomeLen)
            raise Exception('Reached over maximum genome length')
        
        print(myAgent.gene)

    agentsList.append(myAgent)

endTime = time()

print(f'operation runtime: {endTime-startTime} sec')

print(gnm.getGenome(agentsList[0].gene, sus=0))
'''

'''
myAgent = Agent()

myAgent.gene.joints.append(gnm.Sensor())
myAgent.gene.joints[0].joints.append(gnm.Processor())
myAgent.gene.joints[0].joints.append(gnm.Processor())

myGenome = gnm.getGenome(myAgent.gene)

noRootGenome = myGenome.copy()
noRootGenome.pop(0)

print(myAgent.gene.joints)
print(myAgent.gene.joints[0].joints)

print(noRootGenome)

addbl = mtn._getAddblJoints(noRootGenome)
print(f'============================\n{addbl}')
'''

myAgent = Agent()
myAgent.gene.joints.append(gnm.Sensor())

myGenome = gnm.getGenome(myAgent.gene)
print(f'=====\n{myGenome}')

mtn.mutate(myAgent)
myGenome = gnm.getGenome(myAgent.gene)
print(f'=====\n{myGenome}')

mtn.mutate(myAgent)
myGenome = gnm.getGenome(myAgent.gene)
print(f'=====\n{myGenome}')

agentGenomeLen = len(myGenome)-1
print(f'length: {agentGenomeLen}')