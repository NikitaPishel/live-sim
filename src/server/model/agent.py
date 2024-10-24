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
agents = []
for i in range(200):
    print('creating agent...')
    agents.append(Agent())

    agents[i].gene.joints.append(mtn.Sensor())
    agents[i].gene.joints[0].cmd = rnd.choice(mtn.nrnCmd.inputCmd)
    
    mtn.mutate(agents[i])

    print(mtn.getGenome(agents[i].gene))
    print(f'agent {i} created!')