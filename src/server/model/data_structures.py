class _AvlNode:
    def __init__(self):
        self.key = None
        self.data = None
        self.lChild = None
        self.rChild = None
        self.height = 1
        self.balance = 0
    
    def insertNode(self, key):
        if key < self.key:
            if self.lChild != None:
                self.lChild.insertNode(key)
            
            else:
                self.lChild = _AvlNode()
                self.lChild.key = key
        
        if key > self.key:
            if self.rChild != None:
                self.rChild.insertNode(key)

            else:
                self.rChild = _AvlNode()
                self.rChild.key = key

        else:
            raise Exception(f'Current tree key \'{key}\' already exists')

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

        print(f'key: {self.key}')
        print(f'current heights: {lHeight}, {rHeight}')
        print(f'current balance: {self.balance}')
        print('================')
        balanceTree(self)
        return self.height

def balanceTree(node):
    if node.balance < -1:
        node = _lTurn(node)
        print(f'\nreassigned:\n- node: {node.key}\n- left: {node.lChild.key}\n- right: {node.rChild.key}\n')
        
    elif node.balance > 1:
        node = _rTurn(node)

    else:
        return node

def _lTurn(node):
    print('\nlTurning...\n')
    newRoot = node.rChild
    midTree = newRoot.lChild
    
    newRoot.lChild = node
    node.rChild = midTree

    print(f'New tree:\n- root: {newRoot.key}\n- left: {newRoot.lChild.key}\n- right: {newRoot.rChild.key}\n')
    return newRoot

def _rTurn(node):
    print('\nrTurning...\n')
    newRoot = node.lChild
    midTree = newRoot.rChild

    node.lChild = midTree
    newRoot.rChild = node
    node = newRoot
    return newRoot

def _lrTurn(node):
    node.lChild._rTurn()
    node._lTurn()

def _rlTurn(node):
        node.rChild._lTurn()
        node._rTurn()

class AvlTree:
    def __init__(self):
        self.root = None

    # Internal function

    # External functions
    def search(self, key):
        if self.root != None:
            self.root.searchByIndex

        else:
            return None

    def insert(self, key):
        print(f'!!! INSERTING A NODE {key}')
        if self.root != None:
            self.root.insertNode(key)
            self.root.updateHeight()
        
        else:
            self.root = _AvlNode()
            self.root.key = key
            self.root.isRoot = True

    def delete(self, key):
        if self.root != None:
            self.root._deleteNode(key)
        
        else:
            raise Exception("Deleting a node from an empty tree")

# Test tree

tTree = AvlTree()
tTree.insert(1)
tTree.insert(2)
tTree.insert(3)

try:
    print(tTree.root.rChild.rChild.key)
    print("Tree haven't balanced")

except:
    print(tTree.root.key)
    print(tTree.root.lChild)
    print(tTree.root.rChild)
    #print(tTree.root.lChild.key)
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
