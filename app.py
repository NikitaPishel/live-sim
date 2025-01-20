import threading
from time import time
import sys
from src.server.api import server

sys.path.append('./src/server/model')

import modelExample as model

#dataFile = input('Enter name of your output file: ')
#dataFile += '.json'
dataFile = 'testlog1.json'

# Run threads

serverThr = threading.Thread(
    target=server.runServer,
    args=[model.getData],
    daemon=False
    )

modelThr = threading.Thread(
    target=model.run,
    args=[dataFile],
    daemon=True
    )

start = time()
serverThr.start()
modelThr.start()

serverThr.join()
modelThr.join()

end = time()
print(f'time taken: {(end - start)/60} min')