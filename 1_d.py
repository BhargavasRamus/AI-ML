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
x0=np.full(np.shape(x),1)
X=np.column_stack(x0,x)
W = np.zeros((N,N))
W = np.matmul(np.linalg.pinv(X),y)
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
print "variance in y:"
print variance
