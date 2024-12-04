class _AvlNode:
    def __init__(self, lChild=None, rChild=None):
        self.index = None
        self.data = None
        self.lChild = lChild
        self.rChild = rChild
        self.height = 1
    
    def insertNode(self, index):
        if index < self.index:
            if self.lChild == None:
                self.lChild = _AvlNode()
                self.lChild.index = index
            
            else:
                self.lChild.insertNode(index)
        
        if index >= self.index:
            if self.rChild == None:
                self.rChild = _AvlNode()
                self.rChild.index = index
            
            else:
                self.rChild.insertNode(index)

    def delValue(self, index):
        pass

class AvlTree:
    def __init__(self):
        self.root = None

    # Internal functions
    def _lTurn(self, node):
        midNode = node.rChild
        
        node.rChild = midNode.lChild
        midNode.lChild = node
        node = midNode

    def _rTurn(self, node):
        midNode = node.lChild
        
        node.lChild = midNode.rChild
        midNode.rChild = node
        node = midNode

    def _lrTurn(self, node):
        node.lChild.lTurn()
        node.rTurn()

    def _rlTurn(self, node):
        node.rChild.rTurn()
        node.lTurn()
    
    def _checkLength(self):
        if self.lChild != None:
            lHeight = self.lChild._checkLength() + 1

        else:
            lHeight = 1

        if self.rChild != None:
            rHeight = self.rChild._checkLength() + 1
        
        else:
            rHeight = 1

            return max(lHeight, rHeight)

    # External functions
    def searchData(self, index):
        if self.index == self.index:
            return self.data
        
        elif index < self.index:
            if self.lChild != None:
                self.lChild.searchData(index)
        
        elif index >= self.index:
            if self.rChild != None:
                self.rChild.searchData(index)
    
    def insert(self, index):
        if self.root != None:
            self.root.insertNode(index)
        
        else:
            self.root = _AvlNode()
            self.root.index = index

# Test tree

tTree = AvlTree()
tTree.insert(1)
tTree.insert(2)
tTree.insert(3)

print(tTree.root.rChild.rChild.index)

# ================================================================

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
        if self.front == None:
            return None
        
        else:
            return self.front.data

    def getLength(self):
        if self.front != None:
            return self.front.itrLength(0)
        
        else:
            return 0
