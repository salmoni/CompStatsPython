class LinearRegression( object ):
	def __init__ ( self , x, y ):
		self.statistics = """
		Multiple Linear Regression \n\n
		Note that some of these are scalars, others are vectors\n\n
		n = number of cases\n
		k = number of predictor variables\n
		beta = beta coefficients\n
		t_est = t as estimated from the beta coefficients\n
		residual = residual\n
		dfmean = degrees of freedom for the mean\n
		dfreg = degrees of freedom for the regression\n
		dfres = degrees of freedom for the residual\n
		SSmean = sum of squares for the mean\n
		SSreg = sum of squares for the regression\n
		SSres = sum of squares for the residual\n
		MSreg = mean square for the regression\n
		MSres = mean square for the residual\n
		F = F-ratio for the analysis of variance table\n
		R_2 = R squared\n
		F2 = another F-ratio calculated for internal consistency\n
		p = p-value for the regression in the analysis of variance table
		"""
		self.x = x
		self.y = y
		self.PrepareIV ( )
		self.CalculateBeta ( )
		self.CalculateEstY ( )
		self.CalculateResidual ( )
		self.CalculateDF ( )
		self.CalculateSS ( )
		self.CalculateF ( )
		self.CalculateP ( )

	def PrepareIV ( self ):
		try:
			self.n = len ( self.x[0] )
			self.k = len ( self.x )
			sh = shape ( self.x )
			self.xadj = ones ( [ self.k + 1 , self.n ] )
			self.xadj [ 1: ] = self.x
		except TypeError:
			self.n = len ( self.x )
			self.k = ones ( [ 2 , self.n ] )
			self.xadj [ 1 ] = self.x

	def CalculateBeta ( self ):
		self.invXX = la.inverse ( dot ( self.xadj , transpose ( self.xadj ) ) )
		self.Xy = dot ( self.xadj , self.y )
		self.beta = dot ( self.invXX , self.Xy )

	def CalculateEstY ( self ):
		self.y_est = dot ( self.beta , self.xadj )

	def CalculateResidual ( self ):
		self.residual = self.y - self.y_est

	def CalculateDF ( self ):
		self.dfmean = self.n - 1
		self.dfreg = self.k
		self.dfres = self.n - self.k - 1

	def CalculateSS ( self ):
		self.SSmean = sum ( ( self.y - average ( self.y ) ) ** 2 )
		self.SSres  = sum ( self.residual ** 2 )
		self.SSreg  = sum ( ( self.y_est - average ( self.y ) ) ** 2 )
		self.SStotal = self.SSmean + self.SSreg + self.SSreg

	def CalculateF ( self ):
		self.MSreg = self.SSreg / float ( self.dfreg )
		self.MSres = self.SSres / float ( self.dfres )
		self.F = self.MSreg / self.MSres

	def CalculateR_2 ( self ):
		self.R_2 = self.SSreg / self.SStotal
		self.F2 = ( self.R_2 / self.k ) / ( ( 1 - self.R_2 ) / ( self.n - self.k - 1 ) )


























