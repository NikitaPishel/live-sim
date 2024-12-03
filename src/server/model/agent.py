import mutation as mtn
import genome as gnm
import data_structures as dts
import random as rnd
from configuration import config

class Agent:
    def __init__(self, x=0, y=0):
        self.pos = [x, y]
        self.dir = 0 # 8 directions 0 to 7 from down clockwise (south=0, south-east=1, east=2, etc.)

        self.gene = gnm.GeneRoot() # decision map of an agent
        self.id = 0
