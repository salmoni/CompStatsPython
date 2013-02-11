def chi_square ( data ):
	colsum = sum ( data )
	rowsum = sum ( transpose ( data ) )
	total = sum ( colsum )
	N = len ( ravel ( data ) )
	E = zeros ( shape ( data ) )
	for i in range ( len ( colsum ) ):
		for j in range ( len ( rowsum ) ):
			E[ i , j ] = colsum [ j ] + rowsum [ i ]
	E = E / float ( total )
	OE = ( data - E ) ** 2
	chi = sum ( ravel ( OE / E ) )
	return chi
