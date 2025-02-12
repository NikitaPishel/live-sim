import unittest as ut
import math

import mutation as mtn
import genome as gnm
import neuronCmd as cmds
import genePrcs
import agent
import data_structures as dts

class TestMutation(ut.TestCase):

    def test_fixedGenlength(self):
        for i in range(10):
            genRoot = gnm.GeneRoot()

            genRoot.joints.append(gnm.Sensor())
            genRoot.joints.append(gnm.Sensor())

            arrGenome = gnm.getGenome(genRoot, [])
            noRootGenome = arrGenome.copy()
            noRootGenome.pop(0)

            neurons = mtn._searchNeurons(arrGenome)
            
            mtn._delRndJoint(arrGenome, neurons)
            mtn._addRndJoint(noRootGenome, genRoot)

            arrGenome = gnm.getGenome(genRoot, [])
            noRootGenome = arrGenome.copy()
            noRootGenome.pop(0)

            self.assertIn(len(noRootGenome), [1, 2])
            self.assertNotIn(genRoot, noRootGenome)

    def test_anyGenLength(self):
        for i in range(50):
            genRoot = gnm.GeneRoot()
            genRoot.joints.append(gnm.Sensor())

            for i in range(15):
                noRootGenome = gnm.getGenome(genRoot, [])
                noRootGenome.pop(0)

                mtn._addRndJoint(noRootGenome, genRoot)

            arrGenome = gnm.getGenome(genRoot, [])
            noRootGenome = arrGenome.copy()
            noRootGenome.pop(0)

            self.assertLessEqual(len(noRootGenome), 16)
            self.assertNotIn(genRoot, noRootGenome)

    def test_getGenome(self):
        myGenome = _genGenomeLoop()

        myGenomeArr = gnm.getGenome(myGenome, [])

        self.assertEqual(
        myGenome.joints[0].joints[0].joints[0].joints[0],
        myGenome.joints[0].joints[1]
        )
        self.assertEqual(len(myGenomeArr), 7)

    def test_genePrcsNrnJump(self):
        tOut = []
        
        def snsInp(fieldTree, agent):
            return 0.45

        def sgnOut(fieldTree, agent, amp):
            tOut.append(amp)
        
        tRoot = gnm.GeneRoot()

        tRoot.joints.append(gnm.Sensor())
        tRoot.joints[0].cmd = snsInp

        tRoot.joints[0].joints.append(gnm.Processor())
        tRoot.joints[0].joints[0].cmd = cmds.tanhList

        tRoot.joints[0].joints.append(gnm.Processor())
        tRoot.joints[0].joints[1].cmd = cmds.tanhList

        tRoot.joints[0].joints[0].joints.append(
            tRoot.joints[0].joints[1]
            )

        tRoot.joints[0].joints[1].joints.append(
            gnm.Signal()
            )

        tRoot.joints[0].joints[1].joints[0].cmd = sgnOut

        tAgent = agent.Agent()
        tAgent.gene = tRoot

        genePrcs.runGene(tAgent, None)
        
        dp = 3
        res1 = (math.floor(tOut[0][0]*(10**dp))/(10**dp))
        res2 = (math.floor(tOut[1][0]*(10**dp))/(10**dp))

        self.assertEqual(res1, 0.421)
        self.assertEqual(res2, 0.702)

    def test_PrcsLoop(self):
        pass

    def test_avl_lTurn(self):
        tTree = dts.AvlTree()
        tTree.insert(1)
        tTree.insert(2)
        tTree.insert(3)

        self.assertEqual(tTree.root.key, 2)
        self.assertEqual(tTree.root.lChild.key, 1)
        self.assertEqual(tTree.root.rChild.key, 3)
        '''
        print('\n\n=======')
        print('l turn test')
        print(f' 3\n  \\\n   1\n    \\\n     2')
        print('\n   ↓')
        print(f'\n   {tTree.root.key}\n /   \\\n{tTree.root.lChild.key}     {tTree.root.rChild.key}')
        print("Tree successfully balanced")
        '''
    
    def test_avl_rTurn(self):
        tTree = dts.AvlTree()
        tTree.insert(3)
        tTree.insert(2)
        tTree.insert(1)

        self.assertEqual(tTree.root.key, 2)
        self.assertEqual(tTree.root.lChild.key, 1)
        self.assertEqual(tTree.root.rChild.key, 3)
        '''
        print('\n\n=======')
        print('r turn test')
        print(f'     3\n    /\n   1\n  /\n 2')
        print('\n   ↓')
        print(f'\n   {tTree.root.key}\n /   \\\n{tTree.root.lChild.key}     {tTree.root.rChild.key}')
        print("Tree successfully balanced")
        '''
    
    def test_avl_lrTurn(self):
        tTree = dts.AvlTree()
        tTree.insert(1)
        tTree.insert(3)
        tTree.insert(2)

        self.assertEqual(tTree.root.key, 2)
        self.assertEqual(tTree.root.lChild.key, 1)
        self.assertEqual(tTree.root.rChild.key, 3)
        '''
        print('\n\n=======')
        print('lr turn test')
        print(f'  3\n   \\\n    1\n   /\n  2')
        print('\n   ↓')
        print(f'\n   {tTree.root.key}\n /   \\\n{tTree.root.lChild.key}     {tTree.root.rChild.key}')
        print("Tree successfully balanced")
        '''
    
    def test_avl_rlurn(self):
        tTree = dts.AvlTree()
        tTree.insert(3)
        tTree.insert(1)
        tTree.insert(2)

        self.assertEqual(tTree.root.key, 2)
        self.assertEqual(tTree.root.lChild.key, 1)
        self.assertEqual(tTree.root.rChild.key, 3)
        '''
        print('\n\n=======')
        print('rl turn test')
        print(f'    3\n   /\n  1\n   \\\n    2')
        print('\n   ↓')
        print(f'\n   {tTree.root.key}\n /   \\\n{tTree.root.lChild.key}     {tTree.root.rChild.key}')
        print("Tree successfully balanced")
        '''
    
    def test_avl_delete(self):
        tTree = dts.AvlTree()

        tTree.insert(10)
        tTree.insert(20)
        tTree.insert(30)
        tTree.insert(5)
        tTree.insert(40)
        tTree.insert(35)
        tTree.insert(32)

        self.assertEqual(tTree.root.key, 20)

        tTree.delete(20)

        self.assertEqual(tTree.root.key, 30)
        self.assertEqual(tTree.root.rChild.lChild.key, 32)

    def test_avl_search(self):
        tTree = dts.AvlTree()

        tTree.insert(10)
        tTree.insert(20)
        tTree.insert(30)
        tTree.insert(5)
        tTree.insert(40)
        tTree.insert(35)
        tTree.insert(32)
        tTree.insert(59)

        self.assertEqual(tTree.get(32).key, 32)
        self.assertEqual(tTree.get(5).key, 5)
        self.assertEqual(tTree.get(59).key, 59)
        self.assertRaises(Exception, tTree.get, 100)

    def test_stackInsert(self):
        tStack = dts.Stack()

        tStack.insert(5)

        self.assertEqual(tStack.peek(), 5)

        tStack.insert(3)
        tStack.insert(4)

    def test_stackLength(self):
        tStack = dts.Stack()

        tStack.insert(5)
        tStack.insert(3)
        tStack.insert(4)

        self.assertEqual(tStack.getLength(), 3)

    def test_stackFind(self):
        tStack = dts.Stack()

        tStack.insert(5)
        tStack.insert(3)
        tStack.insert(4)

        self.assertEqual(tStack.find(3), True)
        self.assertEqual(tStack.find(4), True)
        self.assertEqual(tStack.find(5), True)
        self.assertEqual(tStack.find(6), False)

    def test_stackDel(self):
        tStack = dts.Stack()

        tStack.insert(5)
        tStack.insert(3)
        tStack.insert(4)

        self.assertEqual(tStack.peek(), 4)

        tStack.delete()
        self.assertEqual(tStack.peek(), 3)

        tStack.delete()
        self.assertEqual(tStack.peek(), 5)

        tStack.delete()
        self.assertEqual(tStack.peek(), None)
        
        self.assertRaises(Exception, tStack.delete)
    
    def test_cloneGene(self):
        myGenome = _genGenomeLoop()

        geneClone = gnm.cloneGene(myGenome)

        origGene = gnm.getGenome(myGenome)
        newGene = gnm.getGenome(geneClone)

        for i in range(len(origGene)):
            self.assertEqual(type(origGene[i]), type(newGene[i]))


def _genGenomeLoop():
    myGenome = gnm.GeneRoot()

    myGenome.joints.append(gnm.Sensor())
    signal1 = myGenome.joints[0]

    signal1.joints.append(gnm.Processor())
    signal1.joints.append(gnm.Processor())

    signal1.joints[1].joints.append(signal1.joints[0])
    signal1.joints[0].joints.append(gnm.Processor())

    signal1.joints[0].joints[0].joints.append(
            signal1.joints[1]
            )

    myGenome.joints.append(gnm.Sensor())

    signal2 = myGenome.joints[1]

    signal2.joints.append(gnm.Processor())
    
    return myGenome

if __name__ == '__main__':
    ut.main()
