import unittest as ut

import mutation as mtn
import genome as gnm

class TestMutation(ut.TestCase):

    def test_genomelength(self):
        for i in range(10):
            testGenome = gnm.GeneRoot()

            testGenome.joints.append(gnm.Sensor())
            testGenome.joints.append(gnm.Sensor())

            arrGenome = gnm.getGenome(testGenome)
            noRootGenome = arrGenome.copy()
            noRootGenome.pop(0)

            neurons = mtn._searchNeurons(arrGenome)

            mtn._delRndJoint(arrGenome, neurons)
            mtn._addRndJoint(testGenome, noRootGenome)

            arrGenome = gnm.getGenome(testGenome)
            noRootGenome = arrGenome.copy()
            noRootGenome.pop(0)

            self.assertEqual(len(noRootGenome), 2)
            self.assertNotIn(testGenome, noRootGenome)

        for i in range(10):
            testGenome = gnm.GeneRoot()
            testGenome.joints.append(gnm.Sensor())

            for i in range(5):
                noRootGenome = gnm.getGenome(testGenome)
                noRootGenome.pop(0)

                mtn._addRndJoint(testGenome, noRootGenome)

            arrGenome = gnm.getGenome(testGenome)
            noRootGenome = arrGenome.copy()
            noRootGenome.pop(0)

            self.assertLess(len(noRootGenome), 6)
            self.assertNotIn(testGenome, noRootGenome)

if __name__ == '__main__':
    ut.main()