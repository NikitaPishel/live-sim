import unittest as ut

import mutation as mtn
import genome as gnm
import neuronCmd as cmds
import genePrcs
import agent

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
        for i in range(10):
            genRoot = gnm.GeneRoot()
            genRoot.joints.append(gnm.Sensor())

            for i in range(15):
                noRootGenome = gnm.getGenome(genRoot, [])
                noRootGenome.pop(0)

                mtn._addRndJoint(noRootGenome, genRoot)

            arrGenome = gnm.getGenome(genRoot, [])
            noRootGenome = arrGenome.copy()
            noRootGenome.pop(0)

            self.assertLessEqual(len(noRootGenome), 11)
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

        self.assertEqual(tOut[0], [0.42189900525000795])
        self.assertEqual(tOut[1], [0.7023376822305316])
if __name__ == '__main__':
    ut.main()
