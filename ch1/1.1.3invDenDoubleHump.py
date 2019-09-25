import matplotlib.pyplot as plt
import math

#Double hump
def f(x):
	if(x<0.5):
		return 16*(0.5-x)*x
	else:
		return 16*(1-x)*(-0.5+x)

#invariant density function
def rhoFun(x0,T):
	rho=[]
	xi=x0
	for i in range(T):
		rho.append(f(xi))
		xi=f(xi)
	return rho


fig,ax=plt.subplots(2,2)
plt.subplots_adjust(wspace=0.4,hspace=0.5)
x0Val=[[0.2,0.4],[0.6,0.8]]

#loop over axes in subplot, plotting histogram of time evolution
for xAx in range(2):
	for yAx in range(2):
		x0=x0Val[xAx][yAx]
		rho=rhoFun(x0,10000)
		axCur=ax[xAx][yAx]
		axCur.hist(rho,bins=25,density='True')
		axCur.set_title('x0: %.2f'%x0)
		axCur.set_xlabel('x')
		axCur.set_ylabel('Density of x')
fig.suptitle('Sine Map invariant Density')
plt.show()