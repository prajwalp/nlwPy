#time evolution of invariant density
import numpy as np
import matplotlib.pyplot as plt

#initialising x-array for values
h=0.001
x=np.arange(0,1+h,h)
p0=np.ones(len(x))
pi=np.zeros(len(x))
T=10

def f(y):
	return 4*y*(1-y)

def fInv(z):
	xVal=[]
	for xy in x:
		if(abs(f(xy) - z)<1e-3):
			xVal.append(xy)
	return xVal

plt.plot(x,p0)

for t in range(T):
	for j in range(len(x)):
		yVal=x[j]
		xVal=fInv(yVal)
		pSum=0
		for xy in xVal:
			indX=int(xy/h)-1
			pSum+=p0[indX]
		pi[j]=float(pSum)
	p0=np.array(pi)
	plt.clf()
	plt.plot(x,p0)
	plt.pause(0.0001)
	print(t)
plt.show()

