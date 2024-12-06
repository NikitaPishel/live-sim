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
        myGenomeArr = gnm.getGenome(myGenome)

        self.assertEqual(
        signal1.joints[0].joints[0].joints[0],
        signal1.joints[1]
        )
        self.assertEqual(len(myGenomeArr), 7)

    def test_genePrcsNrnJump(self):
        tOut = []
        
        def snsInp(agent):
            return 0.45

        def sgnOut(agent, amp):
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

        genePrcs.runGene(tAgent)
        
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

if __name__ == '__main__':
    ut.main()
