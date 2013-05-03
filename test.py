"""
Unit test for stats routines
(c) 2013 Alan James Salmoni

"""

import unittest, numpy
from Data import *
from AllRoutines import *
import KruskalWallis
"""
Vsort
Msort7
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
    def testCount1(self):
        self.assertEqual(Count(intvector),8)

    def testCount2(self):
        self.assertEqual(Count(intmatrix),24)

    def testCount3(self):
        self.assertEqual(Count(fltvector),8)

    def testCount4(self):
        self.assertEqual(Count(fltmisvec),6)

    def testCount5(self):
        self.assertEqual(Count(fltmismat),19)

    def testSum1(self):
        self.assertAlmostEqual(Sum(intvector),73, places=0)

    def testSum2(self):
        self.assertAlmostEqual(Sum(intmatrix),237, places=0)

    def testSum3(self):
        self.assertAlmostEqual(Sum(fltvector),72.281, places=3)

    def testSum4(self):
        self.assertAlmostEqual(Sum(fltmisvec),67.574, places=3)

    def testSum5(self):
        self.assertAlmostEqual(Sum(fltmismat),211.45, places=3)

    def testMinimum1(self):
        self.assertAlmostEqual(Minimum(intvector),0, places=0)

    def testMinimum2(self):
        self.assertAlmostEqual(Minimum(intmatrix),0, places=0)

    def testMinimum3(self):
        self.assertAlmostEqual(Minimum(fltvector),0.46, places=2)

    def testMinimum4(self):
        self.assertAlmostEqual(Minimum(fltmisvec),0.46, places=2)

    def testMinimum5(self):
        self.assertAlmostEqual(Minimum(fltmismat),0.37, places=2)

    def testMaximum1(self):
        self.assertAlmostEqual(Maximum(intvector),19, places=0)

    def testMaximum2(self):
        self.assertAlmostEqual(Maximum(intmatrix),19, places=0)

    def testMaximum3(self):
        self.assertAlmostEqual(Maximum(fltvector),19.021, places=2)

    def testMaximum4(self):
        self.assertAlmostEqual(Maximum(fltmisvec),19.021, places=3)

    def testMaximum5(self):
        self.assertAlmostEqual(Maximum(fltmismat),19.28, places=2)

    def testRange1(self):
        self.assertAlmostEqual(Range(intvector),19, places=0)

    def testRange2(self):
        self.assertAlmostEqual(Range(fltvector),18.561, places=3)

    def testRange3(self):
        self.assertAlmostEqual(Range(intmisvec),19, places=0)

    def testRange4(self):
        self.assertAlmostEqual(Range(fltmisvec),18.561, places=3)

    def testMidRange(self):
        self.assertAlmostEqual(Midrange(longvec),5.0965, places=4)

    def testFrequencies1(self):
        vals, freqs = Frequencies(uniques)
        self.assertListEqual(vals.tolist(), [1, 2, 3, 4])
        self.assertListEqual(freqs.round(4).tolist(), [2,7,5,2])

    def testFrequencies2(self):
        vals, freqs = Frequencies(uniqmis)
        self.assertListEqual(vals.tolist(), [1, 2, 3, 4])
        self.assertListEqual(freqs.round(8).tolist(), [2,7,3,1])

    def testProportions1(self):
        vals, props = Proportions(uniques)
        self.assertListEqual(vals.tolist(), [1, 2, 3, 4])
        self.assertListEqual(props.round(4).tolist(), [0.125, 0.4375, 0.3125, 0.125])

    def testProportions2(self):
        vals, props = Proportions(uniqmis)
        self.assertListEqual(vals.tolist(), [1, 2, 3, 4])
        self.assertListEqual(props.round(8).tolist(), [0.15384615, 0.53846154, 0.23076923, 0.07692308])

    def testPercentages1(self):
        vals, percs = Percentages(uniques)
        self.assertListEqual(vals.tolist(), [1, 2, 3, 4])
        self.assertListEqual(percs.round(2).tolist(), [12.5, 43.75, 31.25, 12.5])

    def testPercentages2(self):
        vals, percs = Percentages(uniqmis)
        self.assertListEqual(vals.tolist(), [1, 2, 3, 4])
        self.assertListEqual(percs.round(6).tolist(), [15.384615, 53.846154, 23.076923, 7.692308])

    def testMean1(self):
        self.assertAlmostEqual(Mean(intvector),9.125, places=3)

    def testMean2(self):
        self.assertAlmostEqual(Mean(intmatrix),9.875, places=3)

    def testMean3(self):
        self.assertAlmostEqual(Mean(fltvector),9.035125, places=6)

    def testMean4(self):
        self.assertAlmostEqual(Mean(fltmisvec),11.26233, places=5)

    def testMean5(self):
        self.assertAlmostEqual(Mean(fltmismat),11.12895, places=5)

    def testTrimmedMean1(self):
        self.assertAlmostEqual(TrimmedMean(intvector, trim=0.05),9.125, places=3)

    def testTrimmedMean2(self):
        self.assertAlmostEqual(TrimmedMean(intmisvec, trim=0.05),11.33333, places=5)

    def testTrimmedMean3(self):
        self.assertAlmostEqual(TrimmedMean(fltvector, trim=0.05),9.035125, places=6)

    def testTrimmedMean4(self):
        self.assertAlmostEqual(TrimmedMean(fltmisvec, trim=0.05),11.26233, places=5)

    def testMedian1(self):
        self.assertAlmostEqual(Median(intvector),7.5, places=1)

    def testMedian2(self):
        self.assertAlmostEqual(Median(intmatrix),12, places=0)

    def testMedian3(self):
        self.assertAlmostEqual(Median(fltvector),7.247, places=3)

    def testMedian4(self):
        self.assertAlmostEqual(Median(fltmisvec),13.9785, places=3)

    def testMode1(self):
        maxes, idx = Mode(uniques)
        self.assertAlmostEqual(maxes,7, places=0)
        self.assertListEqual(idx.tolist(), [2])

    def testMode2(self):
        maxes, idx = Mode(uniqmis)
        self.assertAlmostEqual(maxes,7, places=0)
        self.assertListEqual(idx.tolist(), [2])

    def testSampVar1(self):
        self.assertAlmostEqual(SampVar(intvector),67.55357, places=5)
        #self.assertAlmostEqual(SampVar(intmatrix),, places=6)

    def testSampVar3(self):
        self.assertAlmostEqual(SampVar(fltvector),66.6899, places=4)

    def testSampVar4(self):
        self.assertAlmostEqual(SampVar(fltmisvec),69.4777, places=4)
        #self.assertAlmostEqual(SampVar(fltmismat),0.37, places=2)

    def testPopVar1(self):
        self.assertAlmostEqual(PopVar(intvector),59.10938, places=4)
        #self.assertAlmostEqual(PopVar(intmatrix),, places=)

    def testPopVar3(self):
        self.assertAlmostEqual(PopVar(fltvector),58.35366, places=4)

    def testPopVar4(self):
        self.assertAlmostEqual(PopVar(fltmisvec),57.89808, places=4)
        #self.assertAlmostEqual(SampVar(fltmismat),0.37, places=2)

    def testSampStdDev1(self):
        self.assertAlmostEqual(SampStdDev(intvector),8.219098, places=6)

    def testSampStdDev2(self):
        self.assertAlmostEqual(SampStdDev(intmisvec),8.430105, places=6)

    def testSampStdDev3(self):
        self.assertAlmostEqual(SampStdDev(fltvector),8.166389, places=6)

    def testSampStdDev4(self):
        self.assertAlmostEqual(SampStdDev(fltmisvec),8.335328, places=6)
        #self.assertAlmostEqual(SampVar(fltmismat),0.37, places=2)

    def testPopStdDev1(self):
        self.assertAlmostEqual(PopStdDev(intvector),7.688262, places=6)

    def testPopStdDev2(self):
        self.assertAlmostEqual(PopStdDev(intmisvec),7.695598, places=6)

    def testPopStdDev3(self):
        self.assertAlmostEqual(PopStdDev(fltvector),7.638957, places=6)

    def testPopStdDev4(self):
        self.assertAlmostEqual(PopStdDev(fltmisvec),7.609079, places=6)
        #self.assertAlmostEqual(SampVar(fltmismat),0.37, places=2)

    def testStdErr1(self):
        self.assertAlmostEqual(StdErr(fltvector),2.887254, places=6)

    def testStdErr2(self):
        self.assertAlmostEqual(StdErr(fltmisvec),3.402884, places=6)

    def testQ1_1(self):
        self.assertAlmostEqual(Q1(longvec, 0.25), 2.889, places=3)

    def testQ1_2(self):
        self.assertAlmostEqual(Q1(longvec, 0.75), 6.814, places=3)

    def testQ2_1(self):
        self.assertAlmostEqual(Q2(longvec, 0.25), 3.1175, places=4)

    def testQ2_2(self):
        self.assertAlmostEqual(Q2(longvec, 0.75), 7.39, places=2)
 
    def testQ3_1(self):
        self.assertAlmostEqual(Q3(longvec, 0.25), 2.889, places=3)

    def testQ3_2(self):
        self.assertAlmostEqual(Q3(longvec, 0.75), 6.814, places=3)
 
    def testQ4_1(self):
        self.assertAlmostEqual(Q4(longvec, 0.25), 2.889, places=3)

    def testQ4_2(self):
        self.assertAlmostEqual(Q4(longvec, 0.75), 6.814, places=3)
 
    def testQ5_1(self):
        self.assertAlmostEqual(Q5(longvec, 0.25), 3.1175, places=4)

    def testQ5_2(self):
        self.assertAlmostEqual(Q5(longvec, 0.75), 7.39, places=2)
 
    def testQ6_1(self):
        self.assertAlmostEqual(Q6(longvec, 0.25), 3.00325, places=5)

    def testQ6_2(self):
        self.assertAlmostEqual(Q6(longvec, 0.75), 7.678, places=3)
 
    def testQ7_1(self):
        self.assertAlmostEqual(Q7(longvec, 0.25), 3.23175, places=5)

    def testQ7_2(self):
        self.assertAlmostEqual(Q7(longvec, 0.75), 7.102, places=3)
 
    def testQ8_1(self):
        self.assertAlmostEqual(Q8(longvec, 0.25), 3.079417, places=6)

    def testQ8_2(self):
        self.assertAlmostEqual(Q8(longvec, 0.75), 7.486, places=3)
 
    def testQ9_1(self):
        self.assertAlmostEqual(Q9(longvec, 0.25), 3.088938, places=5)

    def testQ9_2(self):
        self.assertAlmostEqual(Q9(longvec, 0.75), 7.462, places=3)

    def testMAD1(self):
        self.assertAlmostEqual(MAD(intvector), 9.6369, places=4)
        
    def testMAD2(self):
        self.assertAlmostEqual(MAD(intmisvec), 7.413, places=3)

    def testMAD3(self):
        self.assertAlmostEqual(MAD(fltvector), 9.197309, places=6)

    def testMAD4(self):
        self.assertAlmostEqual(MAD(fltmisvec), 7.096465, places=6)

    def testMoment1(self):
        self.assertAlmostEqual(Moment(intvector,2), 59.10938, places=4)

    def testMoment2(self):
        self.assertAlmostEqual(Moment(intmisvec,4), 5245.074, places=3)

    def testMoment3(self):
        self.assertAlmostEqual(Moment(fltvector,1), -6.661338e-16, places=6)

    def testMoment4(self):
        self.assertAlmostEqual(Moment(fltmisvec,3), -197.1184, places=4)

    def testGeometricMean1(self):
        self.assertAlmostEqual(GeometricMean(intvector), 7.009916, places=6)

    def testGeometricMean2(self):
        self.assertAlmostEqual(GeometricMean(intmisvec), 10.675, places=3)

    def testGeometricMean3(self):
        self.assertAlmostEqual(GeometricMean(fltvector), 4.769588, places=6)

    def testGeometricMean4(self):
        self.assertAlmostEqual(GeometricMean(fltmisvec), 6.07197, places=5)

    def testHarmonicMean1(self):
        #self.assertAlmostEqual(HarmonicMean(intvector), 0, places=0)
        #self.assertAlmostEqual(HarmonicMean(intmisvec), 0, places=0)
        self.assertAlmostEqual(HarmonicMean(fltvector), 2.039296, places=6)

    def testHarmonicMean4(self):
        self.assertAlmostEqual(HarmonicMean(fltmisvec), 1.972304, places=6)

    def testWinsorisedMean1(self):
        self.assertAlmostEqual(WinsorisedMean(intvector, 0.1), 9.3, places=1)

    def testWinsorisedMean2(self):
        self.assertAlmostEqual(WinsorisedMean(intmisvec, 0.1), 11.5, places=6)

    def testWinsorisedMean3(self):
        self.assertAlmostEqual(WinsorisedMean(fltvector, 0.1), 9.092438, places=5)

    def testWinsorisedMean4(self):
        self.assertAlmostEqual(WinsorisedMean(fltmisvec, 0.1), 11.31692, places=4)

    def testSkewness1(self):
        self.assertAlmostEqual(Skewness(intvector), 0.1544885, places=7)

    def testSkewness2(self):
        self.assertAlmostEqual(Skewness(intmisvec), -0.4628102, places=7)

    def testSkewness3(self):
        self.assertAlmostEqual(Skewness(fltvector), 0.1683335, places=7)

    def testSkewness4(self):
        self.assertAlmostEqual(Skewness(fltmisvec), -0.447436, places=6)


    def testKurtosis1(self):
        self.assertAlmostEqual(Kurtosis(intvector), 1.245587, places=6)

    def testKurtosis2(self):
        self.assertAlmostEqual(Kurtosis(intmisvec), 1.495486, places=6)

    def testKurtosis3(self):
        self.assertAlmostEqual(Kurtosis(fltvector), 1.22172, places=5)

    def testKurtosis4(self):
        self.assertAlmostEqual(Kurtosis(fltmisvec), 1.453783, places=6)

    def testKruskal(self):
        data = numpy.array(([longvec[:10],longvec[10:]]))
        KW = KruskalWallis.KruskalWallis(data)
        self.assertAlmostEqual(KW, 3.5714, places=4)

    

if __name__ == '__main__':
    unittest.main()

