import numpy as np
import matplotlib.pyplot as plt

h=0.01
T=int(1e3)

def f(x):
	return 4*x*(1-x)

def df_dx(x):
	return (f(x+h)-f(x-h))/(2*h)

def lyapFunc(x0):
	exp=0.0
	xi=x0
	for t in range(T):
		temp=abs(df_dx(xi))
		if(temp>1e-5):
			exp+=np.log(temp)
			xi=f(xi)
	return exp/T

xRange=np.arange(0+h,1-h,h)
lya=[]
for y in xRange:
	lya.append(lyapFunc(y))

plt.plot(xRange,lya)
plt.xlabel('x')
plt.ylabel('Lyapunov Exponent')
plt.title('Lyapunov Exponents for Logistic Map | T=1e6')
plt.show()