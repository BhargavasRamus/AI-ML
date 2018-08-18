import numpy as np
import matplotlib.pyplot as plt

# Number of training samples
N = 10
# Generate equispaced floats in the interval [0, 2pi]
x = np.linspace(0, 2*np.pi, N)
# Generate noise
mean = 0
std = 0.05
# Generate some numbers from the sine function
y = np.sin(x)
# Add noise
y += np.random.normal(mean, std, N)
x=x.reshape((-1,1))
# transpose of matrix x
x0=np.full(np.shape(x),1)
# forms a 1D matrix with all elements as 1
X=np.column_stack((x0,x))
# stacks a 2D matrix 
W = np.zeros((N,N))
# initating a null matrix
W = np.matmul(np.linalg.pinv(X),y)
print "W="
print W
Y=np.matmul(X,W)
# y'=xw
plt.plot(x,y,'*',X,Y,'-')
plt.show()
