class QueueNode:

    def __init__(self, data=None, child=None):
        self.data = data
        self.child = child
    
    def getData(self, data):
        if self.data == data:
            return data
    
    def enqueue(self, data):
       newQueue = QueueNode(data, self)
       self = newQueue
        
    def dequeue(self, data):
        if self.child == None:
            self.child = data
        
        else:
            deque(self.child)

queue = QueueNode(5)

queue.enqueue(8)

print(queue.data)