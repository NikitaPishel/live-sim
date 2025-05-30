import math
import json
import sys

class Configuration:
    _instance = None

    def __init__(self):
        Configuration._instance = self

        # Changing recursion limit
        sys.setrecursionlimit(2500)

        # Load standard settings
        self.loadConfig(f'./data/presets/standard.json')

    @classmethod
    def getInstance(cls):
        if Configuration._instance == None:
            Configuration()
        return cls._instance

    # This method loads different parameters from the configurational JSON file.
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
        
        if settings['leveledMutation'] != None:
            self.lvldMutation = settings['leveledMutation']

        # Amount of mutations that are created on the start of a simulation
        if settings['startMutation'] != None:
            self.startMutation = settings['startMutation']

        if settings['maxActions'] != None:
            self.maxActions = settings['maxActions']

        geneRuntime = settings['geneRuntime']

        if geneRuntime != None:
            if geneRuntime['multiplier'] != None:
                self._multiplier = geneRuntime['multiplier']
            
            if geneRuntime['dependency'] != None:
                self.dependency = geneRuntime['dependency']

            if self.dependency == 'fixed':

                if geneRuntime['fixedValue'] != None:
                    self._fixedGeneValue = geneRuntime['fixedValue']

                self.geneTime = self._multiplier * self._fixedGeneValue

            elif self.dependency == 'geneLength':
                self.geneTime = self._multiplier * self.maxGenomeLen
                math.floor(self.geneTime)
            
            else:
                raise Exception('unknow dependency in \'geneRuntime\' variable')
        
        trigParams = settings['triggerConditions']

        if settings['newGenTrigger'] == 'timer':
            self.trigger = 'timer'
            
            if trigParams['timeLimit'] != None:
                self.timeLim = trigParams['timeLimit']
        
        elif settings['newGenTrigger'] == 'minAgents':
            self.trigger = 'minAgents'

            if self.agentsLim != None:
                self.agentsLim = trigParams['minAmountOfAgents']
        
        if settings['numberOfIterations'] != None:
            self.itrNum = settings['numberOfIterations']
        
        if settings['savingLevels'] != None:

            svLvls = settings['savingLevels']

            if svLvls['passedNumber'] != None:
                self.savePassedNumber = svLvls['passedNumber']
            
            if svLvls['passedGenomes'] != None:
                self.savePassedGenomes = svLvls['passedGenomes']
            
            if svLvls['iteration'] != None:
                self.saveIteration = svLvls['iteration']
        
        if settings['outputPath'] != None:
            self.outputPath = settings['outputPath']

        # exceptions
        if self.maxActions < 1:
            raise Exception('configErr, maxActions below 1')
        
        if self.geneTime < 1:
            raise Exception('configErr, maxActions below 1')

            

config = Configuration.getInstance()