import numpy as np
from numpy import asarray
from PIL import Image
from numpy.linalg import norm


image = Image.open("unnamed.png") #reading the imag
data = asarray(image) #converting the imag into an array
Mat=data[1,0:3] #Selecting a Matrix from the array
print(Mat) 
Mat_transpose=Mat.T
print(Mat_transpose)
def isDiagonal(M):
    if len(M[0])!=len(M[:,0]) : return "Matrix not square"
    for i in range(0, len(M[0])): 
        for j in range(0, len(M[0])): 
            if ((i != j) and (M[i][j] != 0)) : 
                return False
    return True

print(isDiagonal(Mat))

def isIdentity(M):
    if len(M[0])!=len(M[:,0]) : return "Matrix not square"
    if (M!=np.identity(len(M[0]))).all(): return False
    return True

print(isIdentity(Mat))

print(np.allclose(Mat, np.diag(np.diag(Mat)))) # check if diagonal

print(np.allclose(Mat, np.tril(Mat))) # check if lower triangular
print(np.allclose(Mat, np.triu(Mat))) # check if upper triangular


V=Mat[1]
print(V)
print("The L1 norm",norm(V,1))
print("The L2 norm",norm(V))
