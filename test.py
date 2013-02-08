"""
Unit test for stats routines
(c) 2013 Alan James Salmoni

"""

import unittest
from Data import *
from AllRoutines import *

class univariateTest(unittest.TestCase):
    def testSum(self):
        self.failUnlessAlmostEqual(Sum(intvector),73, places=0)
        self.failUnlessAlmostEqual(Sum(intmatrix),237, places=0)
        self.failUnlessAlmostEqual(Sum(fltvector),72.281, places=3)
        self.failUnlessAlmostEqual(Sum(fltmisvec),67.574, places=3)
        self.failUnlessAlmostEqual(Sum(fltmismat),211.45, places=3)

    def testCount(self):
        self.failUnlessEqual(Count(intvector),8)
        self.failUnlessEqual(Count(intmatrix),24)
        self.failUnlessEqual(Count(fltvector),8)
        self.failUnlessEqual(Count(fltmisvec),6)
        self.failUnlessEqual(Count(fltmismat),19)

    def testMean(self):
        self.failUnlessAlmostEqual(Mean(intvector),9.125, places=3)
        self.failUnlessAlmostEqual(Mean(intmatrix),9.875, places=3)
        self.failUnlessAlmostEqual(Mean(fltvector),9.035125, places=6)
        self.failUnlessAlmostEqual(Mean(fltmisvec),11.26233, places=5)
        self.failUnlessAlmostEqual(Mean(fltmismat),11.12895, places=5)

    def testMinimum(self):
        self.failUnlessAlmostEqual(Minimum(intvector),0, places=0)
        self.failUnlessAlmostEqual(Minimum(intmatrix),0, places=0)
        self.failUnlessAlmostEqual(Minimum(fltvector),0.37, places=2)
        self.failUnlessAlmostEqual(Minimum(fltmisvec),0.46, places=2)
        self.failUnlessAlmostEqual(Minimum(fltmismat),0.37, places=2)

    def testMaximum(self):
        self.failUnlessAlmostEqual(Maximum(intvector),19, places=0)
        self.failUnlessAlmostEqual(Maximum(intmatrix),19, places=0)
        self.failUnlessAlmostEqual(Maximum(fltvector),19.28, places=2)
        self.failUnlessAlmostEqual(Maximum(fltmisvec),19.021, places=3)
        self.failUnlessAlmostEqual(Maximum(fltmismat),19.28, places=2)

    def testSampVar(self):
        self.failUnlessAlmostEqual(SampVar(intvector),67.55357, places=5)
        #self.failUnlessAlmostEqual(SampVar(intmatrix),, places=6)
        self.failUnlessAlmostEqual(SampVar(fltvector),66.6899, places=4)
        self.failUnlessAlmostEqual(SampVar(fltmisvec),69.4777, places=4)
        #self.failUnlessAlmostEqual(SampVar(fltmismat),0.37, places=2)

    def testPopVar(self):
        self.failUnlessAlmostEqual(PopVar(intvector),59.10938, places=4)
        #self.failUnlessAlmostEqual(PopVar(intmatrix),, places=)
        self.failUnlessAlmostEqual(PopVar(fltvector),58.53366, places=4)
        self.failUnlessAlmostEqual(PopVar(fltmisvec),60.79299, places=4)
        #self.failUnlessAlmostEqual(SampVar(fltmismat),0.37, places=2)

    def testSampStdDev(self):
        self.failUnlessAlmostEqual(SampVar(intvector),8.219098, places=6)
        self.failUnlessAlmostEqual(SampVar(intmisvec),8.430105, places=6)
        self.failUnlessAlmostEqual(SampVar(fltvector),8.166389, places=6)
        self.failUnlessAlmostEqual(SampVar(fltmisvec),8.335328, places=6)
        #self.failUnlessAlmostEqual(SampVar(fltmismat),0.37, places=2)

    def testPopStdDev(self):
        self.failUnlessAlmostEqual(PopStdDev(intvector),7.191711, places=6)
        self.failUnlessAlmostEqual(PopStdDev(intmatrix),7.376342, places=6)
        self.failUnlessAlmostEqual(PopStdDev(fltvector),7.14599, places=6)
        self.failUnlessAlmostEqual(PopStdDev(fltmisvec),7.293412, places=6)
        #self.failUnlessAlmostEqual(SampVar(fltmismat),0.37, places=2)

    def testStdErr(self):
        self.failUnlessAlmostEqual(StdErr(fltvector),2.887254, places=6)
        self.failUnlessAlmostEqual(StdErr(fltmisvec),3.402884, places=6)



if __name__ == '__main__':
    unittest.main()

