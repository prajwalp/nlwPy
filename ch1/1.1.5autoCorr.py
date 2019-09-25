import numpy as np
import matplotlib.pyplot as plt

T=int(1e4)

#logistic map
def f(y):
	return 4*y*(1-y)

#defining autocorrelation function
def autoC(t,x0):
	x=[x0]
	for i in range(T):
		x.append(f(x[len(x)-1]))
	xbar=np.mean(x)
	cxx=0.0
	for i in range(T-t):
		cxx+=(x[i]-xbar)*(x[i+t]-xbar)
	return cxx/T


#loop over axes in subplot, plotting autocorrelation function
fig,ax=plt.subplots(2,2)
plt.subplots_adjust(wspace=0.4,hspace=0.5)
x0Val=[[0.2,0.4],[0.6,0.8]]
for xAx in range(2):
	for yAx in range(2):
		C=[]
		x0=x0Val[xAx][yAx]
		for j in range(100):
			C.append([j,autoC(j,x0)])
		axCur=ax[xAx][yAx]
		C=np.array(C)
		axCur.plot(C[:,0],C[:,1])
		axCur.set_title('x0: %.2f'%x0)
		axCur.set_xlabel('Tau')
		axCur.set_ylabel('C_xx(tau)')
fig.suptitle('Autocorrelation Function for Logistic map')
plt.show()