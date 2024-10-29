import mutation as mtn
import genome as gnm
import data_structures as dts
import random as rnd

class Agent:
    def __init__(self, x=0, y=0):
        self.pos = [x, y]
        self.dir = 0 # 8 directions -1 to 1 from down clockwise (south=-1, south-west=-0.75, west=-0.5, etc.)

        self.gene = gnm.GeneRoot() # decision map of an agent
        self.id = 0

# Temporary test files
# from time import time
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

myAgent = Agent()
myAgent.gene.joints.append(mtn.Sensor())

for i in range(20):
    try:
        mtn.mutate(myAgent)
        print(f'mutation {i} created!')
    
    except:
        print('error occured!')
        
        agentGenome = gnm.getGenome(myAgent.gene)
        agentGenome.pop(0)

        print(f'agent genome: {agentGenome}\njoints of root: {myAgent.gene.joints}')

endTime = time()
print(f'operation runtime: {endTime-startTime} sec')
'''