import random as rnd

import genome as gnm
from configuration import config
import neuronCmd as nrnCmd

'''
Agent class is a main training element, which has some parameters and can function different depending from environment set by a 
programmer. Main part of gene always stays the same. It current example It has got parameters needed in a simple environment where agents can change their position.
'''
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
    
    # Creates in memory exact clone of the agent
    def clone(self):
        agentClone = Agent()

        agentClone.pos = self.pos
        agentClone.gene = gnm.cloneGene(self.gene)

        return agentClone
