#time evolution of invariant density
import numpy as np
import matplotlib.pyplot as plt

#initialising x-array for values
h=0.001
x=np.arange(0,1+h,h)
p0=np.ones(len(x))
pi=np.zeros(len(x))
T=10

#defining logistic map
def f(y):
	return 4*y*(1-y)

#defining inverse function
def fInv(z):
	xVal=[]
	for xy in x:
		if(abs(f(xy) - z)<1e-3):
			xVal.append(xy)
	return xVal

#initialising with p0=1
nbins=30;
newx=np.linspace(0,1,num=nbins,endpoint=True)
avgp=[]
for i in range(0,len(newx)-1):
	pval=0
	npts=0
	for j in range(len(x)):
		if(newx[i]<x[j] and x[j]<newx[i+1]):
			pval+=p0[j]
			npts+=1.
	avgp.append(pval/npts)

avgp=np.array(avgp)
avgp=avgp/(sum(avgp/nbins))
plt.bar(newx[0:nbins-1],avgp,width=1./nbins)

#time evoluton of invariant density using inverse values of a point
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
	print(t)
	avgp=[]
	#plotting bar graph of average values of invariant density in a bin
	for i in range(0,len(newx)-1):
		pval=0
		npts=0
		for j in range(len(x)):
			if(newx[i]<x[j] and x[j]<newx[i+1]):
				pval+=p0[j]
				npts+=1.
		avgp.append(pval/npts)

	avgp=np.array(avgp)
	avgp=avgp/(sum(avgp/nbins))
	plt.bar(newx[0:nbins-1]+0.5/nbins,avgp,width=1./nbins)
	plt.pause(0.0001)

plt.show()

