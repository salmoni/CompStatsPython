v1 <- c(-13.57011,  -8.87107,  -3.36186,   1.48964,  -9.97446)
v2 <- c(-5.29861, -11.34901,  -9.62941, -11.53654, -15.86822)
v3 <- c(  2.01274,   9.59148,  -6.45352,  20.03864,   9.62793)
v4 <- c(-19.78022,  -6.51878,  19.3489 ,  -4.31552,  -5.59646)
v5 <- c(-11.99721,   1.235  ,  -8.87957,  24.13849,  10.34974)
v6 <- c( 4.14648,  -3.81692,  21.21134,   6.97652,  22.09707)

mat1 <- data.frame(v1, v2, v3, v4, v5)
mat2 <- data.frame(v1, v2, v3, v4, v5, v6)

mmat1 <- data.matrix(mat1)
mmat2 <- data.matrix(mat2)

var1 <- c(2,4,6)
var2 <- c(2, 4, 5, 4, 6, 7)
var3 <- data.matrix(c(1, 2, 3, 2), c(4, 5, 4, 5))
var4 <- c(1.36, 1.79, 1.18, 1.42, 1.40, 1.37)

res = var2 + var4
print(cat('var2 + var4 = ', res))
res = var2 - var4
print(cat('var2 - var4 = ', res))
res = var2 * var4
print(cat('var2 * var4 = ', res))
res = var2 / var4
print(cat('var2 / var4 = ', res))
res = sum(var2 * var4)
print(cat('dot(var2, var4)=', res))

# diagonal here!

res = t(mmat1)
print(cat('Transpose mmat1 = ',res))
res = det(mmat1)
print(cat('Determinant mmat1 = ',res))
res = solve(mmat1)
print(cat('Inverse mmat1 = ',res))

