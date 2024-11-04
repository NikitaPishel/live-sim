class AvlNode:
    def __init__(self, lChild=None, rChild=None):
        self.index = None
        self.data = None
        self.lChild = lChild
        self.rChild = rChild

    # Internal functions
    def lTurn(node):
        newRoot = node.rChild

        node.rChild = newRoot.lChild
        newRoot.lChild = node
        node = newRoot

    def rTurn(node):
        midTree = node.lChild.rChild
        
        node.lChild.rChild = node
        node.rChild = midTree

    def lrTurn(node):
        node.lChild.lTurn()
        node.rTurn()

    def rlTurn(node):
        node.rChild.rTurn()
        node.lTurn()
    
    def checkLength(self):
        if self.lChild != None:
            lHeight = self.lChild.checkLength() + 1

        else:
            lHeight = 1

        if self.rChild != None:
            rHeight = self.rChild.checkLength() + 1

            return max(rHeight)

    # External functions
    def searchData(self, index):
        if index == self.index:
            return self.data
        
        elif index < self.index:
            if self.lChild != None:
                self.lChild.searchData(index)
        
        elif index >= self.index:
            if self.rChild != None:
                self.rChild.searchData(index)

    def setIndex(self, index):
        if index < self.index:
            if self.lChild == None:
                self.lChild = AvlNode()
                self.lChild.index = index
            
            else:
                self.lChild.setIndex(index)
        
        if index >= self.index:
            if self.rChild == None:
                self.rChild = AvlNode()
                self.rChild.index = index
            
            else:
                self.rChild.setIndex(index)

    def delValue(self, index):
        pass

class QueueNode:

    def __init__(self, data=None, child=None):
        self.data = data
        self.child = child

    def searchData(self, data) -> bool:
        if self == data:
            return True
        
        elif self.child == None:
                return None
            
        else:
            self.child.searchData(data)
    
    def itrLength(self, qLength) -> int:
        qLength += 1

        if self.child != None:
            return self.child.itrLength(qLength)
        
        elif self.child == None:
            return qLength

class Queue:
    def __init__(self):
        self.rear = None
        self.front = None
    
    def enqueue(self, data):
        newNode = QueueNode(data)

        if self.rear == None:
            self.front = newNode
            self.rear = newNode
        
        else:
            self.rear.child = newNode
            self.rear = newNode
        
        
    def dequeue(self):
        if self.front == self.rear:
            self.front = None
            self.rear = None

        elif self.front != None:
            self.front = self.front.child

        else:
            raise Exception('Calling \'deque\' command in an empty Queue')
    
    def peek(self):
        return self.front.data

    def getLength(self):
        if self.front != None:
            return self.front.itrLength(0)
        
        else:
            return 0