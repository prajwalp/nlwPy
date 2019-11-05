#bifurcation diagram for logistic map
import numpy as np
import matplotlib.pyplot as plt

def f(r,x):
	return r*x*(1-x)

rVec=np.arange(0,4,0.01)
T=int(1e4)
x0=0.25
rVal=[]
for i in rVec:
	x=x0
	for j in range(T):
		x=f(i,x)
		if(j>9000):
			rVal.append([i,x])
rVal=np.array(rVal)
plt.plot(rVal[:,0],rVal[:,1],'r.',markersize=1)
plt.xlabel('r')
plt.ylabel('f(x) values reached')
plt.title('Chaos of Logistic Map')
plt.show()
