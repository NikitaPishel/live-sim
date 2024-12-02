import math
import json

class Configuration:
    _instance = None

    def __init__(self, filename):
        Configuration._instance = self

        # Load standart settings
        self.loadConfig('./src/server/data/presets/standart.json')

        # Load non-standart settings
        self.loadConfig(filename)
    
        # exceptional settings
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

        if settings['field size'] != None:
            self.fieldSize = settings['field size']

        if settings['max amount of agents'] != None:
            self.maxAgents = settings['max amount of agents']
        
        if settings['max genome length'] != None:
            self.maxGenomeLen = settings['max genome length']

        if settings['mutation chance'] != None:
            self.mutationChance = settings['mutation chance']

        if settings['new neuron chance'] != None:
            self.newNeuronChance = settings['new neuron chance']

        if settings['max actions'] != None:
            self.maxActions = settings['max actions']

        geneRuntime = settings['gene runtime']
        if geneRuntime != None:
            multiplier = geneRuntime['multiplier']
            dependecy = geneRuntime['dependency']

            if dependecy == None:
                self.geneTime = multiplier * geneRuntime['fixed value']

            elif dependecy == 'gene length':
                self.geneTime = multiplier * self.maxGenomeLen
                math.floor(self.geneTime)
            
            else:
                raise Exception('unknow dependency in \'geneRuntime\' variable')

filePath = './src/server/data/presets/.example.json'
config = Configuration.getInstance(filePath)