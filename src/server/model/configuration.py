import math
import json
import os

os.chdir('./src/server/data/presets')

class Configuration:
    _instance = None

    def __new__(cls, filename):
        if cls._instance is None:

            cls._instance = super(Configuration, cls).__new__(cls)
        
            # Load standart settings
            cls.loadConfig('standart.json')

            # Load non-standart settings
            cls.loadConfig(filename)
        
            # exceptional settings
            if cls.maxActions < 1:
                raise Exception('configErr, maxActions below 1')
            
            if cls.geneTime < 1:
                raise Exception('configErr, maxActions below 1')

        return cls._instance

    @classmethod
    def getInstance(cls, filename):
        if Configuration._instance == None:
            Configuration(filename)
        return cls._instance

    @classmethod
    def loadConfig(cls, filename):
        with open(filename, 'r') as file:
            settings = json.load(file)

        if settings['field size'] != None:
            cls.fieldSize = settings['field size']

        if settings['max amount of agents'] != None:
            cls.maxAgents = settings['max amount of agents']
        
        if settings['max genome length'] != None:
            cls.maxGenomeLen = settings['max genome length']

        if settings['mutation chance'] != None:
            cls.mutationChance = settings['mutation chance']

        if settings['new neuron chance'] != None:
            cls.newNeuronChance = settings['new neuron chance']

        if settings['max actions'] != None:
            cls.maxActions = settings['max actions']

        geneRuntime = settings['gene runtime']
        if geneRuntime != None:
            multiplier = geneRuntime['multiplier']
            dependecy = geneRuntime['dependency']

            if dependecy == None:
                cls.geneTime = multiplier * geneRuntime['fixed value']

            elif dependecy == 'gene length':
                cls.geneTime = multiplier * cls.maxGenomeLen
                math.floor(cls.geneTime)
            
            else:
                raise Exception('unknow dependency in \'geneRuntime\' variable')

config = Configuration.getInstance('.example.json')