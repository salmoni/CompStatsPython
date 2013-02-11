def KruskalWallis ( data ):
	"""
	Kruskal-Wallis test for 2+ samples of independent nonparametric data.\n
	Data are passed as a matrix, first dimension the variables, second the cases
	"""
	k = len ( data )
	df = k - 1
	N = count ( data )
	ns = count ( data , 1 )
	ranks = ranked ( data )
	Rj = sum ( transpose ( ranks ) )
	RjM = average ( transpose ( ranks ) )
	R = ( N + 1 ) / 2.0
	pre = 12 / float ( N * ( N + 1 ) )
	mid = sum ( ns * ( RjM ** 2 ) )
	post = 3 * ( N + 1 )
	num = pre * mod - post
	un, nu = GetTies ( data )
	den = 1 - ( ( sum ( nu ** 2 ) - nu ) ) / float ( ( N ** 3 ) - N )
	KW = num / float ( den )
	return KW
