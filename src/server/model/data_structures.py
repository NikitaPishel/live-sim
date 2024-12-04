class _AvlNode:
    def __init__(self):
        self.index = None
        self.data = None
        self.lChild = None
        self.rChild = None
        self.height = 1
        self. balance = 0
    
    def updateHeight(self):
        if self.lChild != None:
            lHeight = self.lChild.updateHeight() + 1
        
        else:
            lHeight = 0

        if self.rChild != None:
            rHeight = self.rChild.updateHeight() + 1
        
        else:
            rHeight = 0
        
        self.height = max(lHeight, rHeight)
        self.balance = lHeight - rHeight

        print(f'index: {self.index}')
        print(f'current heights: {lHeight}, {rHeight}')
        print(f'current balance: {self.balance}')
        print('================')
        self.balanceTree()
        return self.height
    
    def balanceTree(self):
        if self.balance < -1:
            if self.rChild.balance != 1:
                self._lTurn(self)
                self.updateHeight()
            
            else:
                self._lrTurn(self)
                self.updateHeight()

        if self.balance > 1:
            if self.lChild.balance != -1:
                self._rTurn(self)
                self.updateHeight()
            
            else:
                self._rlTurn(self)
                self.updateHeight()
    
    def insertNode(self, index):
        if index < self.index:
            if self.lChild != None:
                self.lChild.insertNode(index)
            
            else:
                self.lChild = _AvlNode()
                self.lChild.index = index
        
        if index > self.index:
            if self.rChild != None:
                self.rChild.insertNode(index)

            else:
                self.rChild = _AvlNode()
                self.rChild.index = index

        else:
            raise Exception(f'Current tree index \'{index}\' already exists')

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
        node.lChild._rTurn()
        node._lTurn()

    def _rlTurn(self, node):
        node.rChild._lTurn()
        node._rTurn()

class AvlTree:
    def __init__(self):
        self.root = None

    # Internal function

    # External functions
    def search(self, index):
        if self.root != None:
            self.root.searchByIndex

        else:
            return None

    def insert(self, index):
        print(f'!!! INSERTING A NODE {index}')
        if self.root != None:
            self.root.insertNode(index)
            self.root.updateHeight()
        
        else:
            self.root = _AvlNode()
            self.root.index = index
    
    def delete(self, index):
        if self.root != None:
            self.root._deleteNode(index)
        
        else:
            raise Exception("Deleting a node from an empty tree")

# Test tree

tTree = AvlTree()
tTree.insert(1)
tTree.insert(2)
tTree.insert(3)

try:
    print(tTree.root.rChild.rChild.index)
    print("Tree haven't balanced")

except:
    print(tTree.root.rChild.index)
    print(tTree.root.lChild.index)
    print("Tree successfully balanced")

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
