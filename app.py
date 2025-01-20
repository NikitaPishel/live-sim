import threading
from time import time
import sys
from src.server.api.server import app

sys.path.append('./src/server/model')

import modelExample as model

#dataFile = input('Enter name of your output file: ')
#dataFile += '.json'
dataFile = 'testlog1.json'

# Run threads

serverThr = threading.Thread(
    target=app.run,
    )

modelThr = threading.Thread(
    target=model.run,
    args=(dataFile)
    )

start = time()
serverThr.run()
modelThr.run()
end = time()

print(f'time taken: {(end - start)/60} min')