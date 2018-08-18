import numpy as np
import matplotlib.pyplot as plt

# Number of training samples
N = 10
# Generate equispaced floats in the interval [0, 2π]
x = np.linspace(0, 2*np.pi, N)
# Generate noise
mean = 0
std = 0.05
# Generate some numbers from the sine function
y = np.sin(x)
# Add noise
y += np.random.normal(mean, std, N)
xT=x.reshape((-1,1))
print "enter the highest degree of the poynomial="
m=input()
m= int(m)
X=np.full(np.shape(x),1)
for i in range(1,m,1)
    X_=x**i
    X=np.column_stack(X,X_)
print X
print "enter the value of Lagrangian multiplier="
l=input()
l=float(l)
W = np.zeros((N,N))
X_inv=np.linalg.inv(np.matmul(X.T,X)+l*np.identity(m))
W = np.matmul(np.matmul(X_inv,X.T),y)
print "W="
print W
Y=np.matmul(X,W)
plt.plot(x,y,'*',X,Y,'-')
plt.show()

print "enter the standard deviation of labels="
std1 = input()
std1=float(std1)
labels = np.random.normal(Y,std1,N)
error=Y-labels
variance= np.var(error)
print "variance in labels:"
print variance
a=np.sqrt((std1**2)/l)
print "the variance of weights="
print a
