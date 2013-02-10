"""
Unit test for stats routines
(c) 2013 Alan James Salmoni

"""

import unittest, numpy
from Data import *
from AllRoutines import *

"""
Vsort
Msort
CalculateRanks
GetSSCP_M
GetVarsCovars_M
GetVariances
getStdDevs
GetCorelationMatrix
MidRange
Proportions
Percentages
"""

class univariateTest(unittest.TestCase):
    def testCount(self):
        self.assertEqual(Count(intvector),8)
        self.assertEqual(Count(intmatrix),24)
        self.assertEqual(Count(fltvector),8)
        self.assertEqual(Count(fltmisvec),6)
        self.assertEqual(Count(fltmismat),19)

    def testSum(self):
        self.assertAlmostEqual(Sum(intvector),73, places=0)
        self.assertAlmostEqual(Sum(intmatrix),237, places=0)
        self.assertAlmostEqual(Sum(fltvector),72.281, places=3)
        self.assertAlmostEqual(Sum(fltmisvec),67.574, places=3)
        self.assertAlmostEqual(Sum(fltmismat),211.45, places=3)

    def testMinimum(self):
        self.assertAlmostEqual(Minimum(intvector),0, places=0)
        self.assertAlmostEqual(Minimum(intmatrix),0, places=0)
        self.assertAlmostEqual(Minimum(fltvector),0.46, places=2)
        self.assertAlmostEqual(Minimum(fltmisvec),0.46, places=2)
        self.assertAlmostEqual(Minimum(fltmismat),0.37, places=2)

    def testMaximum(self):
        self.assertAlmostEqual(Maximum(intvector),19, places=0)
        self.assertAlmostEqual(Maximum(intmatrix),19, places=0)
        self.assertAlmostEqual(Maximum(fltvector),19.021, places=2)
        self.assertAlmostEqual(Maximum(fltmisvec),19.021, places=3)
        self.assertAlmostEqual(Maximum(fltmismat),19.28, places=2)

    def testRange(self):
        self.assertAlmostEqual(Range(intvector),19, places=0)
        self.assertAlmostEqual(Range(fltvector),18.561, places=3)
        self.assertAlmostEqual(Range(intmisvec),19, places=0)
        self.assertAlmostEqual(Range(fltmisvec),18.561, places=3)

    def testMidRange(self):
        self.assertAlmostEqual(Midrange(longvec),5.0965, places=4)

    def testFrequencies(self):
        vals, freqs = Frequencies(uniques)
        self.assertListEqual(vals.tolist(), [1, 2, 3, 4])
        self.assertListEqual(freqs.round(4).tolist(), [2,7,5,2])
        vals, freqs = Frequencies(uniqmis)
        self.assertListEqual(vals.tolist(), [1, 2, 3, 4])
        self.assertListEqual(freqs.round(8).tolist(), [2,7,3,1])

    def testProportions(self):
        vals, props = Proportions(uniques)
        self.assertListEqual(vals.tolist(), [1, 2, 3, 4])
        self.assertListEqual(props.round(4).tolist(), [0.125, 0.4375, 0.3125, 0.125])
        vals, props = Proportions(uniqmis)
        self.assertListEqual(vals.tolist(), [1, 2, 3, 4])
        self.assertListEqual(props.round(8).tolist(), [0.15384615, 0.53846154, 0.23076923, 0.07692308])

    def testPercentages(self):
        vals, percs = Percentages(uniques)
        self.assertListEqual(vals.tolist(), [1, 2, 3, 4])
        self.assertListEqual(percs.round(2).tolist(), [12.5, 43.75, 31.25, 12.5])
        vals, percs = Percentages(uniqmis)
        self.assertListEqual(vals.tolist(), [1, 2, 3, 4])
        self.assertListEqual(percs.round(6).tolist(), [15.384615, 53.846154, 23.076923, 7.692308])

    def testMean(self):
        self.assertAlmostEqual(Mean(intvector),9.125, places=3)
        self.assertAlmostEqual(Mean(intmatrix),9.875, places=3)
        self.assertAlmostEqual(Mean(fltvector),9.035125, places=6)
        self.assertAlmostEqual(Mean(fltmisvec),11.26233, places=5)
        self.assertAlmostEqual(Mean(fltmismat),11.12895, places=5)

    def testSampVar(self):
        self.assertAlmostEqual(SampVar(intvector),67.55357, places=5)
        #self.assertAlmostEqual(SampVar(intmatrix),, places=6)
        self.assertAlmostEqual(SampVar(fltvector),66.6899, places=4)
        self.assertAlmostEqual(SampVar(fltmisvec),69.4777, places=4)
        #self.assertAlmostEqual(SampVar(fltmismat),0.37, places=2)

    def testPopVar(self):
        self.assertAlmostEqual(PopVar(intvector),59.10938, places=4)
        #self.assertAlmostEqual(PopVar(intmatrix),, places=)
        self.assertAlmostEqual(PopVar(fltvector),58.35366, places=4)
        self.assertAlmostEqual(PopVar(fltmisvec),57.89808, places=4)
        #self.assertAlmostEqual(SampVar(fltmismat),0.37, places=2)

    def testSampStdDev(self):
        self.assertAlmostEqual(SampStdDev(intvector),8.219098, places=6)
        self.assertAlmostEqual(SampStdDev(intmisvec),8.430105, places=6)
        self.assertAlmostEqual(SampStdDev(fltvector),8.166389, places=6)
        self.assertAlmostEqual(SampStdDev(fltmisvec),8.335328, places=6)
        #self.assertAlmostEqual(SampVar(fltmismat),0.37, places=2)

    def testPopStdDev(self):
        self.assertAlmostEqual(PopStdDev(intvector),7.688262, places=6)
        self.assertAlmostEqual(PopStdDev(intmisvec),7.695598, places=6)
        self.assertAlmostEqual(PopStdDev(fltvector),7.638957, places=6)
        self.assertAlmostEqual(PopStdDev(fltmisvec),7.609079, places=6)
        #self.assertAlmostEqual(SampVar(fltmismat),0.37, places=2)

    def testStdErr(self):
        self.assertAlmostEqual(StdErr(fltvector),2.887254, places=6)
        self.assertAlmostEqual(StdErr(fltmisvec),3.402884, places=6)

    def testQ1(self):
        self.assertAlmostEqual(Q1(longvec, 0.25), 2.889, places=3)
        self.assertAlmostEqual(Q1(longvec, 0.75), 6.814, places=3)

    def testQ2(self):
        self.assertAlmostEqual(Q2(longvec, 0.25), 3.1175, places=4)
        self.assertAlmostEqual(Q2(longvec, 0.75), 7.39, places=2)
 
    def testQ3(self):
        self.assertAlmostEqual(Q3(longvec, 0.25), 2.889, places=3)
        self.assertAlmostEqual(Q3(longvec, 0.75), 6.814, places=3)
 
    def testQ4(self):
        self.assertAlmostEqual(Q4(longvec, 0.25), 2.889, places=3)
        self.assertAlmostEqual(Q4(longvec, 0.75), 6.814, places=3)
 
    def testQ5(self):
        self.assertAlmostEqual(Q5(longvec, 0.25), 3.1175, places=4)
        self.assertAlmostEqual(Q5(longvec, 0.75), 7.39, places=2)
 
    def testQ6(self):
        self.assertAlmostEqual(Q6(longvec, 0.25), 3.00325, places=5)
        self.assertAlmostEqual(Q6(longvec, 0.75), 7.678, places=3)
 
    def testQ7(self):
        self.assertAlmostEqual(Q7(longvec, 0.25), 3.23175, places=5)
        self.assertAlmostEqual(Q7(longvec, 0.75), 7.102, places=3)
 
    def testQ8(self):
        self.assertAlmostEqual(Q8(longvec, 0.25), 3.079417, places=6)
        self.assertAlmostEqual(Q8(longvec, 0.75), 7.486, places=3)
 
    def testQ9(self):
        self.assertAlmostEqual(Q9(longvec, 0.25), 3.088938, places=5)
        self.assertAlmostEqual(Q9(longvec, 0.75), 7.462, places=3)


if __name__ == '__main__':
    unittest.main()

