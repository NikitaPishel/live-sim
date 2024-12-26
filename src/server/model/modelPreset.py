# Preset for custom models

from time import time

from configuration import config

# Simulation execution code
def run():
    dataOut = {}

    for i in range(config.itrNum):
        print(f'running iteration {i+1}/{config.itrNum}')

        dataOut[i+1] = {}

dataFile = input('Enter name of your output file: ')
dataFile += '.json'

start = time()
run(dataFile)
end = time()

print(f'time taken: {(end - start)/60} min')