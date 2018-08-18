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
# transpose of x
print "enter the highest degree of the poynomial="
m=input()
m= int(m)
# degree of polynomial
print "enter the value of Lagrangian multiplier="
l=input()
l=float(l)
# Lagrangian multiplier
X=np.full(np.shape(x),1)
for i in range(1,m,1)
    X_=x**i
    X=np.column_stack(X,X_)
print X
# basis function

W = np.zeros((N,N))
X_inv=np.linalg.inv(np.matmul(X.T,X)+l*np.identity(m))
W = np.matmul(np.matmul(X_inv,X.T),y)
print "W="
print W
Y=np.matmul(X,W)
plt.plot(x,y,'*',X,Y,'-')
plt.show()
