import unittest as ut

import mutation as mtn
import genome as gnm

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
if __name__ == '__main__':
    ut.main()

'''
# SHOULD BE REBUILT INTO UNIT TESTs

# GET GENOME TEST

myGenome = GeneRoot()

myGenome.joints.append(
    Sensor()
)

signal1 = myGenome.joints[0]

signal1.joints.append(
    Processor()
)
signal1.joints.append(
    Processor()
)

signal1.joints[1].joints.append(
    signal1.joints[0]
)

signal1.joints[0].joints.append(
    Processor()
)

signal1.joints[0].joints[0].joints.append(
 signal1.joints[1]   
)

myGenome.joints.append(
    Sensor()
)

signal2 = myGenome.joints[1]

signal2.joints.append(
    Processor()
)

myGenomeArr = getGenome(myGenome)
print(myGenomeArr)

print(
    signal1.joints[0].joints[0].joints[0] == signal1.joints[1]
)

print(len(myGenomeArr))
'''