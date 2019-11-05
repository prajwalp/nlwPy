#Invariant Density for Bungalow Tent Map

import matplotlib.pyplot as plt

#Bungalow Tent Map
def f(x,a):
	if(x<a):
		return (1-a)*x/a
	elif(x<0.5):
		return 2*a*x/(1-2*a) + (1-3*a)/(1-2*a)
	elif(x<1-a):
		return 2*a*(1-x)/(1-2*a) + (1-3*a)/(1-2*a)
	else:
		return (1-a)*(1-x)/a

#invariant density function
def rhoFun(x0,T):
	rho=[]
	xi=x0
	for i in range(T):
		rho.append(f(xi,0.25))
		xi=f(xi,0.25)
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
fig.suptitle('Bungalow Tent Map invariant Density | a: %.2f'%0.25)
plt.show()