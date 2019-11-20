#jacobian method for calculating lyaponov exponent spectrum

import numpy as np
import matplotlib.pyplot as plt

'''
#henon map has been chosen as example
a=1.4
b=0.3
def f(x,y):
	return (1 - a*x**2 + y, b*x)

T=5000
z=np.zeros((T,2),dtype=float)
z[0]=0.5,0.3
for i in range(1,T):
	val=f(z[i-1,0],z[i-1,1])
	z[i]=val[0],val[1]
'''

def f(y):
	return 4*y*(1-y)

T=4000
x=np.zeros(size=(T,1))
x[0]=np.random.random()
for i in range(1,T):
	x[i]=f(x[i-1])

de=3