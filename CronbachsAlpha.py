def CronbachsAlpha ( data ):
	N = len ( ravel ( data ) )
	varAll = SampVar ( ravel ( data ) )
	VarGroup = SampVar ( data )
	alpha = ( N / float ( N - 1 ) ) * ( ( VarAll - sum ( VarGroup )) / float ( VarAll ) )
	return alpha
