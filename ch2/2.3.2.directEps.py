#direct method with epsilon neighbourhood to calculate Lyapunov exponent for a time series data

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
		eps=0.005
		minind=0
		dtemp=[]
		for j in range(t-1):
			if(abs(xVal[i]-xVal[j])<eps and i!=j):
				dtemp.append([abs(xVal[i]-xVal[j]),abs(xVal[i+1]-xVal[j+1])])
				minind+=1
		if(minind>=1):
			dtemp=np.array(dtemp)
			d.append(sum(np.log((dtemp[:,1]/dtemp[:,0])))/minind)
	
	maxlyap=sum(d)/(t-1)
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