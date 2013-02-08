"""
Stats routines

A complete list of statistics routine for the 'Computational Statistics' book

The routines are:

VSort - sort a vector
MSort - sort a numpy.matrix
CalculateRanks - for calculating the ranks of a numpy.matrix
GetSSCP_M - calculates the sum of squares and cross-products numpy.matrix
GetVarsCovars_M - calculates the variances and covariances numpy.matrix
GetVariances - calculates the variances of a numpy.matrix of variables
GetStdDevs - calculates the standard deviations of a numpy.matrix of variables
GetCorrelationMatrix - calculates the correlation numpy.matrix
Count - returns the number of non-missing data
sum - returns the sum of non-missing data
minimum - returns the minimum of non-missing data
maximum - returns the maximum of non-missing data
Range - maximum minus the minimum
proportions - 
relfreqmode - 
cumsum - 
cumproduct - 
cumpercent - 
frequencies - 
trimmeddata - 
trimmedmean - 
bitrimmedmean - 
mean - 
median - 
mode - 
moment - 
TukeyQuartiles - returns Tukey's hinges
MooreQuartiles - returns Moore & McCabe's hinges
SPQuantile - quantile used by S-Plus
TradQuantile - quantile used by SPSS
MidstepQuantile - mid-step qua
Q1 - Q1 quantile from Hyndnumpy.man & Fan
Q2 - Q2 quantile from Hyndnumpy.man & Fan
Q3 - Q3 quantile from Hyndnumpy.man & Fan
Q4 - Q4 quantile from Hyndnumpy.man & Fan
Q5 - Q5 quantile from Hyndnumpy.man & Fan
Q6 - Q6 quantile from Hyndnumpy.man & Fan
Q7 - Q7 quantile from Hyndnumpy.man & Fan
Q8 - Q8 quantile from Hyndnumpy.man & Fan
Q9 - Q9 quantile from Hyndnumpy.man & Fan 
InterquartileRange - 
SS - sum of squares
SSDevs - sum of squared deviations from the mean
SampVar - sample variance
PopVar - population variance
SampStdDev - sample standard deviation
PopStdDev - population standard deviation
StdErr - standard error
CoeffVar - coefficient of variation
ConfidenceIntervals - returns the confidence intervals
numpy.maD - Median absolute deviation
GeometricMean - the geometric mean
HarmonicMean - the harmonic mean
MSSD - mean of subsequent squared deviations
Skewness - returns the skewness
Kurtosis - returns the kurtosis
StandardScore - transforms a vector into a standard (ie, z-) score
EffectSizeControl - returns an effect size if a control condition is present
EffectSize - returns an effect size if no control is present
FiveNumber - Tukey's five number sumnumpy.mary (minimum, lower quartile, median, upper quartile, maximum)
OutliersSQR - returns two arrays, one of outliers defined by 1.5 * IQR, and the other without these outliers

"""
import numpy 
import numpy.ma


def Vsort(data):
	# check that 'data' is a vector
	return numpy.ma.sort(data)

def Msort(data):
	# check that 'data' is a numpy.matrix
	dims = numpy.ma.shape(data)
	length = dims[0] * dims[1]
	return numpy.ma.reshape(numpy.ma.sort(numpy.ma.reshape(data, length)), dims)

def UniqueVals(data):
    data = numpy.ma.array(data)
    uniques = numpy.ma.sort(list(set(data.compressed())))
    numbers = numpy.zeros((len(uniques)))
    for idx, unique in enumerate(uniques):
        number = numpy.ma.equal(data, unique).sum()
        numbers[idx] = number
    return uniques, numbers

def CalculateRanks(data, start = 1):
        data = numpy.ma.array(data)
        vals = sort(list(set(data.compressed())))
        rank = start - 0.5
        ranks = numpy.ma.zeros(numpy.ma.shape(data), 'f')
        for i in vals:
                numpy.match = numpy.ma.equal(data, i)
                incr = numpy.ma.sum(numpy.ma.sum(numpy.match))
                numpy.match = array(numpy.match)
                ranks[numpy.match] = rank + (incr / 2.0)
                rank = rank + incr
        return numpy.ma.numpy.masked_where(numpy.ma.equal(ranks, 0), ranks)

def GetSSCP_M(data):
	Xd = data - numpy.ma.average(data)
	Xdp = numpy.ma.transpose(Xd)
	return numpy.ma.dot(Xdp, Xd)

def GetVarsCovars_M(data):
	SSCP = GetSSCP_M(data)
	return SSCP / len(data[1]) # is the len(data[1]) correct?

def GetVariances(data):
	return numpy.ma.diagonal(GetVarsCovars_M(data))

def GetStdDevs(data):
	return numpy.ma.sqrt(GetVariances(data))
	
def GetCorrelationnMatrix(data):
	VCV = GetVarsCovars_M(data)
	return VCV / numpy.ma.sqrt(numpy.ma.diagonal(VCV))

def Count(data):
	"""
	"count", "N", "number"
	"""
	data = numpy.ma.array(data)
	return int(numpy.ma.count(data))

def Sum(data):
	"""
	"sum", "total"
	"""
	t = str(data.dtype.type)
	if 'string' in t:
		return None# is string
	elif "int" in t:
		return int(numpy.ma.sum(data))
	elif 'float' in t:
		return float(numpy.ma.sum(data))
	else: 
		return None

def Minimum(data):
	"""
	"minimum", "min", "lowest", "snumpy.mallest", "least"
	"""
	t = str(data.dtype.type)
	if 'string' in t:
		return data.sort[0] # is string
	elif "int" in t:
		return int(numpy.ma.minimum(data))
	elif 'float' in t:
		return float(numpy.ma.minimum(data))
	else: 
		return None

def Maximum(data):
	"""
	"maximum", "max", "highest", "largest", "biggest"
	"""
	t = str(data.dtype.type)
	if 'string' in t:
		return sort(a)[-1] # is string
	elif "int" in t:
		return int(numpy.ma.maximum(data))
	elif 'float' in t:
		return float(numpy.ma.maximum(data))
	else: 
		return None

def Range(data):
	return Maximum(data) - Minimum(data)

def Midrange(data):
    maximum = Maximum(data)
    minimum = Minimum(data)
    midrange = (maximum - minimum) / 2.0
    return midrange

def Proportions(data):
	"""
	"proportions", "proportion"
	"""
	un, nu = UniqueVals(data)
	return un, nu / numpy.ma.sum(nu)

def Percentages(data):
    un, nu = Proportions(data)
    return un, nu * 100

def RelFreqMode(data):
	"""
	"relative frequency of mode"
	"relativefrequencymode", "relative frequency of the mode", 
	"""
	vals, nums = UniqueVals(data)
	m = Maximum(nums)
	total = numpy.ma.sum(nums)
	modes = numpy.ma.equal(data, m)
	return modes, (m / float(total)) * 100.0
	
def sum(data):
    return data.sum()

def CumSum(data):
	"""
	"cumulative sum", "cumsum"
	"""
	t = str(data.dtype.type)
	if 'string' in t:
		return None
	elif "int" in t:
		return int(cumsum(data)[-1])
	elif 'float' in t:
		return float(CumSum(data)[-1])
	else: 
		return None

def CumProduct(data):
	"""
	"cumulative product", "cumproduct"
	"""
	t = str(data.dtype.type)
	if 'string' in t:
		return None
	elif "int" in t:
		return int(numpy.ma.cumprod(data)[-1])
	elif 'float' in t:
		return float(numpy.ma.cumprod(data)[-1])
	else: 
		return None

def CumPercent(data):
	"""
	"cumulative percent", "cumpercent", "cumulative percentage"
	"""
	# assumes numbers of frequencies are sent
	return data / float(numpy.ma.sum(data)) * 100.0

def Frequencies(data):
    """
    "frequencies", "frequency", "freq"
    """
    uniques, numbers = UniqueVals(data)
    return uniques, numbers, CumPercent(numbers) / 100.0 #, nu, nu / CumPercent(nu)

def TrimmedData(data, Lsplit, Usplit = None):
	if Usplit == None:
		Usplit = Lsplit
	data = numpy.ma.sort(data)
	LB = MidstepQuantile(data, Lsplit)
	UB = MidstepQuantile(data, 1.0-Usplit)
	data = numpy.ma.compress(numpy.ma.greater(data, LB), data)
	data = numpy.ma.compress(numpy.ma.less(data, UB), data)
	return data

def TrimmedMean(data, trim):
	"""
	"trimmed mean", "trimmean", "trimmedmean"
	"""
	t = str(data.dtype.type)
	if 'string' in t:
		return None
	elif "int" in t:
		split = (trim / 200.0)
		data = TrimmedData(data, split, split)
		return int(numpy.ma.average(data))
	elif 'float' in t:
		split = (trim / 200.0)
		data = TrimmedData(data, split, split)
		return float(numpy.ma.average(data))
	else: 
		return None

def BiTrimmedMean(data, Ltrim, Utrim):
	t = str(data.dtype.type)
	if 'string' in t:
		return None
	else:
		Lsplit = Ltrim / 100.0
		Usplit = Utrim / 100.0
		data = TrimmedData(data, Lsplit, Usplit)
		if "int" in t:
			return int(numpy.ma.average(data))
		elif 'float' in t:
			return float(numpy.ma.average(data))
		else:
			return None

def Mean(data):
	"""
	"mean", "average", "arithmetic mean"
	"""
	t = str(data.dtype.type)
	if 'string' in t:
		return None
	else:
		try:
			return float(numpy.ma.average(data))
		except:
			return

def Median(data):
	"""
	"median"
	"""
	t = str(data.dtype.type)
	if 'string' in t:
		l = numpy.ma.count(data)
		if mod(l, 2):
			# odd numbered
			return data[(l/2)+1]
		else:
			return (data[l/2], data[(l/2)+1])
	if 'float' in t or 'int' in t:
		return float(numpy.ma.median(data))
	else: 
		return None

def Mode(data):
	"""
	"mode", "most common"
	"""
	# get list of values
	sa = set(data)
	nums = []
	# gather number of occurences of each
	for i in sa:
		nums.append(len(compress(i == data, data)))
	# get maximum number of occurences
	nums = array(nums)
	modes = Maximum(nums)
	ind = modes == data
	return data[ind], float(modes/numpy.ma.count(data))

def Moment(data, m):
	t = str(data.dtype.type)
	if 'string' in t:
		return 
	elif 'float' in t or 'int' in t:
		return float(numpy.ma.sum((data - numpy.ma.average(data)) ** m) / numpy.ma.count(data))
	else:
		return 

def TukeyQuartiles(data):
	data = numpy.ma.sort(data)
	med = Median(data)
	firstQ = numpy.ma.compress(numpy.ma.less_equal(data, med), data)
	thirdQ = numpy.ma.compress(numpy.ma.greater_equal(data, med), data)
	return Median(data[firstQ]), Median(data[thirdQ])

def MooreQuartiles(data):
	data = numpy.ma.sort(data)
	med = Median(data)
	firstQ = numpy.ma.compress(numpy.ma.less(data, med), data)
	thirdQ = numpy.ma.compress(numpy.ma.greater(data, med), data)
	return Median(data[firstQ]), Median(data[thirdQ])

def QuantileDef(data, k, a):
	return ((1-a)*data[k-1])+(a*data[k])

def SPQuantile(data, alpha):
	data = numpy.ma.sort(data)
	n = numpy.ma.count(data)
	k = int(1+(alpha*(n-1)))
	a = 1+(alpha*(n-1))-k
	Q = QuantileDef(data, k, a)
	return Q

def TradQuantile(data, alpha):
	data = numpy.ma.sort(data)
	n = numpy.ma.count(data)
	k = int(alpha * (n+1))
	a = (alpha*(n+1))-k
	Q = QuantileDef(data, k, a)
	return Q

def MidstepQuantile(data, alpha):
	# has limits up to alpha < 0.98 and alpha > 0.02
	data = numpy.ma.sort(data)
	n = numpy.ma.count(data)
	k = int((alpha * n) + 0.5)
	a = (alpha*n)-k+0.5
	Q = QuantileDef(data, k, a)
	return Q

def Q1(data, alpha):
	n = numpy.ma.count(data)
	data = numpy.ma.sort(data)
	k = int(alpha * n)
	g = (alpha * n) - k
	if g == 0:
		a = 0.0
	else:
		a = 1.0
	Q = QuantileDef(data, k, a)
	return Q

def Q2(data, alpha):
	n = numpy.ma.count(data)
	data = numpy.ma.sort(data)
	k = int(alpha * n)
	g = (alpha * n) - k
	if g == 0:
		a = 0.5
	else:
		a = 1.0
	Q = QuantileDef(data, k, a)
	return Q

def Q3(data, alpha):
	n = numpy.ma.count(data)
	data = numpy.ma.sort(data)
	m = -0.5
	k = int((alpha * n) + m)
	g = (alpha * n) + m - k
	a = 1.0
	if g == 0 and not k % 2:
		a = 0
	Q = QuantileDef(data, k, a)
	return Q

def Q4(data, alpha):
	n = numpy.ma.count(data)
	data = numpy.ma.sort(data)
	m = 0.0
	k = int((alpha * n) + m)
	a = ((alpha * n) + m) - k
	Q = QuantileDef(data, k, a)
	return Q

def Q5(data, alpha):
	n = numpy.ma.count(data)
	data = numpy.ma.sort(data)
	m = 0.5
	k = int((alpha * n) + m)
	a = ((alpha * n) + m) - k
	Q = QuantileDef(data, k, a)
	return Q

def Q6(data, alpha):
	n = numpy.ma.count(data)
	data = numpy.ma.sort(data)
	m = alpha
	k = int((alpha * n) + m)
	a = ((alpha * n) + m) - k
	Q = QuantileDef(data, k, a)
	return Q

def Q7(data, alpha):
	n = numpy.ma.count(data)
	data = numpy.ma.sort(data)
	m = 1.0 - alpha
	k = int((alpha * n) + m)
	a = ((alpha * n) + m) - k
	Q = QuantileDef(data, k, a)
	return Q

def Q8(data, alpha):
	n = numpy.ma.count(data)
	data = numpy.ma.sort(data)
	m = (alpha + 1) / 3.0
	k = int((alpha * n) + m)
	a = ((alpha * n) + m) - k
	Q = QuantileDef(data, k, a)
	return Q

def Q9(data, alpha):
	n = numpy.ma.count(data)
	data = numpy.ma.sort(data)
	m = (0.25 * alpha) + (3 / 8.0)
	k = int((alpha * n) + m)
	a = ((alpha * n) + m) - k
	Q = QuantileDef(data, k, a)
	return Q

def Quartiles(data):
    q1 = Q8(data, 0.25)
    q2 = Q8(data, 0.50)
    q3 = Q8(data, 0.75)
    return q1, q2, q3

def InterquartileRange(data, Qtype = "8"):
	"""
	"interquartile range", "interquartilerange", "iqr"
	"""
	t = str(data.dtype.type)
	if 'int' in t or 'float' in t:
		numpy.ma.sort(data)
		minimum, median, maximum = Quartiles(data)
		return float(maximum - minimum)
	else:
		return

def SS(data):
	"""
	"sum of squares", "ss", "sumofsquares", "SS"
	"""
	t = str(data.dtype.type)
	if 'int' in t or 'float' in t:
		return float(numpy.ma.sum(data ** 2))
	else:
		return

def SSDevs(data):
	"""
	"ssdevs", "sum of squared deviations"
	"""
	t = str(data.dtype.type)
	if 'int' in t or 'float' in t:
		try:
			tmp = data - numpy.ma.average(data)
			return float(numpy.ma.sum(tmp ** 2))
		except:
			return None
	else:
		return

def SampVar(data):
	"""
	"variance", "sampvar", "sample variance", "var"
	"""
	t = str(data.dtype.type)
	if 'int' in t or 'float' in t:
		try:
			return float(SSDevs(data) / float(numpy.ma.count(data) - 1))
		except:
			return None
	else:
		return

def PopVar(data):
	"""
	"population variance", "popvar"
	"""
	t = str(data.dtype.type)
	if 'int' in t or 'float' in t:
		try:
			return float(SSDevs(data) / float(numpy.ma.count(data)))
		except:
			return None
	else:
		return

def SampStdDev(data):
	"""
	"sample standard deviation","sampstddev", "sample stddev", "sampstdev", 
	"sample stdev", "stdev", "stddev", "sd", "standard deviation"
	"""
	t = str(data.dtype.type)
	if 'int' in t or 'float' in t:
		try:
			return float(numpy.ma.sqrt(SampVar(data)))
		except:
			return None
	else:
		return

def PopStdDev(data):
	"""
	"population standard deviation",
	"popstddev", "population stddev", "population stdev"
	"""
	t = str(data.dtype.type)
	if 'int' in t or 'float' in t:
		try:
			return float(numpy.ma.sqrt(PopVar(data)))
		except:
			return None
	else:
		return

def CoeffVar(data):
	"""
	"coefficient of variation", "coeffvar", "coeff var"
	"""
	t = str(data.dtype.type)
	if 'int' in t or 'float' in t:
		try:
			return float(SampStdDev(data) / numpy.ma.average(data))
		except:
			return None
	else:
		return

def StdErr(data):
	"""
	"standard error", "stderr", "se"
	"""
	t = str(data.dtype.type)
	if 'int' in t or 'float' in t:
		try:
			return float(SampStdDev(data) / float(numpy.math.sqrt(Count(data))))
		except:
			return None
	else:
		return

def ConfidenceIntervals(data, p=0.95):
	p = 1.0 - p
	n = numpy.ma.count(data)
	m = numpy.ma.average(data)
	sd = SampStdDev(data)
	diff = (pstats.inverset(p, n-1) * sd) / numpy.math.sqrt(n)
	lb = m - diff
	ub = m + diff
	return lb, ub

def MAD(data):
	"""
	"median absolute deviation", "mad"
	"""
	t = str(data.dtype.type)
	if 'int' in t or 'float' in t:
		med = Median(data)
		return float(Median(data - med))
	else:
		return

def GeometricMean(data):
	"""
	"geometric mean", "geometricmean", "geomean"
	"""
	t = str(data.dtype.type)
	if 'int' in t or 'float' in t:
		try:
			return float(numpy.math.sqrt(numpy.math.sqrt(CumProduct(data))))
		except:
			return None
	else:
		return

def HarmonicMean(data):
	"""
	"harmonic mean", "harmonicmean", "harmmean"
	"""
	t = str(data.dtype.type)
	if 'int' in t or 'float' in t:
		val = numpy.ma.sum(1.0-data)
		if val != 0.0:
			val = numpy.ma.count(data)/val
		return float(val)
	else:
		return

def MSSD(data):
	t = str(data.dtype.type)
	if 'int' in t or 'float' in t:
		val = (data[1:] - data[0:-1]) ** 2
		try:
			return float(numpy.ma.average(val) / float(numpy.ma.count(data) - 2))
		except:
			return None
	else:
		return
	
def Skewness(data):
	"""
	"skewness", "skew"
	"""
	t = str(data.dtype.type)
	if 'int' in t or 'float' in t:
		m3 = Moment(data, 3)
		m2 = Moment(data, 2)
		try:
			return float(m3 / float(m2 * numpy.math.sqrt(m2)))
		except:
			return None
	else:
		return

def Kurtosis(data):
	"""
	"kurtosis", "kurt"
	"""
	t = str(data.dtype.type)
	if 'int' in t or 'float' in t:
		m4 = Moment(data, 4)
		m22 = (Moment(data, 2) ** 2)
		try:
			return float((m4 / float(m22)) - 3.0)
		except:
			return None
	else:
		return

def StandardScore(data):
	av = numpy.ma.average(data)
	sd = SampStdDev(data)
	try:
		z = (data - av) / float(sd)
	except:
		z = None
	return z

def calceffectsizescontrol(d1, d2):
	return abs((numpy.ma.average(d1)-numpy.ma.average(d2))/SampStdDev(data.compressed()))

def EffectSizeControl(data):
	# first index is control second on are data
	if numpy.ma.count(numpy.ma.shape(data)) != 2:
		return
	else:
		return CalcEffectSizeControl(data[0], data[1])

def calceffectsize(d1, d2):
	Psd = numpy.math.sqrt((SampStdDev(d1)**2) + (SampStdDev(d2)**2) / 2.0)
	ES = abs((numpy.ma.average(d1)-numpy.ma.average(d2))/Psd)
	return ES

def EffectSize(data):
	s = len(numpy.ma.shape(data))
	if s != 2:
		return
	s = numpy.ma.count(data)
	if s == 2:
		return CalcEffectSize(data[0], data[1])
	else:
		# permute and apply
		n = 0
		for i in range(3, s+1):
			n = n + i
		vals = numpy.ma.zeros((n), numpy.ma.Float)
		count = 0
		for i in range(1, n+1):
			for j in range(i+1, n+1):
				vals[count] = CalcEffectSize(data[i-1], data[j-1])
				count = count + 1
		return vals

def FiveNumber(data):
	mn = Minimum(data)
	mx = Maximum(data)
	med = Median(data)
	quartiles = (Q8(data, 0.25), Q8(data, 0.75))
	return mn, quartiles[0], med, quartiles[1], mx

def OutliersIQR(data):
	IQR = InterquartileRange(data)
	# returns outliers defined as those outside 1.5 * IQR
	# note - this is not finished - needs the 1.5 and the centre point (mean)
	firstQ = numpy.ma.compress(numpy.ma.less(data, IQR[0]), data)
	secondQ = numpy.ma.compress(numpy.ma.greater(data, IQR[1]), data)
	outliers = numpy.ma.concatenate((firstQ, secondQ))
	step1 = numpy.ma.compress(numpy.ma.greater(data, IQR[0]), data)
	step2 = numpy.ma.compress(numpy.ma.less(step1, IQR[1]), data)
	return outliers, step2

