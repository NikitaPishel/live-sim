# Example of a working model
from time import time

from configuration import config
import dataOutput as dtOut
from envExample import *

# Simulation execution code
def run(outFile):

    # Data for info output
    dataOut = {}

    # Env setup
    maxPos = config.fieldSize[0] * config.fieldSize[1]
    itrData = []

    # Training process
    for i in range(config.itrNum):
        print(f'running iteration {i+1}/{config.itrNum}')
        # Creating new iteration record
        dataOut[i+1] = {}

        # Loading new iteration
        currEnv = genEnv(itrData, maxPos)
        fieldTree = currEnv['field']
        agentQueue = currEnv['queue']

        # Running an iteration
        itrData = runItr(maxPos, fieldTree, agentQueue)

        # Saving data into current iteration record
        dtOut.saveGenome(dataOut, i+1, itrData)
        dtOut.savePassedNum(dataOut, i+1, itrData)

    # After sim end saving final result
    dataOut[config.itrNum] = {}
    dtOut.saveGenome(dataOut, config.itrNum, itrData)
    dtOut.saveRunData(dataOut, outFile)

# User input
dataFile = input('Enter name of your output file: ')
dataFile += '.json'

# Run training
start = time()
run(dataFile)
end = time()

print(f'time taken: {(end - start)/60} min')

# C:/projects/now/live-sim/src/server/data/presets/config1