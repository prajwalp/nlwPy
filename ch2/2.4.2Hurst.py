#Hurst exponent for Logistic Map

import numpy as np
import matplotlib.pyplot as plt

T=4500
nFact=[]
aFact=[]	
for i in range(10,int(T/2)):
	if(T%i==0):
		nFact.append(i)
		aFact.append(T/i)

def f(y):
	return 4*y*(1-y)

def hurst(x0):
	x=[x0]
	for i in range(T-1):
		x.append(f(x[-1]))

	hurstVec=[]

	for i in range(len(nFact)):
		n=int(nFact[i])
		a=int(aFact[i])
		N=np.zeros((a,n),dtype=float)
		X=np.zeros((a,n),dtype=float)
		E=np.zeros((a,1),dtype=float)
		for j in range(a):
			for k in range(n):
				N[j,k]=x[ n*j + k]
				X[j,k]=sum(N[j])
			E[j]=np.sum(N[j])/n
			for k in range(n):
				X[j,k]=X[j,k] - (k+1)*E[j]
		R=np.amax(X,axis=1)-np.amin(X,axis=1)
		S=np.sqrt(np.sum((N-E)**2,axis=1)/n)
		h=np.sum(R/S)/a
		hurstVec.append([n,h])
	hurstVec=np.array(hurstVec)
	V=np.log(hurstVec[:,0])
	X=np.ones((len(V),2))
	X[:,1]=V
	Y=np.log(hurstVec[:,1])
	Xt=np.transpose(X)
	b=np.linalg.inv(Xt.dot(X)).dot(Xt).dot(Y)
	return b[1]

avgH=[]
for temp in range(100):
	x0=np.random.random()
	avgH.append([x0,hurst(x0)])
avgH=np.array(avgH)
plt.scatter(avgH[:,0],avgH[:,1],s=5)
plt.xlim((0,1))
plt.ylim((0.2,0.8))
plt.xlabel('x0')
plt.ylabel('Hurst exponent')
plt.show()

