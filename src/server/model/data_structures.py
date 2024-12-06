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
        
        elif key > self.key:
            if self.rChild != None:
                self.rChild.insertNode(key)

            else:
                self.rChild = _AvlNode()
                self.rChild.key = key

        elif self.key == key:
            raise Exception(f'Current tree key \'{key}\' already exists')
        
        else:
            raise Exception(f'Unexpected tree key \'{key}\' was used')

    def updateHeight(self):
        if self.lChild != None:
            lHeight = self.lChild.updateHeight()
            self.rChild = _balanceTree(self.rChild)
        
        else:
            lHeight = 0

        if self.rChild != None:
            rHeight = self.rChild.updateHeight()
            self. rChild = _balanceTree(self.rChild)

        else:
            rHeight = 0
        
        self.height = max(lHeight, rHeight) + 1

        return self.height

def getBalance(node):
    if node == None:
        return 0

    else:
        if node != None:
            if node.lChild != None:
                lHeight = node.lChild.height

            else:
                lHeight = 0

            if node.rChild != None:
                rHeight = node.rChild.height
            
            else:
                rHeight = 0
        
        return lHeight - rHeight     

def _balanceTree(node):

        balance = getBalance(node)
        
        if balance < -1:
            rBalance = getBalance(node.rChild)

            if rBalance == 1:
                newTree = _lrTurn(node)
                return newTree
            
            else:
                newTree = _lTurn(node)
                return newTree

        elif balance > 1:
            lBalance = getBalance(node.lChild)

            if lBalance == -1:
                newTree = _rlTurn(node)
                return newTree
            
            else:
                newTree = _rTurn(node)
                return newTree


        else:
            return node

def _lTurn(node):
    newRoot = node.rChild
    midTree = newRoot.lChild
    
    newRoot.lChild = node
    node.rChild = midTree

    return newRoot

def _rTurn(node):
    newRoot = node.lChild
    midTree = newRoot.rChild

    node.lChild = midTree
    newRoot.rChild = node

    return newRoot

def _lrTurn(node):
    node.rChild = _rTurn(node.rChild)
    newTree = _lTurn(node)

    return newTree

def _rlTurn(node):
    node.lChild = _lTurn(node.lChild)
    newTree = _rTurn(node)
    return newTree

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
        if self.root != None:
            self.root.insertNode(key)
            self.root.updateHeight()
            self.root = _balanceTree(self.root)
        
        else:
            self.root = _AvlNode()
            self.root.key = key

    def delete(self, key):
        if self.root != None:
            self.root._deleteNode(key)
        
        else:
            raise Exception("Deleting a node from an empty tree")

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
