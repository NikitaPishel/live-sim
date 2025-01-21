# Example of a working model
from time import sleep
import os

print(os.getcwd())

from configuration import config
import dataOutput as dtOut
from envExample import *

# Data for info output
dataOut = {}

def getData():
    return dataOut

# Simulation execution code
def run(outFile):
    # Env setup
    maxPos = config.fieldSize[0] * config.fieldSize[1]
    itrData = []

    num = 0

    # Training process
    while True:

        #print(f'running iteration {num+1}/{config.itrNum}')
        # Creating new iteration record
        dataOut[num] = {}

        # Loading new iteration
        currEnv = genEnv(itrData, maxPos)
        fieldTree = currEnv['field']
        agentQueue = currEnv['queue']

        # Running an iteration
        itrData = runItr(maxPos, fieldTree, agentQueue)

        # Saving data into current iteration record
        dtOut.saveGenomeMiddle(dataOut, num, itrData)
        dtOut.savePassedNum(dataOut, num, itrData)

        sleep(0.5)

        
        if config.itrNum > 0:
            num += 1

            if num >= config.itrNum:
                break

    # After sim end saving final result
    
    if config.itrNum > 0:
        print(f'Iteration Number: {config.itrNum}')
        dtOut.saveGenome(dataOut, config.itrNum-1, itrData)
        dtOut.saveRunData(dataOut, outFile)