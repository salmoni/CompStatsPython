def Wilcoxon ( sample1 , sample 2 ):
	diff = sample1 - sample2
	diff = diff [ not_equal ( x , 0 ) ]
	diff_abs = abs ( diff )
	r_diff = ranked ( diff_abs )
	lx = less ( diff , 0 )
	gx = greater ( diff , 0 )
	ranks = r_diff * -lx
	ranks [ gx ] = r_diff [ gx ]
	W = sum ( ranks )
	return W
