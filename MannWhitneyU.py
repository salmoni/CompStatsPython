def MannWhitneyU ( sample1 , sample2 ):
	n1 = len ( sample1 )
	n2 = len ( sample2 )
	[ r1 , r2 ] = ranked ( [ sample1 , sample2 ] )
	R = sum ( r1 )
	U = ( n1 * n2 ) + ( ( n1 * ( n1 + 1 ) ) / float ( 2 ) ) - R
	return U
