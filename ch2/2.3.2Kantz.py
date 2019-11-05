#Kantz method of evaluating Lyapunov exponent

import numpy as np
import matplotlib.pyplot as plt

S=[]
tau=np.arange(1,8,1,dtype=int)
T=1000
eps=0.005

#example used is logistic map
def f(x):
	return 4*x*(1-x)

def kantz(x0):
	xVec=[x0]
	for i in range(T-1):
		xVec.append(f(xVec[-1]))
	for t in tau:
		sumT=0
		for i in range(T-t):
			dist=0
			for j in range(T-t):
				if(abs(xVec[i]-xVec[j])<eps and i!=j):
					dist+=(abs(xVec[i+t]-xVec[j+t]))
			sumT+=np.log(dist)
		S.append(sumT/T)
	plt.title('x_0 = %.3f'%x0)
	plt.plot(tau,S,label='S(tau)')
	plt.plot(tau,np.log(2)*tau,label='log(2) * tau')
	plt.xlabel('tau')
	plt.legend()
	plt.show()

x0=np.random.random()
kantz(x0)


