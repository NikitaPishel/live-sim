class _AvlNode:
    def __init__(self):
        self.key = None
        self.data = None
        self.lChild = None
        self.rChild = None
        self.height = 1
        self.balance = 0
    
    def _searchNode(self, key):
        if key > self.key:
            if self.rChild != None:
                return self.rChild._searchNode(key)

            else:
                raise Exception(f'Trying to search for unexisting tree key \'{key}\'')    

        elif key < self.key:
            if self.lChild != None:
                return self.lChild._searchNode(key)
            
            else:
                raise Exception(f'Trying to search for unexisting tree key \'{key}\'')
        
        elif self.key == key:
            return self

    def inTree(self, key):
        if key > self.key:
            if self.rChild != None:
                return self.rChild.inTree(key)

            else:
                return False    

        elif key < self.key:
            if self.lChild != None:
                return self.lChild.inTree(key)
            
            else:
                return False

        elif self.key == key:
            return True

    def insertNode(self, key, data):
        if key < self.key:
            if self.lChild != None:
                self.lChild.insertNode(key, data)
            
            else:
                self.lChild = _AvlNode()
                self.lChild.key = key
                self.lChild.data = data
        
        elif key > self.key:
            if self.rChild != None:
                self.rChild.insertNode(key, data)

            else:
                self.rChild = _AvlNode()
                self.rChild.key = key
                self.rChild.data = data

        elif self.key == key:
            raise Exception(f'Current tree key \'{key}\' already exists')
        
        else:
            raise Exception(f'Unexpected tree key \'{key}\' was used')
    
    def deleteNode(self):
        if self.lChild != None and self.rChild != None:
            newNode = self.rChild.lowest()

            newSubtree = deleteTree(self.rChild, newNode.key)
            self.rChild = newSubtree

            newNode.lChild = self.lChild
            newNode.rChild = self.rChild

        elif self.lChild != None:
            newNode = self.lChild

        elif self.rChild != None:
            newNode = self.rChild
        
        else:
            return None
        
        return newNode

    def findSuccessorParent(self, tree):
        if tree.lChild.key == self.key:
            return tree.rChild

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

    def lowest(self):
        if self.lChild != None:
            scrNode = self.lChild.lowest()
            
            return scrNode
            
        else:
            return self

def deleteTree(node, key):
    if node != None:
        if key < node.key:
            newSub = deleteTree(node.lChild, key)
            node.lChild = newSub
            
            return node
        
        elif key > node.key:
            newSub = deleteTree(node.rChild, key)
            node.rChild = newSub
            
            return node

        elif node.key == key:
            newRoot = node.deleteNode()

            return newRoot
        
    else:
        raise Exception('Trying to delete unexisting tree key \'{key}\'')

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
    def get(self, key):
        if self.root != None:
            return self.root._searchNode(key)

        else:
            raise Exception(f'Trying to search for unexisting tree key \'{key}\'')
        
    def setData(self, key, data):
        if self.root != None:
            node = self.root._searchNode(key)

            node.data = data

        else:
            raise Exception(f'Trying to search for unexisting tree key \'{key}\'')

    def insert(self, key, data=None):
        if self.root != None:
            self.root.insertNode(key, data)
            self.root.updateHeight()
            self.root = _balanceTree(self.root)
        
        else:
            self.root = _AvlNode()
            self.root.key = key
            self.root.data = data

    def delete(self, key):
        if self.root != None:
            self.root = deleteTree(self.root, key)

            if self.root != None:
                self.root.updateHeight()
                self.root = _balanceTree(self.root)

        else:
            raise Exception("Deleting a node from an empty tree")
    
    def exists(self, key):
        if self.root != None:
            keyExists = self.root.inTree(key)
            return keyExists

        else:
            return False

# ================================================================
#   Queue

class _QueueNode:

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
        newNode = _QueueNode(data)

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

# ================================================================
#   Stack

class _StackNode:
    def __init__(self):
        self.data = None
        self.child = None

    def itrLength(self, currLength):
        if self.child != None:
            return self.child.itrLength(currLength + 1)
        
        else:
            return currLength + 1

    def itrFind(self, data):

        if self.data == data:
            return True
        
        elif self.child != None:
            return self.child.itrFind(data)
        
        else:
            return False

class Stack:
    def __init__(self):
        self.front = None
    
    def isOccupied(self):
        if self.front == None:
            return False
        
        else:
            return True
    
    def peek(self):
        if self.isOccupied():
            return self.front.data
        
        else:
            return None
    
    def insert(self, data):
        oldFront = self.front
        newFront = _StackNode()

        newFront.data = data
        newFront.child = self.front
        self.front = newFront
    
    def getLength(self):
        if self.isOccupied():
            return self.front.itrLength(0)
    
    def find(self, data):
        if self.isOccupied():
            return self.front.itrFind(data)
    
    def delete(self):
        if self.isOccupied():
            self.front = self.front.child
        
        else:
            raise Exception ('deleting an element from an empty stack')