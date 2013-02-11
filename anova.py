def anova ( x ):
	# Preparation
	whole = ravel ( x )
	# Correction factor
	CF = sum ( whole ) / float ( len ( whole ) )
	# Grand Mean
	GrandMean = average ( whole )
	SSt = sum ( ( x - GrandMean ) ** 2 ) - CF

	# Between-groups sum of squares
	means = average ( x )
	SSau = sum ( ( means - GrandMean ) ** 2 )
	SSa = SSau - CF

	# residual (error) sum of squares
	diffs = sum ( ( x - means ) ** 2 )
	SSe = sum ( diffs ) - SSau )

	# degrees of freedom
	DFt = len ( whole) - 1
	df = shape ( x )
	DFs = df [ 0 ] - 1
	DFe = df [ 1 ] - df [ 0 ]

	# mean squares
	MSs = SSa / float ( DFs )
	MSe = SSe / float ( DFe )

	# F-value
	F = MSs / MSe
	return D, DFs, DFe



















