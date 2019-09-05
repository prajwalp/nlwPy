#Example 4: Bungalow Tent map trajectory

import fractions as fr
import math


def f(x,a):
	if(x<a):
		return (1-a)*x/a
	elif(x<0.5):
		return 2*a*x/(1-2*a) + (1-3*a)/(1-2*a)
	elif(x<1-a):
		return 2*a*(1-x)/(1-2*a) + (1-3*a)/(1-2*a)
	else:
		return (1-a)*(1-x)/a


check = int(input('Enter 1 for fractional mode or 2 for float mode: '))

if(check == 1):
	num = int(input('Enter numerator of starting point: '))
	den = int(input('Enter denominator of starting point: '))	
	y0 = fr.Fraction(num,den)
	y=y0
	num = int(input('Enter numerator of control parameter: '))
	den = int(input('Enter denominator of control parameter: '))	
	a0 = fr.Fraction(num,den)
	a=a0

else:
	y0 = float(input('Enter the starting point: '))
	a= float(input("Enter the control parameter: "))	
	y=float(y0)

t = int(input('Enter the number of iterations: '))

l=[]
l.append(y)
e=0

for i in range(t):
	y = f(y,a)
	if(e==0 and y in l):
		e = 1
	l.append(y)
	print(float(y))

if (e==1):
	print('The starting point is eventually periodic')


