#correlation coefficient

import matplotlib.pyplot as plt
import numpy as np

#x is taken is a linear range
#y is taken as sin(x) + some random noise of strength n

def corr(n):
	x=np.arange(0,1,0.001)
	T=len(x)
	y=x + np.random.random(size=T)*n-n/2

	r=(T*sum(x*y) - sum(x)*sum(y))/np.sqrt((T*sum(x**2) - sum(x)**2)*(T*sum(y**2) - sum(y)**2))
	axCur.scatter(x,y,s=4)
	return r


fig,ax=plt.subplots(2,2)
plt.subplots_adjust(wspace=0.4,hspace=0.5)
nVal=[[0.1,0.5],[5,10]]

#loop over axes in subplot, plotting histogram of time evolution
for xAx in range(2):
	for yAx in range(2):
		n=nVal[xAx][yAx]
		axCur=ax[xAx][yAx]
		r=corr(n)
		axCur.set_title('n: %.1f | r=%.3f'%(n,r))
		axCur.set_xlabel('x')
		axCur.set_ylabel('y')

fig.suptitle('Correlation coefficients for different noise')
plt.show()
