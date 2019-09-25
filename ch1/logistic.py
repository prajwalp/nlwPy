import numpy as np
import matplotlib.pyplot as plt

def f(x):
	return 4*x*(1-x)

h=1e-3
T=int(1e6)
xRange=np.arange(0,1+h,h)
y=[]
for x in xRange:
	l=[x]
	for t in range(T):
		xi=f(l[-1])
		if(xi in l):
			y.append(1)
			break
		if(t==T-1):
			y.append(0)
		l.append(xi)

plt.plot(xRange,y)
plt.xlabel('x')
plt.ylabel('Periodic/Eventually Periodic/Stable')
plt.show()