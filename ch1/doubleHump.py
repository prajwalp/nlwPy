#double hump map and the bifurcation diagram
import numpy as np
import matplotlib.pyplot as plt

#defining double hump map
def f(r,x):
	if(x<0.5):
		return r*(0.5-x)*x
	else:
		return r*(1-x)*(-0.5+x)

#plotting the map
xVec=np.arange(0,1,0.01)
y=[]
for i in xVec:
	y.append(f(16,i))

plt.plot(xVec,y)
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Double Hump Map')
plt.show()

#bifurcation diagram for what values of function are reached
rVec=np.arange(0,20,0.1)
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
plt.title('Chaos of Double Hump Map')
plt.show()
