import numpy, scipy

"""
A small collection of useful statistics routines

"""

def GetIVs(x):
    """
    returns values within an independent variable
    """
    return numpy.array(list(set(x)))

def GetAllCrossTabs(vars):
    """
    returns all crosstabbed values
    """
    k = len(vars)
    # numpy.where((x == itemx) & (y == itemy))
    # returns the indicaes of x[itemx] and y[itemy]
    
