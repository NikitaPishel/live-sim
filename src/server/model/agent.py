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