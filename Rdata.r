#Data.py
#
#This module contains definitions for data and nothing else. These will be used for unit testing and comparing against other statistics programs.
#
#Integer vectors
#Integer matrices
#Integer missing vector
#Integer missing arrays
#Float vectors I
#Float vectors II
#Float matrices
#Float missing vector
#Float missing arrays

# This is a version for testing on R


intvector <- c(0,19,2,3,16,19,12,2)
intmatrix <- matrix(c(0,19,2,3,16,19,12,2,19,1,5,4,4,12,18,16,0,4,14,13,19,17,6,12), nrow=3, ncol=8)
intmisvec <- c(0,19,2,NA,16,19,12,NA)
intmismat <- c(0,19,2,NA,16,19,12,NA,19,NA,5,4,4,12,18,16,0,4,NA,13,19,NA,6,12)
fltvector <- c(0.460, 18.509, 1.627, 2.795, 16.258, 19.021, 11.699, 1.912)
fltmatrix <- matrix(c(0.46, 18.50, 1.62, 2.79, 16.25, 19.02, 11.69, 1.91,18.96, 0.66, 4.82, 4.12, 13.97, 12.00, 17.74, 16.06,0.37, 4.32, 13.74, 13.49, 19.28, 16.88, 6.29, 12.49),nrow=3, ncol=8)
fltmisvec <- c(0.460, 18.509, 1.627, NA, 16.258, 19.021, 11.699, NA)
fltmismat <- matrix(c(0.46, 18.50, 1.62, NA, 16.25, 19.02, 11.69, NA,18.96, NA, 4.82, 4.12, 13.97, 12.00, 17.74, 16.06,0.37, 4.32, NA, 13.49, 19.28, NA, 6.29, 12.49),nrow=3, ncol=8)
longvec <- c(5.233, 8.012, 7.966, 2.608, 4.67, 8.924, 3.897, 5.537, 4.351, 9.147, 2.889, 3.418, 3.393, 8.202, 1.046, 2.684, 1.504, 6.814, 3.346, 6.311)
uniques <- c(1,2,3,4,3,2,1,2,3,4,3,2,3,2,2,2)
uniqmis <-c(1,2,3,NA,NA,2,1,2,3,4,3,2,NA,2,2,2)


