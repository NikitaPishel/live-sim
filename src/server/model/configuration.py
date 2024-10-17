class Configuration:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Configuration, cls).__new__(cls)

            cls.fieldSize = [32, 32]
            cls.amountOfCells = 20
            cls.mutationChance = 0.1
        
        return cls._instance