import math

class Configuration:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Configuration, cls).__new__(cls)

            cls.fieldSize = [32, 32]
            cls.maxAgents = 20

            cls.maxGenomeLen = 5
            cls.mutationChance = 0.1    # a chance of mutation of a new-born cell
            cls.newNeuronChance = 0.3   # a chance in which cell adds new neuron instead of new connection

            cls.geneTimeType = 'fixed'
            cls.geneTimeValue = None

            if cls.geneTimeType == 'fixed':
                cls.geneTime = cls.geneTimeValue
            
            elif cls.geneTimeType == 'length multiplier':
                cls.geneTime = cls.geneTimeValue * cls.maxGenomeLen
                math.floor(cls.geneTime)
        
        return cls._instance

config = Configuration()