class avlNode:
    def __init__(self, lChild=None, rChild=None):
        self.index = None
        self.data = None
        self.lChild = lChild
        self.rChild = rChild

    # Internal functions
    def lTurn(self):
        newRoot = self.rChild

        self.rChild = newRoot.lChild
        newRoot.lChild = self
        self = newRoot

    def rTurn(self):
        midTree = self.lChild.rChild
        
        self.lChild.rChild = self
        self.rChild = midTree

    def lrTurn(self):
        self.lChild.lTurn()
        self.rTurn()

    def rlTurn(self):
        self.rChild.rTurn()
        self.lTurn()
    
    def checkLength(self):
        if self.lChild != None:
            lHeight = self.lChild.checkLength() + 1
        else:
            lHeight = 1

        if self.rChild != None:
            rHeight = self.rChild.checkLength() + 1
        
        if lHeight > rHeight:
            return lHeight
        
        else:
            return rHeight

    # External functions
    def getValue(self, index):
        if index == self.index:
            return self.data
        
        elif index < self.index:
            if self.lChild != None:
                self.lChild.getValue(index)
        
        elif index >= self.index:
            if self.rChild != None:
                self.rChild.getValue(index)

    def setIndex(self, index):
        if index < self.index:
            if self.lChild == None:
                self.lChild = avlNode()
                self.lChild.index = index
            
            else:
                self.lChild.setIndex(index)
        
        if index >= self.index:
            if self.rChild == None:
                self.rChild = avlNode()
                self.rChild.index = index
            
            else:
                self.rChild.setIndex(index)

    def delValue(self, index):
        pass




tree = avlNode()
tree.index = 10

tree.setIndex(15)
tree.setIndex(25)
# tree.setIndex(30)

print([tree.index, tree.rChild.index, tree.rChild.rChild.index])

tree.lTurn()

#print([tree.lChild.index, tree.index, tree.rChild.index])

print(tree.lChild)