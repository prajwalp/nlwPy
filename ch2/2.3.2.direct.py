#direct method to calculate Lyapunov exponent for a time series data

import numpy as np
import matplotlib.pyplot as plt

#for this example, we consider the logistic map
def f(x):
	return 4*x*(1-x)

t=100
lyapArr=[]
def lyapCalc(x0):
	xVal=[x0]
	for i in range(t):
		xVal.append(f(xVal[-1]))
	d=[]
	for i in range(t-1):
		mindist=1.0
		minind=i
		for j in range(t-1):
			if(abs(xVal[i]-xVal[j])<mindist and i!=j):
				mindist=abs(xVal[i]-xVal[j])
				minind=j
		d.append([abs(xVal[i]-xVal[minind]),abs(xVal[i+1]-xVal[minind+1])])
	d=np.array(d)
	maxlyap=sum(np.log(d[:,1]/d[:,0]))/(t-1)
	lyapArr.append([x0,maxlyap])

h=0.01
xRange=np.arange(0+h,1,h)
for y in xRange:
	lyapCalc(y)
lyapArr=np.array(lyapArr)
plt.plot(lyapArr[:,0],lyapArr[:,1])
plt.ylim(0,1)
plt.xlabel('x_0')
plt.ylabel('Maximal Lyaponov Exponents')
plt.title('Lyaponov Exponent by Direct Method')
plt.show()