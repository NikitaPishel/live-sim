import threading
from time import time
import sys
from src.server.api import server

sys.path.append('./src/server/model')

import modelExample as model
from configuration import config

#dataFile = input('Enter name of your output file: ')
#dataFile += '.json'
dataFile = 'testlog1.json'

#filePath = input(f'Enter a config path: ')
filePath = './data/presets/config1'
config.loadConfig(f'{filePath}.json')

# Run threads
modelThr = threading.Thread(
    target=model.run,
    args=[dataFile],
    daemon=False
    )

start = time()
modelThr.start()
server.runServer(model.getData)

modelThr.join()

end = time()
print(f'time taken: {(end - start)/60} min')