import math
import json
import os

class Configuration:
    _instance = None

    def __init__(self, filename):
        Configuration._instance = self
        os.chdir('../')
        self._serverDir = os.getcwd()

        # Load standart settings
        self.loadConfig(f'{self._serverDir}/data/presets/standart.json')

        # Load non-standart settings
        self.loadConfig(filename)
    
        # exceptions
        if self.maxActions < 1:
            raise Exception('configErr, maxActions below 1')
        
        if self.geneTime < 1:
            raise Exception('configErr, maxActions below 1')

    @classmethod
    def getInstance(cls, filename=None):
        if Configuration._instance == None:
            Configuration(filename)
        return cls._instance

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
        # Amount of mutations that are created on the start of a simulation
        if settings['startMutation'] != None:
            self.startMutation = settings['startMutation']

        if settings['maxActions'] != None:
            self.maxActions = settings['maxActions']

        geneRuntime = settings['geneRuntime']

        if geneRuntime != None:
            multiplier = geneRuntime['multiplier']
            dependecy = geneRuntime['dependency']

            if dependecy == None:
                self.geneTime = multiplier * geneRuntime['fixedValue']

            elif dependecy == 'geneLength':
                self.geneTime = multiplier * self.maxGenomeLen
                math.floor(self.geneTime)
            
            else:
                raise Exception('unknow dependency in \'geneRuntime\' variable')

filePath = 'C:/projects/now/live-sim/src/server/data/presets/.example.json'
config = Configuration.getInstance(filePath)