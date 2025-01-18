from time import time
import sys

sys.path.append('./src/server/model')

import modelExample as model

dataFile = input('Enter name of your output file: ')
dataFile += '.json'

# Run training
start = time()
model.run(dataFile)
end = time()

print(f'time taken: {(end - start)/60} min')