#time evolution of invariant density
import numpy as np
import matplotlib.pyplot as plt

#initialising x-array for values
h=0.001
x=np.arange(0,1,h)
p0=np.ones(len(x))
pi=np.zeros(len(x))
T=100

def f(y):
	return 4*y*(1-y)

def fInv(z):
	return (1+np.sqrt(1-z))/2.

for t in range(T):
	for j in range(len(x)):
		yVal=x[j]
		xVal=fInv(yVal)
		indX=int(xVal/h)-1
		pi[j]=p0[indX]
	p0=np.array(pi)

plt.plot(x,p0)
plt.show()
